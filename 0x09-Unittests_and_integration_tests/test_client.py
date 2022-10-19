#!/usr/bin/env python3
'''unittest'''
from http import client
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        '''unit-test GithubOrgClient._public_repos_url'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as test_mock:
            test_mock.return_value = {'repos_url': 'http://monta2234.com'}
            cls = GithubOrgClient('monta2234')
            self.assertEqual(
                    cls._public_repos_url, test_mock.return_value['repos_url'])

    @patch('client.get_json',
           return_value=[{"name": "valo"}, {"name": "lol"}])
    def test_public_repos(self, test_payload):
        '''unit-test GithubOrgClient.public_repos'''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as test_mock:
            test_mock.return_value = 'http://monta2234.com'
            cls = GithubOrgClient('monta2234')
            self.assertEqual(cls.public_repos(), ['valo', 'lol'])
            test_payload.assert_called_once()
            test_mock.assert_called_once()
