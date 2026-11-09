# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import AsyncIterator, Iterator, List, Optional

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import (
    AsyncDownload,
    AsyncResource,
    Cursor,
    Download,
    FileInput,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.m10_response200 import M10Response200
from mirakl_seller.models.m11_response200 import M11Response200
from mirakl_seller.models.m12_request_multipart_form_data_message_input import M12RequestMultipartFormDataMessageInput
from mirakl_seller.models.m12_response201 import M12Response201
from mirakl_seller.models.m14_request_multipart_form_data_thread_input import M14RequestMultipartFormDataThreadInput
from mirakl_seller.models.m14_response201 import M14Response201

_m10: Operation[M10Response200] = Operation(
    id="M10",
    method="GET",
    path="/api/inbox/threads/{thread_id}",
    resource="messages",
    name="get_thread",
    params=(
        Param("thread_id", "thread_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=M10Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_MESSAGE_READ",
                    "ROLE_PARTNER_MESSAGE_READ",
                ),
            ),
        ),
    ),
)
_m11: Operation[M11Response200] = Operation(
    id="M11",
    method="GET",
    path="/api/inbox/threads",
    resource="messages",
    name="list_threads",
    params=(
        Param("entity_type", "entity_type", "query"),
        Param("entity_id", "entity_id", "query"),
        Param("updated_since", "updated_since", "query"),
        Param("with_messages", "with_messages", "query"),
        Param("channel_codes", "channel_codes", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
    ),
    response=M11Response200,
    returns_json=True,
    iterator="iter_threads",
    item=_models.M11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_MESSAGE_READ",
                    "ROLE_PARTNER_MESSAGE_READ",
                ),
            ),
        ),
    ),
)
_m12: Operation[M12Response201] = Operation(
    id="M12",
    method="POST",
    path="/api/inbox/threads/{thread_id}/message",
    resource="messages",
    name="reply",
    params=(
        Param("thread_id", "thread_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("files", "files", "form"),
        Param("message_input", "message_input", "form"),
    ),
    response=M12Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_MESSAGE_WRITE",
                    "ROLE_PARTNER_MESSAGE_WRITE",
                ),
            ),
        ),
    ),
)
_m13: Operation[None] = Operation(
    id="M13",
    method="GET",
    path="/api/inbox/threads/{attachment_id}/download",
    resource="messages",
    name="download_attachment",
    params=(
        Param("attachment_id", "attachment_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_OFFER_MESSAGE_READ",
                    "ROLE_PARTNER_MESSAGE_READ",
                ),
            ),
        ),
    ),
)
_m14: Operation[M14Response201] = Operation(
    id="M14",
    method="POST",
    path="/api/inbox/threads",
    resource="messages",
    name="create_thread",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("files", "files", "form"),
        Param("thread_input", "thread_input", "form"),
    ),
    response=M14Response201,
    returns_json=True,
    security=((Scheme("Shop-API-Key", ("ROLE_SHOP_ADMIN",)),),),
)

OPERATIONS = (
    _m10,
    _m11,
    _m12,
    _m13,
    _m14,
)


class MessagesApi(Resource):
    @checked
    def get_thread(
        self,
        thread_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> M10Response200:
        """Get a message thread (M10)."""
        return self._call(
            _m10,
            thread_id=thread_id,
            shop_id=shop_id,
        )

    @checked
    def list_threads(
        self,
        *,
        entity_type: Optional[StrictStr] = None,
        entity_id: Optional[List[StrictStr]] = None,
        updated_since: Optional[datetime] = None,
        with_messages: Optional[StrictBool] = None,
        channel_codes: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
    ) -> M11Response200:
        """List one page of message threads (M11)."""
        return self._call(
            _m11,
            entity_type=entity_type,
            entity_id=entity_id,
            updated_since=updated_since,
            with_messages=with_messages,
            channel_codes=channel_codes,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
        )

    @checked
    def iter_threads(
        self,
        *,
        entity_type: Optional[StrictStr] = None,
        entity_id: Optional[List[StrictStr]] = None,
        updated_since: Optional[datetime] = None,
        with_messages: Optional[StrictBool] = None,
        channel_codes: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
    ) -> Iterator[_models.M11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _m11,
            entity_type=entity_type,
            entity_id=entity_id,
            updated_since=updated_since,
            with_messages=with_messages,
            channel_codes=channel_codes,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
        )

    @checked
    def reply(
        self,
        thread_id: StrictStr,
        *,
        message_input: M12RequestMultipartFormDataMessageInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> M12Response201:
        """Reply to a message thread (M12)."""
        return self._call(
            _m12,
            thread_id=thread_id,
            shop_id=shop_id,
            files=files,
            message_input=message_input,
        )

    @checked
    def download_attachment(
        self,
        attachment_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download a message attachment (M13). Close the download, or read it in a `with` block."""
        return self._download(
            _m13,
            attachment_id=attachment_id,
            shop_id=shop_id,
        )

    @checked
    def create_thread(
        self,
        *,
        thread_input: M14RequestMultipartFormDataThreadInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> M14Response201:
        """Start a message thread with the operator (M14)."""
        return self._call(
            _m14,
            shop_id=shop_id,
            files=files,
            thread_input=thread_input,
        )


class AsyncMessagesApi(AsyncResource):
    @checked
    async def get_thread(
        self,
        thread_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> M10Response200:
        """Get a message thread (M10)."""
        return await self._call(
            _m10,
            thread_id=thread_id,
            shop_id=shop_id,
        )

    @checked
    async def list_threads(
        self,
        *,
        entity_type: Optional[StrictStr] = None,
        entity_id: Optional[List[StrictStr]] = None,
        updated_since: Optional[datetime] = None,
        with_messages: Optional[StrictBool] = None,
        channel_codes: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
    ) -> M11Response200:
        """List one page of message threads (M11)."""
        return await self._call(
            _m11,
            entity_type=entity_type,
            entity_id=entity_id,
            updated_since=updated_since,
            with_messages=with_messages,
            channel_codes=channel_codes,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
        )

    @checked
    def iter_threads(
        self,
        *,
        entity_type: Optional[StrictStr] = None,
        entity_id: Optional[List[StrictStr]] = None,
        updated_since: Optional[datetime] = None,
        with_messages: Optional[StrictBool] = None,
        channel_codes: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.M11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _m11,
            entity_type=entity_type,
            entity_id=entity_id,
            updated_since=updated_since,
            with_messages=with_messages,
            channel_codes=channel_codes,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
        )

    @checked
    async def reply(
        self,
        thread_id: StrictStr,
        *,
        message_input: M12RequestMultipartFormDataMessageInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> M12Response201:
        """Reply to a message thread (M12)."""
        return await self._call(
            _m12,
            thread_id=thread_id,
            shop_id=shop_id,
            files=files,
            message_input=message_input,
        )

    @checked
    async def download_attachment(
        self,
        attachment_id: StrictStr,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download a message attachment (M13). Close the download, or read it in an `async with` block."""
        return await self._download(
            _m13,
            attachment_id=attachment_id,
            shop_id=shop_id,
        )

    @checked
    async def create_thread(
        self,
        *,
        thread_input: M14RequestMultipartFormDataThreadInput,
        shop_id: Optional[StrictInt] = None,
        files: Optional[List[FileInput]] = None,
    ) -> M14Response201:
        """Start a message thread with the operator (M14)."""
        return await self._call(
            _m14,
            shop_id=shop_id,
            files=files,
            thread_input=thread_input,
        )
