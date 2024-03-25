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


class UploadTrialDataRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            trialName = schemas.StrSchema
            cohortName = schemas.StrSchema
            dataName = schemas.StrSchema
            filePayloadBase64 = schemas.StrSchema
            __annotations__ = {
                "trialName": trialName,
                "cohortName": cohortName,
                "dataName": dataName,
                "filePayloadBase64": filePayloadBase64,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trialName"]) -> MetaOapg.properties.trialName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cohortName"]) -> MetaOapg.properties.cohortName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataName"]) -> MetaOapg.properties.dataName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filePayloadBase64"]) -> MetaOapg.properties.filePayloadBase64: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["trialName", "cohortName", "dataName", "filePayloadBase64", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trialName"]) -> typing.Union[MetaOapg.properties.trialName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cohortName"]) -> typing.Union[MetaOapg.properties.cohortName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataName"]) -> typing.Union[MetaOapg.properties.dataName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filePayloadBase64"]) -> typing.Union[MetaOapg.properties.filePayloadBase64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trialName", "cohortName", "dataName", "filePayloadBase64", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        trialName: typing.Union[MetaOapg.properties.trialName, str, schemas.Unset] = schemas.unset,
        cohortName: typing.Union[MetaOapg.properties.cohortName, str, schemas.Unset] = schemas.unset,
        dataName: typing.Union[MetaOapg.properties.dataName, str, schemas.Unset] = schemas.unset,
        filePayloadBase64: typing.Union[MetaOapg.properties.filePayloadBase64, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UploadTrialDataRequest':
        return super().__new__(
            cls,
            *args,
            trialName=trialName,
            cohortName=cohortName,
            dataName=dataName,
            filePayloadBase64=filePayloadBase64,
            _configuration=_configuration,
            **kwargs,
        )
