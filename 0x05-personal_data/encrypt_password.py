#!/usr/bin/env python3
'''hash_password'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''hashing'''
    bytes = password.encode('utf-8')
    hash =  bcrypt.hashpw(bytes, bcrypt.gensalt())
    return hash
