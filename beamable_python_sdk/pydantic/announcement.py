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

from beamable_python_sdk.pydantic.announcement_attachment import AnnouncementAttachment
from beamable_python_sdk.pydantic.announcement_client_data import AnnouncementClientData
from beamable_python_sdk.pydantic.announcement_validation_errors import AnnouncementValidationErrors
from beamable_python_sdk.pydantic.player_reward import PlayerReward
from beamable_python_sdk.pydantic.player_stat_requirement import PlayerStatRequirement

class Announcement(BaseModel):
    summary: typing.Optional[str] = Field(None, alias='summary')

    title: typing.Optional[str] = Field(None, alias='title')

    body: typing.Optional[str] = Field(None, alias='body')

    channel: typing.Optional[str] = Field(None, alias='channel')

    start_date: typing.Optional[str] = Field(None, alias='start_date')

    gift: typing.Optional[PlayerReward] = Field(None, alias='gift')

    mongo_start_date: typing.Optional[int] = Field(None, alias='mongo_start_date')

    stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = Field(None, alias='stat_requirements')

    mongo_end_date: typing.Optional[int] = Field(None, alias='mongo_end_date')

    symbol: typing.Optional[str] = Field(None, alias='symbol')

    client_data: typing.Optional[AnnouncementClientData] = Field(None, alias='clientData')

    validation_errors: typing.Optional[AnnouncementValidationErrors] = Field(None, alias='validationErrors')

    end_date: typing.Optional[str] = Field(None, alias='end_date')

    attachments: typing.Optional[typing.List[AnnouncementAttachment]] = Field(None, alias='attachments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
