from flask import render_template, redirect, url_for, request
from app.models.student.student import Student
from app.models.student.student_final_exam import StudentFinalExam
from app.models.student.student_subject import StudentSubject
from app.models.subject import Subject
from app.modules.exam_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.final_exam import FinalExam
from app import db

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    subjects_student = StudentSubject.query.filter_by(student_id=student.id, status=2).all()
    exams = []
    for subj in subjects_student:
        for exam in FinalExam.query.filter_by(subject_id=subj.subject_id).all():
            subject = Subject.query.filter_by(id=subj.subject_id).first()
            exams.append({
                "id":exam.id,
                "subject_id":exam.subject_id,
                "date":exam.date,
                "start_time":exam.start_time,
                "end_time":exam.end_time,
                "subject_name":subject.name
            })
    
    return render_template("student/exam_registration.html", exams=exams)

@bp.route('/register', methods=['POST'])
@require_profile("ESTUDIANTE")
def register():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    subject_id = request.form.get('exam_id')  # Obtener exam_id del formulario

    # Crear la relación estudiante-materia
    student_exam = StudentFinalExam.register(student_id=student.id, final_exam_id=subject_id)

    return redirect(url_for('subject_registration.index'))


@bp.route('/unregister', methods=['POST'])
@require_profile("ESTUDIANTE")
def unregister():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    exam_id = request.form.get('exam_id')  # Obtener subject_id del formulario

    # Buscar la relación estudiante-materia y eliminarla
    student_subject = StudentFinalExam.query.filter_by(student_id=student.id, final_exam_id=exam_id).first()
    db.session.delete(student_subject)
    db.session.commit()

    return redirect(url_for('subject_registration.index'))
