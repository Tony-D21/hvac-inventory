from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import db
from datetime import datetime

class Material(db.Model):
    __tablename__ = "Materiales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable=False, unique=True)
    nombre = Column(String(50), nullable=False)
    especificacion = Column(String(100), nullable=False)
    unidad = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=True)

    def __repr__(self):
        return f"Material(id={self.id}, nombre='{self.nombre}', unidad='{self.unidad}', descripcion='{self.descripcion}')"



class Almacen(db.Model):
    __tablename__ = "Almacenes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False )
    ciudad = Column(String(50), nullable=False)

class Inventario(db.Model):
    __tablename__ = "Inventario"
    #id
    id = Column(Integer, primary_key=True, autoincrement=True)
    #material_id
    material_id = Column(Integer, ForeignKey("Materiales.id"), nullable=False)#creamos nuestra llave foranea y le decimos que id utilizar, en esta caso ("Materiales=corresponde a la tabla   .id= Columna") "relaciona las tablas en la base de datos"
    material = relationship("Material") #Informamos sqlalchemy sobre la conexion 
    #cantidad
    cantidad = Column(Float, nullable=False)
    #almacen_id
    #creamos la llave foranea
    almacen_id = Column(Integer, ForeignKey("Almacenes.id"), nullable=False)
    #Informamos sqlalchemy sobre la conexion
    almacen = relationship("Almacen")#Le decimos a sqlalchemy sobre la conexion

class Movimiento(db.Model):
    __tablename__ = "Movimientos"
    #id
    id = Column(Integer, primary_key=True, autoincrement=True)
    #Creamos la llave foranea
    material_id = Column(Integer, ForeignKey("Materiales.id"), nullable=False)
    #Informamos sqlalchemy sobre la conexion
    material = relationship("Material")
    #creamos la llave foranea
    almacen_id = Column(Integer, ForeignKey("Almacenes.id"), nullable=False)
    #Informamos sqlalchemy sobre la conexion
    almacen = relationship("Almacen")
    tipo = Column(String(50), nullable=False )
    cantidad = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.now, nullable=False)
    observacion = Column(String(255), nullable=True)

    