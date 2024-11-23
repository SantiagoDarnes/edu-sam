from flask import render_template, request, redirect, url_for, flash, session
from app.main import bp
from app.auth import AuthService, login_required

auth_service = AuthService()

# Ruta principal
@bp.route('/')
@login_required
def index():
    user = auth_service.get_current_user()
    return render_template('home.html', username="Santiago Darnes")
