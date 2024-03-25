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

from beamable_python_sdk.type.attachment import Attachment
from beamable_python_sdk.type.mail_rewards import MailRewards
from beamable_python_sdk.type.message_reactions import MessageReactions

class RequiredMessage(TypedDict):
    receiverGamerTag: int

    id: int

    senderGamerTag: int

class OptionalMessage(TypedDict, total=False):
    roomId: str

    gamerTag: int

    reactions: MessageReactions

    timestampMillis: int

    censoredContent: str

    messageId: str

    content: str

    body: str

    expires: int

    subject: str

    state: str

    sent: int

    category: str

    bodyRef: int

    attachments: typing.List[Attachment]

    rewards: MailRewards

    claimedTimeMs: int

class Message(RequiredMessage, OptionalMessage):
    pass
