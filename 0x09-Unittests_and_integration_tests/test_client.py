#!/usr/bin/env python3
'''unittest'''
from http import client
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient class'''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_URL, test_payload):
        '''test that GithubOrgClient.org returns the correct value'''
        cls = GithubOrgClient(org_URL)
        self.assertEqual(cls.org, test_payload.return_value)
        test_payload.assert_called_once()
