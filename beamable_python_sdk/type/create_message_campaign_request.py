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

from beamable_python_sdk.type.attachment_request import AttachmentRequest
from beamable_python_sdk.type.create_message_campaign_request_rules import CreateMessageCampaignRequestRules

class RequiredCreateMessageCampaignRequest(TypedDict):
    resend_to_past_recipients: bool

    sent: int

class OptionalCreateMessageCampaignRequest(TypedDict, total=False):
    mtype: str

    mb_store: str

    mb_expiration: str

    name: str

    subject: str

    mb_ent_spec: str

    mb_ent_quant: int

    datepoint: str

    mb_attachments: typing.List[AttachmentRequest]

    recur: str

    msg: str

    rules: CreateMessageCampaignRequestRules

    mb_ent: str

    start: str

    days: str

class CreateMessageCampaignRequest(RequiredCreateMessageCampaignRequest, OptionalCreateMessageCampaignRequest):
    pass
