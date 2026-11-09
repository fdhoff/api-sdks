# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.items_paged_collection import ItemsPagedCollection
from ebay_sell.marketing.models.promotions_paged_collection import PromotionsPagedCollection

_get_listing_set: Operation[ItemsPagedCollection] = Operation(
    id="getListingSet",
    method="GET",
    path="/sell/marketing/v1/promotion/{promotion_id}/get_listing_set",
    resource="promotions",
    name="get_listing_set",
    params=(
        Param("promotion_id", "promotion_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("q", "q", "query"),
        Param("sort", "sort", "query"),
        Param("status", "status", "query"),
    ),
    response=ItemsPagedCollection,
    returns_json=True,
    iterator="iter_listing_set",
    item=_models.ListingDetail,
    paging=NextLink(
        items="listings",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_promotions: Operation[PromotionsPagedCollection] = Operation(
    id="getPromotions",
    method="GET",
    path="/sell/marketing/v1/promotion",
    resource="promotions",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("marketplace_id", "marketplace_id", "query"),
        Param("offset", "offset", "query"),
        Param("promotion_status", "promotion_status", "query"),
        Param("promotion_type", "promotion_type", "query"),
        Param("q", "q", "query"),
        Param("sort", "sort", "query"),
    ),
    response=PromotionsPagedCollection,
    returns_json=True,
    iterator="iter",
    item=_models.PromotionDetail,
    paging=NextLink(
        items="promotions",
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
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                ),
            ),
        ),
    ),
    host="api",
)
_pause_promotion: Operation[None] = Operation(
    id="pausePromotion",
    method="POST",
    path="/sell/marketing/v1/promotion/{promotion_id}/pause",
    resource="promotions",
    name="pause",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_resume_promotion: Operation[None] = Operation(
    id="resumePromotion",
    method="POST",
    path="/sell/marketing/v1/promotion/{promotion_id}/resume",
    resource="promotions",
    name="resume",
    params=(Param("promotion_id", "promotion_id", "path"),),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)

OPERATIONS = (
    _get_listing_set,
    _get_promotions,
    _pause_promotion,
    _resume_promotion,
)


class PromotionsApi(Resource):
    @checked
    def get_listing_set(
        self,
        promotion_id: StrictStr,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> ItemsPagedCollection:
        """List one page of the listings in a promotion."""
        return self._call(
            _get_listing_set,
            promotion_id=promotion_id,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
            status=status,
        )

    @checked
    def iter_listing_set(
        self,
        promotion_id: StrictStr,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> Iterator[_models.ListingDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listing_set,
            promotion_id=promotion_id,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
            status=status,
        )

    @checked
    def list(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PromotionsPagedCollection:
        """List one page of the seller's promotions on a marketplace."""
        return self._call(
            _get_promotions,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.PromotionDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_promotions,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
            sort=sort,
        )

    @checked
    def pause(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Pause a promotion."""
        return self._call(
            _pause_promotion,
            promotion_id=promotion_id,
        )

    @checked
    def resume(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Resume a paused promotion."""
        return self._call(
            _resume_promotion,
            promotion_id=promotion_id,
        )


class AsyncPromotionsApi(AsyncResource):
    @checked
    async def get_listing_set(
        self,
        promotion_id: StrictStr,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> ItemsPagedCollection:
        """List one page of the listings in a promotion."""
        return await self._call(
            _get_listing_set,
            promotion_id=promotion_id,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
            status=status,
        )

    @checked
    def iter_listing_set(
        self,
        promotion_id: StrictStr,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ListingDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_listing_set,
            promotion_id=promotion_id,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
            status=status,
        )

    @checked
    async def list(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PromotionsPagedCollection:
        """List one page of the seller's promotions on a marketplace."""
        return await self._call(
            _get_promotions,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        marketplace_id: StrictStr,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        promotion_status: Optional[StrictStr] = None,
        promotion_type: Optional[StrictStr] = None,
        q: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PromotionDetail]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_promotions,
            limit=limit,
            marketplace_id=marketplace_id,
            offset=offset,
            promotion_status=promotion_status,
            promotion_type=promotion_type,
            q=q,
            sort=sort,
        )

    @checked
    async def pause(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Pause a promotion."""
        return await self._call(
            _pause_promotion,
            promotion_id=promotion_id,
        )

    @checked
    async def resume(
        self,
        promotion_id: StrictStr,
    ) -> None:
        """Resume a paused promotion."""
        return await self._call(
            _resume_promotion,
            promotion_id=promotion_id,
        )
