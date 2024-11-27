from flask import render_template, redirect, url_for, request
from app.modules.subject_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.student.student_career import StudentCareer
from app.models.subject import Subject
from app.models.student.student_subject import StudentSubject
from app.models.student.student import Student
from app.models.academic_period import AcademicPeriod
from app.models.semester import Semester
from app import db

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
    
    registered_subjects = StudentSubject.query.filter_by(student_id=student.id).all()
    registered_subject_ids = [ss.subject_id for ss in registered_subjects]

    available_subjects = [subject for subject in subjects if subject.id not in registered_subject_ids]
    registered_subjects = [subject for subject in subjects if subject.id in registered_subject_ids]

    return render_template("student/subject_registration.html", available_subjects=available_subjects, registered_subjects=registered_subjects)

@bp.route('/register', methods=['POST'])
@require_profile("ESTUDIANTE")
def register():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    subject_id = request.form.get('subject_id')  # Obtener subject_id del formulario

    # Crear la relación estudiante-materia
    student_subject = StudentSubject(student_id=student.id, subject_id=subject_id, enrollment_date=db.func.current_date(), status=1)
    db.session.add(student_subject)
    db.session.commit()

    return redirect(url_for('subject_registration.index'))


@bp.route('/unregister', methods=['POST'])
@require_profile("ESTUDIANTE")
def unregister():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    subject_id = request.form.get('subject_id')  # Obtener subject_id del formulario

    # Buscar la relación estudiante-materia y eliminarla
    student_subject = StudentSubject.query.filter_by(student_id=student.id, subject_id=subject_id).first()
    db.session.delete(student_subject)
    db.session.commit()

    return redirect(url_for('subject_registration.index'))
