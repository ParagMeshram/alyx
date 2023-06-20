from flask import Blueprint
from flask_cors import CORS

from api.utils import ok
from api.v1.model.employee import EmployeeModel

app = Blueprint("employees", __name__)

CORS(app)


@app.route("employees", methods=["GET"])
def get_employees():
    return ok([{"name": "Parag Meshram"}], EmployeeModel(many=True))
