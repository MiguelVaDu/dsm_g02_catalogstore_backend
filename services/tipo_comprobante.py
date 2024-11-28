from flask import Blueprint, request, jsonify, make_response
from models.tipo_comprobante import Tipo_comprobante
from utils.db import db
from schemas.tipo_comprobante_schema import tipo_comprobante_schema, tipos_comprobante_schema
from flask_jwt_extended import jwt_required

tipos_comprobante = Blueprint('tipos_comprobante', __name__)

@tipos_comprobante.route('/tipos_comprobante/get', methods=['GET'])
@jwt_required()
def get_tipos_comprobante():
    result = {}
    tipos_comprobante = Tipo_comprobante.query.all()
    result = tipos_comprobante_schema.dump(tipos_comprobante)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'tipos_comprobante': result
    }

    return make_response(jsonify(data), 200)

@tipos_comprobante.route('/tipos_comprobante/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    descripcion_comprobante = data.get('descripcion_comprobante')
    serie = data.get('serie')
    correlativo = data.get('correlativo')
    
    if descripcion_comprobante==None or serie==None or correlativo==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    tipo_comprobante = Tipo_comprobante(descripcion_comprobante, serie, correlativo)
    db.session.add(tipo_comprobante)
    db.session.commit()
    
    data = {
        'message': 'Tipo del comprobante creado con éxito',
        'status': 201,
        'tipo_comprobante': tipo_comprobante_schema.dump(tipo_comprobante)
    }
    
    return make_response(jsonify(data), 201)

@tipos_comprobante.route('/tipos_comprobante/update/<int:comprobante_id>', methods=['PUT'])
@jwt_required()
def update(comprobante_id):
    tipo_comprobante = Tipo_comprobante.query.get(comprobante_id)
    
    if not tipo_comprobante:
        data = {
            'message': 'Tipo de comprobante no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    tipo_comprobante.descripcion_comprobante = request.get_json().get('descripcion_comprobante')
    tipo_comprobante.serie = request.get_json().get('serie')
    tipo_comprobante.correlativo = request.get_json().get('correlativo')
    
    db.session.commit()
    
    data = {
        'message': 'Tipo de comprobante actualizado con éxito',
        'status': 200,
        'tipo_comprobante': tipo_comprobante_schema.dump(tipo_comprobante)
    }
    
    return make_response(jsonify(data), 200)

@tipos_comprobante.route('/tipos_comprobante/delete/<int:comprobante_id>', methods=['DELETE'])
@jwt_required()
def delete(comprobante_id):
    tipo_comprobante = Tipo_comprobante.query.get(comprobante_id)
    
    if not tipo_comprobante:
        data = {
            'message': 'Tipo de comprobante no encontrado',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(tipo_comprobante)
    db.session.commit()
        
    data = {
        'message': 'Tipo de comprobante eliminado con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)