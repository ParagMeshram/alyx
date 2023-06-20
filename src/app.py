import flask

from api.v1.controllers import employees


def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    app.register_blueprint(employees.app, url_prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000)
