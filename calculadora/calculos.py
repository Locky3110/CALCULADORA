from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import math

app = Blueprint('calculos_DE', __name__,template_folder='calculadora/templates')

@app.route('/')
def inicio():
    return render_template('base.html')

# ✅ Rutas individuales para cada tema

@app.route('/coulomb')
def coulomb():
    return render_template('coulomb.html')

@app.route('/gauss')
def gauss():
    return render_template('gauss.html')

@app.route('/energia')
def energia():
    return render_template('energia.html')

@app.route('/capacitores')
def capacitores():
    return render_template('capacitores.html')

@app.route('/potencia')
def potencia():
    return render_template('potencia.html')

@app.route('/kirchhoff')
def kirchhoff():
    return render_template('kirchhoff.html')

@app.route('/ampere')
def ampere():
    return render_template('ampere.html')

@app.route('/faraday')
def faraday():
    return render_template('faraday.html')
