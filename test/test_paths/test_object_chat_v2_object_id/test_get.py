# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

import unittest
from unittest.mock import patch

import urllib3

import beamable_python_sdk
from beamable_python_sdk.paths.object_chat_v2_object_id import get
from beamable_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestObjectChatV2ObjectId(ApiTestMixin, unittest.TestCase):
    """
    ObjectChatV2ObjectId unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
