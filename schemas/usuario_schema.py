from utils.ma import ma
from models.usuario import Usuario
from schemas.persona_schema import PersonaSchema

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = (
            'usuario_id',
            'correo',
            'password'
        )
    persona = ma.Nested(PersonaSchema)

usuario_schema = UsuarioSchema()
usuario_schema = UsuarioSchema(many=True)