# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

import unittest

import os
from pprint import pprint
from beamable_python_sdk import Beamable

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        beamable = Beamable(
        
                        api = 'YOUR_API_KEY',
        
                        scope = 'YOUR_API_KEY',
        
            access_token = 'YOUR_BEARER_TOKEN',
        
                        user_required = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(beamable)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
