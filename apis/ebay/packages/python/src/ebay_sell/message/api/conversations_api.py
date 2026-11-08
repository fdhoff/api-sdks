# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.message import models as _models
from ebay_sell.message.models.bulk_update_conversations_request import BulkUpdateConversationsRequest
from ebay_sell.message.models.bulk_update_conversations_response import BulkUpdateConversationsResponse
from ebay_sell.message.models.get_all_my_conversations_response import GetAllMyConversationsResponse
from ebay_sell.message.models.get_messages_by_conversation_id_response import GetMessagesByConversationIdResponse
from ebay_sell.message.models.send_message_request import SendMessageRequest
from ebay_sell.message.models.send_message_response import SendMessageResponse
from ebay_sell.message.models.update_conversation_request import UpdateConversationRequest

_bulk_update_conversation: Operation[BulkUpdateConversationsResponse] = Operation(
    id="bulkUpdateConversation",
    method="POST",
    path="/commerce/message/v1/bulk_update_conversation",
    resource="conversations",
    name="bulk_update",
    params=(),
    response=BulkUpdateConversationsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.message",)),),),
    host="api",
)
_get_conversation: Operation[GetMessagesByConversationIdResponse] = Operation(
    id="getConversation",
    method="GET",
    path="/commerce/message/v1/conversation/{conversation_id}",
    resource="conversations",
    name="get",
    params=(
        Param("conversation_id", "conversation_id", "path"),
        Param("conversation_type", "conversation_type", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=GetMessagesByConversationIdResponse,
    returns_json=True,
    iterator="iter_messages",
    item=_models.MessageDetail,
    paging=NextLink(
        items="messages",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.message",)),),),
    host="api",
)
_get_conversations: Operation[GetAllMyConversationsResponse] = Operation(
    id="getConversations",
    method="GET",
    path="/commerce/message/v1/conversation",
    resource="conversations",
    name="list",
    params=(
        Param("conversation_status", "conversation_status", "query"),
        Param("conversation_type", "conversation_type", "query"),
        Param("end_time", "end_time", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("other_party_username", "other_party_username", "query"),
        Param("reference_id", "reference_id", "query"),
        Param("reference_type", "reference_type", "query"),
        Param("start_time", "start_time", "query"),
    ),
    response=GetAllMyConversationsResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ConversationDetail,
    paging=NextLink(
        items="conversations",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.message",)),),),
    host="api",
)
_send_message: Operation[SendMessageResponse] = Operation(
    id="sendMessage",
    method="POST",
    path="/commerce/message/v1/send_message",
    resource="conversations",
    name="send",
    params=(),
    response=SendMessageResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.message",)),),),
    host="api",
)
_update_conversation: Operation[None] = Operation(
    id="updateConversation",
    method="POST",
    path="/commerce/message/v1/update_conversation",
    resource="conversations",
    name="update",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.message",)),),),
    host="api",
)

OPERATIONS = (
    _bulk_update_conversation,
    _get_conversation,
    _get_conversations,
    _send_message,
    _update_conversation,
)


class ConversationsApi(Resource):
    @checked
    def bulk_update(
        self,
        body: Optional[Union[BulkUpdateConversationsRequest, Mapping[str, Any]]] = None,
    ) -> BulkUpdateConversationsResponse:
        """Update the status of several conversations."""
        return self._call(
            _bulk_update_conversation,
            _body=body,
        )

    @checked
    def get(
        self,
        conversation_id: StrictStr,
        *,
        conversation_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> GetMessagesByConversationIdResponse:
        """Get one conversation with one page of its messages."""
        return self._call(
            _get_conversation,
            conversation_id=conversation_id,
            conversation_type=conversation_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_messages(
        self,
        conversation_id: StrictStr,
        *,
        conversation_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.MessageDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_conversation,
            conversation_id=conversation_id,
            conversation_type=conversation_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def list(
        self,
        *,
        conversation_type: StrictStr,
        conversation_status: Optional[StrictStr] = None,
        end_time: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        other_party_username: Optional[StrictStr] = None,
        reference_id: Optional[StrictStr] = None,
        reference_type: Optional[StrictStr] = None,
        start_time: Optional[StrictStr] = None,
    ) -> GetAllMyConversationsResponse:
        """List one page of conversations."""
        return self._call(
            _get_conversations,
            conversation_status=conversation_status,
            conversation_type=conversation_type,
            end_time=end_time,
            limit=limit,
            offset=offset,
            other_party_username=other_party_username,
            reference_id=reference_id,
            reference_type=reference_type,
            start_time=start_time,
        )

    @checked
    def iter(
        self,
        *,
        conversation_type: StrictStr,
        conversation_status: Optional[StrictStr] = None,
        end_time: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        other_party_username: Optional[StrictStr] = None,
        reference_id: Optional[StrictStr] = None,
        reference_type: Optional[StrictStr] = None,
        start_time: Optional[StrictStr] = None,
    ) -> Iterator[_models.ConversationDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_conversations,
            conversation_status=conversation_status,
            conversation_type=conversation_type,
            end_time=end_time,
            limit=limit,
            offset=offset,
            other_party_username=other_party_username,
            reference_id=reference_id,
            reference_type=reference_type,
            start_time=start_time,
        )

    @checked
    def send(
        self,
        body: Optional[Union[SendMessageRequest, Mapping[str, Any]]] = None,
    ) -> SendMessageResponse:
        """Send a message"""
        return self._call(
            _send_message,
            _body=body,
        )

    @checked
    def update(
        self,
        body: Optional[Union[UpdateConversationRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the status of one conversation."""
        return self._call(
            _update_conversation,
            _body=body,
        )


class AsyncConversationsApi(AsyncResource):
    @checked
    async def bulk_update(
        self,
        body: Optional[Union[BulkUpdateConversationsRequest, Mapping[str, Any]]] = None,
    ) -> BulkUpdateConversationsResponse:
        """Update the status of several conversations."""
        return await self._call(
            _bulk_update_conversation,
            _body=body,
        )

    @checked
    async def get(
        self,
        conversation_id: StrictStr,
        *,
        conversation_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> GetMessagesByConversationIdResponse:
        """Get one conversation with one page of its messages."""
        return await self._call(
            _get_conversation,
            conversation_id=conversation_id,
            conversation_type=conversation_type,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter_messages(
        self,
        conversation_id: StrictStr,
        *,
        conversation_type: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.MessageDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_conversation,
            conversation_id=conversation_id,
            conversation_type=conversation_type,
            limit=limit,
            offset=offset,
        )

    @checked
    async def list(
        self,
        *,
        conversation_type: StrictStr,
        conversation_status: Optional[StrictStr] = None,
        end_time: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        other_party_username: Optional[StrictStr] = None,
        reference_id: Optional[StrictStr] = None,
        reference_type: Optional[StrictStr] = None,
        start_time: Optional[StrictStr] = None,
    ) -> GetAllMyConversationsResponse:
        """List one page of conversations."""
        return await self._call(
            _get_conversations,
            conversation_status=conversation_status,
            conversation_type=conversation_type,
            end_time=end_time,
            limit=limit,
            offset=offset,
            other_party_username=other_party_username,
            reference_id=reference_id,
            reference_type=reference_type,
            start_time=start_time,
        )

    @checked
    def iter(
        self,
        *,
        conversation_type: StrictStr,
        conversation_status: Optional[StrictStr] = None,
        end_time: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        other_party_username: Optional[StrictStr] = None,
        reference_id: Optional[StrictStr] = None,
        reference_type: Optional[StrictStr] = None,
        start_time: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ConversationDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_conversations,
            conversation_status=conversation_status,
            conversation_type=conversation_type,
            end_time=end_time,
            limit=limit,
            offset=offset,
            other_party_username=other_party_username,
            reference_id=reference_id,
            reference_type=reference_type,
            start_time=start_time,
        )

    @checked
    async def send(
        self,
        body: Optional[Union[SendMessageRequest, Mapping[str, Any]]] = None,
    ) -> SendMessageResponse:
        """Send a message"""
        return await self._call(
            _send_message,
            _body=body,
        )

    @checked
    async def update(
        self,
        body: Optional[Union[UpdateConversationRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the status of one conversation."""
        return await self._call(
            _update_conversation,
            _body=body,
        )
