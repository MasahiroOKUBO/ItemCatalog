from sqlalchemy import asc
from sqlalchemy import desc
from flask import render_template, redirect, url_for, flash
from flask import session as login_session
from flask import send_from_directory
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


@app.route('/your_exhibit/')
def ShowYourExhibit():
    if 'username' not in login_session:
        flash("Your Exhibit is not allowed for guests. Please Login first.")
        return redirect(url_for('Login'))
    user_id = login_session['user_id']
    items = db_session.query(Item).filter_by(user_id=user_id).order_by(desc(Item.created_time))

    return render_template('page_your_exhibit.html', items=items)
