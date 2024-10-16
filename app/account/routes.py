from flask import render_template, request, redirect, url_for, flash, session
from app.account import bp
from app.autentication import AuthService
from app.models import User

auth_service = AuthService()

# Ruta inicio de sesión
@bp.route('/acceso', methods=['POST'])
def acceso():
    username = request.form['username']
    password = request.form['password']
    
    # Utilizar el AuthService para autenticar
    if auth_service.authenticate(username, password):
        return redirect(url_for('account.inicio'))
    else:
        flash("Usuario o contraseña incorrectos. Intenta de nuevo.")
        return redirect(url_for('main.index'))
    
    
# Ruta recuperar contraseña
@bp.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        email = request.form['email']
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash("Se ha enviado un correo con instrucciones para recuperar tu contraseña.", "info",)
        else:
            flash("No se encontró un usuario con el correo proporcionado.", "warning")
        
        return redirect(url_for('main.index'))
    
    return render_template('/login/recuperar.html')


# Ruta inicio
@bp.route('/inicio')
def inicio():
    curren_user = auth_service.get_current_user()
    if not curren_user:
        return redirect(url_for('main.index'))
    return render_template('inicio.html', username=curren_user.username)


# Ruta cerrar sesión
@bp.route('/logout')
def logout():
    auth_service.logout()
    return redirect(url_for('main.index'))

