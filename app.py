from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.user import db, User
from services.auth_service import AuthService
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de la base de datos
db.init_app(app)

# Inicialización del servicio de autenticación (Singleton)
auth_service = AuthService()


# Ruta principal
@app.route('/')
def index():
    return render_template('login/acceso.html')


# Ruta inicio de sesión
@app.route('/acceso', methods=['POST'])
def acceso():
    username = request.form['username']
    password = request.form['password']
    
    # Utilizar el AuthService para autenticar
    if auth_service.authenticate(username, password):
        return redirect(url_for('inicio'))
    else:
        flash("Usuario o contraseña incorrectos. Intenta de nuevo.")
        return redirect(url_for('index'))


# Ruta inicio
@app.route('/inicio')
def inicio():
    curren_user = auth_service.get_current_user()
    if not curren_user:
        return redirect(url_for('index'))
    return render_template('inicio.html', username=curren_user.username)


# Rutas páginas estáticas
@app.route('/fechas_examen')
def fechas_examen():
    return render_template('login/fechas_examen.html')

@app.route('/horarios_cursadas')
def horarios_cursadas():
    return render_template('login/horarios_cursadas.html')

@app.route('/validador_certificados')
def validador_certificados():
    return render_template('login/validador_certificados.html')

@app.route('/ayuda_menu')
def ayuda_menu():
    return render_template('login/ayuda_menu.html')


# Ruta cerrar sesión
@app.route('/logout')
def logout():
    auth_service.logout()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
