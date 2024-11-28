from flask import Blueprint, request, jsonify, make_response
from models.entrega import Entrega
from utils.db import db
from schemas.entrega_schema import entrega_schema, entregas_schema
from flask_jwt_extended import jwt_required

entregas = Blueprint('entregas', __name__)

@entregas.route('/entregas/get', methods=['GET'])
@jwt_required()
def get_entregas():
    result = {}
    entregas = Entrega.query.all()
    result = entregas_schema.dump(entregas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'entregas': result
    }

    return make_response(jsonify(data), 200)

@entregas.route('/entregas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    tipo_entrega = data.get('tipo_entrega')
    fecha_entrega = data.get('fecha_entrega')
    estado_entrega = data.get('estado_entrega')
    pedido_id = data.get('pedido_id')
    
    if tipo_entrega==None or fecha_entrega==None or estado_entrega==None or pedido_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    entrega = Entrega(tipo_entrega, fecha_entrega, estado_entrega, pedido_id)
    db.session.add(entrega)
    db.session.commit()
    
    data = {
        'message': 'Entrega creada con éxito',
        'status': 201,
        'entrega': entrega_schema.dump(entrega)
    }
    
    return make_response(jsonify(data), 201)

@entregas.route('/entregas/update/<int:entrega_id>', methods=['PUT'])
@jwt_required()
def update(entrega_id):
    entrega = Entrega.query.get(entrega_id)
    
    if not entrega:
        data = {
            'message': 'Entrega no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    entrega.tipo_entrega = request.get_json().get('tipo_entrega')
    entrega.fecha_entrega = request.get_json().get('fecha_entrega')
    entrega.estado_entrega = request.get_json().get('estado_entrega')
    entrega.pedido_id = request.get_json().get('pedido_id')
    
    db.session.commit()
    
    data = {
        'message': 'Entrega actualizada con éxito',
        'status': 200,
        'entrega': entrega_schema.dump(entrega)
    }
    
    return make_response(jsonify(data), 200)

@entregas.route('/entregas/delete/<int:entrega_id>', methods=['DELETE'])
@jwt_required()
def delete(entrega_id):
    entrega = Entrega.query.get(entrega_id)
    
    if not entrega:
        data = {
            'message': 'Entrega no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(entrega)
    db.session.commit()
        
    data = {
        'message': 'Entrega eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)