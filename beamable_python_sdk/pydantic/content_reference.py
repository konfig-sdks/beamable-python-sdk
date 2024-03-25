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

from beamable_python_sdk.pydantic.content_reference_tags import ContentReferenceTags

class ContentReference(BaseModel):
    tags: typing.Optional[ContentReferenceTags] = Field(None, alias='tags')

    version: typing.Optional[str] = Field(None, alias='version')

    content_prefix: typing.Optional[str] = Field(None, alias='contentPrefix')

    tag: typing.Optional[str] = Field(None, alias='tag')

    uri: typing.Optional[str] = Field(None, alias='uri')

    id: typing.Optional[str] = Field(None, alias='id')

    checksum: typing.Optional[str] = Field(None, alias='checksum')

    type: typing.Optional[Literal["not-available"]] = Field(None, alias='type')

    visibility: typing.Optional[Literal["not-available"]] = Field(None, alias='visibility')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
