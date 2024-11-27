from flask import render_template, redirect, url_for, request
from app.modules.procedures import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    # TODO: Falta completar esto
    
    return render_template("student/procedures.html")

@bp.route("/regular_student")
@login_required
@require_profile("ESTUDIANTE")
def regular_student():
    
    return "<h1>Completar certificado de alumno regular</h3>"

@bp.route("/boleto")
@login_required
@require_profile("ESTUDIANTE")
def boleto():
    return "<h1>Completar boleto estudiantil</h1>"