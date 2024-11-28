from models.detalle_pedido import Detalle_pedido
from models.pedido import Pedido
from models.producto import Producto
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import selectinload
from utils.db import db

dto = Blueprint('dto', __name__)

@dto.route('/detalles_pedido/dto/get/<int:pedido_id>', methods=['GET'])
def get_detalle_by_pedido(pedido_id):
    detalles_pedido = Detalle_pedido.query.options(
        selectinload(Detalle_pedido.pedido),
        selectinload(Detalle_pedido.producto).selectinload(Producto.nombre),
    ).filter(
        Detalle_pedido.pedido_id == Pedido.pedido_id,
        Detalle_pedido.sku == Producto.sku
    ).filter_by(pedido_id=pedido_id).order_by(Detalle_pedido.detalle_id.desc()).all()
    
    result = [
        {
            "detalle_id": detalle_pedido.detalle_id,
            "unidades": detalle_pedido.unidades,
            "costo_unidad": str(detalle_pedido.costo_unidad),
            "descuento": str(detalle_pedido.descuento),
            "total": str(detalle_pedido.total),
            "pedido_id": detalle_pedido.pedido_id,
            "sku": detalle_pedido.sku
        } for detalle_pedido in detalles_pedido
    ]
    
    data = {
        'message': 'Lista generada con éxito',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)