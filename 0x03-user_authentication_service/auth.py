#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Register a new user in the system"""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If the user does not exist, proceed with registration
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(
                    email,
                    hashed_password.decode("utf-8")
            )
            return new_user


if __name__ == '__main__':
    # Code to test the Auth class (if needed)
    pass
