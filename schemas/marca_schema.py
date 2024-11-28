from utils.ma import ma
from marshmallow import fields

class MarcaSchema(ma.Schema):
    marca_id = fields.String()
    descripcion = fields.String()

marca_schema = MarcaSchema()
marcas_schema = MarcaSchema(many=True)