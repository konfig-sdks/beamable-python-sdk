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


class LeaderboardCreateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sharded",
        }
        
        class properties:
            sharded = schemas.BoolSchema
            freezeTime = schemas.IntSchema
        
            @staticmethod
            def derivatives() -> typing.Type['LeaderboardCreateRequestDerivatives']:
                return LeaderboardCreateRequestDerivatives
            scoreName = schemas.StrSchema
        
            @staticmethod
            def permissions() -> typing.Type['ClientPermission']:
                return ClientPermission
            maxEntries = schemas.IntSchema
            partitioned = schemas.BoolSchema
            ttl = schemas.IntSchema
            __annotations__ = {
                "sharded": sharded,
                "freezeTime": freezeTime,
                "derivatives": derivatives,
                "scoreName": scoreName,
                "permissions": permissions,
                "maxEntries": maxEntries,
                "partitioned": partitioned,
                "ttl": ttl,
            }
    
    sharded: MetaOapg.properties.sharded
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sharded"]) -> MetaOapg.properties.sharded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freezeTime"]) -> MetaOapg.properties.freezeTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["derivatives"]) -> 'LeaderboardCreateRequestDerivatives': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreName"]) -> MetaOapg.properties.scoreName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'ClientPermission': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxEntries"]) -> MetaOapg.properties.maxEntries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partitioned"]) -> MetaOapg.properties.partitioned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sharded", "freezeTime", "derivatives", "scoreName", "permissions", "maxEntries", "partitioned", "ttl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sharded"]) -> MetaOapg.properties.sharded: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freezeTime"]) -> typing.Union[MetaOapg.properties.freezeTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["derivatives"]) -> typing.Union['LeaderboardCreateRequestDerivatives', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreName"]) -> typing.Union[MetaOapg.properties.scoreName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['ClientPermission', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxEntries"]) -> typing.Union[MetaOapg.properties.maxEntries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partitioned"]) -> typing.Union[MetaOapg.properties.partitioned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sharded", "freezeTime", "derivatives", "scoreName", "permissions", "maxEntries", "partitioned", "ttl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sharded: typing.Union[MetaOapg.properties.sharded, bool, ],
        freezeTime: typing.Union[MetaOapg.properties.freezeTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        derivatives: typing.Union['LeaderboardCreateRequestDerivatives', schemas.Unset] = schemas.unset,
        scoreName: typing.Union[MetaOapg.properties.scoreName, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union['ClientPermission', schemas.Unset] = schemas.unset,
        maxEntries: typing.Union[MetaOapg.properties.maxEntries, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        partitioned: typing.Union[MetaOapg.properties.partitioned, bool, schemas.Unset] = schemas.unset,
        ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LeaderboardCreateRequest':
        return super().__new__(
            cls,
            *args,
            sharded=sharded,
            freezeTime=freezeTime,
            derivatives=derivatives,
            scoreName=scoreName,
            permissions=permissions,
            maxEntries=maxEntries,
            partitioned=partitioned,
            ttl=ttl,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.client_permission import ClientPermission
from beamable_python_sdk.model.leaderboard_create_request_derivatives import LeaderboardCreateRequestDerivatives
