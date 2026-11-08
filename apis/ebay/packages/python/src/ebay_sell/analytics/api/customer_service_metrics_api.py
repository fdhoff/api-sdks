# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.analytics.models.get_customer_service_metric_response import GetCustomerServiceMetricResponse

_get_customer_service_metric: Operation[GetCustomerServiceMetricResponse] = Operation(
    id="getCustomerServiceMetric",
    method="GET",
    path="/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}",
    resource="customer_service_metrics",
    name="get",
    params=(
        Param("customer_service_metric_type", "customer_service_metric_type", "path"),
        Param("evaluation_type", "evaluation_type", "path"),
        Param("evaluation_marketplace_id", "evaluation_marketplace_id", "query"),
    ),
    response=GetCustomerServiceMetricResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)

OPERATIONS = (_get_customer_service_metric,)


class CustomerServiceMetricsApi(Resource):
    @checked
    def get(
        self,
        customer_service_metric_type: StrictStr,
        evaluation_type: StrictStr,
        *,
        evaluation_marketplace_id: StrictStr,
    ) -> GetCustomerServiceMetricResponse:
        """Get the seller's rating for one customer service metric."""
        return self._call(
            _get_customer_service_metric,
            customer_service_metric_type=customer_service_metric_type,
            evaluation_type=evaluation_type,
            evaluation_marketplace_id=evaluation_marketplace_id,
        )


class AsyncCustomerServiceMetricsApi(AsyncResource):
    @checked
    async def get(
        self,
        customer_service_metric_type: StrictStr,
        evaluation_type: StrictStr,
        *,
        evaluation_marketplace_id: StrictStr,
    ) -> GetCustomerServiceMetricResponse:
        """Get the seller's rating for one customer service metric."""
        return await self._call(
            _get_customer_service_metric,
            customer_service_metric_type=customer_service_metric_type,
            evaluation_type=evaluation_type,
            evaluation_marketplace_id=evaluation_marketplace_id,
        )
