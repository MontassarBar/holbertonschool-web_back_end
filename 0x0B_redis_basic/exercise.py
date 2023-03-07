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
