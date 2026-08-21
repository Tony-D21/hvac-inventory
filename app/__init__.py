from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os




load_dotenv()#Carga las variables del archivo .env
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "clave_por_defecto")    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    db.init_app(app)
    from .models import Material #Importamos del archivo models la clase Material
    with app.app_context():#Habilita el contexto de la app para ejecutar código fuera de una petición
        db.create_all()#Mandamos a crear todas las tablas a la db,(las creamo es models.py)
    from .routes import main #Importamos la variable main del archivo routes, como quiero que busque en un archivo especifico uso el "."
    app.register_blueprint(main)
    return app
