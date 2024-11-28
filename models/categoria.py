from utils.db import db
from dataclasses import dataclass

@dataclass
class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    categoria_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    descripcion = db.Column(db.String(250))

    producto = db.relationship('Producto', backref='categoria', cascade = 'all, delete-orphan')

    def __init__ (self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

