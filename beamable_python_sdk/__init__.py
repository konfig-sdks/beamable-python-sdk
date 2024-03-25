# coding: utf-8

# flake8: noqa

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

__version__ = "1.0"

# import ApiClient
from beamable_python_sdk.api_client import ApiClient

# import Configuration
from beamable_python_sdk.configuration import Configuration

# import exceptions
from beamable_python_sdk.exceptions import OpenApiException
from beamable_python_sdk.exceptions import ApiAttributeError
from beamable_python_sdk.exceptions import ApiTypeError
from beamable_python_sdk.exceptions import ApiValueError
from beamable_python_sdk.exceptions import ApiKeyError
from beamable_python_sdk.exceptions import ApiException

from beamable_python_sdk.client import Beamable
