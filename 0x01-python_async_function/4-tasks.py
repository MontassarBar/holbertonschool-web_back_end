#!/usr/bin/env python3
'''Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is
being called'''
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''basic stuff'''
    i = 0
    list = []
    for i in range(0, n):
        r = await task_wait_random(max_delay)
        list.append(r)
    return sorted(list)
