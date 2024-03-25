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

from beamable_python_sdk.model.announcement_client_data import AnnouncementClientData as AnnouncementClientDataSchema
from beamable_python_sdk.model.empty_response import EmptyResponse as EmptyResponseSchema
from beamable_python_sdk.model.announcement_attachment import AnnouncementAttachment as AnnouncementAttachmentSchema
from beamable_python_sdk.model.announcement import Announcement as AnnouncementSchema
from beamable_python_sdk.model.player_stat_requirement import PlayerStatRequirement as PlayerStatRequirementSchema
from beamable_python_sdk.model.announcement_validation_errors import AnnouncementValidationErrors as AnnouncementValidationErrorsSchema
from beamable_python_sdk.model.player_reward import PlayerReward as PlayerRewardSchema

from beamable_python_sdk.type.player_reward import PlayerReward
from beamable_python_sdk.type.empty_response import EmptyResponse
from beamable_python_sdk.type.player_stat_requirement import PlayerStatRequirement
from beamable_python_sdk.type.announcement_client_data import AnnouncementClientData
from beamable_python_sdk.type.announcement_validation_errors import AnnouncementValidationErrors
from beamable_python_sdk.type.announcement_attachment import AnnouncementAttachment
from beamable_python_sdk.type.announcement import Announcement

from ...api_client import Dictionary
from beamable_python_sdk.pydantic.player_stat_requirement import PlayerStatRequirement as PlayerStatRequirementPydantic
from beamable_python_sdk.pydantic.empty_response import EmptyResponse as EmptyResponsePydantic
from beamable_python_sdk.pydantic.announcement_attachment import AnnouncementAttachment as AnnouncementAttachmentPydantic
from beamable_python_sdk.pydantic.player_reward import PlayerReward as PlayerRewardPydantic
from beamable_python_sdk.pydantic.announcement import Announcement as AnnouncementPydantic
from beamable_python_sdk.pydantic.announcement_client_data import AnnouncementClientData as AnnouncementClientDataPydantic
from beamable_python_sdk.pydantic.announcement_validation_errors import AnnouncementValidationErrors as AnnouncementValidationErrorsPydantic

# body param
SchemaForRequestBodyApplicationJson = AnnouncementSchema


request_body_announcement = api_client.RequestBody(
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

    def _create_new_announcement_mapped_args(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if summary is not None:
            _body["summary"] = summary
        if title is not None:
            _body["title"] = title
        if body is not None:
            _body["body"] = body
        if channel is not None:
            _body["channel"] = channel
        if start_date is not None:
            _body["start_date"] = start_date
        if gift is not None:
            _body["gift"] = gift
        if mongo_start_date is not None:
            _body["mongo_start_date"] = mongo_start_date
        if stat_requirements is not None:
            _body["stat_requirements"] = stat_requirements
        if mongo_end_date is not None:
            _body["mongo_end_date"] = mongo_end_date
        if symbol is not None:
            _body["symbol"] = symbol
        if client_data is not None:
            _body["clientData"] = client_data
        if validation_errors is not None:
            _body["validationErrors"] = validation_errors
        if end_date is not None:
            _body["end_date"] = end_date
        if attachments is not None:
            _body["attachments"] = attachments
        args.body = _body
        return args

    async def _acreate_new_announcement_oapg(
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
            path_template='/basic/announcements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_announcement.serialize(body, content_type)
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


    def _create_new_announcement_oapg(
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
            path_template='/basic/announcements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_announcement.serialize(body, content_type)
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


class CreateNewAnnouncementRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_announcement(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_announcement_mapped_args(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
        )
        return await self._acreate_new_announcement_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_announcement(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_announcement_mapped_args(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
        )
        return self._create_new_announcement_oapg(
            body=args.body,
        )

class CreateNewAnnouncement(BaseApi):

    async def acreate_new_announcement(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmptyResponsePydantic:
        raw_response = await self.raw.acreate_new_announcement(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
            **kwargs,
        )
        if validate:
            return EmptyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponsePydantic, raw_response.body)
    
    
    def create_new_announcement(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
        validate: bool = False,
    ) -> EmptyResponsePydantic:
        raw_response = self.raw.create_new_announcement(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
        )
        if validate:
            return EmptyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmptyResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_announcement_mapped_args(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
        )
        return await self._acreate_new_announcement_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        summary: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        gift: typing.Optional[PlayerReward] = None,
        mongo_start_date: typing.Optional[int] = None,
        stat_requirements: typing.Optional[typing.List[PlayerStatRequirement]] = None,
        mongo_end_date: typing.Optional[int] = None,
        symbol: typing.Optional[str] = None,
        client_data: typing.Optional[AnnouncementClientData] = None,
        validation_errors: typing.Optional[AnnouncementValidationErrors] = None,
        end_date: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[AnnouncementAttachment]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_announcement_mapped_args(
            summary=summary,
            title=title,
            body=body,
            channel=channel,
            start_date=start_date,
            gift=gift,
            mongo_start_date=mongo_start_date,
            stat_requirements=stat_requirements,
            mongo_end_date=mongo_end_date,
            symbol=symbol,
            client_data=client_data,
            validation_errors=validation_errors,
            end_date=end_date,
            attachments=attachments,
        )
        return self._create_new_announcement_oapg(
            body=args.body,
        )

