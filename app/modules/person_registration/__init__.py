from flask import Blueprint

bp = Blueprint('person_registration', __name__)

from app.modules.person_registration import routes
