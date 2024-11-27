from flask import render_template, redirect, url_for, request
from app.models.student.student import Student
from app.models.student.student_subject import StudentSubject
from app.models.subject import Subject
from app.models.subject_status import SubjectStatus

from app.modules.reports import bp
from app.auth import AuthService, login_required, require_profile

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    subjects_student = StudentSubject.query.filter_by(student_id=student.id, status=2).all()
    subjects = []
    for subj in subjects_student:
        subject = Subject.query.filter_by(id=subj.subject_id).first()
        status = SubjectStatus.query.filter_by(id=subj.status).first()
        subjects.append({
            "enrollment_date":subj.enrollment_date,
            "grade":subj.grade,
            "status":status.name,
            "subject_name":subject.name
        })
    
    return render_template("student/reports.html", subjects=subjects)
