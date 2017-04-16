from flask import jsonify
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/JSON/item/<int:item_id>/')
def JsonOneItem(item_id):
    # def JsonOneMenu(restaurant_id, menu_id):
    item = db_session.query(Item).filter_by(id=item_id).one()

    return jsonify(ItemInfo=item.serialize)
