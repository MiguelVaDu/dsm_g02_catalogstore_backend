from flask import Blueprint, request, jsonify, make_response
from models.vendedor import Vendedor
from utils.db import db
from schemas.vendedor_schema import vendedor_schema, vendedores_schema
from flask_jwt_extended import jwt_required

vendedores = Blueprint('vendedores', __name__)

@vendedores.route('/vendedores/get', methods=['GET'])
@jwt_required()
def get_vendedores():
    result = {}
    vendedores = Vendedor.query.all()
    result = vendedores_schema.dump(vendedores)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'vendedores': result
    }

    return make_response(jsonify(data), 200)

@vendedores.route('/vendedores/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    usuario_id = data.get('usuario_id')
    
    if usuario_id==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    vendedor = Vendedor(usuario_id)
    db.session.add(vendedor)
    db.session.commit()
    
    data = {
        'message': 'Vendedor creado con éxito',
        'status': 201,
        'vendedor': vendedor_schema.dump(vendedor)
    }
    
    return make_response(jsonify(data), 201)

@vendedores.route('/vendedores/update/<int:vendedor_id>', methods=['PUT'])
@jwt_required()
def update(vendedor_id):
    vendedor = Vendedor.query.get(vendedor_id)
    
    if not vendedor:
        data = {
            'message': 'Vendedor no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    vendedor.usuario_id = request.get_json().get('usuario_id')
    
    db.session.commit()
    
    data = {
        'message': 'Vendedor actualizado con éxito',
        'status': 200,
        'vendedor': vendedor_schema.dump(vendedor)
    }
    
    return make_response(jsonify(data), 200)

@vendedores.route('/vendedores/delete/<int:vendedor_id>', methods=['DELETE'])
@jwt_required()
def delete(vendedor_id):
    vendedor = Vendedor.query.get(vendedor_id)
    
    if not vendedor:
        data = {
            'message': 'Vendedor no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(vendedor)
    db.session.commit()
        
    data = {
        'message': 'Vendedor eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)