# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.negotiation import models as _models
from ebay_sell.negotiation.models.create_offers_request import CreateOffersRequest
from ebay_sell.negotiation.models.paged_eligible_item_collection import PagedEligibleItemCollection
from ebay_sell.negotiation.models.send_offer_to_interested_buyers_collection_response import (
    SendOfferToInterestedBuyersCollectionResponse,
)

_find_eligible_items: Operation[PagedEligibleItemCollection] = Operation(
    id="findEligibleItems",
    method="GET",
    path="/sell/negotiation/v1/find_eligible_items",
    resource="offers",
    name="find_eligible_items",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=PagedEligibleItemCollection,
    returns_json=True,
    iterator="iter_eligible_items",
    item=_models.EligibleItem,
    paging=NextLink(
        items="eligibleItems",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                ),
            ),
        ),
    ),
    host="api",
)
_send_offer_to_interested_buyers: Operation[SendOfferToInterestedBuyersCollectionResponse] = Operation(
    id="sendOfferToInterestedBuyers",
    method="POST",
    path="/sell/negotiation/v1/send_offer_to_interested_buyers",
    resource="offers",
    name="send_to_interested_buyers",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=SendOfferToInterestedBuyersCollectionResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)

OPERATIONS = (
    _find_eligible_items,
    _send_offer_to_interested_buyers,
)


class OffersApi(Resource):
    @checked
    def find_eligible_items(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PagedEligibleItemCollection:
        """List one page of the seller's listings with interested buyers."""
        return self._call(
            _find_eligible_items,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter_eligible_items(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Iterator[_models.EligibleItem]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_eligible_items,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def send_to_interested_buyers(
        self,
        body: Optional[Union[CreateOffersRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SendOfferToInterestedBuyersCollectionResponse:
        """Send a discount offer to the buyers interested in a listing."""
        return self._call(
            _send_offer_to_interested_buyers,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncOffersApi(AsyncResource):
    @checked
    async def find_eligible_items(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PagedEligibleItemCollection:
        """List one page of the seller's listings with interested buyers."""
        return await self._call(
            _find_eligible_items,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter_eligible_items(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.EligibleItem]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_eligible_items,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def send_to_interested_buyers(
        self,
        body: Optional[Union[CreateOffersRequest, Mapping[str, Any]]] = None,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> SendOfferToInterestedBuyersCollectionResponse:
        """Send a discount offer to the buyers interested in a listing."""
        return await self._call(
            _send_offer_to_interested_buyers,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
