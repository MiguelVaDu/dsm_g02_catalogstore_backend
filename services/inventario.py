from flask import Blueprint, request, jsonify, make_response
from models.inventario import Inventario
from utils.db import db
from schemas.inventario_schema import inventario_schema, inventarios_schema
from flask_jwt_extended import jwt_required

inventarios = Blueprint('inventarios', __name__)

@inventarios.route('/inventarios/get', methods=['GET'])
@jwt_required()
def get_inventarios():
    result = {}
    inventarios = Inventario.query.all()
    result = inventarios_schema.dump(inventarios)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'inventarios': result
    }

    return make_response(jsonify(data), 200)

@inventarios.route('/inventarios/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    fecha_registro = data.get('fecha_registro')
    motivo = data.get('motivo')
    sku = data.get('sku')
    
    if fecha_registro==None or motivo==None or sku==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    inventario = Inventario(fecha_registro, motivo, sku)
    db.session.add(inventario)
    db.session.commit()
    
    data = {
        'message': 'Inventario creado con éxito',
        'status': 201,
        'inventario': inventario_schema.dump(inventario)
    }
    
    return make_response(jsonify(data), 201)

@inventarios.route('/inventarios/update/<int:inventario_id>', methods=['PUT'])
@jwt_required()
def update(inventario_id):
    inventario = Inventario.query.get(inventario_id)
    
    if not inventario:
        data = {
            'message': 'Inventario no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    inventario.fecha_registro = request.get_json().get('fecha_registro')
    inventario.motivo = request.get_json().get('motivo')
    inventario.sku = request.get_json().get('sku')
    
    db.session.commit()
    
    data = {
        'message': 'Inventario actualizado con éxito',
        'status': 200,
        'inventario': inventario_schema.dump(inventario)
    }
    
    return make_response(jsonify(data), 200)

@inventarios.route('/inventarios/delete/<int:inventario_id>', methods=['DELETE'])
@jwt_required()
def delete(inventario_id):
    inventario = Inventario.query.get(inventario_id)
    
    if not inventario:
        data = {
            'message': 'Inventario no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(inventario)
    db.session.commit()
        
    data = {
        'message': 'Inventario eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)