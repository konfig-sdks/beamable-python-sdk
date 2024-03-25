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

from beamable_python_sdk.type.announcement_attachment import AnnouncementAttachment
from beamable_python_sdk.type.announcement_client_data import AnnouncementClientData
from beamable_python_sdk.type.announcement_validation_errors import AnnouncementValidationErrors
from beamable_python_sdk.type.player_reward import PlayerReward
from beamable_python_sdk.type.player_stat_requirement import PlayerStatRequirement

class RequiredAnnouncement(TypedDict):
    pass

class OptionalAnnouncement(TypedDict, total=False):
    summary: str

    title: str

    body: str

    channel: str

    start_date: str

    gift: PlayerReward

    mongo_start_date: int

    stat_requirements: typing.List[PlayerStatRequirement]

    mongo_end_date: int

    symbol: str

    clientData: AnnouncementClientData

    validationErrors: AnnouncementValidationErrors

    end_date: str

    attachments: typing.List[AnnouncementAttachment]

class Announcement(RequiredAnnouncement, OptionalAnnouncement):
    pass
