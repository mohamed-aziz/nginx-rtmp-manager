from marshmallow import Schema, fields
from marshmallow.validate import OneOf


class StreamSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    stype = fields.Str(required=True, validate=OneOf(['video', 'audio']))


StreamsSchema = StreamSchema(many=True)
StreamSchema = StreamSchema()
