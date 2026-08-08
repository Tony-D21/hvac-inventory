from flask import Blueprint
from flask import render_template

main = Blueprint("main", __name__)#Aquí estás creando un blueprint llamado "main", __name__ le dice a Flask en qué módulo está definido, lo que ayuda a ubicar recursos como plantillas o archivos estáticos.
@main.route("/")
def home():
    return render_template("index.html")

@main.route("/inventario")
def inventario ():
    return render_template("inventario.html")

@main.route("/inventario/nuevo")
def nuevo():
    return render_template("nuevo_material.html")