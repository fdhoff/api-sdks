# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.metadata.models.shipping_carrier_response import ShippingCarrierResponse
from ebay_sell.metadata.models.shipping_exclude_location_response import ShippingExcludeLocationResponse
from ebay_sell.metadata.models.shipping_handling_time_response import ShippingHandlingTimeResponse
from ebay_sell.metadata.models.shipping_location_response import ShippingLocationResponse
from ebay_sell.metadata.models.shipping_service_response import ShippingServiceResponse

_get_exclude_shipping_locations: Operation[ShippingExcludeLocationResponse] = Operation(
    id="getExcludeShippingLocations",
    method="GET",
    path="/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_exclude_shipping_locations",
    resource="shipping",
    name="get_excluded_locations",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ShippingExcludeLocationResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_handling_times: Operation[ShippingHandlingTimeResponse] = Operation(
    id="getHandlingTimes",
    method="GET",
    path="/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_handling_times",
    resource="shipping",
    name="get_handling_times",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ShippingHandlingTimeResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_shipping_carriers: Operation[ShippingCarrierResponse] = Operation(
    id="getShippingCarriers",
    method="GET",
    path="/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_carriers",
    resource="shipping",
    name="get_carriers",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ShippingCarrierResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_shipping_locations: Operation[ShippingLocationResponse] = Operation(
    id="getShippingLocations",
    method="GET",
    path="/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_locations",
    resource="shipping",
    name="get_locations",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ShippingLocationResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_shipping_services: Operation[ShippingServiceResponse] = Operation(
    id="getShippingServices",
    method="GET",
    path="/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_services",
    resource="shipping",
    name="get_services",
    params=(Param("marketplace_id", "marketplace_id", "path"),),
    response=ShippingServiceResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)

OPERATIONS = (
    _get_exclude_shipping_locations,
    _get_handling_times,
    _get_shipping_carriers,
    _get_shipping_locations,
    _get_shipping_services,
)


class ShippingApi(Resource):
    @checked
    def get_excluded_locations(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingExcludeLocationResponse:
        """List the regions and countries a seller can exclude from shipping."""
        return self._call(
            _get_exclude_shipping_locations,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_handling_times(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingHandlingTimeResponse:
        """List the handling times a marketplace accepts."""
        return self._call(
            _get_handling_times,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_carriers(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingCarrierResponse:
        """List the shipping carriers of a marketplace."""
        return self._call(
            _get_shipping_carriers,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_locations(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingLocationResponse:
        """List the shipping locations of a marketplace."""
        return self._call(
            _get_shipping_locations,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_services(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingServiceResponse:
        """List the shipping services of a marketplace."""
        return self._call(
            _get_shipping_services,
            marketplace_id=marketplace_id,
        )


class AsyncShippingApi(AsyncResource):
    @checked
    async def get_excluded_locations(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingExcludeLocationResponse:
        """List the regions and countries a seller can exclude from shipping."""
        return await self._call(
            _get_exclude_shipping_locations,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_handling_times(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingHandlingTimeResponse:
        """List the handling times a marketplace accepts."""
        return await self._call(
            _get_handling_times,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_carriers(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingCarrierResponse:
        """List the shipping carriers of a marketplace."""
        return await self._call(
            _get_shipping_carriers,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_locations(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingLocationResponse:
        """List the shipping locations of a marketplace."""
        return await self._call(
            _get_shipping_locations,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_services(
        self,
        marketplace_id: StrictStr,
    ) -> ShippingServiceResponse:
        """List the shipping services of a marketplace."""
        return await self._call(
            _get_shipping_services,
            marketplace_id=marketplace_id,
        )
