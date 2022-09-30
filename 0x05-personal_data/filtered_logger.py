#!/usr/bin/env python3
'''Regex-ing'''
import re
from typing import List


def filter_datum(fields: List[
                str], redaction: str, message: str, separator: str):
    '''returns the log message obfuscated'''
    for y in fields:
        message = re.sub(f"{y}=.+?{separator}",
                         f"{y}={redaction}{separator}", message)
    return message
