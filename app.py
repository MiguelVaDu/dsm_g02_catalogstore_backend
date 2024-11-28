from flask import Flask
from utils.db import db
from config import DATABASE_CONNECTION
from flask_migrate import Migrate
from services.categoria import categorias
from services.cliente import clientes
from services.detalle_pedido import detalles_pedido
from services.devolucion import devoluciones
from services.entrega import entregas
from services.inventario import inventarios
from services.pedido import pedidos
from services.persona import personas
from services.producto import productos
from services.tipo_comprobante import tipos_comprobante
from services.usuario import usuarios
from services.vendedor import vendedores

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app=Flask(__name__)

app.config['SECRET_KEY']=''
app.config['JWT_SECRET_KEY']=''
app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=2)
app.config['JWT_REFRESH_TOKEN_EXPIRES']=timedelta(days=1)

jwt=JWTManager(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
db.init_app(app)

app.register_blueprint(categorias)
app.register_blueprint(clientes)
app.register_blueprint(detalles_pedido)
app.register_blueprint(devoluciones)
app.register_blueprint(entregas)
app.register_blueprint(inventarios)
app.register_blueprint(pedidos)
app.register_blueprint(personas)
app.register_blueprint(productos)
app.register_blueprint(tipos_comprobante)
app.register_blueprint(usuarios)
app.register_blueprint(vendedores)


from services.dto import dto
app.register_blueprint(dto)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)