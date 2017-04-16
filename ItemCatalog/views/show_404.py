from flask import render_template
from ItemCatalog import app

@app.errorhandler(404)
def Show404(e):
    return render_template('page_404.html'), 404

