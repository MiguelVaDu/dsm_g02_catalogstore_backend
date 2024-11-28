from utils.ma import ma
from marshmallow import fields

class TipoComprobanteSchema(ma.Schema):
    comprobante_id = fields.String()
    descripcion_comprobante = fields.String()

tipo_comprobante_schema = TipoComprobanteSchema()
tipos_comprobante_schema = TipoComprobanteSchema(many=True)