# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.flex_token_api import FlexTokenApi


class TestFlexTokenApi(unittest.TestCase):
    """ FlexTokenApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.flex_token_api.FlexTokenApi()

    def tearDown(self):
        pass

    def test_tokenize(self):
        """
        Test case for tokenize

        Flex Tokenize card
        """
        pass


if __name__ == '__main__':
    unittest.main()
