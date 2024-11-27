from flask import render_template, redirect, url_for, request
from app.modules.reports import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    # TODO: Falta completar esto
    
    return render_template("student/procedures.html")
