from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from ItemCatalog.models import Category
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/category/<int:catgory_id>/edit/', methods=['GET', 'POST'])
def EditCategory(catgory_id):
    category = db_session.query(Category).filter_by(id=catgory_id).one()
    print category.id
    if 'username' not in login_session:
        return redirect('/login')
    # if edited_category.user_id != login_session['user_id']:
    #     return render_template('parts_alert.html')
    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
            db_session.add(category)
            db_session.commit()
            flash('Category Successfully Edited %s' % category.name)
            return redirect(url_for('ShowAllCategory'))
    else:
        return render_template('form_edit_category.html', category=category)
