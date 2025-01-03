from functools import wraps
from flask import redirect, url_for, session
from werkzeug.security import check_password_hash
from app.models.person import Person
from app.models.profile import Profile
from app import db


class AuthService:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls)
        return cls._instance

    def authenticate(self, username, password):
        user = db.session.query(Person).filter_by(username=username).first()
        # user = Person.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            session['user_id'] = user.id
            session['profile'] = db.session.query(Profile).filter_by(id=user.default_profile).first().name
            session['profiles'] = [profile.name for profile in user.profiles]
            return True
        return False

    def logout(self):
        session.pop('username', None)
        session.pop('user_id', None)
        session.pop('profile', None)
        session.pop('profiles', None)

    def is_authenticated(self):
        return 'username' in session

    def get_current_user(self):
        if 'user_id' in session:
            return db.session.query(Person).filter_by(id=session["user_id"]).first()
            
        return None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_service = AuthService() 
        if not auth_service.is_authenticated():
            return redirect(url_for('login.index'))
        return f(*args, **kwargs)
    return decorated_function


def require_profile(profile):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if profile not in session['profiles']:
                return redirect(url_for('login.index'))
            
            session['profile'] = profile
            return f(*args, **kwargs)
        return wrapped
    return decorator

