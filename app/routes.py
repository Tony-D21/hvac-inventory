from flask import Blueprint, request, render_template, flash
from .models import Material, Almacen
from . import db


main = Blueprint("main", __name__)#Aquí estás creando un blueprint llamado "main", __name__ le dice a Flask en qué módulo está definido, lo que ayuda a ubicar recursos como plantillas o archivos estáticos.
@main.route("/")
def home():
    return render_template("index.html")

@main.route("/inventario")
def inventario ():
    materiales = Material.query.all()#Creamos una variable, y hacemos un query para que nos genere una lista con todos los materiales registros en la database
    return render_template ("inventario.html", materiales=materiales)#retornamos "inventario.html" y nombramos la variable de python a varible de html para llamarla en el for de jinja

@main.route("/inventario/nuevo", methods=['GET','POST'])#Definimos el metodo 'get' y 'post' para poder enviar y recibir informacion del formulario 
def nuevo():
    if request.method == 'POST':
        #Añadimos validaciones
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

        #Hacemos un query para saber cual es el numero mayor de la tabla(siempre sera el ultimo registrado)
        ultimo_material = Material.query.order_by(Material.id.desc()).first()

        #Hacemos una validacion para ver si existe un ultimo material, si si, se le suma un numero al ultimo material 
        if ultimo_material:
            siguiente_numero = ultimo_material.id + 1
        else:
            siguiente_numero = 1
            
        #Formateamos la cadena para que conceptualemente en la Base de datos se escriba: MAT-0001,MAT-0002,MAT-0003.... (04D): 0=Rellena con ceros a la izquierda, 4=Ancho minimo de la cadena(4 caracteres), d=formato decimal(entero)
        codigo = f"MAT-{siguiente_numero:04d}"

        #Creacion de los objetos
        nuevo_material = Material(codigo= codigo, 
                                      nombre= nombre, 
                                      especificacion= especificacion, 
                                      unidad=unidad, 
                                      descripcion=descripcion
                                      )
        #Tomando como analogia git, es practicamente el mismo procedimiento
        db.session.add(nuevo_material)#le decimos a la sesion de SQLAlchemy que queremos añadir este objeto(nuevo_material)
        db.session.commit()#Confirmamos el movimiento
        print("Agregado con exito")

    return render_template("nuevo_material.html")

@main.route("/entrada", methods= ["GET","POST"])
def nueva_entrada():
        if request.method == "POST":
                    material_id = request.form.get("material_id")
                    almacen_id = request.form.get("almacen_id")
                    cantidad = request.form.get("cantidad")
                    unidad = request.form.get("unidad")
                    n_serie = request.form.get("n_serie")
                    estatus = request.form.get("estatus")
                    recepcion = request.form.get("recepcion")
        
        
                    print(material_id)
                    print(almacen_id)
                    print(cantidad)
                    print(unidad)
                    print(n_serie)
                    print(estatus)
                    print(recepcion)

                              
        materiales = Material.query.all()       
        almacenes = Almacen.query.all()

        return render_template(
                               "nueva_entrada.html",
                               materiales=materiales,
                               almacenes=almacenes
                               )

        