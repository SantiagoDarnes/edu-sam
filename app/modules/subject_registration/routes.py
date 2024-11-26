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
def available_subjects():
    user = auth_service.get_current_user()
    # careers = StudentCareer.query.filter_by(student_id=user.id).join(Subject.career_id).all()
    careers = StudentCareer.query.filter_by(student_id=user.id).all()
    career_id_unique = []
    for career in careers:
        if career.career_id not in career_id_unique:
            career_id_unique.append(career.career_id)
    
    subjects = []
    for career_id in career_id_unique:
        for subj in Subject.query.filter_by(career_id=career_id).all():
            
            subjects.append({
                "id":subj.id,
                "code":subj.code,
                "name":subj.name,
                "academic_period_id":subj.academic_period_id,
                "min_passing_grade":subj.min_passing_grade,
                "min_promotion_grade":subj.min_promotion_grade
            })
    
    return render_template("subject_registration/subject_registration.html", subjects=subjects)

@bp.route("subject_selected/<subject_id>")
@login_required
@require_profile("ESTUDIANTE")
def select_subject(subj):
    user = auth_service.get_current_user()
    student_subj = StudentSubject(
        student_id=Student.query.where(person_id=user.id).first(),
        subject_id=subj,
        enrollment_date="2024-11-26",
        status=1,
        created_at="2024-11-26 17:32:00.0",
        updated_at="2024-11-26 17:32:00.0"
    )
    # db.add(student_subj)