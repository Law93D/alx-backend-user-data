#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def _generate_uuid(self) -> str:
        """Generate a new UUID"""
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """Register a new user in the system"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(
                    email=email,
                    hashed_password=hashed_password.decode("utf-8")
            )
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user credentials"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password.encode('utf-8')
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for a user and return the session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(email=email, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy the session for the given user ID
        """
        user = self._db.find_user_by(id=user_id)
        if user:
            self._db.update_user(user_id, session_id=None)

    def update_password(self, reset_token: str, new_password: str) -> None:
        """
        Update the user's password using a reset token
        """
        user = self._db.find_user_by(reset_token=reset_token)
        if not user:
            raise ValueError("User not found with the given reset token")

        hashed_password = self._hash_password(new_password)
        self._db.update_user(
                user.id,
                hashed_password=hashed_password.decode("utf-8"),
                reset_token=None
        )


if __name__ == '__main__':
    # Code to test the Auth class (if needed)
    pass
