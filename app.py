""" app file, used to start the server"""
from flask import Flask, jsonify
from marshmallow import ValidationError
from epam_project.rest.view import endpoints

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(error):
    """ error handler """
    code = 500
    if isinstance(error, ValidationError):
        return jsonify(error=str(error)), 400
    if isinstance(error, Exception):
        return jsonify(error=str(error)), 400

    return jsonify(error=str(error)), code


app.register_blueprint(endpoints)


if __name__ == '__main__':
    app.run(debug=True)
