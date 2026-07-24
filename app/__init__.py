from flask import Flask 
from .routes import main #Importamos la variable main del archivo routes, como quiero que busque en un archivo especifico uso el "."



def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app