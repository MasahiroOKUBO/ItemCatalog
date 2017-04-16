from flask import render_template
from flask import session as login_session
from ItemCatalog.models import User
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


def GetUserObj(user_id):
    user_obj = db_session.query(User).filter_by(id=user_id).one()
    return user_obj


@app.route('/item/<int:item_id>/')
def ShowItem(item_id):
    item = db_session.query(Item).filter_by(id=item_id).one()
    print item
    print item.id
    owner = GetUserObj(item.user_id)
    print "item.id : %s" % item.id
    print "login_session : %s" % login_session
    print "item_owner.id : %s" % owner.id
    if 'username' not in login_session or owner.id != login_session['user_id']:
        return render_template('page_item_public.html', item=item, owner=owner)
    else:
        print "login_session['user_id'] : %s" % login_session['user_id']
        return render_template('page_item_owner.html', item=item, owner=owner)

