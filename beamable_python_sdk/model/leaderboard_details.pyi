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


class LeaderboardDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "numberOfEntries",
        }
        
        class properties:
            numberOfEntries = schemas.IntSchema
            lbid = schemas.StrSchema
        
            @staticmethod
            def orules() -> typing.Type['OrderRules']:
                return OrderRules
            fullName = schemas.StrSchema
        
            @staticmethod
            def view() -> typing.Type['LeaderBoardView']:
                return LeaderBoardView
            __annotations__ = {
                "numberOfEntries": numberOfEntries,
                "lbid": lbid,
                "orules": orules,
                "fullName": fullName,
                "view": view,
            }
    
    numberOfEntries: MetaOapg.properties.numberOfEntries
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfEntries"]) -> MetaOapg.properties.numberOfEntries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lbid"]) -> MetaOapg.properties.lbid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orules"]) -> 'OrderRules': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullName"]) -> MetaOapg.properties.fullName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> 'LeaderBoardView': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["numberOfEntries", "lbid", "orules", "fullName", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfEntries"]) -> MetaOapg.properties.numberOfEntries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lbid"]) -> typing.Union[MetaOapg.properties.lbid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orules"]) -> typing.Union['OrderRules', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullName"]) -> typing.Union[MetaOapg.properties.fullName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union['LeaderBoardView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["numberOfEntries", "lbid", "orules", "fullName", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        numberOfEntries: typing.Union[MetaOapg.properties.numberOfEntries, decimal.Decimal, int, ],
        lbid: typing.Union[MetaOapg.properties.lbid, str, schemas.Unset] = schemas.unset,
        orules: typing.Union['OrderRules', schemas.Unset] = schemas.unset,
        fullName: typing.Union[MetaOapg.properties.fullName, str, schemas.Unset] = schemas.unset,
        view: typing.Union['LeaderBoardView', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LeaderboardDetails':
        return super().__new__(
            cls,
            *args,
            numberOfEntries=numberOfEntries,
            lbid=lbid,
            orules=orules,
            fullName=fullName,
            view=view,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.leader_board_view import LeaderBoardView
from beamable_python_sdk.model.order_rules import OrderRules
