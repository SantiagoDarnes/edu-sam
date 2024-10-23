from flask import Blueprint

bp = Blueprint('gestor_usuario', __name__)

from app.gestor_usuarios import routes