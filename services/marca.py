from flask import Blueprint, request, jsonify, make_response
from models.marca import Marca
from utils.db import db
from schemas.marca_schema import marca_schema, marcas_schema
from flask_jwt_extended import jwt_required

marcas = Blueprint('marcas', __name__)

@marcas.route('/marcas/get', methods=['GET'])
@jwt_required()
def get_marcas():
    result = {}
    marcas = Marca.query.all()
    result = marcas_schema.dump(marcas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'marcas': result
    }

    return make_response(jsonify(data), 200)

@marcas.route('/marcas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    descripcion = data.get('descripcion')
    
    if descripcion==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    marca = Marca(descripcion)
    db.session.add(marca)
    db.session.commit()
    
    data = {
        'message': 'Marca creada con éxito',
        'status': 201,
        'marca': marca_schema.dump(marca)
    }
    
    return make_response(jsonify(data), 201)

@marcas.route('/marcas/update/<int:marca_id>', methods=['PUT'])
@jwt_required()
def update(marca_id):
    marca = Marca.query.get(marca_id)
    
    if not marca:
        data = {
            'message': 'Marca no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    marca.descripcion = request.get_json().get('descripcion')
    
    db.session.commit()
    
    data = {
        'message': 'Marca actualizada con éxito',
        'status': 200,
        'marca': marca_schema.dump(marca)
    }
    
    return make_response(jsonify(data), 200)

@marcas.route('/marcas/delete/<int:marca_id>', methods=['DELETE'])
@jwt_required()
def delete(marca_id):
    marca = Marca.query.get(marca_id)
    
    if not marca:
        data = {
            'message': 'Marca no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(marca)
    db.session.commit()
        
    data = {
        'message': 'Marca eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)