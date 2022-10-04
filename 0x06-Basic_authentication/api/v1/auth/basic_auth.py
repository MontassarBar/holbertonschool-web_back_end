#!/usr/bin/env python3
'''BasicAuth class'''

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    '''empty'''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''returns the Base64 part of the Authorization header'''
        if authorization_header is None:
            return None
        if str(authorization_header).isnumeric() is True:
            return None
        x = ""
        y = ""
        for i in range(0, len(authorization_header)):
            if i <= 5:
                x += authorization_header[i]
            if i > 5:
                y += authorization_header[i]
        if x != "Basic ":
            return None
        else:
            return y

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''returns the decoded value of a Base64 string
            base64_authorization_header'''
        if base64_authorization_header is None:
            return None
        if str(base64_authorization_header).isnumeric() is True:
            return None
        try:
            x = base64.b64decode(base64_authorization_header)
            return x.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' returns the user email and password from the Base64
            decoded value'''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if str(decoded_base64_authorization_header).isnumeric() is True:
            return (None, None)
        x = 0
        for i in range(0, len(decoded_base64_authorization_header)):
            if decoded_base64_authorization_header[i] == ':':
                x += 1
        if x < 1:
            return (None, None)
        elif x == 1:
            return (decoded_base64_authorization_header.split(':')[0],
                    decoded_base64_authorization_header.split(':')[1])
        else:
            email = ""
            pwd = ""
            for i in range(0, len(decoded_base64_authorization_header)):
                if decoded_base64_authorization_header[i] == ':':
                    c = i
                    break
            for i in range(0, len(decoded_base64_authorization_header)):
                if i < c:
                    email += decoded_base64_authorization_header[i]
                if i > c:
                    pwd += decoded_base64_authorization_header[i]
            return (email, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''returns the User instance based on his email and password'''
        if user_email is None or user_pwd is None:
            return None
        if str(user_email).isnumeric() is True or str(
                user_pwd).isnumeric() is True:
            return None
        user = User()
        x = user.search({"email": user_email})
        if len(x) == 0:
            return None
        for u in x:
            if u.is_valid_password(user_pwd) is True:
                return u
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''overloads Auth and retrieves the User instance for a request'''
        autho = self.authorization_header(request)
        autho = self.extract_base64_authorization_header(autho)
        autho = self.decode_base64_authorization_header(autho)
        autho = self.extract_user_credentials(autho)
        autho = self.user_object_from_credentials(autho[0], autho[1])
        return autho
