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


class RedemptionDef(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "creatorGt",
            "timeCreated",
            "id",
            "maxPerUser",
        }
        
        class properties:
            creatorGt = schemas.IntSchema
            timeCreated = schemas.IntSchema
            maxPerUser = schemas.IntSchema
            id = schemas.IntSchema
            description = schemas.StrSchema
            name = schemas.StrSchema
            timeExpires = schemas.IntSchema
        
            @staticmethod
            def reward() -> typing.Type['EntitlementGenerator']:
                return EntitlementGenerator
        
            @staticmethod
            def gift() -> typing.Type['PlayerReward']:
                return PlayerReward
        
            @staticmethod
            def whitelist() -> typing.Type['RedemptionDefWhitelist']:
                return RedemptionDefWhitelist
            classification = schemas.StrSchema
            __annotations__ = {
                "creatorGt": creatorGt,
                "timeCreated": timeCreated,
                "maxPerUser": maxPerUser,
                "id": id,
                "description": description,
                "name": name,
                "timeExpires": timeExpires,
                "reward": reward,
                "gift": gift,
                "whitelist": whitelist,
                "classification": classification,
            }
    
    creatorGt: MetaOapg.properties.creatorGt
    timeCreated: MetaOapg.properties.timeCreated
    id: MetaOapg.properties.id
    maxPerUser: MetaOapg.properties.maxPerUser
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creatorGt"]) -> MetaOapg.properties.creatorGt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxPerUser"]) -> MetaOapg.properties.maxPerUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeExpires"]) -> MetaOapg.properties.timeExpires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reward"]) -> 'EntitlementGenerator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gift"]) -> 'PlayerReward': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["whitelist"]) -> 'RedemptionDefWhitelist': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification"]) -> MetaOapg.properties.classification: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["creatorGt", "timeCreated", "maxPerUser", "id", "description", "name", "timeExpires", "reward", "gift", "whitelist", "classification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creatorGt"]) -> MetaOapg.properties.creatorGt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxPerUser"]) -> MetaOapg.properties.maxPerUser: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeExpires"]) -> typing.Union[MetaOapg.properties.timeExpires, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reward"]) -> typing.Union['EntitlementGenerator', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gift"]) -> typing.Union['PlayerReward', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["whitelist"]) -> typing.Union['RedemptionDefWhitelist', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification"]) -> typing.Union[MetaOapg.properties.classification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["creatorGt", "timeCreated", "maxPerUser", "id", "description", "name", "timeExpires", "reward", "gift", "whitelist", "classification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        creatorGt: typing.Union[MetaOapg.properties.creatorGt, decimal.Decimal, int, ],
        timeCreated: typing.Union[MetaOapg.properties.timeCreated, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        maxPerUser: typing.Union[MetaOapg.properties.maxPerUser, decimal.Decimal, int, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        timeExpires: typing.Union[MetaOapg.properties.timeExpires, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reward: typing.Union['EntitlementGenerator', schemas.Unset] = schemas.unset,
        gift: typing.Union['PlayerReward', schemas.Unset] = schemas.unset,
        whitelist: typing.Union['RedemptionDefWhitelist', schemas.Unset] = schemas.unset,
        classification: typing.Union[MetaOapg.properties.classification, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RedemptionDef':
        return super().__new__(
            cls,
            *args,
            creatorGt=creatorGt,
            timeCreated=timeCreated,
            id=id,
            maxPerUser=maxPerUser,
            description=description,
            name=name,
            timeExpires=timeExpires,
            reward=reward,
            gift=gift,
            whitelist=whitelist,
            classification=classification,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.entitlement_generator import EntitlementGenerator
from beamable_python_sdk.model.player_reward import PlayerReward
from beamable_python_sdk.model.redemption_def_whitelist import RedemptionDefWhitelist
