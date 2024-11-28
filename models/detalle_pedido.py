from utils.db import db
from dataclasses import dataclass
from models.producto import Producto
from models.pedido import Pedido

@dataclass
class Detalle_pedido(db.Model):
    __tablename__ = 'detalle_pedidos'
    
    detalle_id = db.Column(db.Integer, primary_key=True)
    unidades = db.Column(db.Integer)
    costo_unidad = db.Column(db.Numeric(10,2))
    descuento = db.Column(db.Numeric(10,2))
    total = db.Column(db.Numeric(10,2))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    sku = db.Column(db.Integer, db.ForeignKey('productos.sku'))
    
    def __init__ (self,unidades,costo_unidad,descuento,total,pedido_id,sku):
        self.unidades = unidades
        self.costo_unidad = costo_unidad
        self.descuento = descuento
        self.total = total
        self.pedido_id = pedido_id
        self.sku = sku