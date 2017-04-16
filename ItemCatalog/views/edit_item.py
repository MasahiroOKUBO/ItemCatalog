from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def EditItem(item_id):
    if 'username' not in login_session:
        return redirect('/login')
    item_to_edit = db_session.query(Item).filter_by(id=item_id).one()
    if login_session['user_id'] != item_to_edit.user_id:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        print request.form['name']
        print request.form['description']
        print request.form['price']
        if request.form['name']:
            item_to_edit.name = request.form['name']
        if request.form['description']:
            item_to_edit.description = request.form['description']
        if request.form['price']:
            item_to_edit.price = request.form['price']
        db_session.add(item_to_edit)
        db_session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('ShowItem', item_id=item_id))
    else:
        return render_template('form_edit_item.html', item=item_to_edit)
