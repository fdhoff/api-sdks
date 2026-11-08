# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.notification.models.public_key import PublicKey

_get_public_key: Operation[PublicKey] = Operation(
    id="getPublicKey",
    method="GET",
    path="/commerce/notification/v1/public_key/{public_key_id}",
    resource="public_keys",
    name="get",
    params=(Param("public_key_id", "public_key_id", "path"),),
    response=PublicKey,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (_get_public_key,)


class PublicKeysApi(Resource):
    @checked
    def get(
        self,
        public_key_id: StrictStr,
    ) -> PublicKey:
        """Get the public key that verifies a notification's signature."""
        return self._call(
            _get_public_key,
            public_key_id=public_key_id,
        )


class AsyncPublicKeysApi(AsyncResource):
    @checked
    async def get(
        self,
        public_key_id: StrictStr,
    ) -> PublicKey:
        """Get the public key that verifies a notification's signature."""
        return await self._call(
            _get_public_key,
            public_key_id=public_key_id,
        )
