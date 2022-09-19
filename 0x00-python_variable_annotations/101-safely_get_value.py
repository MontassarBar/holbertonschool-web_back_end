#!/usr/bin/env python3
'''annotating a function'''
from typing import Union, Sequence,  Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[
                        T, None]) -> Union[Any, T]:
    '''annotation'''
    if key in dct:
        return dct[key]
    else:
        return default
