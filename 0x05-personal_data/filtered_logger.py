#!/usr/bin/env python3
'''Log formatter'''
import re
from typing import List
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''filter values in incoming log records using filter_datum'''
        return filter_datum(
            self.fields, self.REDACTION, super().format(
                record), self.SEPARATOR)


def get_logger(self) -> logging.Logger:
    '''Create logger'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def filter_datum(fields: List[
                str], redaction: str,
                message: str, separator: str) -> str:
    '''returns the log message obfuscated'''
    for y in fields:
        message = re.sub(f"{y}=.+?{separator}",
                         f"{y}={redaction}{separator}", message)
    return message
