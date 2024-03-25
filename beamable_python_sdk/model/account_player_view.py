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


class AccountPlayerView(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "deviceIds",
            "thirdPartyAppAssociations",
            "id",
            "scopes",
        }
        
        class properties:
        
            @staticmethod
            def deviceIds() -> typing.Type['AccountPlayerViewDeviceIds']:
                return AccountPlayerViewDeviceIds
        
            @staticmethod
            def scopes() -> typing.Type['AccountPlayerViewScopes']:
                return AccountPlayerViewScopes
            id = schemas.Int64Schema
        
            @staticmethod
            def thirdPartyAppAssociations() -> typing.Type['AccountPlayerViewThirdPartyAppAssociations']:
                return AccountPlayerViewThirdPartyAppAssociations
            email = schemas.StrSchema
            language = schemas.StrSchema
            __annotations__ = {
                "deviceIds": deviceIds,
                "scopes": scopes,
                "id": id,
                "thirdPartyAppAssociations": thirdPartyAppAssociations,
                "email": email,
                "language": language,
            }
    
    deviceIds: 'AccountPlayerViewDeviceIds'
    thirdPartyAppAssociations: 'AccountPlayerViewThirdPartyAppAssociations'
    id: MetaOapg.properties.id
    scopes: 'AccountPlayerViewScopes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceIds"]) -> 'AccountPlayerViewDeviceIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> 'AccountPlayerViewScopes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirdPartyAppAssociations"]) -> 'AccountPlayerViewThirdPartyAppAssociations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["deviceIds", "scopes", "id", "thirdPartyAppAssociations", "email", "language", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceIds"]) -> 'AccountPlayerViewDeviceIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> 'AccountPlayerViewScopes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirdPartyAppAssociations"]) -> 'AccountPlayerViewThirdPartyAppAssociations': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deviceIds", "scopes", "id", "thirdPartyAppAssociations", "email", "language", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        deviceIds: 'AccountPlayerViewDeviceIds',
        thirdPartyAppAssociations: 'AccountPlayerViewThirdPartyAppAssociations',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        scopes: 'AccountPlayerViewScopes',
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountPlayerView':
        return super().__new__(
            cls,
            *args,
            deviceIds=deviceIds,
            thirdPartyAppAssociations=thirdPartyAppAssociations,
            id=id,
            scopes=scopes,
            email=email,
            language=language,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.account_player_view_device_ids import AccountPlayerViewDeviceIds
from beamable_python_sdk.model.account_player_view_scopes import AccountPlayerViewScopes
from beamable_python_sdk.model.account_player_view_third_party_app_associations import AccountPlayerViewThirdPartyAppAssociations
