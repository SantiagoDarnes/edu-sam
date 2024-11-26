from flask import Blueprint

bp = Blueprint('subject_registration', __name__)

from app.modules.subject_registration import routes
