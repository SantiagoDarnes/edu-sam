from flask import render_template, redirect, url_for, request
from app.models.student.student import Student
from app.models.professor.professor import Professor

from app.modules.personal_data import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/student")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    print(user)
    print(user.__dict__)
    student = Student.query.filter_by(person_id=user.id).first()
    
    
    return render_template("student/personal_data.html", person=user, student=student)

@bp.route("/professor")
@login_required
@require_profile("PROFESOR")
def personal_data_professor():
    return "<h1>Completar</h1>"