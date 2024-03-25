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

from beamable_python_sdk.model.notification_request_data import NotificationRequestData as NotificationRequestDataSchema
from beamable_python_sdk.model.notification_request_dbids import NotificationRequestDbids as NotificationRequestDbidsSchema
from beamable_python_sdk.model.notification_request import NotificationRequest as NotificationRequestSchema
from beamable_python_sdk.model.common_response import CommonResponse as CommonResponseSchema

from beamable_python_sdk.type.notification_request import NotificationRequest
from beamable_python_sdk.type.notification_request_data import NotificationRequestData
from beamable_python_sdk.type.notification_request_dbids import NotificationRequestDbids
from beamable_python_sdk.type.common_response import CommonResponse

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.common_response import CommonResponse as CommonResponsePydantic
from beamable_python_sdk.pydantic.notification_request_dbids import NotificationRequestDbids as NotificationRequestDbidsPydantic
from beamable_python_sdk.pydantic.notification_request_data import NotificationRequestData as NotificationRequestDataPydantic
from beamable_python_sdk.pydantic.notification_request import NotificationRequest as NotificationRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = NotificationRequestSchema


request_body_notification_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CommonResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CommonResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CommonResponse


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

    def _send_notification_mapped_args(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if payload is not None:
            _body["payload"] = payload
        if dbid is not None:
            _body["dbid"] = dbid
        if custom_channel_suffix is not None:
            _body["customChannelSuffix"] = custom_channel_suffix
        if dbids is not None:
            _body["dbids"] = dbids
        args.body = _body
        return args

    async def _asend_notification_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
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
            path_template='/basic/notification/generic',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_notification_request.serialize(body, content_type)
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


    def _send_notification_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
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
            path_template='/basic/notification/generic',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_notification_request.serialize(body, content_type)
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


class SendNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asend_notification(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_notification_mapped_args(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
        )
        return await self._asend_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def send_notification(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_notification_mapped_args(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
        )
        return self._send_notification_oapg(
            body=args.body,
        )

class SendNotification(BaseApi):

    async def asend_notification(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
        validate: bool = False,
        **kwargs,
    ) -> CommonResponsePydantic:
        raw_response = await self.raw.asend_notification(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
            **kwargs,
        )
        if validate:
            return CommonResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CommonResponsePydantic, raw_response.body)
    
    
    def send_notification(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
        validate: bool = False,
    ) -> CommonResponsePydantic:
        raw_response = self.raw.send_notification(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
        )
        if validate:
            return CommonResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CommonResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_notification_mapped_args(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
        )
        return await self._asend_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        payload: typing.Optional[NotificationRequestData] = None,
        dbid: typing.Optional[int] = None,
        custom_channel_suffix: typing.Optional[str] = None,
        dbids: typing.Optional[NotificationRequestDbids] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_notification_mapped_args(
            payload=payload,
            dbid=dbid,
            custom_channel_suffix=custom_channel_suffix,
            dbids=dbids,
        )
        return self._send_notification_oapg(
            body=args.body,
        )

