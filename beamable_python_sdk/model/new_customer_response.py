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


class NewCustomerResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "pid",
            "projectName",
            "cid",
            "token",
        }
        
        class properties:
            name = schemas.StrSchema
            projectName = schemas.StrSchema
            cid = schemas.Int64Schema
            pid = schemas.StrSchema
        
            @staticmethod
            def token() -> typing.Type['TokenResponse']:
                return TokenResponse
            alias = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "projectName": projectName,
                "cid": cid,
                "pid": pid,
                "token": token,
                "alias": alias,
            }
    
    name: MetaOapg.properties.name
    pid: MetaOapg.properties.pid
    projectName: MetaOapg.properties.projectName
    cid: MetaOapg.properties.cid
    token: 'TokenResponse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectName"]) -> MetaOapg.properties.projectName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pid"]) -> MetaOapg.properties.pid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> 'TokenResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "projectName", "cid", "pid", "token", "alias", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectName"]) -> MetaOapg.properties.projectName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pid"]) -> MetaOapg.properties.pid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> 'TokenResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "projectName", "cid", "pid", "token", "alias", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        pid: typing.Union[MetaOapg.properties.pid, str, ],
        projectName: typing.Union[MetaOapg.properties.projectName, str, ],
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, ],
        token: 'TokenResponse',
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewCustomerResponse':
        return super().__new__(
            cls,
            *args,
            name=name,
            pid=pid,
            projectName=projectName,
            cid=cid,
            token=token,
            alias=alias,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.token_response import TokenResponse
