import random
import string
from flask import render_template
from flask import session as login_session
from ItemCatalog.utility import GOOGLE_CLIENT_ID
from ItemCatalog.utility import FACEBOOK_APP_ID
from ItemCatalog import app


@app.route('/login/')
def Login():
    state = ''
    for i in range(32):
        state += state.join(random.choice(string.ascii_uppercase + string.digits))
    login_session['state'] = state
    print "print state " + state
    return render_template('page_login.html',
                           STATE=state,
                           CLIENT_ID=GOOGLE_CLIENT_ID,
                           APP_ID=FACEBOOK_APP_ID)
