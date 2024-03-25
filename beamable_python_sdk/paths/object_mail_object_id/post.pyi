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

from beamable_python_sdk.model.send_mail_object_request import SendMailObjectRequest as SendMailObjectRequestSchema
from beamable_python_sdk.model.attachment_request import AttachmentRequest as AttachmentRequestSchema
from beamable_python_sdk.model.send_mail_response import SendMailResponse as SendMailResponseSchema
from beamable_python_sdk.model.mail_rewards import MailRewards as MailRewardsSchema

from beamable_python_sdk.type.mail_rewards import MailRewards
from beamable_python_sdk.type.send_mail_response import SendMailResponse
from beamable_python_sdk.type.attachment_request import AttachmentRequest
from beamable_python_sdk.type.send_mail_object_request import SendMailObjectRequest

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.mail_rewards import MailRewards as MailRewardsPydantic
from beamable_python_sdk.pydantic.send_mail_response import SendMailResponse as SendMailResponsePydantic
from beamable_python_sdk.pydantic.attachment_request import AttachmentRequest as AttachmentRequestPydantic
from beamable_python_sdk.pydantic.send_mail_object_request import SendMailObjectRequest as SendMailObjectRequestPydantic

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
SchemaForRequestBodyApplicationJson = SendMailObjectRequestSchema


request_body_send_mail_object_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = SendMailResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SendMailResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SendMailResponse


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

    def _create_object_mail_mapped_args(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if body is not None:
            _body["body"] = body
        if expires is not None:
            _body["expires"] = expires
        if subject is not None:
            _body["subject"] = subject
        if rewards is not None:
            _body["rewards"] = rewards
        if id is not None:
            _body["id"] = id
        if sender_gamer_tag is not None:
            _body["senderGamerTag"] = sender_gamer_tag
        if category is not None:
            _body["category"] = category
        if body_ref is not None:
            _body["bodyRef"] = body_ref
        if attachments is not None:
            _body["attachments"] = attachments
        args.body = _body
        if object_id is not None:
            _path_params["objectId"] = object_id
        args.path = _path_params
        return args

    async def _acreate_object_mail_oapg(
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
            path_template='/object/mail/{objectId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_send_mail_object_request.serialize(body, content_type)
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


    def _create_object_mail_oapg(
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
            path_template='/object/mail/{objectId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_send_mail_object_request.serialize(body, content_type)
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


class CreateObjectMailRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_object_mail(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_object_mail_mapped_args(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
        )
        return await self._acreate_object_mail_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_object_mail(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_object_mail_mapped_args(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
        )
        return self._create_object_mail_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateObjectMail(BaseApi):

    async def acreate_object_mail(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
        validate: bool = False,
        **kwargs,
    ) -> SendMailResponsePydantic:
        raw_response = await self.raw.acreate_object_mail(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
            **kwargs,
        )
        if validate:
            return SendMailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SendMailResponsePydantic, raw_response.body)
    
    
    def create_object_mail(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
        validate: bool = False,
    ) -> SendMailResponsePydantic:
        raw_response = self.raw.create_object_mail(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
        )
        if validate:
            return SendMailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SendMailResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_object_mail_mapped_args(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
        )
        return await self._acreate_object_mail_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        sender_gamer_tag: int,
        object_id: str,
        body: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        rewards: typing.Optional[MailRewards] = None,
        id: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        body_ref: typing.Optional[int] = None,
        attachments: typing.Optional[typing.List[AttachmentRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_object_mail_mapped_args(
            sender_gamer_tag=sender_gamer_tag,
            object_id=object_id,
            body=body,
            expires=expires,
            subject=subject,
            rewards=rewards,
            id=id,
            category=category,
            body_ref=body_ref,
            attachments=attachments,
        )
        return self._create_object_mail_oapg(
            body=args.body,
            path_params=args.path,
        )

