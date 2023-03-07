#!/usr/bin/env python3
'''Redis'''

import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
     a system to count how many times methods of the Cache class are called
    '''
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''
        a wrapper
        '''
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    store the history of inputs and outputs for a particular function
    '''
    inputs_list = method.__qualname__ + ':inputs'
    outputs_list = method.__qualname__ + ':outputs'
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''
        a wrapper
        '''
        self._redis.rpush(inputs_list, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs_list, result)
        return result
    return wrapper


def replay(method):
    '''
     display the history of calls of a particular function
    '''
    inputs = method.__self__._redis.lrange(
        "{}:inputs".format(method.__qualname__), 0, -1)
    outputs = method.__self__._redis.lrange(
        "{}:outputs".format(method.__qualname__), 0, -1)
    lis = list(zip(inputs, outputs))
    print('{} was called {} times:'.format(method.__qualname__, len(lis)))
    for x in range(0, len(lis)):
        for y in range(0, 1):
            print("{}(*{}) -> {}".format(
                method.__qualname__, lis[x][y].decode(
                    "utf-8"), lis[x][y + 1].decode("utf-8")))


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''
        store an instance of the Redis client
        as a private variable named _redis
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
