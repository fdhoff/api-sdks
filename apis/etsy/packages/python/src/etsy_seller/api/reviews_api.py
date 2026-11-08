# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller import models as _models
from etsy_seller._runtime import AsyncResource, Offset, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_reviews import ListingReviews
from etsy_seller.models.transaction_reviews import TransactionReviews

_get_reviews_by_listing: Operation[ListingReviews] = Operation(
    id="getReviewsByListing",
    method="GET",
    path="/v3/application/listings/{listing_id}/reviews",
    resource="reviews",
    name="list_by_listing",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("min_created", "min_created", "query"),
        Param("max_created", "max_created", "query"),
    ),
    response=ListingReviews,
    returns_json=True,
    iterator="iter_by_listing",
    item=_models.ListingReview,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)
_get_reviews_by_shop: Operation[TransactionReviews] = Operation(
    id="getReviewsByShop",
    method="GET",
    path="/v3/application/shops/{shop_id}/reviews",
    resource="reviews",
    name="list_by_shop",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("min_created", "min_created", "query"),
        Param("max_created", "max_created", "query"),
    ),
    response=TransactionReviews,
    returns_json=True,
    iterator="iter_by_shop",
    item=_models.TransactionReview,
    paging=Offset(items="results", total="count", offset="offset"),
    security=((Scheme("api_key", ()),),),
)

OPERATIONS = (
    _get_reviews_by_listing,
    _get_reviews_by_shop,
)


class ReviewsApi(Resource):
    @checked
    def list_by_listing(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> ListingReviews:
        """List one page of a listing's reviews."""
        return self._call(
            _get_reviews_by_listing,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    def iter_by_listing(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> Iterator[_models.ListingReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_reviews_by_listing,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    def list_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> TransactionReviews:
        """List one page of a shop's reviews."""
        return self._call(
            _get_reviews_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    def iter_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> Iterator[_models.TransactionReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_reviews_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )


class AsyncReviewsApi(AsyncResource):
    @checked
    async def list_by_listing(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> ListingReviews:
        """List one page of a listing's reviews."""
        return await self._call(
            _get_reviews_by_listing,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    def iter_by_listing(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> AsyncIterator[_models.ListingReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_reviews_by_listing,
            listing_id=listing_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    async def list_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> TransactionReviews:
        """List one page of a shop's reviews."""
        return await self._call(
            _get_reviews_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )

    @checked
    def iter_by_shop(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        min_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
        max_created: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None,
    ) -> AsyncIterator[_models.TransactionReview]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_reviews_by_shop,
            shop_id=shop_id,
            limit=limit,
            offset=offset,
            min_created=min_created,
            max_created=max_created,
        )
