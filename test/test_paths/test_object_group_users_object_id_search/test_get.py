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
from beamable_python_sdk.paths.object_group_users_object_id_search import get
from beamable_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestObjectGroupUsersObjectIdSearch(ApiTestMixin, unittest.TestCase):
    """
    ObjectGroupUsersObjectIdSearch unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
