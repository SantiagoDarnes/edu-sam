from flask import render_template, redirect, url_for, session
from app.modules.subject_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.student.student_career import StudentCareer
from app.models.subject import Subject
from app.models.student.student_subject import StudentSubject
from app.models.student.student import Student
from app.models.academic_period import AcademicPeriod
from app.models.semester import Semester
from app import db
# No tengo idea de como usar AcademicPeriod

auth_service = AuthService()

@bp.route('/')
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    student_careers = StudentCareer.query.filter_by(student_id=student.id).all()
    academic_period = AcademicPeriod.query.filter_by(is_active=True).first()

    subjects = []
    for student_career in student_careers:
        subjects += Subject.query.filter_by(career_id=student_career.career_id, academic_period_id=academic_period.id).all()
    
    return render_template("student/subject_registration.html", subjects=subjects)

@bp.route('/register', methods=['POST'])
@require_profile("ESTUDIANTE")
def register(subject_id):
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    student_subject = StudentSubject(student_id=student.id, subject_id=subject_id)
    db.session.add(student_subject)
    db.session.commit()
    return redirect(url_for('subject_registration.index'))

@bp.route('/unregister/<int:subject_id>', methods=['POST'])
@require_profile("ESTUDIANTE")
def unregister(subject_id):
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    student_subject = StudentSubject.query.filter_by(student_id=student.id, subject_id=subject_id).first()
    db.session.delete(student_subject)
    db.session.commit()
    return redirect(url_for('subject_registration.index'))