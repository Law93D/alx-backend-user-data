#!/usr/bin/env python3
""" Class to manage API Auth.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None


def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    if path is None or excluded_paths is None or not excluded_paths:
        return True
    if path[-1] != '/':
        path += '/'
    for excl_path in excluded_paths:
        if excl_path.endswith('/'):
            if path == excl_path:
                return False
        else:
            if path.startswith(excl_path):
                return False
    return True


def authorization_header(self, request=None) -> str:
    if request is None or 'Authorization' not in request.headers:
        return None
    return request.headers['Authorization']
