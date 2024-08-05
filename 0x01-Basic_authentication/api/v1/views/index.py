#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify
from api.v1.views import app_views
from flask import abort


@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_route():
    abort(401)


@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden_route():
    abort(403)
