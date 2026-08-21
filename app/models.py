from sqlalchemy import Column, Integer, String
from . import db

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

