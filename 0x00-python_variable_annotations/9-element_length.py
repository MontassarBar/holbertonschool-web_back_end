#!/usr/bin/env python3
'''annotating a function'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''annotate'''
    return [(i, len(i)) for i in lst]
