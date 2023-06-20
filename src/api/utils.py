from flask import jsonify
from marshmallow import Schema

from api.enums import HttpStatus


def _make(status: HttpStatus, response, schema: Schema = None):
    response = schema.dump(response) if schema else response
    return jsonify(response), status


def ok(response, schema: Schema = None):
    return _make(HttpStatus.OK, response, schema)


def created(response, schema: Schema = None):
    return _make(HttpStatus.CREATED, response, schema)


def bad_request(response, schema: Schema = None):
    _make(HttpStatus.BAD_REQUEST, response, schema)


def not_found(response, schema: Schema = None):
    _make(HttpStatus.NOT_FOUND, response, schema)


def conflict(response, schema: Schema = None):
    _make(HttpStatus.CONFLICT, response, schema)
