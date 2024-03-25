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


class GroupSearchRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            scoreMin = schemas.IntSchema
            sortField = schemas.StrSchema
            userScore = schemas.IntSchema
            hasSlots = schemas.BoolSchema
            enrollmentTypes = schemas.StrSchema
            offset = schemas.IntSchema
            scoreMax = schemas.IntSchema
            subGroup = schemas.BoolSchema
            sortValue = schemas.IntSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "not-available": "NOTAVAILABLE",
                    }
                
                @schemas.classproperty
                def NOTAVAILABLE(cls):
                    return cls("not-available")
            limit = schemas.IntSchema
            __annotations__ = {
                "name": name,
                "scoreMin": scoreMin,
                "sortField": sortField,
                "userScore": userScore,
                "hasSlots": hasSlots,
                "enrollmentTypes": enrollmentTypes,
                "offset": offset,
                "scoreMax": scoreMax,
                "subGroup": subGroup,
                "sortValue": sortValue,
                "type": type,
                "limit": limit,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreMin"]) -> MetaOapg.properties.scoreMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sortField"]) -> MetaOapg.properties.sortField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userScore"]) -> MetaOapg.properties.userScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasSlots"]) -> MetaOapg.properties.hasSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enrollmentTypes"]) -> MetaOapg.properties.enrollmentTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreMax"]) -> MetaOapg.properties.scoreMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subGroup"]) -> MetaOapg.properties.subGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sortValue"]) -> MetaOapg.properties.sortValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "scoreMin", "sortField", "userScore", "hasSlots", "enrollmentTypes", "offset", "scoreMax", "subGroup", "sortValue", "type", "limit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreMin"]) -> typing.Union[MetaOapg.properties.scoreMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sortField"]) -> typing.Union[MetaOapg.properties.sortField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userScore"]) -> typing.Union[MetaOapg.properties.userScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasSlots"]) -> typing.Union[MetaOapg.properties.hasSlots, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enrollmentTypes"]) -> typing.Union[MetaOapg.properties.enrollmentTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreMax"]) -> typing.Union[MetaOapg.properties.scoreMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subGroup"]) -> typing.Union[MetaOapg.properties.subGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sortValue"]) -> typing.Union[MetaOapg.properties.sortValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "scoreMin", "sortField", "userScore", "hasSlots", "enrollmentTypes", "offset", "scoreMax", "subGroup", "sortValue", "type", "limit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        scoreMin: typing.Union[MetaOapg.properties.scoreMin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sortField: typing.Union[MetaOapg.properties.sortField, str, schemas.Unset] = schemas.unset,
        userScore: typing.Union[MetaOapg.properties.userScore, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hasSlots: typing.Union[MetaOapg.properties.hasSlots, bool, schemas.Unset] = schemas.unset,
        enrollmentTypes: typing.Union[MetaOapg.properties.enrollmentTypes, str, schemas.Unset] = schemas.unset,
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        scoreMax: typing.Union[MetaOapg.properties.scoreMax, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subGroup: typing.Union[MetaOapg.properties.subGroup, bool, schemas.Unset] = schemas.unset,
        sortValue: typing.Union[MetaOapg.properties.sortValue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupSearchRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            scoreMin=scoreMin,
            sortField=sortField,
            userScore=userScore,
            hasSlots=hasSlots,
            enrollmentTypes=enrollmentTypes,
            offset=offset,
            scoreMax=scoreMax,
            subGroup=subGroup,
            sortValue=sortValue,
            type=type,
            limit=limit,
            _configuration=_configuration,
            **kwargs,
        )
