""" app file, used to start the server"""
from flask import Flask, jsonify
from marshmallow import ValidationError

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, ValidationError):
        return jsonify(error=str(e)), 400
    if isinstance(e, Exception):
        return jsonify(error=str(e)), 400

    return jsonify(error=str(e)), code


from epam_project.rest.view import endpoints
app.register_blueprint(endpoints)


if __name__ == '__main__':
    app.run(debug=True)
