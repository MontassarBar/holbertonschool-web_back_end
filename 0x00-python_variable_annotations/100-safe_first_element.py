#!/usr/bin/env python3
'''annotating a function'''
from typing import Union, Sequence,  Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''annotation'''
    if lst:
        return lst[0]
    else:
        return None
