# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.pong import Pong

_ping: Operation[Pong] = Operation(
    id="ping",
    method="GET",
    path="/v3/application/openapi-ping",
    resource="application",
    name="ping",
    params=(),
    response=Pong,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_token_scopes: Operation[object] = Operation(
    id="tokenScopes",
    method="POST",
    path="/v3/application/scopes",
    resource="application",
    name="get_token_scopes",
    params=(Param("token", "token", "urlencoded"),),
    response=object,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)

OPERATIONS = (
    _ping,
    _token_scopes,
)


class ApplicationApi(Resource):
    @checked
    def ping(
        self,
    ) -> Pong:
        """Check that the API key works."""
        return self._call(
            _ping,
        )

    @checked
    def get_token_scopes(
        self,
        *,
        token: StrictStr,
    ) -> object:
        """List the scopes an access token grants."""
        return self._call(
            _token_scopes,
            token=token,
        )


class AsyncApplicationApi(AsyncResource):
    @checked
    async def ping(
        self,
    ) -> Pong:
        """Check that the API key works."""
        return await self._call(
            _ping,
        )

    @checked
    async def get_token_scopes(
        self,
        *,
        token: StrictStr,
    ) -> object:
        """List the scopes an access token grants."""
        return await self._call(
            _token_scopes,
            token=token,
        )
