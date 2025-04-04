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

from beamable_python_sdk.model.stat_update_request_string_list_format import StatUpdateRequestStringListFormat as StatUpdateRequestStringListFormatSchema
from beamable_python_sdk.model.empty_response import EmptyResponse as EmptyResponseSchema
from beamable_python_sdk.model.stat_string_list_entry import StatStringListEntry as StatStringListEntrySchema

from beamable_python_sdk.type.empty_response import EmptyResponse
from beamable_python_sdk.type.stat_update_request_string_list_format import StatUpdateRequestStringListFormat
from beamable_python_sdk.type.stat_string_list_entry import StatStringListEntry

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.stat_update_request_string_list_format import StatUpdateRequestStringListFormat as StatUpdateRequestStringListFormatPydantic
from beamable_python_sdk.pydantic.empty_response import EmptyResponse as EmptyResponsePydantic
from beamable_python_sdk.pydantic.stat_string_list_entry import StatStringListEntry as StatStringListEntryPydantic

# Path params
ObjectIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'objectId': typing.Union[ObjectIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_object_id = api_client.PathParameter(
    name="objectId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ObjectIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = StatUpdateRequestStringListFormatSchema


request_body_stat_update_request_string_list_format = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = EmptyResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmptyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmptyResponse


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

    def _post_client_stringlist_mapped_args(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if set is not None:
            _body["set"] = set
        args.body = _body
        if object_id is not None:
            _path_params["objectId"] = object_id
        args.path = _path_params
        return args

    async def _apost_client_stringlist_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_object_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/object/stats/{objectId}/client/stringlist',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_stat_update_request_string_list_format.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _post_client_stringlist_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_object_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/object/stats/{objectId}/client/stringlist',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_stat_update_request_string_list_format.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class PostClientStringlistRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apost_client_stringlist(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._post_client_stringlist_mapped_args(
            object_id=object_id,
            set=set,
        )
        return await self._apost_client_stringlist_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post_client_stringlist(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._post_client_stringlist_mapped_args(
            object_id=object_id,
            set=set,
        )
        return self._post_client_stringlist_oapg(
            body=args.body,
            path_params=args.path,
        )

class PostClientStringlist(BaseApi):

    async def apost_client_stringlist(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmptyResponsePydantic:
        raw_response = await self.raw.apost_client_stringlist(
            object_id=object_id,
            set=set,
            **kwargs,
        )
        if validate:
            return EmptyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponsePydantic, raw_response.body)
    
    
    def post_client_stringlist(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
        validate: bool = False,
    ) -> EmptyResponsePydantic:
        raw_response = self.raw.post_client_stringlist(
            object_id=object_id,
            set=set,
        )
        if validate:
            return EmptyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._post_client_stringlist_mapped_args(
            object_id=object_id,
            set=set,
        )
        return await self._apost_client_stringlist_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        object_id: str,
        set: typing.Optional[typing.List[StatStringListEntry]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._post_client_stringlist_mapped_args(
            object_id=object_id,
            set=set,
        )
        return self._post_client_stringlist_oapg(
            body=args.body,
            path_params=args.path,
        )

