from flask import render_template, request, redirect, url_for, flash, session
from app.modules.login import bp
from app.auth import AuthService
from app.models.user import User

auth_service = AuthService()

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Utilizar el AuthService para autenticar
        if auth_service.authenticate(username, password):
            return redirect(url_for('main.index'))
        else:
            flash("Usuario o contraseña incorrectos. Intenta de nuevo.")
    return render_template('login.html')


@bp.route('/logout')
def logout():
    auth_service.logout()
    return redirect(url_for('login.index'))    
    