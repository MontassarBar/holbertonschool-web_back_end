#!/usr/bin/env python3
''' a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''basic stuff'''
    t = time.perf_counter()
    await asyncio.gather(async_comprehension(
    ), async_comprehension(), async_comprehension(), async_comprehension())
    t2 = time.perf_counter() - t
    return t2
