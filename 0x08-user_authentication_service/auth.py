#!/usr/bin/env python3
'''auth'''
import uuid
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    '''hashing'''
    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
    return hash


def _generate_uuid() -> str:
    '''return a string representation of a new UUID'''
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' hash the password with _hash_password, save the user to the
            database using self._db and return the User object'''
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        ''' check the password with bcrypt.checkpw. If it matches return True.
            In any other case, return False'''
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                'utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''generate a new UUID and store it in the database as the user's
            session_id, then return the session ID'''
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''returns the corresponding User'''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
