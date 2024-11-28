from utils.ma import ma
from models.cliente import Cliente
from schemas.usuario_schema import UsuarioSchema

class ClienteSchema(ma.Schema):
    class Meta:
        model = Cliente
        fields = (
            'cliente_id',
            'preferencias'
        )
    usuario = ma.Nested(UsuarioSchema)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)