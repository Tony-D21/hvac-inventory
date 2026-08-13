from flask import Blueprint, request, render_template, flash


main = Blueprint("main", __name__)#Aquí estás creando un blueprint llamado "main", __name__ le dice a Flask en qué módulo está definido, lo que ayuda a ubicar recursos como plantillas o archivos estáticos.
@main.route("/")
def home():
    return render_template("index.html")

@main.route("/inventario")
def inventario ():
    return render_template("inventario.html")

@main.route("/inventario/nuevo", methods=['GET','POST'])#Definimos el metodo 'get' y 'post' para poder enviar y recibir informacion del formulario 
def nuevo():
    if request.method == 'POST':

        nombre = request.form['nombre']
        if not nombre.strip():
            flash("Nombre es un campo obligatorio")
            return render_template("nuevo_material.html") 
               
        especificacion = request.form['especificacion']
        if not especificacion.strip():
            flash("Especifica el material a ingresar")
            return render_template("nuevo_material.html")
        
        unidad = request.form.get('unidad')
        if not unidad:
            flash("Es necesario seleccionar Unidad de medida")
            return render_template("nuevo_material.html")
        
        descripcion = request.form['descripcion']
        print(nombre, especificacion, unidad, descripcion)
    return render_template("nuevo_material.html")