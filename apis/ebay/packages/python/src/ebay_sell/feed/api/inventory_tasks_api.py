# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.feed import models as _models
from ebay_sell.feed.models.create_inventory_task_request import CreateInventoryTaskRequest
from ebay_sell.feed.models.inventory_task import InventoryTask
from ebay_sell.feed.models.inventory_task_collection import InventoryTaskCollection

_create_inventory_task: Operation[None] = Operation(
    id="createInventoryTask",
    method="POST",
    path="/sell/feed/v1/inventory_task",
    resource="inventory_tasks",
    name="create",
    params=(),
    response=None,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_inventory_task: Operation[InventoryTask] = Operation(
    id="getInventoryTask",
    method="GET",
    path="/sell/feed/v1/inventory_task/{task_id}",
    resource="inventory_tasks",
    name="get",
    params=(Param("task_id", "task_id", "path"),),
    response=InventoryTask,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_inventory_tasks: Operation[InventoryTaskCollection] = Operation(
    id="getInventoryTasks",
    method="GET",
    path="/sell/feed/v1/inventory_task",
    resource="inventory_tasks",
    name="list",
    params=(
        Param("feed_type", "feed_type", "query"),
        Param("schedule_id", "schedule_id", "query"),
        Param("look_back_days", "look_back_days", "query"),
        Param("date_range", "date_range", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
    ),
    response=InventoryTaskCollection,
    returns_json=True,
    iterator="iter",
    item=_models.InventoryTask,
    paging=NextLink(
        items="tasks",
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

OPERATIONS = (
    _create_inventory_task,
    _get_inventory_task,
    _get_inventory_tasks,
)


class InventoryTasksApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateInventoryTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds an inventory report."""
        return self._call(
            _create_inventory_task,
            _body=body,
        )

    @checked
    def get(
        self,
        task_id: StrictStr,
    ) -> InventoryTask:
        """Get one inventory report task."""
        return self._call(
            _get_inventory_task,
            task_id=task_id,
        )

    @checked
    def list(
        self,
        *,
        feed_type: Optional[StrictStr] = None,
        schedule_id: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        date_range: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> InventoryTaskCollection:
        """List one page of inventory report tasks."""
        return self._call(
            _get_inventory_tasks,
            feed_type=feed_type,
            schedule_id=schedule_id,
            look_back_days=look_back_days,
            date_range=date_range,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        feed_type: Optional[StrictStr] = None,
        schedule_id: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        date_range: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> Iterator[_models.InventoryTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_tasks,
            feed_type=feed_type,
            schedule_id=schedule_id,
            look_back_days=look_back_days,
            date_range=date_range,
            limit=limit,
            offset=offset,
        )


class AsyncInventoryTasksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateInventoryTaskRequest, Mapping[str, Any]],
    ) -> None:
        """Start a task that builds an inventory report."""
        return await self._call(
            _create_inventory_task,
            _body=body,
        )

    @checked
    async def get(
        self,
        task_id: StrictStr,
    ) -> InventoryTask:
        """Get one inventory report task."""
        return await self._call(
            _get_inventory_task,
            task_id=task_id,
        )

    @checked
    async def list(
        self,
        *,
        feed_type: Optional[StrictStr] = None,
        schedule_id: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        date_range: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> InventoryTaskCollection:
        """List one page of inventory report tasks."""
        return await self._call(
            _get_inventory_tasks,
            feed_type=feed_type,
            schedule_id=schedule_id,
            look_back_days=look_back_days,
            date_range=date_range,
            limit=limit,
            offset=offset,
        )

    @checked
    def iter(
        self,
        *,
        feed_type: Optional[StrictStr] = None,
        schedule_id: Optional[StrictStr] = None,
        look_back_days: Optional[StrictStr] = None,
        date_range: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.InventoryTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_inventory_tasks,
            feed_type=feed_type,
            schedule_id=schedule_id,
            look_back_days=look_back_days,
            date_range=date_range,
            limit=limit,
            offset=offset,
        )
