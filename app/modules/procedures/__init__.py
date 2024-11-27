from flask import Blueprint

bp = Blueprint('procedures', __name__)

from app.modules.procedures import routes
