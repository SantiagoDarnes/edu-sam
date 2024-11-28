from flask import Blueprint

bp = Blueprint('add_subject', __name__)

from app.modules.add_subject import routes
