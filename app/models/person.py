from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    identity_number = db.Column(db.String(20), unique=True, nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # default_profile

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    birth_date = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    students = db.relationship('Student', backref='person', lazy=True)
    professors = db.relationship('Professor', backref='person', lazy=True)
    administrators = db.relationship('Administrator', backref='person', lazy=True)


    def set_password(self, password):
        """Genera el hash de la contraseña."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si la contraseña es correcta."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Person {self.username}, ID: {self.identity_number}>'
