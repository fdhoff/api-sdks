# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.recommendation import models as _models
from ebay_sell.recommendation.models.find_listing_recommendation_request import FindListingRecommendationRequest
from ebay_sell.recommendation.models.paged_listing_recommendation_collection import PagedListingRecommendationCollection

_find_listing_recommendations: Operation[PagedListingRecommendationCollection] = Operation(
    id="findListingRecommendations",
    method="POST",
    path="/sell/recommendation/v1/find",
    resource="listing_recommendations",
    name="find",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=PagedListingRecommendationCollection,
    returns_json=True,
    iterator="iter",
    item=_models.ListingRecommendation,
    paging=NextLink(
        items="listingRecommendations",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)

OPERATIONS = (_find_listing_recommendations,)


class ListingRecommendationsApi(Resource):
    @checked
    def find(
        self,
        body: Optional[Union[FindListingRecommendationRequest, Mapping[str, Any]]] = None,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PagedListingRecommendationCollection:
        """List one page of recommendations for the seller's listings."""
        return self._call(
            _find_listing_recommendations,
            _body=body,
            filter=filter,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        body: Optional[Union[FindListingRecommendationRequest, Mapping[str, Any]]] = None,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> Iterator[_models.ListingRecommendation]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_listing_recommendations,
            _body=body,
            filter=filter,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncListingRecommendationsApi(AsyncResource):
    @checked
    async def find(
        self,
        body: Optional[Union[FindListingRecommendationRequest, Mapping[str, Any]]] = None,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> PagedListingRecommendationCollection:
        """List one page of recommendations for the seller's listings."""
        return await self._call(
            _find_listing_recommendations,
            _body=body,
            filter=filter,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        body: Optional[Union[FindListingRecommendationRequest, Mapping[str, Any]]] = None,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ListingRecommendation]:
        """Iterate every item across all pages."""
        return self._paginate(
            _find_listing_recommendations,
            _body=body,
            filter=filter,
            limit=limit,
            offset=offset,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
