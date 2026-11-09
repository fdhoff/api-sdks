# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.user_details import UserDetails
from mercury_banking.models.users_paginated_response import UsersPaginatedResponse

_get_user: Operation[UserDetails] = Operation(
    id="getUser",
    method="GET",
    path="/users/{userId}",
    resource="users",
    name="get",
    params=(Param("userId", "user_id", "path"),),
    response=UserDetails,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_users: Operation[UsersPaginatedResponse] = Operation(
    id="getUsers",
    method="GET",
    path="/users",
    resource="users",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=UsersPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.UserDetails,
    paging=Cursor(items="users", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_user,
    _get_users,
)


class UsersApi(Resource):
    @checked
    def get(
        self,
        user_id: UUID,
    ) -> UserDetails:
        """Get one user."""
        return self._call(
            _get_user,
            user_id=user_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> UsersPaginatedResponse:
        """List one page of your organization's users."""
        return self._call(
            _get_users,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.UserDetails]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_users,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )


class AsyncUsersApi(AsyncResource):
    @checked
    async def get(
        self,
        user_id: UUID,
    ) -> UserDetails:
        """Get one user."""
        return await self._call(
            _get_user,
            user_id=user_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> UsersPaginatedResponse:
        """List one page of your organization's users."""
        return await self._call(
            _get_users,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.UserDetails]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_users,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )
