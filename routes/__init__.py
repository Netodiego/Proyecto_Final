from .user_routes import iniciar_sesion_bp, registar_usuario_bp
from .base import base_bp, calcular_ruta_bp, ver_grafo_bp, ruta_nueva_bp, ruta_predeterminada_bp

def register_blueprints(app):
    app.register_blueprint(iniciar_sesion_bp)
    app.register_blueprint(registar_usuario_bp)
    app.register_blueprint(base_bp)
    app.register_blueprint(calcular_ruta_bp)
    app.register_blueprint(ver_grafo_bp)
    app.register_blueprint(ruta_nueva_bp)
    app.register_blueprint(ruta_predeterminada_bp)