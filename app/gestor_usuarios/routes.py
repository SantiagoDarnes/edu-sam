from flask import render_template, request, redirect, url_for, flash, session
from app.gestor_usuarios import bp
from app.models import User
from app import db

roles = {
    "admin":1,
    "student":2,
    "professor":3,
}

@bp.route("/gestor_usuario", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        role = request.form["role"]

        # Comprobar si el usuario ya existe
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('El correo electrónico ya está registrado.')
            return redirect(url_for('gestor_usuario.register'))

        # Crear nuevo usuario
        new_user = User(username=username, email=email, role_id=roles[role.strip()])
        new_user.set_password(username)

        # Guardar en la base de datos
        db.session.add(new_user)
        db.session.commit()

        flash('Usuario registrado exitosamente.')
        return redirect(url_for('gestor_usuario.register'))

    return render_template('gestor_usuarios/register.html')