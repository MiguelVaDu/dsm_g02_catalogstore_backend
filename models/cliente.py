from utils.db import db
from dataclasses import dataclass
from models.usuario import Usuario

@dataclass
class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    cliente_id = db.Column(db.Integer, primary_key=True)
    preferencias = db.Column(db.String(50))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'))
    
    pedido = db.relationship('Pedido', backref='cliente', cascade='all, delete-orphan')
    
    def __init__ (self,preferencias,usuario_id):
        self.preferencias = preferencias
        self.usuario_id = usuario_id