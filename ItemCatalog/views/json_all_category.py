from flask import jsonify
from ItemCatalog.models import Category
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/JSON/allcategory')
def JsonAllCategory():
    categories = db_session.query(Category).all()
    return jsonify(categories=[category.serialize for category in categories])
