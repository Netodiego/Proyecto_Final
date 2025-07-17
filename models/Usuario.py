from extensions import db

class Usuarios(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)