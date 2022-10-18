#!/usr/bin/env python3
'''unittest'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    '''TestAccessNestedMap class'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, value):
        '''test that the method returns what it is supposed to'''
        return self.assertEqual(access_nested_map(nested_map, path), value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence):
        '''test that a KeyError is raised'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
