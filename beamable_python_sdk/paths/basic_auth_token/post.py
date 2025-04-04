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

from beamable_python_sdk.model.token_response import TokenResponse as TokenResponseSchema
from beamable_python_sdk.model.token_request_wrapper import TokenRequestWrapper as TokenRequestWrapperSchema
from beamable_python_sdk.model.token_request_wrapper_scope import TokenRequestWrapperScope as TokenRequestWrapperScopeSchema

from beamable_python_sdk.type.token_response import TokenResponse
from beamable_python_sdk.type.token_request_wrapper import TokenRequestWrapper
from beamable_python_sdk.type.token_request_wrapper_scope import TokenRequestWrapperScope

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.token_request_wrapper import TokenRequestWrapper as TokenRequestWrapperPydantic
from beamable_python_sdk.pydantic.token_response import TokenResponse as TokenResponsePydantic
from beamable_python_sdk.pydantic.token_request_wrapper_scope import TokenRequestWrapperScope as TokenRequestWrapperScopePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TokenRequestWrapperSchema


request_body_token_request_wrapper = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'scope',
]
SchemaFor200ResponseBodyApplicationJson = TokenResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TokenResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TokenResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _request_token_mapped_args(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if username is not None:
            _body["username"] = username
        if scope is not None:
            _body["scope"] = scope
        if refresh_token is not None:
            _body["refresh_token"] = refresh_token
        if third_party is not None:
            _body["third_party"] = third_party
        if redirect_uri is not None:
            _body["redirect_uri"] = redirect_uri
        if client_id is not None:
            _body["client_id"] = client_id
        if code is not None:
            _body["code"] = code
        if token is not None:
            _body["token"] = token
        if customer_scoped is not None:
            _body["customerScoped"] = customer_scoped
        if grant_type is not None:
            _body["grant_type"] = grant_type
        if password is not None:
            _body["password"] = password
        args.body = _body
        return args

    async def _arequest_token_oapg(
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
            path_template='/basic/auth/token',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_token_request_wrapper.serialize(body, content_type)
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


    def _request_token_oapg(
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
            path_template='/basic/auth/token',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_token_request_wrapper.serialize(body, content_type)
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


class RequestTokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arequest_token(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_token_mapped_args(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
        )
        return await self._arequest_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def request_token(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_token_mapped_args(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
        )
        return self._request_token_oapg(
            body=args.body,
        )

class RequestToken(BaseApi):

    async def arequest_token(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TokenResponsePydantic:
        raw_response = await self.raw.arequest_token(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
            **kwargs,
        )
        if validate:
            return TokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenResponsePydantic, raw_response.body)
    
    
    def request_token(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TokenResponsePydantic:
        raw_response = self.raw.request_token(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
        )
        if validate:
            return TokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_token_mapped_args(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
        )
        return await self._arequest_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        username: typing.Optional[str] = None,
        scope: typing.Optional[TokenRequestWrapperScope] = None,
        refresh_token: typing.Optional[str] = None,
        third_party: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        customer_scoped: typing.Optional[bool] = None,
        grant_type: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_token_mapped_args(
            username=username,
            scope=scope,
            refresh_token=refresh_token,
            third_party=third_party,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code=code,
            token=token,
            customer_scoped=customer_scoped,
            grant_type=grant_type,
            password=password,
        )
        return self._request_token_oapg(
            body=args.body,
        )

