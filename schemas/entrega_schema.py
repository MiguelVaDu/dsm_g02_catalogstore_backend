from utils.ma import ma
from models.entrega import Entrega
from schemas.pedido_schema import PedidoSchema

class EntregaSchema(ma.Schema):
    class Meta:
        model = Entrega
        fields = (
            'entrega_id',
            'tipo_entrega',
            'fecha_entrega',
            'estado_entrega'
        )
    pedido = ma.Nested(PedidoSchema)

entrega_schema = EntregaSchema()
entregas_schema = EntregaSchema(many=True)