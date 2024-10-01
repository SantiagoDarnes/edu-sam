from app import app
from models.user import db

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()
    print("Tablas creadas correctamente.")
