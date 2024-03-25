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
from beamable_python_sdk.type.mail_rewards import MailRewards

class RequiredSendMailObjectRequest(TypedDict):
    senderGamerTag: int

class OptionalSendMailObjectRequest(TypedDict, total=False):
    body: str

    expires: str

    subject: str

    rewards: MailRewards

    id: int

    category: str

    bodyRef: int

    attachments: typing.List[AttachmentRequest]

class SendMailObjectRequest(RequiredSendMailObjectRequest, OptionalSendMailObjectRequest):
    pass
