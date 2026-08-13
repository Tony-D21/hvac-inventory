from flask import Flask
import os
from .routes import main #Importamos la variable main del archivo routes, como quiero que busque en un archivo especifico uso el "."



def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "clave_por_defecto")
    app.register_blueprint(main)
    return app
    