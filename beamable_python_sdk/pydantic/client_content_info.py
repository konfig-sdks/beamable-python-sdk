# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from beamable_python_sdk.pydantic.client_content_info_tags import ClientContentInfoTags

class ClientContentInfo(BaseModel):
    tags: typing.Optional[ClientContentInfoTags] = Field(None, alias='tags')

    version: typing.Optional[str] = Field(None, alias='version')

    uri: typing.Optional[str] = Field(None, alias='uri')

    content_id: typing.Optional[str] = Field(None, alias='contentId')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
