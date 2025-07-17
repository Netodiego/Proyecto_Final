from extensions import db

class Rutas(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Ciudad_1 = db.Column(db.String(100), nullable=False)
    Ciudad_2 = db.Column(db.String(100), nullable=False)
    Distancia = db.Column(db.Float, nullable=False)
    
    