import os
from sqlalchemy import asc
from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
from flask import send_from_directory
from werkzeug.utils import secure_filename
from ItemCatalog.models import Category
from ItemCatalog.models import Item
from ItemCatalog.utility import db_session
from ItemCatalog import app


def allowed_file(filename):
    if '.' not in filename:
        return False
    if filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return False
    return True


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/item/new/', methods=['GET', 'POST'])
def NewItem():
    if 'username' not in login_session:
        return redirect('/login')
    categories = db_session.query(Category).order_by(asc(Category.name))
    category_name_list = []
    for category in categories:
        category_name_list.append(category.name)
    print category_name_list
    if request.method == 'POST':
        print "name : %s" % request.form['name']
        print "description : %s" % request.form['description']
        print "price : %s" % request.form['price']
        print "category_id : %s" % request.form['category_id']
        print "user_id : %s" % login_session['user_id']
        new_item = Item(name=request.form['name'],
                        description=request.form['description'],
                        price=request.form['price'],
                        category_id=request.form['category_id'],
                        user_id=login_session['user_id'])
        db_session.add(new_item)
        db_session.commit()
        if 'file' not in request.files:
            flash('No file part')
            new_item.picture = 'images/default_item.png'
            print new_item.picture
        else:
            uploaded_file = request.files['file']
            print "upload_file : %s" % uploaded_file
            if uploaded_file.filename == '':
                flash('No selected file')
                new_item.picture = 'images/default_item.png'
                print new_item.picture
            else:
                print new_item.id
                if uploaded_file and allowed_file(uploaded_file.filename):
                    filename = str(new_item.id) + '_' + uploaded_file.filename
                    print "filename : %s" % filename
                    uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    new_item.picture = 'uploads/' + filename
                    print new_item.picture
        db_session.add(new_item)
        db_session.commit()
        flash('New Item %s Item Successfully Created' % new_item.name)

        return redirect(url_for('ShowNewArrival'))
    else:
        return render_template('form_new_item.html', categories=categories)
