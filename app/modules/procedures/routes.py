from flask import render_template, redirect, url_for, request, flash
from app.modules.procedures import bp
from app.auth import AuthService, login_required, require_profile
from app.notifications.manager import NotificationsManager
from app.notifications.email_notifier import EmailNotifier
from app.models.student.student import Student

auth_service = AuthService()
notifications_manager = NotificationsManager()
notifications_manager.register(EmailNotifier())

@bp.route("/")
@login_required
@require_profile("ESTUDIANTE")
def index():
    user = auth_service.get_current_user()
    # TODO: Falta completar esto
    
    return render_template("student/procedures.html")

@bp.route("/regular_student", methods=["POST"])
@login_required
@require_profile("ESTUDIANTE")
def regular_student():
    user = auth_service.get_current_user()
    student = Student.query.filter_by(person_id=user.id).first()
    full_name = user.first_name + " " + user.last_name
    if request.method == "POST":
        notifications_manager.notify(
            event="proof_request",
            data={
                "name": full_name.title(),
                "identity_number": user.identity_number,
                "enrollment_number": student.enrollment_number,
                "email": user.email,
            },)
        flash("Proof request sent successfully", "success")

    return redirect(url_for("procedures.index"))

@bp.route("/student_ticket", methods=["POST"])
@login_required
@require_profile("ESTUDIANTE")
def student_ticket():
    user = auth_service.get_current_user()
    full_name = user.first_name + " " + user.last_name
    if request.method == "POST":
        notifications_manager.notify(
            event="student_ticket_request",
            data={
                "name": full_name.title(),
                "identity_number": user.identity_number,
                "email": user.email,
            },)
        flash("Student ticket request sent successfully", "success")

    return redirect(url_for("procedures.index"))
