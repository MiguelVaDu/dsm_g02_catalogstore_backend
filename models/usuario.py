from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash
from models.usuario import Usuario

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    usuario_id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(15))
    password = db.Column(db.String(50))
    documento = db.Column(db.Integer, db.ForeignKey('personas.documento'))
    
    cliente = db.relationship('Cliente', backref='usuario', cascade='all, delete-orphan')
    vendedor = db.relationship('Vendedor', backref='usuario', cascade='all, delete-orphan')
    
    def __init__ (self,correo,password,documento):
        self.correo = correo
        self.password = generate_password_hash(password)
        self.documento = documento