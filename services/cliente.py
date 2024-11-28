from flask import Blueprint, request, jsonify, make_response
from models.cliente import Cliente
from utils.db import db
from schemas.cliente_schema import cliente_schema, clientes_schema
from flask_jwt_extended import jwt_required

clientes = Blueprint('clientes', __name__)

@clientes.route('/clientes/get', methods=['GET'])
@jwt_required()
def get_clientes():
    result = {}
    clientes = Cliente.query.all()
    result = clientes_schema.dump(clientes)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'clientes': result
    }

    return make_response(jsonify(data), 200)

@clientes.route('/clientes/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    preferencias = data.get('preferencias')
    usuario_id = data.get('usuario_id')

    if preferencias==None or usuario_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    cliente = Cliente(preferencias, usuario_id)
    db.session.add(cliente)
    db.session.commit()
    
    data = {
        'message': 'Cliente creado con éxito',
        'status': 201,
        'cliente': cliente_schema.dump(cliente)
    }
    
    return make_response(jsonify(data), 201)

@clientes.route('/clientes/update/<int:cliente_id>', methods=['PUT'])
@jwt_required()
def update(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    
    if not cliente:
        data = {
            'message': 'Cliente no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    cliente.preferencias = request.get_json().get('preferencias')
    cliente.usuario_id = request.get_json().get('usuario_id')
    
    db.session.commit()
    
    data = {
        'message': 'Cliente actualizado con éxito',
        'status': 200,
        'cliente': cliente_schema.dump(cliente)
    }
    
    return make_response(jsonify(data), 200)

@clientes.route('/clientes/delete/<int:cliente_id>', methods=['DELETE'])
@jwt_required()
def delete(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    
    if not cliente:
        data = {
            'message': 'Cliente no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(cliente)
    db.session.commit()
        
    data = {
        'message': 'Cliente eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)