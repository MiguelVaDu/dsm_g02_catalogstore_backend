from utils.db import db
from dataclasses import dataclass

@dataclass
class Tipo_comprobante(db.Model):
    __tablename__ = 'tipo_comprobantes'
    
    comprobante_id = db.Column(db.Integer, primary_key=True)
    descripcion_comprobante = db.Column(db.String(150))
    serie = db.Column(db.String(10))
    correlativo = db.Column(db.String(10))
    
    pedido = db.relationship('Pedido', backref='tipo_comprobante', cascade='all, delete-orphan')
    
    def __init__ (self,descripcion_comprobante, serie, correlativo):
        self.descripcion_comprobante = descripcion_comprobante
        self.serie = serie
        self.correlativo = correlativo