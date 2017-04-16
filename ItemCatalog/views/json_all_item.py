from flask import jsonify
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/JSON/allitem/')
def JsonAllItem():
    items = db_session.query(Item).all()
    return jsonify(Items=[item.serialize for item in items])
