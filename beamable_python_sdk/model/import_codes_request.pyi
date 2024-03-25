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


class ImportCodesRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "claimsPerCode",
            "definitionId",
        }
        
        class properties:
            definitionId = schemas.IntSchema
            claimsPerCode = schemas.IntSchema
        
            @staticmethod
            def codes() -> typing.Type['ImportCodesRequestCodes']:
                return ImportCodesRequestCodes
            __annotations__ = {
                "definitionId": definitionId,
                "claimsPerCode": claimsPerCode,
                "codes": codes,
            }
    
    claimsPerCode: MetaOapg.properties.claimsPerCode
    definitionId: MetaOapg.properties.definitionId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["definitionId"]) -> MetaOapg.properties.definitionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claimsPerCode"]) -> MetaOapg.properties.claimsPerCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["codes"]) -> 'ImportCodesRequestCodes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["definitionId", "claimsPerCode", "codes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["definitionId"]) -> MetaOapg.properties.definitionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claimsPerCode"]) -> MetaOapg.properties.claimsPerCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["codes"]) -> typing.Union['ImportCodesRequestCodes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["definitionId", "claimsPerCode", "codes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        claimsPerCode: typing.Union[MetaOapg.properties.claimsPerCode, decimal.Decimal, int, ],
        definitionId: typing.Union[MetaOapg.properties.definitionId, decimal.Decimal, int, ],
        codes: typing.Union['ImportCodesRequestCodes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportCodesRequest':
        return super().__new__(
            cls,
            *args,
            claimsPerCode=claimsPerCode,
            definitionId=definitionId,
            codes=codes,
            _configuration=_configuration,
            **kwargs,
        )

from beamable_python_sdk.model.import_codes_request_codes import ImportCodesRequestCodes
