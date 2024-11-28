from utils.db import db
from dataclasses import dataclass
from models.producto import Producto
from models.pedido import Pedido

@dataclass
class Devolucion(db.Model):
    __tablename__ = 'devoluciones'
    
    devolucion_id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    motivo = db.Column(db.String(250))
    fecha_devolucion = db.Column(db.DateTime)
    sku = db.Column(db.Integer, db.ForeignKey('productos.sku'))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    
    def __init__ (self,cantidad,motivo,fecha_devolucion,sku,pedido_id):
        self.cantidad = cantidad
        self.motivo = motivo
        self.fecha_devolucion = fecha_devolucion
        self.sku = sku
        self.pedido_id = pedido_id