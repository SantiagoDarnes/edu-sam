from flask import render_template, redirect, url_for
from app.modules.home import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route('/student')
@login_required
@require_profile('ESTUDIANTE')
def home_student():
    user = auth_service.get_current_user()
    username = user.first_name.title() + ' ' + user.last_name.title()
    return render_template('student/home.html', username=username) 

@bp.route('/professor')
@login_required
@require_profile('PROFESOR')
def home_teacher():
    user = auth_service.get_current_user()
    username = user.first_name.title() + ' ' + user.last_name.title()
    return render_template('professor/home.html', username=username)
