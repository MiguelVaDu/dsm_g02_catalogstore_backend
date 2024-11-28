from flask import Blueprint, request, jsonify, make_response
from models.pedido import Pedido
from utils.db import db
from schemas.pedido_schema import pedido_schema, pedidos_schema
from flask_jwt_extended import jwt_required

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos/get', methods=['GET'])
@jwt_required()
def get_pedidos():
    result = {}
    pedidos = Pedido.query.all()
    result = pedidos_schema.dump(pedidos)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'pedidos': result
    }

    return make_response(jsonify(data), 200)

@pedidos.route('/pedidos/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    fecha_pedido = data.get('fecha_pedido')
    estado_pedido = data.get('estado_pedido')
    igv = data.get('igv')
    subtotal = data.get('subtotal')
    monto_total = data.get('monto_total')
    cliente_id = data.get('cliente_id')
    comprobante_id = data.get('comprobante_id')
    
    if fecha_pedido==None or estado_pedido==None or igv==None or subtotal==None or monto_total==None or cliente_id==None or comprobante_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    pedido = Pedido(fecha_pedido, estado_pedido, igv, subtotal, monto_total, cliente_id, comprobante_id)
    db.session.add(pedido)
    db.session.commit()
    
    data = {
        'message': 'Pedido creado con éxito',
        'status': 201,
        'pedido': pedido_schema.dump(pedido)
    }
    
    return make_response(jsonify(data), 201)

@pedidos.route('/pedidos/update/<int:cliente_id>', methods=['PUT'])
@jwt_required()
def update(cliente_id):
    pedido = Pedido.query.get(cliente_id)
    
    if not pedido:
        data = {
            'message': 'Pedido no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    pedido.fecha_pedido = request.get_json().get('fecha_pedido')
    pedido.estado_pedido = request.get_json().get('estado_pedido')
    pedido.igv = request.get_json().get('igv')
    pedido.subtotal = request.get_json().get('subtotal')
    pedido.monto_total = request.get_json().get('monto_total')
    pedido.cliente_id = request.get_json().get('cliente_id')
    pedido.comprobante_id = request.get_json().get('comprobante_id')
    
    db.session.commit()
    
    data = {
        'message': 'Pedido actualizado con éxito',
        'status': 200,
        'pedido': pedido_schema.dump(pedido)
    }
    
    return make_response(jsonify(data), 200)

@pedidos.route('/pedidos/delete/<int:cliente_id>', methods=['DELETE'])
@jwt_required()
def delete(cliente_id):
    pedido = Pedido.query.get(cliente_id)
    
    if not pedido:
        data = {
            'message': 'Pedido no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(pedido)
    db.session.commit()
        
    data = {
        'message': 'Pedido eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)