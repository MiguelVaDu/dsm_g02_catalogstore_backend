from flask import Blueprint, request, jsonify, make_response
from models.categoria import Categoria
from utils.db import db
from schemas.categoria_schema import categoria_schema, categorias_schema
from flask_jwt_extended import jwt_required

categorias = Blueprint('categorias', __name__)

@categorias.route('/categorias/get', methods=['GET'])
@jwt_required()
def get_categorias():
    result = {}
    categorias = Categoria.query.all()
    result = categorias_schema.dump(categorias)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'categorias': result
    }

    return make_response(jsonify(data), 200)

@categorias.route('/categorias/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    
    if nombre==None or descripcion==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    categoria = Categoria(nombre, descripcion)
    db.session.add(categoria)
    db.session.commit()
    
    data = {
        'message': 'Categoria creada con éxito',
        'status': 201,
        'categoria': categoria_schema.dump(categoria)
    }
    
    return make_response(jsonify(data), 201)

@categorias.route('/categorias/update/<int:categoria_id>', methods=['PUT'])
@jwt_required()
def update(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    
    if not categoria:
        data = {
            'message': 'Categoria no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    categoria.nombre = request.get_json().get('nombre')
    categoria.descripcion = request.get_json().get('descripcion')
    
    db.session.commit()
    
    data = {
        'message': 'Categoria actualizada con éxito',
        'status': 200,
        'categoria': categoria_schema.dump(categoria)
    }
    
    return make_response(jsonify(data), 200)

@categorias.route('/categorias/delete/<int:categoria_id>', methods=['DELETE'])
@jwt_required()
def delete(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    
    if not categoria:
        data = {
            'message': 'Categoria no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(categoria)
    db.session.commit()
        
    data = {
        'message': 'Categoria eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)