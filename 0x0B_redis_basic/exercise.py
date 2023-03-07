#!/usr/bin/env python3
'''Redis'''

import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''
        store an instance of the Redis client
        as a private variable named _redis
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        generate a random key, store the input data in Redis
        using the random key and return the key
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        '''
        get method that take a key string argument and an optional Callable
        argument named fn. This callable will be used to convert the data back
        to the desired format
        '''
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: bytes) -> str:
        '''
        convert the key type to str
        '''
        return key.decode("utf-8")

    def get_int(self, key: bytes) -> int:
        '''
        convert the key type to int
        '''
        return int(key)
