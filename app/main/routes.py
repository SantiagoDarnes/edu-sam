from flask import render_template, request, redirect, url_for, flash, session
from app.main import bp
from app.auth import AuthService, login_required

auth_service = AuthService()

# Ruta principal
@bp.route('/')
@login_required
def index():
    if session.get('profile') == 'ESTUDIANTE':
        return redirect(url_for('home.home_student'))
