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

from beamable_python_sdk.pydantic.attachment_request import AttachmentRequest
from beamable_python_sdk.pydantic.mail_rewards import MailRewards

class SendMailObjectRequest(BaseModel):
    sender_gamer_tag: int = Field(alias='senderGamerTag')

    body: typing.Optional[str] = Field(None, alias='body')

    expires: typing.Optional[str] = Field(None, alias='expires')

    subject: typing.Optional[str] = Field(None, alias='subject')

    rewards: typing.Optional[MailRewards] = Field(None, alias='rewards')

    id: typing.Optional[int] = Field(None, alias='id')

    category: typing.Optional[str] = Field(None, alias='category')

    body_ref: typing.Optional[int] = Field(None, alias='bodyRef')

    attachments: typing.Optional[typing.List[AttachmentRequest]] = Field(None, alias='attachments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
