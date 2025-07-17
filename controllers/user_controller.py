# Importa la función para renderizar plantillas HTML
from flask import render_template, redirect, url_for
from models.Usuario import Usuarios

def iniciar_sesion_controlador(usuario, clave):
    usuario = Usuarios.query.filter_by(usuario=usuario, clave=clave).first()
    if usuario:
            return redirect(url_for('base.base'))
    else:
        error = "Usuario o contraseña incorrectos"
        return render_template('iniciar_sesion.html', error=error)
    