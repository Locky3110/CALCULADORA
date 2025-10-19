from flask import Blueprint, render_template, request, jsonify, redirect, url_for

# ✅ Nombre del blueprint y variable = app (como pediste)
app = Blueprint('calculos_DE', __name__)

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.json
    voltaje = float(datos.get('voltaje', 0))
    corriente = float(datos.get('corriente', 0))
    potencia = voltaje * corriente
    return jsonify({'potencia_watts': potencia})

# @app.route('/cerrar_sesion')
# def cerrar_Sesion():
#     # ✅ redirige correctamente a la raíz del blueprint (inicio)
#     return redirect(url_for('calculos_DE.inicio'))
