#!/usr/bin/env python3
'''BasicAuth class'''

from posixpath import split
from typing import Tuple
from api.v1.auth.auth import Auth
import base64


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
            self, decoded_base64_authorization_header: str) -> Tuple(
                str, str):
        ''' returns the user email and password from the Base64
            decoded value'''
        if decoded_base64_authorization_header is None:
            (None, None)
        if str(decoded_base64_authorization_header).isnumeric() is True:
            (None, None)
        x = 0
        for i in range(0, len(decoded_base64_authorization_header)):
            if decoded_base64_authorization_header[i] == ':':
                x = 1
        if x < 1:
            return (None, None)
        else:
            l = decoded_base64_authorization_header.split(':')
            return (l[0], l[1])