from flask import render_template, redirect, url_for, session
from app.modules.subject_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.student.student_career import StudentCareer
from app.models.subject import Subject

auth_service = AuthService()

@bp.route('/')
@login_required
@require_profile("ESTUDIANTE")
def available_subjects():
    print(Subject.query.all())
    # user = auth_service.get_current_user()
    # carrers = StudentCareer.query.filter_by(student_id=user.id).all()
    # print(carrers)
    # for career in carrers:
    #     subjects = Subject.query.filter_by(career_id=career.career_id).all()
    #     print(subjects)
    #     # TODO
    
    # subjects = []
    # for career in carrers.all():
    #     career...
    
    return render_template("subject_registration.html")


# @bp.route('/subject_registration')
# @login_required
# @require_profile('ESTUDIANTE')
# def home_student():
#     user = auth_service.get_current_user()
#     username = user.first_name.title() + ' ' + user.last_name.title()
#     return render_template('student/home.html', username=username) 

# @bp.route('/professor')
# @login_required
# @require_profile('PROFESOR')
# def home_teacher():
#     user = auth_service.get_current_user()
#     username = user.first_name.title() + ' ' + user.last_name.title()
#     return render_template('professor/home.html', username=username)
