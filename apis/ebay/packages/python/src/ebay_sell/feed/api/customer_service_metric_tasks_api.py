# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.feed import models as _models
from ebay_sell.feed.models.create_service_metrics_task_request import CreateServiceMetricsTaskRequest
from ebay_sell.feed.models.customer_service_metric_task_collection import CustomerServiceMetricTaskCollection
from ebay_sell.feed.models.service_metrics_task import ServiceMetricsTask

_create_customer_service_metric_task: Operation[None] = Operation(
    id="createCustomerServiceMetricTask",
    method="POST",
    path="/sell/feed/v1/customer_service_metric_task",
    resource="customer_service_metric_tasks",
    name="create",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)
_get_customer_service_metric_task: Operation[ServiceMetricsTask] = Operation(
    id="getCustomerServiceMetricTask",
    method="GET",
    path="/sell/feed/v1/customer_service_metric_task/{task_id}",
    resource="customer_service_metric_tasks",
    name="get",
    params=(Param("task_id", "task_id", "path"),),
    response=ServiceMetricsTask,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)
_get_customer_service_metric_tasks: Operation[CustomerServiceMetricTaskCollection] = Operation(
    id="getCustomerServiceMetricTasks",
    method="GET",
    path="/sell/feed/v1/customer_service_metric_task",
    resource="customer_service_metric_tasks",
    name="list",
    params=(
        Param("date_range", "date_range", "query"),
        Param("feed_type", "feed_type", "query"),
        Param("limit", "limit", "query"),
        Param("look_back_days", "look_back_days", "query"),
        Param("offset", "offset", "query"),
    ),
    response=CustomerServiceMetricTaskCollection,
    returns_json=True,
    iterator="iter",
    item=_models.ServiceMetricsTask,
    paging=NextLink(
        items="tasks",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",)),),),
    host="api",
)

OPERATIONS = (
    _create_customer_service_metric_task,
    _get_customer_service_metric_task,
    _get_customer_service_metric_tasks,
)


class CustomerServiceMetricTasksApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateServiceMetricsTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds a customer service metric report."""
        return self._call(
            _create_customer_service_metric_task,
            _body=body,
        )

    @checked
    def get(
        self,
        task_id: StrictStr,
    ) -> ServiceMetricsTask:
        """Get one customer service metric task."""
        return self._call(
            _get_customer_service_metric_task,
            task_id=task_id,
        )

    @checked
    def list(
        self,
        *,
        date_range: Optional[StrictStr] = None,
        feed_type: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> CustomerServiceMetricTaskCollection:
        """List one page of customer service metric tasks."""
        return self._call(
            _get_customer_service_metric_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        date_range: Optional[StrictStr] = None,
        feed_type: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.ServiceMetricsTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_customer_service_metric_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
        )


class AsyncCustomerServiceMetricTasksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateServiceMetricsTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds a customer service metric report."""
        return await self._call(
            _create_customer_service_metric_task,
            _body=body,
        )

    @checked
    async def get(
        self,
        task_id: StrictStr,
    ) -> ServiceMetricsTask:
        """Get one customer service metric task."""
        return await self._call(
            _get_customer_service_metric_task,
            task_id=task_id,
        )

    @checked
    async def list(
        self,
        *,
        date_range: Optional[StrictStr] = None,
        feed_type: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> CustomerServiceMetricTaskCollection:
        """List one page of customer service metric tasks."""
        return await self._call(
            _get_customer_service_metric_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        date_range: Optional[StrictStr] = None,
        feed_type: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ServiceMetricsTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_customer_service_metric_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
        )
