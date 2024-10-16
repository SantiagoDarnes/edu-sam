from flask import render_template
from app.main import bp

# Ruta principal
@bp.route('/')
def index():
    return render_template('/login/acceso.html')
