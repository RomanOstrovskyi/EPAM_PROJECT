""" app file, used to start the server"""
from flask import Flask, jsonify
from marshmallow import ValidationError
from epam_project.rest.view import endpoints
from epam_project.views.views import endpoints_for_html
from config import SECRET_KEY

app = Flask(__name__, template_folder="EPAM_PROJECT/templates")
app.secret_key = SECRET_KEY


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
app.register_blueprint(endpoints_for_html)


if __name__ == '__main__':
    app.run(debug=True)
