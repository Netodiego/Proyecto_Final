from utils.grafo_utils import grafo_a_imagen, camino_optimo_con_costera
from models.Rutas import Rutas
from extensions import db

def obtener_imagen_grafo(aristas):
    return grafo_a_imagen(aristas)

def calcular_camino_optimo(origen, destino, aristas):
    return camino_optimo_con_costera(origen, destino, aristas)

def crear_nueva_ruta(origen, destino, distancia):
    nueva_ruta = Rutas(Ciudad_1=origen, Ciudad_2=destino, Distancia=distancia)
    db.session.add(nueva_ruta)
    db.session.commit()
    return nueva_ruta

def obtener_rutas():
    rutas = Rutas.query.all()
    lista_rutas = []
    for ruta in rutas:
        tupla = (ruta.Ciudad_1, ruta.Ciudad_2, ruta.Distancia)
        lista_rutas.append(tupla)
    return lista_rutas