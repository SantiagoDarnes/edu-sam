from flask import render_template, redirect, url_for, request, flash

from app.extensions import db
from app.modules.person_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.person import Person
from app.models.student.student import Student
from app.models.professor.professor import Professor
from app.models.administrator import Administrator

auth_service = AuthService()

@bp.route("/")
@login_required
@require_profile("ADMINISTRADOR")
def index():
    return render_template('admin/person_registration.html')


@bp.route("/register", methods=["POST"])
@login_required
@require_profile("ADMINISTRADOR")
def register():
    if request.method == 'POST':
        identity_number = request.form['identity_number']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        birth_date = request.form['birth_date']
        user_type = request.form['user_type']

        try:
            new_person = Person(
                identity_number=identity_number,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                birth_date=birth_date
            )
            new_person.set_username()
            new_person.set_password()
            db.session.add(new_person)
            db.session.commit()

            if user_type == 'ESTUDIANTE':
                new_student = Student(person_id=new_person.id)
                new_student.set_enrollment_number()
                db.session.add(new_student)
            elif user_type == 'PROFESOR':
                new_professor = Professor(person_id=new_person.id)
                new_professor.set_professor_code()
                db.session.add(new_professor)
            elif user_type == 'ADMINISTRADOR':
                new_admin = Administrator(person_id=new_person.id, access_level_id=1)
                db.session.add(new_admin)

            db.session.commit()
            flash("Persona registrada exitosamente.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al registrar la persona: {str(e)}", "danger")

        return redirect(url_for('person_registration.index'))
