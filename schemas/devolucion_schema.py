from utils.ma import ma
from models.devolucion import Devolucion
from schemas.producto_schema import ProductoSchema
from schemas.pedido_schema import PedidoSchema

class DevolucionSchema(ma.Schema):
    class Meta:
        model = Devolucion
        fields = (
            'devolucion_id',
            'cantidad',
            'fecha_devolucion'
        )
    producto = ma.Nested(ProductoSchema)
    pedido = ma.Nested(PedidoSchema)

devolucion_schema = DevolucionSchema()
devoluciones_schema = DevolucionSchema(many=True)