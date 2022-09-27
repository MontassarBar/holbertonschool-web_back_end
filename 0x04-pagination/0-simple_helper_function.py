#!/usr/bin/env python3
'''index range'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''index range'''
    return (page - 1) * page_size, page_size * page
