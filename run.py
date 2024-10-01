from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret_key'

# Tiempo de inactividad maximo: 30 minutos
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


# Ruta principal
@app.route('/')
def index():
    return render_template('login/acceso.html')


# Ruta inicio de sesión
@app.route('/acceso', methods=['POST'])
def acceso():
    username = request.form['username']
    password = request.form['password']
    

    if username == "admin" and password == "admin":
        session.permanent = True
        session['username'] = username
        return redirect(url_for('inicio'))
    else:
        flash("Usuario o contraseña incorrectos. Intenta de nuevo.")
        return redirect(url_for('index'))


# Ruta inicio
@app.route('/inicio')
def inicio():
    username = session.get('username', None)
    if not username:
        return redirect(url_for('index'))
    return render_template('inicio.html', username=username)


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
def ayuda():
    return render_template('login/ayuda_menu.html')


# Ruta cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
