#!/usr/bin/env python3
'''auth'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''hashing'''
    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
    return hash
