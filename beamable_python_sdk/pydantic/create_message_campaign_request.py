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
from beamable_python_sdk.pydantic.create_message_campaign_request_rules import CreateMessageCampaignRequestRules

class CreateMessageCampaignRequest(BaseModel):
    resend_to_past_recipients: bool = Field(alias='resend_to_past_recipients')

    sent: int = Field(alias='sent')

    mtype: typing.Optional[str] = Field(None, alias='mtype')

    mb_store: typing.Optional[str] = Field(None, alias='mb_store')

    mb_expiration: typing.Optional[str] = Field(None, alias='mb_expiration')

    name: typing.Optional[str] = Field(None, alias='name')

    subject: typing.Optional[str] = Field(None, alias='subject')

    mb_ent_spec: typing.Optional[str] = Field(None, alias='mb_ent_spec')

    mb_ent_quant: typing.Optional[int] = Field(None, alias='mb_ent_quant')

    datepoint: typing.Optional[str] = Field(None, alias='datepoint')

    mb_attachments: typing.Optional[typing.List[AttachmentRequest]] = Field(None, alias='mb_attachments')

    recur: typing.Optional[str] = Field(None, alias='recur')

    msg: typing.Optional[str] = Field(None, alias='msg')

    rules: typing.Optional[CreateMessageCampaignRequestRules] = Field(None, alias='rules')

    mb_ent: typing.Optional[str] = Field(None, alias='mb_ent')

    start: typing.Optional[str] = Field(None, alias='start')

    days: typing.Optional[str] = Field(None, alias='days')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
