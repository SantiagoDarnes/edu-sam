from flask import Blueprint

bp = Blueprint('home', __name__)

from app.modules.home import routes
