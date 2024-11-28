from utils.ma import ma
from models.vendedor import Vendedor
from schemas.usuario_schema import UsuarioSchema

class VendedorSchema(ma.Schema):
    class Meta:
        model = Vendedor
        fields = (
            'vendedor_id'
        )
    usuario = ma.Nested(UsuarioSchema)

vendedor_schema = VendedorSchema()
vendedores_schema = VendedorSchema(many=True)