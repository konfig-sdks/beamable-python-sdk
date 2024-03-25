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

from beamable_python_sdk.pydantic.attachment import Attachment
from beamable_python_sdk.pydantic.mail_rewards import MailRewards
from beamable_python_sdk.pydantic.message_reactions import MessageReactions

class Message(BaseModel):
    receiver_gamer_tag: int = Field(alias='receiverGamerTag')

    id: int = Field(alias='id')

    sender_gamer_tag: int = Field(alias='senderGamerTag')

    room_id: typing.Optional[str] = Field(None, alias='roomId')

    gamer_tag: typing.Optional[int] = Field(None, alias='gamerTag')

    reactions: typing.Optional[MessageReactions] = Field(None, alias='reactions')

    timestamp_millis: typing.Optional[int] = Field(None, alias='timestampMillis')

    censored_content: typing.Optional[str] = Field(None, alias='censoredContent')

    message_id: typing.Optional[str] = Field(None, alias='messageId')

    content: typing.Optional[str] = Field(None, alias='content')

    body: typing.Optional[str] = Field(None, alias='body')

    expires: typing.Optional[int] = Field(None, alias='expires')

    subject: typing.Optional[str] = Field(None, alias='subject')

    state: typing.Optional[str] = Field(None, alias='state')

    sent: typing.Optional[int] = Field(None, alias='sent')

    category: typing.Optional[str] = Field(None, alias='category')

    body_ref: typing.Optional[int] = Field(None, alias='bodyRef')

    attachments: typing.Optional[typing.List[Attachment]] = Field(None, alias='attachments')

    rewards: typing.Optional[MailRewards] = Field(None, alias='rewards')

    claimed_time_ms: typing.Optional[int] = Field(None, alias='claimedTimeMs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
