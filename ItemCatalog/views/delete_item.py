from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def DeleteItem(item_id):
    if 'username' not in login_session:
        return redirect('/login')
    item_to_delete = db_session.query(Item).filter_by(id=item_id).one()
    if not item_to_delete:
        return redirect(url_for('ShowCustom404'))
    if item_to_delete.user_id != login_session['user_id']:
        return render_template('parts_alert.html')
    if request.method == 'POST':
        db_session.delete(item_to_delete)
        db_session.commit()
        flash('Item Successfully Deleted')
        return redirect(url_for('ShowTop'))
    else:
        return render_template('form_delete_item.html', item=item_to_delete)
