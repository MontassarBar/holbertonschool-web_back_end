#!/usr/bin/env python3
'''unction task_wait_random that takes an integer max_delay and returns
    a asyncio.Task'''
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''basic stuff'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
