# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.key_management.models.create_signing_key_request import CreateSigningKeyRequest
from ebay_sell.key_management.models.query_signing_keys_response import QuerySigningKeysResponse
from ebay_sell.key_management.models.signing_key import SigningKey

_create_signing_key: Operation[SigningKey] = Operation(
    id="createSigningKey",
    method="POST",
    path="/developer/key_management/v1/signing_key",
    resource="signing_keys",
    name="create",
    params=(),
    response=SigningKey,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="apiz",
)
_get_signing_key: Operation[SigningKey] = Operation(
    id="getSigningKey",
    method="GET",
    path="/developer/key_management/v1/signing_key/{signing_key_id}",
    resource="signing_keys",
    name="get",
    params=(Param("signing_key_id", "signing_key_id", "path"),),
    response=SigningKey,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="apiz",
)
_get_signing_keys: Operation[QuerySigningKeysResponse] = Operation(
    id="getSigningKeys",
    method="GET",
    path="/developer/key_management/v1/signing_key",
    resource="signing_keys",
    name="list",
    params=(),
    response=QuerySigningKeysResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="apiz",
)

OPERATIONS = (
    _create_signing_key,
    _get_signing_key,
    _get_signing_keys,
)


class SigningKeysApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateSigningKeyRequest, Mapping[str, Any]]] = None,
    ) -> SigningKey:
        """Create a signing key pair and return its private key once."""
        return self._call(
            _create_signing_key,
            _body=body,
        )

    @checked
    def get(
        self,
        signing_key_id: StrictStr,
    ) -> SigningKey:
        """Get one signing key."""
        return self._call(
            _get_signing_key,
            signing_key_id=signing_key_id,
        )

    @checked
    def list(
        self,
    ) -> QuerySigningKeysResponse:
        """List the app's signing keys."""
        return self._call(
            _get_signing_keys,
        )


class AsyncSigningKeysApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateSigningKeyRequest, Mapping[str, Any]]] = None,
    ) -> SigningKey:
        """Create a signing key pair and return its private key once."""
        return await self._call(
            _create_signing_key,
            _body=body,
        )

    @checked
    async def get(
        self,
        signing_key_id: StrictStr,
    ) -> SigningKey:
        """Get one signing key."""
        return await self._call(
            _get_signing_key,
            signing_key_id=signing_key_id,
        )

    @checked
    async def list(
        self,
    ) -> QuerySigningKeysResponse:
        """List the app's signing keys."""
        return await self._call(
            _get_signing_keys,
        )
