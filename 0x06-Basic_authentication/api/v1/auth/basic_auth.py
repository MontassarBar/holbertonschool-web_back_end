#!/usr/bin/env python3
'''BasicAuth class'''

from api.v1.auth.auth import Auth


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
