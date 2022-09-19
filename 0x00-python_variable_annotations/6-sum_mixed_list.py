#!/usr/bin/env python3
'''type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float.'''
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''list sum mixed'''
    x: float = 0
    for i in range(0, len(input_list)):
        x += input_list[i]
    return x
