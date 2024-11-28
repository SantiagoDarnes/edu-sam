from flask import render_template, redirect, url_for
from app.modules.home import bp
from app.auth import AuthService, login_required, require_profile
from app.models.academic_period import AcademicPeriod
from app.qr_factory import QRCodeFactory, send_file

auth_service = AuthService()

@bp.route('/student')
@login_required
@require_profile('ESTUDIANTE')
def home_student():
    user = auth_service.get_current_user()
    username = user.first_name.title() + ' ' + user.last_name.title()

    academic_period = AcademicPeriod.get_current()
    period_data = {
        'start_date': academic_period.start_date.strftime('%d/%m/%Y'),
        'end_date': academic_period.end_date.strftime('%d/%m/%Y'),
        'inscription_start_date': academic_period.inscription_start_date.strftime('%d/%m/%Y'),
        'inscription_end_date': academic_period.inscription_end_date.strftime('%d/%m/%Y'),
    }

    return render_template('student/home.html', username=username, academic_period=period_data )


@bp.route('/academic_period_qr')
@login_required
def academic_period_qr():
    academic_period = AcademicPeriod.get_current()
    event_name = f"EduSam - {academic_period.name}"
    start_date = academic_period.start_date
    end_date = academic_period.end_date

    qr_image = QRCodeFactory.generate_event_qr(event_name, start_date, end_date)
    return send_file(qr_image, mimetype='image/png', as_attachment=False)


@bp.route('/professor')
@login_required
@require_profile('PROFESOR')
def home_professor():
    user = auth_service.get_current_user()
    username = user.first_name.title() + ' ' + user.last_name.title()
    return render_template('professor/home.html', username=username)


@bp.route('/admin')
@login_required
@require_profile('ADMINISTRADOR')
def home_admin():
    user = auth_service.get_current_user()
    username = user.first_name.title() + ' ' + user.last_name.title()
    return render_template('admin/home.html', username=username)
    
