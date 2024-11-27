from flask import render_template, redirect, url_for, request
from app.models.student.student import Student
from app.models.professor.professor import Professor
from app.models.administrator import Administrator

from app.modules.personal_data import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/")
@login_required
def index():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    professor = Professor.query.filter_by(person_id=user.id).first()
    admin = Administrator.query.filter_by(person_id=user.id).first()
    
    
    return render_template("personal_data.html", person=user, student=student, professor=professor, admin=admin)