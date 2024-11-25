from app.models import *

from app import create_app
from app.extensions import db

app = create_app()

# Comando para crear las tablas
with app.app_context():
    db.create_all() 