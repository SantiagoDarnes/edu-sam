from flask import render_template, redirect, url_for, request

from app.modules.add_subject import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ADMINISTRADOR")
def index():
    return render_template("admin/add_subject.html")