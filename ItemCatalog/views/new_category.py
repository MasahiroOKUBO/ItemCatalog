from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
from ItemCatalog.models import Category
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/category/new/', methods=['GET', 'POST'])
def NewCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        new_category = Category(name=request.form['name'],
                                user_id=login_session['user_id'])
        db_session.add(new_category)
        db_session.commit()
        flash('New Category %s Successfully Created' % new_category.name)
        return redirect(url_for('ShowAllCategory'))
    else:
        return render_template('form_new_category.html')
