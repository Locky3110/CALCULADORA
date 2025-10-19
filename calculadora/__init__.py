from flask import Flask

def create_app():
    app = Flask(__name__)

    # ✅ Importa y registra el blueprint "app" de calculos.py
    from .calculos import app as calculos_DE
    app.register_blueprint(calculos_DE, url_prefix='/')

    return app
