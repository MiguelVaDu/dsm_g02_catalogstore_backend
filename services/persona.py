from flask import Blueprint, request, jsonify, make_response
from models.persona import Persona
from utils.db import db
from schemas.persona_schema import persona_schema, personas_schema
from flask_jwt_extended import jwt_required

personas = Blueprint('personas', __name__)

@personas.route('/personas/get', methods=['GET'])
@jwt_required()
def get_personas():
    result = {}
    personas = Persona.query.all()
    result = personas_schema.dump(personas)
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'personas': result
    }

    return make_response(jsonify(data), 200)

@personas.route('/personas/insert', methods=['POST'])
@jwt_required()
def insert():
    data = request.get_json()
    
    documento = data.get("documento")
    tipo_documento = data.get('tipo_documento')
    nombre = data.get('nombre')
    apellido_paterno = data.get('apellido_paterno')
    apellido_materno = data.get('apellido_materno')
    telefono = data.get('telefono')
    fecha_nacimiento = data.get('fecha_nacimiento')
    sexo = data.get('sexo')
    direccion = data.get('direccion')
    
    if documento==None or tipo_documento==None or nombre==None or apellido_paterno==None or apellido_materno==None or telefono==None or fecha_nacimiento==None or sexo==None or direccion==None:
        data = {
            'message': 'Faltan datos',
            'status': 400
        }
        
        return make_response(jsonify(data), 400)
    
    persona = Persona(documento, tipo_documento, nombre, apellido_paterno, apellido_materno, telefono, fecha_nacimiento, sexo, direccion)
    db.session.add(persona)
    db.session.commit()
    
    data = {
        'message': 'Persona creada con éxito',
        'status': 201,
        'persona': persona_schema.dump(persona)
    }
    
    return make_response(jsonify(data), 201)

@personas.route('/personas/update/<int:documento>', methods=['PUT'])
@jwt_required()
def update(documento):
    persona = Persona.query.get(documento)
    
    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    persona.documento = request.get_json().get("documento")
    persona.tipo_documento = request.get_json().get('tipo_documento')
    persona.nombre = request.get_json().get('nombre')
    persona.apellido_paterno = request.get_json().get('apellido_paterno')
    persona.apellido_materno = request.get_json().get('apellido_materno')
    persona.telefono = request.get_json().get('telefono')
    persona.fecha_nacimiento = request.get_json().get('fecha_nacimiento')
    persona.sexo = request.get_json().get('sexo')
    persona.direccion = request.get_json().get('direccion')
    
    db.session.commit()
    
    data = {
        'message': 'Persona actualizada con éxito',
        'status': 200,
        'persona': persona_schema.dump(persona)
    }
    
    return make_response(jsonify(data), 200)

@personas.route('/personas/delete/<int:documento>', methods=['DELETE'])
@jwt_required()
def delete(documento):
    persona = Persona.query.get(documento)
    
    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        
        return make_response(jsonify(data), 404)
    
    db.session.delete(persona)
    db.session.commit()
        
    data = {
        'message': 'Persona eliminada con éxito',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)