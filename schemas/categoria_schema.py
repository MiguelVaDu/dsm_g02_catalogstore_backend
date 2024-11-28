from utils.ma import ma
from marshmallow import fields

class CategoriaSchema(ma.Schema):
    categoria_id = fields.String()
    nombre = fields.String()
    descripcion = fields.String()
categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)