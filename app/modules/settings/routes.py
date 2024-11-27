from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from app.modules.settings import bp
from app.auth import AuthService, login_required
from app.models.profile import Profile

auth_service = AuthService()

@bp.route("/")
@login_required
def index():
    user = auth_service.get_current_user() 
    emial = user.email
    default_profile = Profile.get_default_profile(user.id)
    profiles = user.profiles
    return render_template("settings.html", emial=emial, default_profile=default_profile, profiles=profiles)


@bp.route('/change_email', methods=['POST'])
@login_required
def change_email():
    user = auth_service.get_current_user()
    new_email = request.form.get('new_email')

    if not new_email:
        flash("El nuevo correo no puede estar vacío.")
        return redirect(url_for('settings.index'))

    # Actualizar el correo
    user.email = new_email
    user.update()
    flash("Correo actualizado correctamente.")
    return redirect(url_for('settings.index'))


@bp.route('/change_profile', methods=['POST'])
@login_required
def change_profile():
    user = auth_service.get_current_user()
    new_profile_id = request.form.get('default_profile')

    if not new_profile_id:
        flash("Debe seleccionar un perfil.")
        return redirect(url_for('settings.index'))

    # Actualizar el perfil predeterminado
    user.default_profile = new_profile_id
    user.update()
    flash("Perfil predeterminado actualizado correctamente.")
    return redirect(url_for('settings.index'))


@bp.route('/change_password', methods=['POST'])
@login_required
def change_password():
    user = auth_service.get_current_user()
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if not current_password or not new_password or not confirm_password:
        flash("Todos los campos son obligatorios.")
        return redirect(url_for('settings.index'))

    if not user.check_password(current_password):
        flash("La contraseña actual es incorrecta.")
        return redirect(url_for('settings.index'))

    if new_password != confirm_password:
        flash("Las contraseñas nuevas no coinciden.")
        return redirect(url_for('settings.index'))

    # Actualizar la contraseña
    user.password = generate_password_hash(new_password)
    user.update()
    flash("Contraseña actualizada correctamente.")
    return redirect(url_for('settings.index'))