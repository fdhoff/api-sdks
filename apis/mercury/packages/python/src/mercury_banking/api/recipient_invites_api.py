# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.create_recipient_invite_api_request import CreateRecipientInviteApiRequest
from mercury_banking.models.recipient_invite_api_paginated_response import RecipientInviteApiPaginatedResponse
from mercury_banking.models.recipient_invite_api_response import RecipientInviteApiResponse

_create_recipient_invite: Operation[RecipientInviteApiResponse] = Operation(
    id="createRecipientInvite",
    method="POST",
    path="/recipients/invites",
    resource="recipient_invites",
    name="create",
    params=(),
    response=RecipientInviteApiResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_recipient_invite: Operation[None] = Operation(
    id="deleteRecipientInvite",
    method="DELETE",
    path="/recipients/invites/{inviteId}",
    resource="recipient_invites",
    name="delete",
    params=(Param("inviteId", "invite_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_recipient_invite: Operation[RecipientInviteApiResponse] = Operation(
    id="getRecipientInvite",
    method="GET",
    path="/recipients/invites/{inviteId}",
    resource="recipient_invites",
    name="get",
    params=(Param("inviteId", "invite_id", "path"),),
    response=RecipientInviteApiResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_recipient_invites: Operation[RecipientInviteApiPaginatedResponse] = Operation(
    id="listRecipientInvites",
    method="GET",
    path="/recipients/invites",
    resource="recipient_invites",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
        Param("status", "status", "query"),
    ),
    response=RecipientInviteApiPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.RecipientInviteApiResponse,
    paging=Cursor(items="invites", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_recipient_invite,
    _delete_recipient_invite,
    _get_recipient_invite,
    _list_recipient_invites,
)


class RecipientInvitesApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateRecipientInviteApiRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInviteApiResponse:
        """Invite someone to add their own payment details as a recipient."""
        return self._call(
            _create_recipient_invite,
            _body=body,
        )

    @checked
    def delete(
        self,
        invite_id: StrictStr,
    ) -> None:
        """Delete a recipient invite."""
        return self._call(
            _delete_recipient_invite,
            invite_id=invite_id,
        )

    @checked
    def get(
        self,
        invite_id: StrictStr,
    ) -> RecipientInviteApiResponse:
        """Get one recipient invite."""
        return self._call(
            _get_recipient_invite,
            invite_id=invite_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[StrictStr] = None,
        end_before: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> RecipientInviteApiPaginatedResponse:
        """List one page of recipient invites."""
        return self._call(
            _list_recipient_invites,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            status=status,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[StrictStr] = None,
        end_before: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> Iterator[_models.RecipientInviteApiResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_recipient_invites,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            status=status,
        )


class AsyncRecipientInvitesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateRecipientInviteApiRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInviteApiResponse:
        """Invite someone to add their own payment details as a recipient."""
        return await self._call(
            _create_recipient_invite,
            _body=body,
        )

    @checked
    async def delete(
        self,
        invite_id: StrictStr,
    ) -> None:
        """Delete a recipient invite."""
        return await self._call(
            _delete_recipient_invite,
            invite_id=invite_id,
        )

    @checked
    async def get(
        self,
        invite_id: StrictStr,
    ) -> RecipientInviteApiResponse:
        """Get one recipient invite."""
        return await self._call(
            _get_recipient_invite,
            invite_id=invite_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[StrictStr] = None,
        end_before: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> RecipientInviteApiPaginatedResponse:
        """List one page of recipient invites."""
        return await self._call(
            _list_recipient_invites,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            status=status,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[StrictStr] = None,
        end_before: Optional[StrictStr] = None,
        order: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RecipientInviteApiResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_recipient_invites,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            status=status,
        )
