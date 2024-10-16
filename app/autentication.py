from flask import session
from werkzeug.security import check_password_hash
from app.models import User

class AuthService:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls)
        return cls._instance

    def authenticate(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['username'] = user.username
            session['user_id'] = user.id
            return True
        return False

    def logout(self):
        session.pop('username', None)
        session.pop('user_id', None)

    def is_authenticated(self):
        return 'username' in session

    def get_current_user(self):
        if 'user_id' in session:
            return User.query.get(session['user_id'])
        return None
