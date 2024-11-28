from utils.db import db
from dataclasses import dataclass
from models.categoria import Categoria
from models.marca import Marca


@dataclass
class Producto(db.Model):
    __tablename__ = 'productos'
    
    sku = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    precio = db.Column(db.Numeric(10,2))
    imagen = db.Column(db.Float)
    descripcion = db.Column(db.String(250))
    unidades = db.Column(db.Integer)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'))
    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.marca_id'))
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedores.vendedor_id'))
    
    devolucion = db.relationship('Devolucion', backref='producto', cascade='all, delete-orphan')
    detalle_pedido = db.relationship('Detalle_pedido', backref='producto', cascade='all, delete-orphan')
    inventario = db.relationship('Inventario', backref='producto', cascade='all, delete-orphan')
    
    def __init__ (self,nombre,precio,imagen,descripcion,unidades,categoria_id,marca_id,vendedor_id):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.descripcion = descripcion
        self.unidades = unidades
        self.categoria_id = categoria_id
        self.marca_id = marca_id
        self.vendedor_id = vendedor_id