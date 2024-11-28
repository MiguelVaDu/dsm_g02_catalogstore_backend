from utils.ma import ma
from models.inventario import Inventario
from schemas.producto_schema import ProductoSchema

class InventarioSchema(ma.Schema):
    class Meta:
        model = Inventario
        fields = (
            'inventario_id',
            'fecha_registro',
            'motivo'
        )
    producto = ma.Nested(ProductoSchema)

inventario_schema = InventarioSchema()
inventarios_schema = InventarioSchema(many=True)