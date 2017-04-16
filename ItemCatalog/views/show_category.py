from flask import render_template
from flask import session as login_session
from ItemCatalog.models import User
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog.utility import GetUserObj
from ItemCatalog import app


def GetUserInfo(user_id):
    user = db_session.query(User).filter_by(id=user_id).one()
    return user


@app.route('/category/<int:category_id>/')
def ShowCategory(category_id):
    category = db_session.query(Category).filter_by(id=category_id).one()
    creator = GetUserInfo(category.user_id)
    items = db_session.query(Item).filter_by(category_id=category_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('page_category_public.html',
                               items=items,
                               category=category,
                               creator=creator)
    else:
        return render_template('page_category_loginuser.html',
                               items=items,
                               category=category,
                               creator=creator)
