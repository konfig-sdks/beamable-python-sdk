# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beamable_python_sdk import schemas  # noqa: F401


class EventClaimResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def view() -> typing.Type['EventPlayerStateView']:
                return EventPlayerStateView
            gameRspJson = schemas.StrSchema
            __annotations__ = {
                "view": view,
                "gameRspJson": gameRspJson,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> 'EventPlayerStateView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gameRspJson"]) -> MetaOapg.properties.gameRspJson: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["view", "gameRspJson", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union['EventPlayerStateView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gameRspJson"]) -> typing.Union[MetaOapg.properties.gameRspJson, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["view", "gameRspJson", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        view: typing.Union['EventPlayerStateView', schemas.Unset] = schemas.unset,
        gameRspJson: typing.Union[MetaOapg.properties.gameRspJson, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventClaimResponse':
        return super().__new__(
            cls,
            *args,
            view=view,
            gameRspJson=gameRspJson,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.event_player_state_view import EventPlayerStateView
