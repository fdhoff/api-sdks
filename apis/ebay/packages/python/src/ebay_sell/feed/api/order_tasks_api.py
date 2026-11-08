# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.feed import models as _models
from ebay_sell.feed.models.create_order_task_request import CreateOrderTaskRequest
from ebay_sell.feed.models.order_task import OrderTask
from ebay_sell.feed.models.order_task_collection import OrderTaskCollection

_create_order_task: Operation[None] = Operation(
    id="createOrderTask",
    method="POST",
    path="/sell/feed/v1/order_task",
    resource="order_tasks",
    name="create",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.fulfillment",)),),),
    host="api",
)
_get_order_task: Operation[OrderTask] = Operation(
    id="getOrderTask",
    method="GET",
    path="/sell/feed/v1/order_task/{task_id}",
    resource="order_tasks",
    name="get",
    params=(Param("task_id", "task_id", "path"),),
    response=OrderTask,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.fulfillment",)),),),
    host="api",
)
_get_order_tasks: Operation[OrderTaskCollection] = Operation(
    id="getOrderTasks",
    method="GET",
    path="/sell/feed/v1/order_task",
    resource="order_tasks",
    name="list",
    params=(
        Param("date_range", "date_range", "query"),
        Param("feed_type", "feed_type", "query"),
        Param("limit", "limit", "query"),
        Param("look_back_days", "look_back_days", "query"),
        Param("offset", "offset", "query"),
        Param("schedule_id", "schedule_id", "query"),
    ),
    response=OrderTaskCollection,
    returns_json=True,
    iterator="iter",
    item=_models.OrderTask,
    paging=NextLink(
        items="tasks",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.fulfillment",)),),),
    host="api",
)

OPERATIONS = (
    _create_order_task,
    _get_order_task,
    _get_order_tasks,
)


class OrderTasksApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateOrderTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds an order report."""
        return self._call(
            _create_order_task,
            _body=body,
        )

    @checked
    def get(
        self,
        task_id: StrictStr,
    ) -> OrderTask:
        """Get one order report task."""
        return self._call(
            _get_order_task,
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
        schedule_id: Optional[StrictStr] = None,
    ) -> OrderTaskCollection:
        """List one page of order report tasks."""
        return self._call(
            _get_order_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
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
        schedule_id: Optional[StrictStr] = None,
    ) -> Iterator[_models.OrderTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_order_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
        )


class AsyncOrderTasksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateOrderTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds an order report."""
        return await self._call(
            _create_order_task,
            _body=body,
        )

    @checked
    async def get(
        self,
        task_id: StrictStr,
    ) -> OrderTask:
        """Get one order report task."""
        return await self._call(
            _get_order_task,
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
        schedule_id: Optional[StrictStr] = None,
    ) -> OrderTaskCollection:
        """List one page of order report tasks."""
        return await self._call(
            _get_order_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
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
        schedule_id: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.OrderTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_order_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
        )
