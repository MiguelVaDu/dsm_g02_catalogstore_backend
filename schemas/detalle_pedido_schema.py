from utils.ma import ma
from models.detalle_pedido import Detalle_pedido
from schemas.pedido_schema import PedidoSchema
from schemas.producto_schema import ProductoSchema

class DetallePedidoSchema(ma.Schema):
    class Meta:
        model = Detalle_pedido
        fields = (
            'detalle_id',
            'unidades',
            'costo_unidad',
            'descuento',
            'total'
        )
    pedido = ma.Nested(PedidoSchema)
    producto = ma.Nested(ProductoSchema)

detalle_pedido_schema = DetallePedidoSchema()
detalles_pedido_schema = DetallePedidoSchema(many=True)