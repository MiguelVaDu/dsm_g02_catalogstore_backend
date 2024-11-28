from utils.db import db
from dataclasses import dataclass
from models.cliente import Cliente
from models.tipo_comprobante import Tipo_comprobante

@dataclass
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    
    pedido_id = db.Column(db.Integer, primary_key=True)
    fecha_pedido = db.Column(db.DateTime)
    estado_pedido = db.Column(db.String(10))
    igv = db.Column(db.Numeric(10,2))
    subtotal = db.Column(db.Numeric(10,2))
    monto_total = db.Column(db.Numeric(10,2))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'))
    comprobante_id = db.Column(db.Integer, db.ForeignKey('comprobantes.comprobante_id'))
    
    entrega = db.relationship('Entrega', backref='pedido', cascade='all, delete-orphan')
    devolucion = db.relationship('Devolucion', backref='pedido', cascade='all, delete-orphan')
    detalle_pedido = db.relationship('Detalle_pedido', backref='pedido', cascade='all, delete-orphan')
    
    def __init__ (self,fecha_pedido,estado_pedido,igv,subtotal,monto_total,cliente_id,comprobante_id):
        self.fecha_pedido = fecha_pedido
        self.estado_pedido = estado_pedido
        self.igv = igv
        self.subtotal = subtotal
        self.monto_total = monto_total
        self.cliente_id = cliente_id
        self.comprobante_id = comprobante_id