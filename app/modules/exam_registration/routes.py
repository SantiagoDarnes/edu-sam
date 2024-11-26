from flask import render_template, redirect, url_for, session, request
from app.modules.exam_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.final_exam import FinalExam
from app.models.student.student_subject import StudentSubject


auth_service = AuthService()

@bp.route("/", methods=['GET', 'POST'])
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    if request.method == "POST":
        # request.
        return
    
    # status: 1=cursando, 2=aprobado, 3=promocionado
    subj_aprobado = StudentSubject.query.filter_by(student_id=user.id).where(status=2).all()
    subject_id = []
    for subj in subj_aprobado:
        if subj.subject_id not in subject_id:
            subject_id.append(subj.subject_id)
    
    exams = []
    for subj_id in subject_id:
        for exam in FinalExam.query.filter_by(subject_id=subj_id).all():
            exams.append({
                "id":exam.id,
                "subject_id":exam.subject_id,
                "date":exam.date,
                "start_time":exam.start_time,
                "end_time":exam.end_time
            })
    
    return render_template("student/exam_registration.html", exams=exams)
    
    
    


# @bp.route('/')
# @login_required
# @require_profile("ESTUDIANTE")
# def available_subjects():
#     user = auth_service.get_current_user()
#     # careers = StudentCareer.query.filter_by(student_id=user.id).join(Subject.career_id).all()
#     careers = StudentCareer.query.filter_by(student_id=user.id).all()
#     career_id_unique = []
#     for career in careers:
#         if career.career_id not in career_id_unique:
#             career_id_unique.append(career.career_id)
    
#     subjects = []
#     for career_id in career_id_unique:
#         for subj in Subject.query.filter_by(career_id=career_id).all():
            
#             subjects.append({
#                 "id":subj.id,
#                 "code":subj.code,
#                 "name":subj.name,
#                 "academic_period_id":subj.academic_period_id,
#                 "min_passing_grade":subj.min_passing_grade,
#                 "min_promotion_grade":subj.min_promotion_grade
#             })
    
#     return render_template("subject_registration/subject_registration.html", subjects=subjects)

