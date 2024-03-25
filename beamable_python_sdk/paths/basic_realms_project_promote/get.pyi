# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from beamable_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from beamable_python_sdk.api_response import AsyncGeneratorResponse
from beamable_python_sdk import api_client, exceptions
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

from beamable_python_sdk.model.promote_realm_response_old import PromoteRealmResponseOld as PromoteRealmResponseOldSchema

from beamable_python_sdk.type.promote_realm_response_old import PromoteRealmResponseOld

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.promote_realm_response_old import PromoteRealmResponseOld as PromoteRealmResponseOldPydantic

# Query params
SourcePidSchema = schemas.StrSchema


class PromotionsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PromotionsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class ContentManifestIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContentManifestIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'sourcePid': typing.Union[SourcePidSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'promotions': typing.Union[PromotionsSchema, list, tuple, ],
        'contentManifestIds': typing.Union[ContentManifestIdsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_source_pid = api_client.QueryParameter(
    name="sourcePid",
    style=api_client.ParameterStyle.FORM,
    schema=SourcePidSchema,
    required=True,
    explode=True,
)
request_query_promotions = api_client.QueryParameter(
    name="promotions",
    style=api_client.ParameterStyle.FORM,
    schema=PromotionsSchema,
    explode=True,
)
request_query_content_manifest_ids = api_client.QueryParameter(
    name="contentManifestIds",
    style=api_client.ParameterStyle.FORM,
    schema=ContentManifestIdsSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PromoteRealmResponseOldSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PromoteRealmResponseOld


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PromoteRealmResponseOld


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _project_promote_get_mapped_args(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if source_pid is not None:
            _query_params["sourcePid"] = source_pid
        if promotions is not None:
            _query_params["promotions"] = promotions
        if content_manifest_ids is not None:
            _query_params["contentManifestIds"] = content_manifest_ids
        args.query = _query_params
        return args

    async def _aproject_promote_get_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_source_pid,
            request_query_promotions,
            request_query_content_manifest_ids,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/realms/project/promote',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _project_promote_get_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_source_pid,
            request_query_promotions,
            request_query_content_manifest_ids,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/basic/realms/project/promote',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ProjectPromoteGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aproject_promote_get(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._project_promote_get_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return await self._aproject_promote_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def project_promote_get(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._project_promote_get_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return self._project_promote_get_oapg(
            query_params=args.query,
        )

class ProjectPromoteGet(BaseApi):

    async def aproject_promote_get(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PromoteRealmResponseOldPydantic:
        raw_response = await self.raw.aproject_promote_get(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
            **kwargs,
        )
        if validate:
            return PromoteRealmResponseOldPydantic(**raw_response.body)
        return api_client.construct_model_instance(PromoteRealmResponseOldPydantic, raw_response.body)
    
    
    def project_promote_get(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> PromoteRealmResponseOldPydantic:
        raw_response = self.raw.project_promote_get(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        if validate:
            return PromoteRealmResponseOldPydantic(**raw_response.body)
        return api_client.construct_model_instance(PromoteRealmResponseOldPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._project_promote_get_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return await self._aproject_promote_get_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        source_pid: str,
        promotions: typing.Optional[typing.List[str]] = None,
        content_manifest_ids: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._project_promote_get_mapped_args(
            source_pid=source_pid,
            promotions=promotions,
            content_manifest_ids=content_manifest_ids,
        )
        return self._project_promote_get_oapg(
            query_params=args.query,
        )

