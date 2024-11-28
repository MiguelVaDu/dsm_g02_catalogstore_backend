from utils.db import db
from dataclasses import dataclass
from models.pedido import Pedido

@dataclass
class Entrega(db.Model):
    __tablename__ = 'entregas'
    
    entrega_id = db.Column(db.Integer, primary_key=True)
    tipo_entrega = db.Column(db.String(50))
    fecha_entrega = db.Column(db.DateTime)
    estado_entrega = db.Column(db.String(10))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    
    def __init__ (self,tipo_entrega,fecha_entrega,estado_entrega,pedido_id):
        self.tipo_entrega = tipo_entrega
        self.fecha_entrega = fecha_entrega
        self.estado_entrega = estado_entrega
        self.pedido_id = pedido_id