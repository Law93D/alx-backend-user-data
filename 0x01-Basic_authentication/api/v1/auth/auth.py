#!/usr/bin/env python3
""" Class to manage API Auth.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    manage API auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if auth is required to access path
        """
        if path and not path.endswith('/'):
            path = path + '/'
        if not path or path not in excluded_path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> None:
        """

        """
        return None

    def current_user(self, request=None) -> None:
        """

        """
        return None


if __name__ == '__main__':
    a = Auth()

    print(a.require_auth(None, None))  # True
    print(a.require_auth(None, []))  # True
    print(a.require_auth("/api/v1/status/", []))  # True
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))  # False
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))  # False
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))  # True
    print(
        a.require_auth(
            "/api/v1/users",
            ["/api/v1/status/", "/api/v1/stats"]
        )
    )  # True
