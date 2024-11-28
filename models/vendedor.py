from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Vendedor(db.Model):
    __tablename__ = 'vendedores'
    
    vendedor_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    
    producto = db.relationship('Producto', backref='vendedor', cascade='all, delete-orphan')
    
    def __init__ (self,usuario_id):
        self.usuario_id = usuario_id