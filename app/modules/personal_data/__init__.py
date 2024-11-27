from flask import Blueprint

bp = Blueprint('personal_data', __name__)

from app.modules.personal_data import routes
