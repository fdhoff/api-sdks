# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.me import Me
from etsy_seller.models.user import User

_get_me: Operation[Me] = Operation(
    id="getMe",
    method="GET",
    path="/v3/application/users/me",
    resource="users",
    name="get_me",
    params=(),
    response=Me,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("shops_r",)),
        ),
    ),
)
_get_user: Operation[User] = Operation(
    id="getUser",
    method="GET",
    path="/v3/application/users/{user_id}",
    resource="users",
    name="get",
    params=(Param("user_id", "user_id", "path"),),
    response=User,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("email_r",)),
        ),
    ),
)

OPERATIONS = (
    _get_me,
    _get_user,
)


class UsersApi(Resource):
    @checked
    def get_me(
        self,
    ) -> Me:
        """Get the user and shop IDs the access token belongs to."""
        return self._call(
            _get_me,
        )

    @checked
    def get(
        self,
        user_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> User:
        """Get one user."""
        return self._call(
            _get_user,
            user_id=user_id,
        )


class AsyncUsersApi(AsyncResource):
    @checked
    async def get_me(
        self,
    ) -> Me:
        """Get the user and shop IDs the access token belongs to."""
        return await self._call(
            _get_me,
        )

    @checked
    async def get(
        self,
        user_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> User:
        """Get one user."""
        return await self._call(
            _get_user,
            user_id=user_id,
        )
