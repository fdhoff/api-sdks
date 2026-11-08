# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.developer_analytics.models.rate_limits_response import RateLimitsResponse

_get_rate_limits: Operation[RateLimitsResponse] = Operation(
    id="getRateLimits",
    method="GET",
    path="/developer/analytics/v1_beta/rate_limit/",
    resource="rate_limits",
    name="list",
    params=(
        Param("api_context", "api_context", "query"),
        Param("api_name", "api_name", "query"),
    ),
    response=RateLimitsResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_user_rate_limits: Operation[RateLimitsResponse] = Operation(
    id="getUserRateLimits",
    method="GET",
    path="/developer/analytics/v1_beta/user_rate_limit/",
    resource="rate_limits",
    name="list_for_user",
    params=(
        Param("api_context", "api_context", "query"),
        Param("api_name", "api_name", "query"),
    ),
    response=RateLimitsResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _get_rate_limits,
    _get_user_rate_limits,
)


class RateLimitsApi(Resource):
    @checked
    def list(
        self,
        *,
        api_context: Optional[StrictStr] = None,
        api_name: Optional[StrictStr] = None,
    ) -> RateLimitsResponse:
        """List the app's call limits and current usage."""
        return self._call(
            _get_rate_limits,
            api_context=api_context,
            api_name=api_name,
        )

    @checked
    def list_for_user(
        self,
        *,
        api_context: Optional[StrictStr] = None,
        api_name: Optional[StrictStr] = None,
    ) -> RateLimitsResponse:
        """List the call limits and current usage of the user the token belongs to."""
        return self._call(
            _get_user_rate_limits,
            api_context=api_context,
            api_name=api_name,
        )


class AsyncRateLimitsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        api_context: Optional[StrictStr] = None,
        api_name: Optional[StrictStr] = None,
    ) -> RateLimitsResponse:
        """List the app's call limits and current usage."""
        return await self._call(
            _get_rate_limits,
            api_context=api_context,
            api_name=api_name,
        )

    @checked
    async def list_for_user(
        self,
        *,
        api_context: Optional[StrictStr] = None,
        api_name: Optional[StrictStr] = None,
    ) -> RateLimitsResponse:
        """List the call limits and current usage of the user the token belongs to."""
        return await self._call(
            _get_user_rate_limits,
            api_context=api_context,
            api_name=api_name,
        )
