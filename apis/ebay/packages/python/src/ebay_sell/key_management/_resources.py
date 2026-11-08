# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.key_management.api import signing_keys_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation for operations in (signing_keys_api.OPERATIONS,) for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.signing_keys = signing_keys_api.SigningKeysApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.signing_keys = signing_keys_api.AsyncSigningKeysApi(transport)
