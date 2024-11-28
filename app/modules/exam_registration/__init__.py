from flask import Blueprint

bp = Blueprint('exam_registration', __name__)

from app.modules.exam_registration import routes
