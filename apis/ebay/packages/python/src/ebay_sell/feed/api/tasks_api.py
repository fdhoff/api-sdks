# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, FileInput, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.feed import models as _models
from ebay_sell.feed.models.create_task_request import CreateTaskRequest
from ebay_sell.feed.models.task import Task
from ebay_sell.feed.models.task_collection import TaskCollection

_create_task: Operation[None] = Operation(
    id="createTask",
    method="POST",
    path="/sell/feed/v1/task",
    resource="tasks",
    name="create",
    params=(Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_task: Operation[Task] = Operation(
    id="getTask",
    method="GET",
    path="/sell/feed/v1/task/{task_id}",
    resource="tasks",
    name="get",
    params=(Param("task_id", "task_id", "path"),),
    response=Task,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_tasks: Operation[TaskCollection] = Operation(
    id="getTasks",
    method="GET",
    path="/sell/feed/v1/task",
    resource="tasks",
    name="list",
    params=(
        Param("date_range", "date_range", "query"),
        Param("feed_type", "feed_type", "query"),
        Param("limit", "limit", "query"),
        Param("look_back_days", "look_back_days", "query"),
        Param("offset", "offset", "query"),
        Param("schedule_id", "schedule_id", "query"),
    ),
    response=TaskCollection,
    returns_json=True,
    iterator="iter",
    item=_models.Task,
    paging=NextLink(
        items="tasks",
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
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_upload_file: Operation[object] = Operation(
    id="uploadFile",
    method="POST",
    path="/sell/feed/v1/task/{task_id}/upload_file",
    resource="tasks",
    name="upload_file",
    params=(
        Param("task_id", "task_id", "path"),
        Param("file", "file", "form"),
        Param("fileName", "file_name", "form"),
        Param("name", "name", "form"),
        Param("type", "type", "form"),
    ),
    response=object,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _create_task,
    _get_task,
    _get_tasks,
    _upload_file,
)


class TasksApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateTaskRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create a feed task to upload a file to."""
        return self._call(
            _create_task,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        task_id: StrictStr,
    ) -> Task:
        """Get one feed task."""
        return self._call(
            _get_task,
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
    ) -> TaskCollection:
        """List one page of feed tasks."""
        return self._call(
            _get_tasks,
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
    ) -> Iterator[_models.Task]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
        )

    @checked
    def upload_file(
        self,
        task_id: StrictStr,
        *,
        file: FileInput,
        file_name: Optional[StrictStr] = None,
        name: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
    ) -> object:
        """Upload the input file of a feed task."""
        return self._call(
            _upload_file,
            task_id=task_id,
            file=file,
            file_name=file_name,
            name=name,
            type=type,
        )


class AsyncTasksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateTaskRequest, Mapping[str, Any]],
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> None:
        """Create a feed task to upload a file to."""
        return await self._call(
            _create_task,
            _body=body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        task_id: StrictStr,
    ) -> Task:
        """Get one feed task."""
        return await self._call(
            _get_task,
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
    ) -> TaskCollection:
        """List one page of feed tasks."""
        return await self._call(
            _get_tasks,
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
    ) -> AsyncIterator[_models.Task]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_tasks,
            date_range=date_range,
            feed_type=feed_type,
            limit=limit,
            look_back_days=look_back_days,
            offset=offset,
            schedule_id=schedule_id,
        )

    @checked
    async def upload_file(
        self,
        task_id: StrictStr,
        *,
        file: FileInput,
        file_name: Optional[StrictStr] = None,
        name: Optional[StrictStr] = None,
        type: Optional[StrictStr] = None,
    ) -> object:
        """Upload the input file of a feed task."""
        return await self._call(
            _upload_file,
            task_id=task_id,
            file=file,
            file_name=file_name,
            name=name,
            type=type,
        )
