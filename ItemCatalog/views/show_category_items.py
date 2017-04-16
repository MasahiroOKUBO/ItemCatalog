from sqlalchemy import asc
from flask import render_template
from flask import session as login_session
from flask import send_from_directory
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/category/<int:category_id>/item/')
def ShowCategoryItems(category_id):
    # if 'username' not in login_session:
    #     return render_template('page_category_items_public.html')
    # user_id = login_session['user_id']
    items = db_session.query(Item).filter_by(category_id=category_id).order_by(asc(Item.name))

    return render_template('page_category_item.html', items=items)
