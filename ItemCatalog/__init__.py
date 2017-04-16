from flask import Flask

UPLOAD_FOLDER = 'ItemCatalog/static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from views import ShowNewArrival
from views import ShowYourExhibit
from views import ShowAllCategory
from views import ShowCategoryItems

from views import ShowCategory
from views import ShowItem

from views import Login
from views import LoginWithGoogle
from views import LoginWithFacebook

from views import Logout
from views import LogoutWithGoogle
from views import LogoutWithFacebook

from views import NewCategory
from views import EditCategory
from views import DeleteCategory

from views import NewItem
from views import EditItem
from views import DeleteItem

from views import JsonAllCategory
from views import JsonAllItem
from views import JsonOneItem

from views import Show404
