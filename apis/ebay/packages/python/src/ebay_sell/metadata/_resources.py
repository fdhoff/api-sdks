# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.metadata.api import compatibilities_api, countries_api, marketplaces_api, shipping_api

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        compatibilities_api.OPERATIONS,
        countries_api.OPERATIONS,
        marketplaces_api.OPERATIONS,
        shipping_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.compatibilities = compatibilities_api.CompatibilitiesApi(transport)
        self.countries = countries_api.CountriesApi(transport)
        self.marketplaces = marketplaces_api.MarketplacesApi(transport)
        self.shipping = shipping_api.ShippingApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.compatibilities = compatibilities_api.AsyncCompatibilitiesApi(transport)
        self.countries = countries_api.AsyncCountriesApi(transport)
        self.marketplaces = marketplaces_api.AsyncMarketplacesApi(transport)
        self.shipping = shipping_api.AsyncShippingApi(transport)
