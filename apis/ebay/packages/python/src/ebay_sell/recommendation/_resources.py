# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.recommendation.api import listing_recommendations_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation for operations in (listing_recommendations_api.OPERATIONS,) for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.listing_recommendations = listing_recommendations_api.ListingRecommendationsApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.listing_recommendations = listing_recommendations_api.AsyncListingRecommendationsApi(transport)
