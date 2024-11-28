from flask import Blueprint, request, jsonify, make_response
from models.producto import Producto
from utils.db import db
from schemas.producto_schema import producto_schema, productos_schema
from flask_jwt_extended import jwt_required

productos = Blueprint('productos', __name__)

@productos.route('/productos/get', methods=['GET'])
@jwt_required()
def get_productos():
    result = {}
    productos = Producto.query.all()
    result = productos_schema.dump(productos)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'productos': result
    }

    return make_response(jsonify(data), 200)

@productos.route('/productos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    sku = data.get('sku')
    nombre = data.get('nombre')
    precio = data.get('precio')
    imagen = data.get('imagen')
    descripcion = data.get('descripcion')
    unidades = data.get('unidades')
    categoria_id = data.get('categoria_id')
    marca_id = data.get('marca_id')
    vendedor_id = data.get('vendedor_id')
    
    if sku==None or nombre==None or precio==None or imagen==None or descripcion==None or unidades==None or categoria_id==None or marca_id==None or vendedor_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    producto = Producto(sku, nombre, precio, imagen, descripcion, unidades, categoria_id, marca_id, vendedor_id)
    db.session.add(producto)
    db.session.commit()
    
    data = {
        'message': 'Producto creado con éxito',
        'status': 201,
        'producto': producto_schema.dump(producto)
    }
    
    return make_response(jsonify(data), 201)

@productos.route('/productos/update/<int:sku>', methods=['PUT'])
@jwt_required()
def update(sku):
    producto = Producto.query.get(sku)
    
    if not producto:
        data = {
            'message': 'Producto no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    producto.sku = request.get_json().get('sku')
    producto.nombre = request.get_json().get('nombre')
    producto.precio = request.get_json().get('precio')
    producto.imagen = request.get_json().get('imagen')
    producto.descripcion = request.get_json().get('descripcion')
    producto.unidades = request.get_json().get('unidades')
    producto.categoria_id = request.get_json().get('categoria_id')
    producto.marca_id = request.get_json().get('marca_id')
    producto.vendedor_id = request.get_json().get('vendedor_id')
    
    db.session.commit()
    
    data = {
        'message': 'Producto actualizado con éxito',
        'status': 200,
        'producto': producto_schema.dump(producto)
    }
    
    return make_response(jsonify(data), 200)

@productos.route('/productos/delete/<int:sku>', methods=['DELETE'])
@jwt_required()
def delete(sku):
    producto = Producto.query.get(sku)
    
    if not producto:
        data = {
            'message': 'Producto no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(producto)
    db.session.commit()
        
    data = {
        'message': 'Producto eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)