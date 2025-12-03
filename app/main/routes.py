from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    # Datos simulados para ver que el frontend funciona
    stats = {
        'kernel_checks': 12,
        'os_checks': 45,
        'services_checks': 8
    }
    return render_template('index.html', title='Inicio', stats=stats)
