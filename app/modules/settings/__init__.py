from flask import Blueprint

bp = Blueprint('settings', __name__)

from app.modules.settings import routes
