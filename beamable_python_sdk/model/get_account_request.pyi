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


class GetAccountRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            gamerTag = schemas.IntSchema
            email = schemas.StrSchema
        
            @staticmethod
            def thirdPartyAssoc() -> typing.Type['ThirdPartyAssociation']:
                return ThirdPartyAssociation
            deviceId = schemas.StrSchema
            __annotations__ = {
                "gamerTag": gamerTag,
                "email": email,
                "thirdPartyAssoc": thirdPartyAssoc,
                "deviceId": deviceId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gamerTag"]) -> MetaOapg.properties.gamerTag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirdPartyAssoc"]) -> 'ThirdPartyAssociation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceId"]) -> MetaOapg.properties.deviceId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gamerTag", "email", "thirdPartyAssoc", "deviceId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gamerTag"]) -> typing.Union[MetaOapg.properties.gamerTag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirdPartyAssoc"]) -> typing.Union['ThirdPartyAssociation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceId"]) -> typing.Union[MetaOapg.properties.deviceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gamerTag", "email", "thirdPartyAssoc", "deviceId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gamerTag: typing.Union[MetaOapg.properties.gamerTag, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        thirdPartyAssoc: typing.Union['ThirdPartyAssociation', schemas.Unset] = schemas.unset,
        deviceId: typing.Union[MetaOapg.properties.deviceId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetAccountRequest':
        return super().__new__(
            cls,
            *args,
            gamerTag=gamerTag,
            email=email,
            thirdPartyAssoc=thirdPartyAssoc,
            deviceId=deviceId,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.third_party_association import ThirdPartyAssociation
