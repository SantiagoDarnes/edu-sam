from flask import Blueprint

bp = Blueprint('login', __name__)

from app.modules.login import routes
