from utils.ma import ma
from models.producto import Producto
from schemas.marca_schema import MarcaSchema
from schemas.categoria_schema import CategoriaSchema
from schemas.vendedor_schema import VendedorSchema

class ProductoSchema(ma.Schema):
    class Meta:
        model = Producto
        fields = (
            'sku',
            'nombre',
            'precio',
            'imagen',
            'descripcion',
            'unidades',
            'marca'
        )
    marca = ma.Nested(MarcaSchema)
    categoria = ma.Nested(CategoriaSchema)
    vendedor = ma.Nested(VendedorSchema)
    
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)