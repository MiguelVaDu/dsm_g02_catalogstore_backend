from utils.ma import ma
from models.pedido import Pedido
from schemas.cliente_schema import ClienteSchema
from schemas.tipo_comprobante_schema import TipoComprobanteSchema

class PedidoSchema(ma.Schema):
    class Meta:
        model = Pedido
        fields = (
            'pedido_id',
            'fecha_pedido',
            'estado_pedido',
            'igv',
            'subtotal',
            'monto_total'
        )
    cliente = ma.Nested(ClienteSchema)
    tipo_comprobante = ma.Nested(TipoComprobanteSchema)

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)