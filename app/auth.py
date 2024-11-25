from functools import wraps
from flask import redirect, url_for, session, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.person import Person
from app.models.profile import Profile


class AuthService:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls)
        return cls._instance

    def authenticate(self, username, password):
        user = Person.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            session['user_id'] = user.id
            session['profile'] = Profile.query.get(user.default_profile).name
            return True
        return False

    def logout(self):
        session.pop('username', None)
        session.pop('user_id', None)
        session.pop('profile', None)

    def is_authenticated(self):
        return 'username' in session

    def get_current_user(self):
        if 'user_id' in session:
            return Person.query.get(session['user_id'])
        return None


# Decorador para requerir autenticación
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_service = AuthService() 
        if not auth_service.is_authenticated():
            return render_template('login.html')
        return f(*args, **kwargs)
    return decorated_function
