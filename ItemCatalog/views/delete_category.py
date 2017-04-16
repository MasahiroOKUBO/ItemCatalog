from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from ItemCatalog.models import Category
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def DeleteCategory(category_id):
    category = db_session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        flash("Delete Category is not allowed for guest.")
        return redirect('/login')
    # if category.user_id != login_session['user_id']:
    #     flash("Delete Category is not allowed for guest.")
    #     return render_template('parts_alert.html')
    if request.method == 'POST':
        db_session.delete(category)
        db_session.commit()
        flash('%s Successfully Deleted' % category.name)
        return redirect(url_for('ShowAllCategory'))
    else:
        return render_template('form_delete_category.html', category=category)
