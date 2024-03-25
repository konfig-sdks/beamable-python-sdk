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

from beamable_python_sdk.pydantic.facebook_updated_entry_changed_fields import FacebookUpdatedEntryChangedFields

class FacebookUpdatedEntry(BaseModel):
    time: int = Field(alias='time')

    id: typing.Optional[str] = Field(None, alias='id')

    changed_fields: typing.Optional[FacebookUpdatedEntryChangedFields] = Field(None, alias='changed_fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
