from flask import Blueprint, render_template, send_file, request
from utils.grafo_utils import obtener_ciudades, camino_optimo_con_costera
from controllers.base_controller import obtener_imagen_grafo, calcular_camino_optimo
from controllers.base_controller import crear_nueva_ruta, obtener_rutas

base_bp = Blueprint("base", __name__)
calcular_ruta_bp = Blueprint("calcular_ruta", __name__)
ver_grafo_bp = Blueprint("ver_grafo", __name__)
ruta_nueva_bp = Blueprint("ruta_nueva", __name__)
ruta_predeterminada_bp = Blueprint("ruta_predeterminada", __name__)

@base_bp.route('/base')
def base():
    return render_template('bienvenida.html')    

@calcular_ruta_bp.route('/calcular_ruta')
def mostrar_formulario_ruta():
    return render_template('calcular_ruta.html')    

@ver_grafo_bp.route('/ver_grafo')
def ver_grafo():
    rutas = obtener_rutas()
    img = obtener_imagen_grafo(rutas)
    return send_file(img, mimetype='image/png')

@calcular_ruta_bp.route('/camino', methods=['GET', 'POST'])
def calcular_ruta():
    ciudades = obtener_ciudades()
    resultado = None

    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        if origen and destino and origen != destino:
            resultado = calcular_camino_optimo(origen=origen, destino=destino, aristas=obtener_rutas())

    return render_template("calcular_ruta.html", ciudades=ciudades, resultado=resultado)

@ruta_nueva_bp.route('/ruta_nueva', methods=['GET', 'POST'])
def ruta_nueva():
    if request.method == 'POST':
        ciudad1 = request.form.get('ciudad1')
        ciudad2 = request.form.get('ciudad2')
        distancia = request.form.get('distancia')

        if ciudad1 and ciudad2 and distancia:
            crear_nueva_ruta(ciudad1, ciudad2, distancia)
            return render_template('ruta_nueva.html')
    return render_template('ruta_nueva.html')


@ruta_predeterminada_bp.route('/caminop')
def caminop():
    resultado = camino_optimo_con_costera()
    return render_template('caminop.html', resultado = resultado)