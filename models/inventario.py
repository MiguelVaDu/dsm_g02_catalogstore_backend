from utils.db import db
from dataclasses import dataclass
from models.producto import Producto

@dataclass
class Inventario(db.Model):
    __tablename__ = 'inventarios'
    
    inventario_id = db.Column(db.Integer, primary_key=True)
    fecha_registro = db.Column(db.DateTime)
    motivo = db.Column(db.String(250))
    sku = db.Column(db.Integer, db.ForeignKey('productos.sku'))
        
    def __init__ (self,fecha_registro,motivo,sku):
        self.fecha_registro = fecha_registro
        self.motivo = motivo
        self.sku = sku