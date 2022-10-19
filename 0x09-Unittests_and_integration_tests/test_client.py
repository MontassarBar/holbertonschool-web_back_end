#!/usr/bin/env python3
'''unittest'''
from http import client
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, cond):
        ''' unit-test GithubOrgClient.has_license'''
        cls = GithubOrgClient('monta2234')
        self.assertEqual(cls.has_license(repo, license_key), cond)


@parameterized_class((
    'org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''TestIntegrationGithubOrgClient class'''
    @classmethod
    def setupClass(cls):
        '''start a patcher named'''
        cls.get_patcher = patch('requests.get')
        cls.mock_object = cls.get_patcher.start()
        cls.mock_object.side_effect = [cls.org_payload,
                                       cls.repos_payload,
                                       cls.expected_repos,
                                       cls.apache2_repos]
    @classmethod
    def tearDownClass(cls):
        '''stop the patcher'''
        cls.get_patcher.stop()
