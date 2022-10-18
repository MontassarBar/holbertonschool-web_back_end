#!/usr/bin/env python3
'''unittest'''
import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from unittest.mock import patch


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


class TestGetJson(unittest.TestCase):
    '''TestGetJson class'''
    @parameterized.expand([
        ("http://example.com", {"test_payload": True}),
        ("http://holberton.io", {"test_payload": False})
        ])
    def test_get_json(self, url, test_payload):
        '''Test that the output of get_json is equal to test_payload'''
        return_value = mock.Mock()
        return_value.json.return_value = test_payload
        with patch(
                "requests.get", return_value=return_value):
            self.assertEqual(get_json(url), test_payload)
            return_value.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''TestMemoize calss'''
    def test_memoize(self):
        '''Test that when calling a_property twice, the correct result is
            returned but a_method is only called once'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            self.assertEqual(TestClass().a_property, 42)
            mock_method.assert_called_once()
