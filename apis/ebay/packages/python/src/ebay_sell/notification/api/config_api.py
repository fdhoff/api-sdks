# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.notification.models.config import Config

_get_config: Operation[Config] = Operation(
    id="getConfig",
    method="GET",
    path="/commerce/notification/v1/config",
    resource="config",
    name="get",
    params=(),
    response=Config,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_update_config: Operation[None] = Operation(
    id="updateConfig",
    method="PUT",
    path="/commerce/notification/v1/config",
    resource="config",
    name="update",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_config,
    _update_config,
)


class ConfigApi(Resource):
    @checked
    def get(
        self,
    ) -> Config:
        """Get the app's notification settings."""
        return self._call(
            _get_config,
        )

    @checked
    def update(
        self,
        body: Optional[Union[Config, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the app's notification settings."""
        return self._call(
            _update_config,
            _body=body,
        )


class AsyncConfigApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> Config:
        """Get the app's notification settings."""
        return await self._call(
            _get_config,
        )

    @checked
    async def update(
        self,
        body: Optional[Union[Config, Mapping[str, Any]]] = None,
    ) -> None:
        """Update the app's notification settings."""
        return await self._call(
            _update_config,
            _body=body,
        )
