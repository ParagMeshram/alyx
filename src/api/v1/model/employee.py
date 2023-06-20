from marshmallow.schema import Schema
from marshmallow.fields import String


class EmployeeModel(Schema):
    name: String
