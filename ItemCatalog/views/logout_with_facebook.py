import httplib2
from flask import session as flask_session
from ItemCatalog import app


@app.route('/fbdisconnect/')
def LogoutWithFacebook():
    facebook_id = flask_session['facebook_id']
    access_token = flask_session['access_token']
    '''
    ================
       delete access_token
    ================
    '''
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    print "url : %s" % url
    print "result : %s" % result
    '''
    ================
       delete login_session
    ================
    '''
    del flask_session['facebook_id']
    del flask_session['access_token']
    del flask_session['username']
    del flask_session['email']
    del flask_session['picture']
    del flask_session['user_id']
    del flask_session['state']

    return "you have been logged out"
