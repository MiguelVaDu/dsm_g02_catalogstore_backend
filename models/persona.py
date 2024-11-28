from utils.db import db
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    __tablename__ = 'personas'
    
    documento = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(9))
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    fecha_nacimiento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))
    direccion = db.Column(db.String(60))
    
    
    usuario = db.relationship('Usuario', backref='persona', cascade='all, delete-orphan')
    
    def __init__ (self,tipo_documento,nombre,apellido_paterno,apellido_materno,telefono,fecha_nacimiento,sexo,direccion):
        self.tipo_documento = tipo_documento
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.direccion = direccion