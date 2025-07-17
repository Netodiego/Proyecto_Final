from flask import Blueprint, render_template, request
from controllers.user_controller import iniciar_sesion_controlador

iniciar_sesion_bp = Blueprint("iniciar_sesion", __name__)
registar_usuario_bp = Blueprint("registrar_usuario", __name__)

@iniciar_sesion_bp.route('/', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return iniciar_sesion_controlador(username, password)    
            
    return render_template('iniciar_sesion.html')