# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.feedback.models.awaiting_feedback_response import AwaitingFeedbackResponse
from ebay_sell.feedback.models.get_feedback_rating_summary_response import GetFeedbackRatingSummaryResponse
from ebay_sell.feedback.models.get_feedback_response import GetFeedbackResponse
from ebay_sell.feedback.models.leave_feedback_request import LeaveFeedbackRequest
from ebay_sell.feedback.models.leave_feedback_response import LeaveFeedbackResponse
from ebay_sell.feedback.models.respond_to_feedback_request import RespondToFeedbackRequest

_get_feedback: Operation[GetFeedbackResponse] = Operation(
    id="getFeedback",
    method="GET",
    path="/commerce/feedback/v1/feedback",
    resource="feedback",
    name="list",
    params=(
        Param("feedback_id", "feedback_id", "query"),
        Param("feedback_type", "feedback_type", "query"),
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("listing_id", "listing_id", "query"),
        Param("offset", "offset", "query"),
        Param("order_line_item_id", "order_line_item_id", "query"),
        Param("sort", "sort", "query"),
        Param("transaction_id", "transaction_id", "query"),
        Param("user_id", "user_id", "query"),
    ),
    response=GetFeedbackResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/commerce.feedback",
                    "https://api.ebay.com/oauth/api_scope/commerce.feedback.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_feedback_rating_summary: Operation[GetFeedbackRatingSummaryResponse] = Operation(
    id="getFeedbackRatingSummary",
    method="GET",
    path="/commerce/feedback/v1/feedback_rating_summary",
    resource="feedback",
    name="get_rating_summary",
    params=(
        Param("filter", "filter", "query"),
        Param("user_id", "user_id", "query"),
    ),
    response=GetFeedbackRatingSummaryResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/commerce.feedback",
                    "https://api.ebay.com/oauth/api_scope/commerce.feedback.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_items_awaiting_feedback: Operation[AwaitingFeedbackResponse] = Operation(
    id="getItemsAwaitingFeedback",
    method="GET",
    path="/commerce/feedback/v1/awaiting_feedback",
    resource="feedback",
    name="list_awaiting",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
    ),
    response=AwaitingFeedbackResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.feedback",)),),),
    host="api",
)
_leave_feedback: Operation[LeaveFeedbackResponse] = Operation(
    id="leaveFeedback",
    method="POST",
    path="/commerce/feedback/v1/feedback",
    resource="feedback",
    name="leave",
    params=(),
    response=LeaveFeedbackResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.feedback",)),),),
    host="api",
)
_respond_to_feedback: Operation[object] = Operation(
    id="respondToFeedback",
    method="POST",
    path="/commerce/feedback/v1/respond_to_feedback",
    resource="feedback",
    name="respond",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/commerce.feedback",)),),),
    host="api",
)

OPERATIONS = (
    _get_feedback,
    _get_feedback_rating_summary,
    _get_items_awaiting_feedback,
    _leave_feedback,
    _respond_to_feedback,
)


class FeedbackApi(Resource):
    @checked
    def list(
        self,
        *,
        feedback_type: StrictStr,
        user_id: StrictStr,
        feedback_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_line_item_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> GetFeedbackResponse:
        """List one page of feedback a user left or received."""
        return self._call(
            _get_feedback,
            feedback_id=feedback_id,
            feedback_type=feedback_type,
            filter=filter,
            limit=limit,
            listing_id=listing_id,
            offset=offset,
            order_line_item_id=order_line_item_id,
            sort=sort,
            transaction_id=transaction_id,
            user_id=user_id,
        )

    @checked
    def get_rating_summary(
        self,
        *,
        filter: StrictStr,
        user_id: StrictStr,
    ) -> GetFeedbackRatingSummaryResponse:
        """Get a user's feedback rating summary."""
        return self._call(
            _get_feedback_rating_summary,
            filter=filter,
            user_id=user_id,
        )

    @checked
    def list_awaiting(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AwaitingFeedbackResponse:
        """List one page of the order line items still waiting for feedback."""
        return self._call(
            _get_items_awaiting_feedback,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )

    @checked
    def leave(
        self,
        body: Optional[Union[LeaveFeedbackRequest, Mapping[str, Any]]] = None,
    ) -> LeaveFeedbackResponse:
        """Leave feedback for the other party of an order line item."""
        return self._call(
            _leave_feedback,
            _body=body,
        )

    @checked
    def respond(
        self,
        body: Optional[Union[RespondToFeedbackRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Reply to feedback"""
        return self._call(
            _respond_to_feedback,
            _body=body,
        )


class AsyncFeedbackApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        feedback_type: StrictStr,
        user_id: StrictStr,
        feedback_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        listing_id: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_line_item_id: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
        transaction_id: Optional[StrictStr] = None,
    ) -> GetFeedbackResponse:
        """List one page of feedback a user left or received."""
        return await self._call(
            _get_feedback,
            feedback_id=feedback_id,
            feedback_type=feedback_type,
            filter=filter,
            limit=limit,
            listing_id=listing_id,
            offset=offset,
            order_line_item_id=order_line_item_id,
            sort=sort,
            transaction_id=transaction_id,
            user_id=user_id,
        )

    @checked
    async def get_rating_summary(
        self,
        *,
        filter: StrictStr,
        user_id: StrictStr,
    ) -> GetFeedbackRatingSummaryResponse:
        """Get a user's feedback rating summary."""
        return await self._call(
            _get_feedback_rating_summary,
            filter=filter,
            user_id=user_id,
        )

    @checked
    async def list_awaiting(
        self,
        *,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AwaitingFeedbackResponse:
        """List one page of the order line items still waiting for feedback."""
        return await self._call(
            _get_items_awaiting_feedback,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
        )

    @checked
    async def leave(
        self,
        body: Optional[Union[LeaveFeedbackRequest, Mapping[str, Any]]] = None,
    ) -> LeaveFeedbackResponse:
        """Leave feedback for the other party of an order line item."""
        return await self._call(
            _leave_feedback,
            _body=body,
        )

    @checked
    async def respond(
        self,
        body: Optional[Union[RespondToFeedbackRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Reply to feedback"""
        return await self._call(
            _respond_to_feedback,
            _body=body,
        )
