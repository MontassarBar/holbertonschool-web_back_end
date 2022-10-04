#!/usr/bin/env python3
'''Auth class'''

from flask import request
from typing import List, TypeVar


class Auth:
    '''the template for all authentication system'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''public method require auth'''
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        else:
            p = path
            c = 0
            if p[-1] == '/':
                s = p.rstrip(p[-1])
            else:
                s = p
            for x in excluded_paths:
                if x[-1] == '/':
                    p2 = x
                    s2 = p2.rstrip(p2[-1])
                else:
                    s2 = p2
                if s == s2:
                    c += 1
            if c == 0:
                return True
        return False

    def authorization_header(self, request=None) -> str:
        '''public method authorisation header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return None
