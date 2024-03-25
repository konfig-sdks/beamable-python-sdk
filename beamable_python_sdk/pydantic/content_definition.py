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

from beamable_python_sdk.pydantic.content_definition_properties import ContentDefinitionProperties
from beamable_python_sdk.pydantic.content_definition_tags import ContentDefinitionTags
from beamable_python_sdk.pydantic.content_definition_variants import ContentDefinitionVariants

class ContentDefinition(BaseModel):
    tags: typing.Optional[ContentDefinitionTags] = Field(None, alias='tags')

    prefix: typing.Optional[str] = Field(None, alias='prefix')

    id: typing.Optional[str] = Field(None, alias='id')

    checksum: typing.Optional[str] = Field(None, alias='checksum')

    properties: typing.Optional[ContentDefinitionProperties] = Field(None, alias='properties')

    variants: typing.Optional[ContentDefinitionVariants] = Field(None, alias='variants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
