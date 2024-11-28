from flask import Blueprint, request, jsonify, make_response
from models.devolucion import Devolucion
from utils.db import db
from schemas.devolucion_schema import devolucion_schema, devoluciones_schema
from flask_jwt_extended import jwt_required

devoluciones = Blueprint('devoluciones', __name__)

@devoluciones.route('/devoluciones/get', methods=['GET'])
@jwt_required()
def get_devoluciones():
    result = {}
    devoluciones = Devolucion.query.all()
    result = devoluciones_schema.dump(devoluciones)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'devoluciones': result
    }

    return make_response(jsonify(data), 200)

@devoluciones.route('/devoluciones/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    cantidad = data.get('cantidad')
    motivo = data.get('motivo')
    fecha_devolucion = data.get('fecha_devolucion')
    sku = data.get('sku')
    pedido_id = data.get('pedido_id')
    
    if cantidad==None or motivo==None or fecha_devolucion==None or sku==None or pedido_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    devolucion = Devolucion(cantidad, motivo, fecha_devolucion, sku, pedido_id)
    db.session.add(devolucion)
    db.session.commit()
    
    data = {
        'message': 'Devolucion creada con éxito',
        'status': 201,
        'devolucion': devolucion_schema.dump(devolucion)
    }
    
    return make_response(jsonify(data), 201)

@devoluciones.route('/devoluciones/update/<int:devolucion_id>', methods=['PUT'])
@jwt_required()
def update(devolucion_id):
    devolucion = Devolucion.query.get(devolucion_id)
    
    if not devolucion:
        data = {
            'message': 'Devolucion no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    devolucion.cantidad = request.get_json().get('cantidad')
    devolucion.motivo = request.get_json().get('motivo')
    devolucion.fecha_devolucion = request.get_json().get('fecha_devolucion')
    devolucion.sku = request.get_json().get('sku')
    devolucion.pedido_id = request.get_json().get('pedido_id')
    
    db.session.commit()
    
    data = {
        'message': 'Devolucion actualizada con éxito',
        'status': 200,
        'devolucion': devolucion_schema.dump(devolucion)
    }
    
    return make_response(jsonify(data), 200)

@devoluciones.route('/devoluciones/delete/<int:devolucion_id>', methods=['DELETE'])
@jwt_required()
def delete(devolucion_id):
    devolucion = Devolucion.query.get(devolucion_id)
    
    if not devolucion:
        data = {
            'message': 'Devolucion no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(devolucion)
    db.session.commit()
        
    data = {
        'message': 'Devolucion eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)