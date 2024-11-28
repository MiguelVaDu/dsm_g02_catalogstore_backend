from utils.db import db
from dataclasses import dataclass

@dataclass
class Marca(db.Model):
    __tablename__ = 'marcas'
    
    marca_id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))

    producto = db.relationship('Producto', backref='marca', cascade = 'all, delete-orphan')

    def __init__ (self,descripcion):
        self.descripcion = descripcion