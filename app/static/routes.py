from flask import render_template
from app.static import bp

@bp.route('/fechas_examen')
def fechas_examen():
    return render_template('/login/fechas_examen.html')

@bp.route('/horarios_cursadas')
def horarios_cursadas():
    return render_template('/login/horarios_cursadas.html')

@bp.route('/validador_certificados')
def validador_certificados():
    return render_template('/login/validador_certificados.html')

@bp.route('/ayuda_menu', methods=['GET', 'POST'])
def ayuda_menu():
    return render_template('/login/ayuda_menu.html')