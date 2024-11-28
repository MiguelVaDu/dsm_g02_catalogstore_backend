from flask import Blueprint, request, jsonify, make_response
from models.detalle_pedido import Detalle_pedido
from utils.db import db
from schemas.detalle_pedido_schema import detalle_pedido_schema, detalles_pedido_schema
from flask_jwt_extended import jwt_required

detalles_pedido = Blueprint('detalles_pedido', __name__)

@detalles_pedido.route('/detalles_pedido/get', methods=['GET'])
@jwt_required()
def get_detalles_pedido():
    result = {}
    detalles_pedido = Detalle_pedido.query.all()
    result = detalles_pedido_schema.dump(detalles_pedido)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'detalles_pedido': result
    }

    return make_response(jsonify(data), 200)

@detalles_pedido.route('/detalles_pedido/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    unidades = data.get('unidades')
    costo_unidad = data.get('costo_unidad')
    descuento = data.get('descuento')
    total = data.get('total')
    pedido_id = data.get('pedido_id')
    sku = data.get('sku')
    
    if unidades==None or costo_unidad==None or descuento==None or total==None or pedido_id==None or sku==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    detalle_pedido = Detalle_pedido(unidades, costo_unidad, descuento, total, pedido_id, sku)
    db.session.add(detalle_pedido)
    db.session.commit()
    
    data = {
        'message': 'Detalle del pedido creado con éxito',
        'status': 201,
        'detalle_pedido': detalle_pedido_schema.dump(detalle_pedido)
    }
    
    return make_response(jsonify(data), 201)

@detalles_pedido.route('/detalles_pedido/update/<int:detalle_id>', methods=['PUT'])
@jwt_required()
def update(detalle_id):
    detalle_pedido = Detalle_pedido.query.get(detalle_id)
    
    if not detalle_pedido:
        data = {
            'message': 'Detalle del pedido no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    detalle_pedido.unidades = request.get_json().get('unidades')
    detalle_pedido.costo_unidad = request.get_json().get('costo_unidad')
    detalle_pedido.descuento = request.get_json().get('descuento')
    detalle_pedido.total = request.get_json().get('total')
    detalle_pedido.pedido_id = request.get_json().get('pedido_id')
    detalle_pedido.sku = request.get_json().get('sku')
    
    db.session.commit()
    
    data = {
        'message': 'Detalle del pedido actualizado con éxito',
        'status': 200,
        'detalle_pedido': detalle_pedido_schema.dump(detalle_pedido)
    }
    
    return make_response(jsonify(data), 200)

@detalles_pedido.route('/detalles_pedido/delete/<int:detalle_id>', methods=['DELETE'])
@jwt_required()
def delete(detalle_id):
    detalle_pedido = Detalle_pedido.query.get(detalle_id)
    
    if not detalle_pedido:
        data = {
            'message': 'Detalle del pedido no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(detalle_pedido)
    db.session.commit()
        
    data = {
        'message': 'Detalle del pedido eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)