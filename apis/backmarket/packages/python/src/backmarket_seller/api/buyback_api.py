# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, checked
from backmarket_seller.models.buyback_competitor import BuybackCompetitor
from backmarket_seller.models.buyback_counter_offer_reasons_inner import BuybackCounterOfferReasonsInner
from backmarket_seller.models.buyback_listing import BuybackListing
from backmarket_seller.models.buyback_listing_update import BuybackListingUpdate
from backmarket_seller.models.buyback_message import BuybackMessage
from backmarket_seller.models.buyback_message_page import BuybackMessagePage
from backmarket_seller.models.buyback_message_payload import BuybackMessagePayload
from backmarket_seller.models.buyback_order import BuybackOrder
from backmarket_seller.models.buyback_order_page import BuybackOrderPage
from backmarket_seller.models.buyback_order_state import BuybackOrderState
from backmarket_seller.models.buyback_order_suspension_payload import BuybackOrderSuspensionPayload
from backmarket_seller.models.buyback_paginated_listing_response import BuybackPaginatedListingResponse
from backmarket_seller.models.buyback_reason import BuybackReason

_get_ws_buyback_v1_competitors: Operation[List[BuybackCompetitor]] = Operation(
    id="get-ws-buyback-v1-competitors",
    method="GET",
    path="/ws/buyback/v1/competitors/{listingId}",
    resource="buyback",
    name="list_competitors",
    params=(Param("listingId", "listing_id", "path"),),
    response=List[BuybackCompetitor],
    returns_json=True,
)
_get_ws_buyback_v1_listing: Operation[BuybackListing] = Operation(
    id="get-ws-buyback-v1-listing",
    method="GET",
    path="/ws/buyback/v1/listings/{buybackListingId}",
    resource="buyback",
    name="get_listing",
    params=(Param("buybackListingId", "buyback_listing_id", "path"),),
    response=BuybackListing,
    returns_json=True,
)
_get_ws_buyback_v1_listings: Operation[BuybackPaginatedListingResponse] = Operation(
    id="get-ws-buyback-v1-listings",
    method="GET",
    path="/ws/buyback/v1/listings",
    resource="buyback",
    name="list_listings",
    params=(
        Param("productId", "product_id", "query"),
        Param("cursor", "cursor", "query"),
        Param("pageSize", "page_size", "query"),
    ),
    response=BuybackPaginatedListingResponse,
    returns_json=True,
    iterator="iter_listings",
    item=_models.BuybackListing,
)
_get_ws_buyback_v1_order: Operation[BuybackOrder] = Operation(
    id="get-ws-buyback-v1-order",
    method="GET",
    path="/ws/buyback/v1/orders/{buybackOrderId}",
    resource="buyback",
    name="get_order",
    params=(Param("buybackOrderId", "buyback_order_id", "path"),),
    response=BuybackOrder,
    returns_json=True,
)
_get_ws_buyback_v1_orders: Operation[BuybackOrderPage] = Operation(
    id="get-ws-buyback-v1-orders",
    method="GET",
    path="/ws/buyback/v1/orders",
    resource="buyback",
    name="list_orders",
    params=(
        Param("status", "status", "query"),
        Param("productId", "product_id", "query"),
        Param("creationDate", "creation_date", "query"),
        Param("modificationDate", "modification_date", "query"),
        Param("shippingDate", "shipping_date", "query"),
        Param("receivedDate", "received_date", "query"),
        Param("suspendedDate", "suspended_date", "query"),
        Param("paymentDate", "payment_date", "query"),
        Param("page", "page", "query"),
    ),
    response=BuybackOrderPage,
    returns_json=True,
    iterator="iter_orders",
    item=_models.BuybackOrder,
)
_get_ws_buyback_v1_orders_messages: Operation[BuybackMessagePage] = Operation(
    id="get-ws-buyback-v1-orders-messages",
    method="GET",
    path="/ws/buyback/v1/orders/{buybackOrderId}/messages",
    resource="buyback",
    name="list_messages",
    params=(
        Param("buybackOrderId", "buyback_order_id", "path"),
        Param("page", "page", "query"),
    ),
    response=BuybackMessagePage,
    returns_json=True,
    iterator="iter_messages",
    item=_models.BuybackMessage,
)
_get_ws_buyback_v1_orders_pending_reply: Operation[BuybackOrderPage] = Operation(
    id="get-ws-buyback-v1-orders-pending-reply",
    method="GET",
    path="/ws/buyback/v1/orders/pending-reply",
    resource="buyback",
    name="list_pending_orders",
    params=(Param("page", "page", "query"),),
    response=BuybackOrderPage,
    returns_json=True,
    iterator="iter_pending_orders",
    item=_models.BuybackOrder,
)
_get_ws_buyback_v1_orders_suspend_reasons: Operation[List[BuybackReason]] = Operation(
    id="get-ws-buyback-v1-orders-suspend-reasons",
    method="GET",
    path="/ws/buyback/v1/orders/suspend-reasons",
    resource="buyback",
    name="list_suspend_reasons",
    params=(),
    response=List[BuybackReason],
    returns_json=True,
)
_get_ws_counter_offer_reason: Operation[List[BuybackCounterOfferReasonsInner]] = Operation(
    id="get-ws-counter-offer-reason",
    method="GET",
    path="/ws/buyback/v1/orders/{buybackOrderId}/counter-offers/reasons",
    resource="buyback",
    name="list_counter_offer_reasons",
    params=(Param("buybackOrderId", "buyback_order_id", "path"),),
    response=List[BuybackCounterOfferReasonsInner],
    returns_json=True,
)
_post_ws_buyback_v1_orders_messages: Operation[BuybackMessage] = Operation(
    id="post-ws-buyback-v1-orders-messages",
    method="POST",
    path="/ws/buyback/v1/orders/{buybackOrderId}/messages",
    resource="buyback",
    name="send_message",
    params=(Param("buybackOrderId", "buyback_order_id", "path"),),
    response=BuybackMessage,
    returns_json=True,
)
_put_ws_buyback_v1_listing: Operation[object] = Operation(
    id="put-ws-buyback-v1-listing",
    method="PUT",
    path="/ws/buyback/v1/listings/{buybackListingId}",
    resource="buyback",
    name="update_listing",
    params=(Param("buybackListingId", "buyback_listing_id", "path"),),
    response=object,
    returns_json=True,
)
_put_ws_buyback_v1_orders_suspend: Operation[BuybackOrder] = Operation(
    id="put-ws-buyback-v1-orders-suspend",
    method="PUT",
    path="/ws/buyback/v1/orders/{buybackOrderId}/suspend",
    resource="buyback",
    name="suspend_order",
    params=(Param("buybackOrderId", "buyback_order_id", "path"),),
    response=BuybackOrder,
    returns_json=True,
)
_put_ws_buyback_v1_orders_validate: Operation[BuybackOrder] = Operation(
    id="put-ws-buyback-v1-orders-validate",
    method="PUT",
    path="/ws/buyback/v1/orders/{buybackOrderId}/validate",
    resource="buyback",
    name="validate_order",
    params=(Param("buybackOrderId", "buyback_order_id", "path"),),
    response=BuybackOrder,
    returns_json=True,
)
_put_ws_refurbisher_counter_offer: Operation[None] = Operation(
    id="put-ws-refurbisher-counter-offer",
    method="PUT",
    path="/ws/buyback/v2/orders/{buybackOrderId}/counter-offers",
    resource="buyback",
    name="counter_offer",
    params=(
        Param("buybackOrderId", "buyback_order_id", "path"),
        Param("price", "price", "form"),
        Param("comment", "comment", "form"),
        Param("reasons", "reasons", "form"),
        Param("files", "files", "form"),
    ),
    response=None,
)

OPERATIONS = (
    _get_ws_buyback_v1_competitors,
    _get_ws_buyback_v1_listing,
    _get_ws_buyback_v1_listings,
    _get_ws_buyback_v1_order,
    _get_ws_buyback_v1_orders,
    _get_ws_buyback_v1_orders_messages,
    _get_ws_buyback_v1_orders_pending_reply,
    _get_ws_buyback_v1_orders_suspend_reasons,
    _get_ws_counter_offer_reason,
    _post_ws_buyback_v1_orders_messages,
    _put_ws_buyback_v1_listing,
    _put_ws_buyback_v1_orders_suspend,
    _put_ws_buyback_v1_orders_validate,
    _put_ws_refurbisher_counter_offer,
)


class BuybackApi(Resource):
    @checked
    def list_competitors(
        self,
        listing_id: UUID,
    ) -> List[BuybackCompetitor]:
        """List competitors for a buyback listing."""
        return self._call(
            _get_ws_buyback_v1_competitors,
            listing_id=listing_id,
        )

    @checked
    def get_listing(
        self,
        buyback_listing_id: UUID,
    ) -> BuybackListing:
        """Get one buyback listing."""
        return self._call(
            _get_ws_buyback_v1_listing,
            buyback_listing_id=buyback_listing_id,
        )

    @checked
    def list_listings(
        self,
        *,
        product_id: Optional[UUID] = None,
        cursor: Optional[UUID] = None,
        page_size: Optional[Annotated[int, Field(le=100, strict=True, gt=0)]] = None,
    ) -> BuybackPaginatedListingResponse:
        """List one page of buyback listings."""
        return self._call(
            _get_ws_buyback_v1_listings,
            product_id=product_id,
            cursor=cursor,
            page_size=page_size,
        )

    @checked
    def iter_listings(
        self,
        *,
        product_id: Optional[UUID] = None,
        cursor: Optional[UUID] = None,
        page_size: Optional[Annotated[int, Field(le=100, strict=True, gt=0)]] = None,
    ) -> Iterator[_models.BuybackListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_listings,
            product_id=product_id,
            cursor=cursor,
            page_size=page_size,
        )

    @checked
    def get_order(
        self,
        buyback_order_id: StrictStr,
    ) -> BuybackOrder:
        """Get one buyback order."""
        return self._call(
            _get_ws_buyback_v1_order,
            buyback_order_id=buyback_order_id,
        )

    @checked
    def list_orders(
        self,
        *,
        status: Optional[BuybackOrderState] = None,
        product_id: Optional[StrictInt] = None,
        creation_date: Optional[StrictStr] = None,
        modification_date: Optional[StrictStr] = None,
        shipping_date: Optional[StrictStr] = None,
        received_date: Optional[StrictStr] = None,
        suspended_date: Optional[StrictStr] = None,
        payment_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> BuybackOrderPage:
        """List one page of buyback orders."""
        return self._call(
            _get_ws_buyback_v1_orders,
            status=status,
            product_id=product_id,
            creation_date=creation_date,
            modification_date=modification_date,
            shipping_date=shipping_date,
            received_date=received_date,
            suspended_date=suspended_date,
            payment_date=payment_date,
            page=page,
        )

    @checked
    def iter_orders(
        self,
        *,
        status: Optional[BuybackOrderState] = None,
        product_id: Optional[StrictInt] = None,
        creation_date: Optional[StrictStr] = None,
        modification_date: Optional[StrictStr] = None,
        shipping_date: Optional[StrictStr] = None,
        received_date: Optional[StrictStr] = None,
        suspended_date: Optional[StrictStr] = None,
        payment_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> Iterator[_models.BuybackOrder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders,
            status=status,
            product_id=product_id,
            creation_date=creation_date,
            modification_date=modification_date,
            shipping_date=shipping_date,
            received_date=received_date,
            suspended_date=suspended_date,
            payment_date=payment_date,
            page=page,
        )

    @checked
    def list_messages(
        self,
        buyback_order_id: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> BuybackMessagePage:
        """List one page of a buyback order&#39;s messages."""
        return self._call(
            _get_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            page=page,
        )

    @checked
    def iter_messages(
        self,
        buyback_order_id: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> Iterator[_models.BuybackMessage]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            page=page,
        )

    @checked
    def list_pending_orders(
        self,
        *,
        page: Optional[StrictInt] = None,
    ) -> BuybackOrderPage:
        """List one page of buyback orders awaiting a reply."""
        return self._call(
            _get_ws_buyback_v1_orders_pending_reply,
            page=page,
        )

    @checked
    def iter_pending_orders(
        self,
        *,
        page: Optional[StrictInt] = None,
    ) -> Iterator[_models.BuybackOrder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders_pending_reply,
            page=page,
        )

    @checked
    def list_suspend_reasons(
        self,
    ) -> List[BuybackReason]:
        """List the reasons a buyback order can be suspended."""
        return self._call(
            _get_ws_buyback_v1_orders_suspend_reasons,
        )

    @checked
    def list_counter_offer_reasons(
        self,
        buyback_order_id: StrictStr,
    ) -> List[BuybackCounterOfferReasonsInner]:
        """List the counter-offer reasons for a buyback order."""
        return self._call(
            _get_ws_counter_offer_reason,
            buyback_order_id=buyback_order_id,
        )

    @checked
    def send_message(
        self,
        buyback_order_id: StrictStr,
        body: Union[BuybackMessagePayload, Mapping[str, Any]],
    ) -> BuybackMessage:
        """Send a message on a buyback order."""
        return self._call(
            _post_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            _body=body,
        )

    @checked
    def update_listing(
        self,
        buyback_listing_id: UUID,
        body: Union[BuybackListingUpdate, Mapping[str, Any]],
    ) -> object:
        """Update one buyback listing."""
        return self._call(
            _put_ws_buyback_v1_listing,
            buyback_listing_id=buyback_listing_id,
            _body=body,
        )

    @checked
    def suspend_order(
        self,
        buyback_order_id: StrictStr,
        body: Union[BuybackOrderSuspensionPayload, Mapping[str, Any]],
    ) -> BuybackOrder:
        """Suspend a buyback order."""
        return self._call(
            _put_ws_buyback_v1_orders_suspend,
            buyback_order_id=buyback_order_id,
            _body=body,
        )

    @checked
    def validate_order(
        self,
        buyback_order_id: StrictStr,
    ) -> BuybackOrder:
        """Validate a buyback order."""
        return self._call(
            _put_ws_buyback_v1_orders_validate,
            buyback_order_id=buyback_order_id,
        )

    @checked
    def counter_offer(
        self,
        buyback_order_id: StrictStr,
        *,
        price: float,
        reasons: List[StrictStr],
        files: List[FileInput],
        comment: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None,
    ) -> None:
        """Make a counter-offer on a buyback order."""
        return self._call(
            _put_ws_refurbisher_counter_offer,
            buyback_order_id=buyback_order_id,
            price=price,
            comment=comment,
            reasons=reasons,
            files=files,
        )


class AsyncBuybackApi(AsyncResource):
    @checked
    async def list_competitors(
        self,
        listing_id: UUID,
    ) -> List[BuybackCompetitor]:
        """List competitors for a buyback listing."""
        return await self._call(
            _get_ws_buyback_v1_competitors,
            listing_id=listing_id,
        )

    @checked
    async def get_listing(
        self,
        buyback_listing_id: UUID,
    ) -> BuybackListing:
        """Get one buyback listing."""
        return await self._call(
            _get_ws_buyback_v1_listing,
            buyback_listing_id=buyback_listing_id,
        )

    @checked
    async def list_listings(
        self,
        *,
        product_id: Optional[UUID] = None,
        cursor: Optional[UUID] = None,
        page_size: Optional[Annotated[int, Field(le=100, strict=True, gt=0)]] = None,
    ) -> BuybackPaginatedListingResponse:
        """List one page of buyback listings."""
        return await self._call(
            _get_ws_buyback_v1_listings,
            product_id=product_id,
            cursor=cursor,
            page_size=page_size,
        )

    @checked
    def iter_listings(
        self,
        *,
        product_id: Optional[UUID] = None,
        cursor: Optional[UUID] = None,
        page_size: Optional[Annotated[int, Field(le=100, strict=True, gt=0)]] = None,
    ) -> AsyncIterator[_models.BuybackListing]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_listings,
            product_id=product_id,
            cursor=cursor,
            page_size=page_size,
        )

    @checked
    async def get_order(
        self,
        buyback_order_id: StrictStr,
    ) -> BuybackOrder:
        """Get one buyback order."""
        return await self._call(
            _get_ws_buyback_v1_order,
            buyback_order_id=buyback_order_id,
        )

    @checked
    async def list_orders(
        self,
        *,
        status: Optional[BuybackOrderState] = None,
        product_id: Optional[StrictInt] = None,
        creation_date: Optional[StrictStr] = None,
        modification_date: Optional[StrictStr] = None,
        shipping_date: Optional[StrictStr] = None,
        received_date: Optional[StrictStr] = None,
        suspended_date: Optional[StrictStr] = None,
        payment_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> BuybackOrderPage:
        """List one page of buyback orders."""
        return await self._call(
            _get_ws_buyback_v1_orders,
            status=status,
            product_id=product_id,
            creation_date=creation_date,
            modification_date=modification_date,
            shipping_date=shipping_date,
            received_date=received_date,
            suspended_date=suspended_date,
            payment_date=payment_date,
            page=page,
        )

    @checked
    def iter_orders(
        self,
        *,
        status: Optional[BuybackOrderState] = None,
        product_id: Optional[StrictInt] = None,
        creation_date: Optional[StrictStr] = None,
        modification_date: Optional[StrictStr] = None,
        shipping_date: Optional[StrictStr] = None,
        received_date: Optional[StrictStr] = None,
        suspended_date: Optional[StrictStr] = None,
        payment_date: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.BuybackOrder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders,
            status=status,
            product_id=product_id,
            creation_date=creation_date,
            modification_date=modification_date,
            shipping_date=shipping_date,
            received_date=received_date,
            suspended_date=suspended_date,
            payment_date=payment_date,
            page=page,
        )

    @checked
    async def list_messages(
        self,
        buyback_order_id: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> BuybackMessagePage:
        """List one page of a buyback order&#39;s messages."""
        return await self._call(
            _get_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            page=page,
        )

    @checked
    def iter_messages(
        self,
        buyback_order_id: StrictStr,
        *,
        page: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.BuybackMessage]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            page=page,
        )

    @checked
    async def list_pending_orders(
        self,
        *,
        page: Optional[StrictInt] = None,
    ) -> BuybackOrderPage:
        """List one page of buyback orders awaiting a reply."""
        return await self._call(
            _get_ws_buyback_v1_orders_pending_reply,
            page=page,
        )

    @checked
    def iter_pending_orders(
        self,
        *,
        page: Optional[StrictInt] = None,
    ) -> AsyncIterator[_models.BuybackOrder]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_buyback_v1_orders_pending_reply,
            page=page,
        )

    @checked
    async def list_suspend_reasons(
        self,
    ) -> List[BuybackReason]:
        """List the reasons a buyback order can be suspended."""
        return await self._call(
            _get_ws_buyback_v1_orders_suspend_reasons,
        )

    @checked
    async def list_counter_offer_reasons(
        self,
        buyback_order_id: StrictStr,
    ) -> List[BuybackCounterOfferReasonsInner]:
        """List the counter-offer reasons for a buyback order."""
        return await self._call(
            _get_ws_counter_offer_reason,
            buyback_order_id=buyback_order_id,
        )

    @checked
    async def send_message(
        self,
        buyback_order_id: StrictStr,
        body: Union[BuybackMessagePayload, Mapping[str, Any]],
    ) -> BuybackMessage:
        """Send a message on a buyback order."""
        return await self._call(
            _post_ws_buyback_v1_orders_messages,
            buyback_order_id=buyback_order_id,
            _body=body,
        )

    @checked
    async def update_listing(
        self,
        buyback_listing_id: UUID,
        body: Union[BuybackListingUpdate, Mapping[str, Any]],
    ) -> object:
        """Update one buyback listing."""
        return await self._call(
            _put_ws_buyback_v1_listing,
            buyback_listing_id=buyback_listing_id,
            _body=body,
        )

    @checked
    async def suspend_order(
        self,
        buyback_order_id: StrictStr,
        body: Union[BuybackOrderSuspensionPayload, Mapping[str, Any]],
    ) -> BuybackOrder:
        """Suspend a buyback order."""
        return await self._call(
            _put_ws_buyback_v1_orders_suspend,
            buyback_order_id=buyback_order_id,
            _body=body,
        )

    @checked
    async def validate_order(
        self,
        buyback_order_id: StrictStr,
    ) -> BuybackOrder:
        """Validate a buyback order."""
        return await self._call(
            _put_ws_buyback_v1_orders_validate,
            buyback_order_id=buyback_order_id,
        )

    @checked
    async def counter_offer(
        self,
        buyback_order_id: StrictStr,
        *,
        price: float,
        reasons: List[StrictStr],
        files: List[FileInput],
        comment: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None,
    ) -> None:
        """Make a counter-offer on a buyback order."""
        return await self._call(
            _put_ws_refurbisher_counter_offer,
            buyback_order_id=buyback_order_id,
            price=price,
            comment=comment,
            reasons=reasons,
            files=files,
        )
