import httplib2
import json
import requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import render_template, request, flash
from flask import session as flask_session
from flask import make_response
from ItemCatalog.models import User
from ItemCatalog.utility import db_session
from ItemCatalog.utility import GOOGLE_CLIENT_ID
from ItemCatalog import app


def CreateUser(login_session):
    new_user = User(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    db_session.add(new_user)
    db_session.commit()
    user_obj = db_session.query(User).filter_by(email=login_session['email']).one()
    return user_obj.id

def GetUserID(email):
    try:
        user_obj = db_session.query(User).filter_by(email=email).one()
        return user_obj.id
    except:
        return None


@app.route('/login_with_google', methods=['POST'])
def LoginWithGoogle():
    print request.args.get('state')
    print flask_session['state']
    if request.args.get('state') != flask_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    '''
    ================
       read client_secret_google.json
    ================
    '''
    auth_code = request.data
    try:
        oauth_flow = flow_from_clientsecrets('client_secret_google.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(auth_code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    gplus_id = credentials.id_token['sub']
    print "auth_code : %s" % auth_code
    print "credentials : %s" % credentials
    print "access_token : %s" % access_token
    print "gplus_id : %s" % gplus_id
    '''
    ================
       check google access_token, and
    ================
    '''
    url = 'https://www.googleapis.com/oauth2/v1/tokeninfo' \
          '?access_token=%s' % access_token
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    if result['issued_to'] != GOOGLE_CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print "url : %s" % url
    print "result : %s" % result
    print "error : %s" % result.get('error')
    '''
    ================
       check if already connected.
    ================
    '''
    stored_access_token = flask_session.get('access_token')
    stored_gplus_id = flask_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    '''
    ================
       get google user info
    ================
    '''
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    json_content = answer.json()
    flask_session['provider'] = 'google'
    flask_session['credentials'] = access_token
    flask_session['access_token'] = access_token
    flask_session['gplus_id'] = gplus_id
    flask_session['username'] = json_content['name']
    flask_session['picture'] = json_content['picture']
    flask_session['email'] = json_content['email']
    '''
    ================
       if email not registerd, create new user.
    ================
    '''
    user_id = GetUserID(flask_session['email'])
    print "user_id : %s" % user_id
    if not user_id:
        user_id = CreateUser(flask_session)
        print "Create New User !"
    flask_session['user_id'] = user_id
    '''
    ================
       render login confirm page
    ================
    '''
    print "login_session : %s" % flask_session
    flash("Now logged in as %s" % flask_session['username'])
    return render_template('page_login_confirm.html',
                           username=flask_session['username'],
                           picture=flask_session['picture'])
