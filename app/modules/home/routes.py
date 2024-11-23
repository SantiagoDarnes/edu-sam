from flask import render_template, redirect, url_for
from app.modules.home import bp
from app.auth import AuthService, login_required

auth_service = AuthService()

@bp.route('/')
@login_required
def index():
    user = auth_service.get_current_user()
    return render_template('home.html', username=user.username)
