from sqlalchemy import asc
from flask import render_template
from flask import session as login_session
from flask import send_from_directory
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/all_category/')
def ShowAllCategory():
    categories = db_session.query(Category).order_by(asc(Category.id))
    return render_template('page_all_category.html', categories=categories)

