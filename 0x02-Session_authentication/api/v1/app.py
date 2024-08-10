#!/usr/bin/env python3
"""
Main entry point for the API.
"""

from flask import Flask, jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/api/v1/status', methods=['GET'])
def status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
