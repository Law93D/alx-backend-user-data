#!/usr/bin/env python3
"""
Handles all routes related to User operations.
"""

from flask import Blueprint, jsonify, request, abort
from models.user import User
from api.v1.auth.basic_auth import BasicAuth

app_views = Blueprint('app_views', __name__)
auth = BasicAuth()


@app_views.route('/api/v1/users', methods=['GET'])
def get_users():
    """
    Retrieves the list of all users.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401)  # Unauthorized

    user = auth.authenticate_user(auth_header)
    if not user:
        abort(401)  # Unauthorized

    users = User.all()  # Assuming you have a method to get all users
    return jsonify([user.to_dict() for user in users])


@app_views.route('/api/v1/users/me', methods=['GET'])
def get_me():
    """
    Retrieves the authenticated user.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401)  # Unauthorized

    user = auth.authenticate_user(auth_header)
    if not user:
        abort(401)  # Unauthorized

    return jsonify(user.to_dict())

# Add other routes and methods as necessary...
