#!/usr/bin/env python3
'''async routine called wait_n that takes in 2 int arguments: n and max_delay.
    You will spawn wait_random n times with the specified max_delay'''
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''mmm'''
    i = 0
    list = []
    for i in range(0, n):
        r = await wait_random(max_delay)
        list.append(r)
    return sorted(list)
