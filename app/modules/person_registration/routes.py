from flask import render_template, redirect, url_for, request, flash

from app.extensions import db
from app.modules.person_registration import bp
from app.auth import AuthService, login_required, require_profile
from app.models.person import Person
from app.models.student.student import Student
from app.models.professor.professor import Professor
from app.models.administrator import Administrator

auth_service = AuthService()

@bp.route("/", methods=["GET", "POST"])
@login_required
@require_profile("ADMINISTRADOR")
def index():
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
                first_name=first_name.upper(),
                last_name=last_name.upper(),
                email=email,
                phone=phone,
                birth_date=birth_date
            )
            new_person.set_username()
            new_person.generate_password()
            db.session.add(new_person)
            db.session.commit()

            if user_type == 'ESTUDIANTE':
                new_student = Student(person_id=new_person.id, admission_date=db.func.current_date())
                new_student.set_enrollment_number()
                db.session.add(new_student)
                new_person.default_profile = 1
            elif user_type == 'PROFESOR':
                new_professor = Professor(person_id=new_person.id)
                new_professor.set_professor_code()
                db.session.add(new_professor)
                new_person.default_profile = 2
            elif user_type == 'ADMINISTRADOR':
                new_admin = Administrator(person_id=new_person.id, access_level_id=1)
                db.session.add(new_admin)
                new_person.default_profile = 3

            db.session.commit()
            flash("Persona registrada exitosamente.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al registrar la persona: {str(e)}", "danger")
            print(e)

    return render_template('admin/person_registration.html')
