# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.notification.api import config_api, destinations_api, public_keys_api, subscriptions_api, topics_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        config_api.OPERATIONS,
        destinations_api.OPERATIONS,
        public_keys_api.OPERATIONS,
        subscriptions_api.OPERATIONS,
        topics_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.config = config_api.ConfigApi(transport)
        self.destinations = destinations_api.DestinationsApi(transport)
        self.public_keys = public_keys_api.PublicKeysApi(transport)
        self.subscriptions = subscriptions_api.SubscriptionsApi(transport)
        self.topics = topics_api.TopicsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.config = config_api.AsyncConfigApi(transport)
        self.destinations = destinations_api.AsyncDestinationsApi(transport)
        self.public_keys = public_keys_api.AsyncPublicKeysApi(transport)
        self.subscriptions = subscriptions_api.AsyncSubscriptionsApi(transport)
        self.topics = topics_api.AsyncTopicsApi(transport)
