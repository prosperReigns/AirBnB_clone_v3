#!/usr/bin/python3
""" a script to show current api status """

from flask import Flask, jsonify
from model.storage import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage():
    """close the sstorage if connection is lost
    """
     storage.close()

@app.errorhandler(404)
def handle_error():
    """ """
    return jsonify({'error': 'Not Found'}), 404


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)

