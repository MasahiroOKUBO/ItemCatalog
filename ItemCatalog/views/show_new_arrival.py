from sqlalchemy import asc
from sqlalchemy import desc
from flask import render_template
from flask import session as login_session
from flask import send_from_directory
from ItemCatalog.models import Category

from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app

from flask import send_from_directory


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/')
@app.route('/new_arrival/')
def ShowNewArrival():
    items = db_session.query(Item).order_by(desc(Item.created_time))
    return render_template('page_new_arrival.html', items=items)
