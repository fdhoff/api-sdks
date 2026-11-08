# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.marketing import models as _models
from ebay_sell.marketing.models.create_report_task import CreateReportTask
from ebay_sell.marketing.models.error import Error
from ebay_sell.marketing.models.report_task import ReportTask
from ebay_sell.marketing.models.report_task_paged_collection import ReportTaskPagedCollection

_create_report_task: Operation[Error] = Operation(
    id="createReportTask",
    method="POST",
    path="/sell/marketing/v1/ad_report_task",
    resource="report_tasks",
    name="create",
    params=(),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_delete_report_task: Operation[Error] = Operation(
    id="deleteReportTask",
    method="DELETE",
    path="/sell/marketing/v1/ad_report_task/{report_task_id}",
    resource="report_tasks",
    name="delete",
    params=(Param("report_task_id", "report_task_id", "path"),),
    response=Error,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_report_task: Operation[ReportTask] = Operation(
    id="getReportTask",
    method="GET",
    path="/sell/marketing/v1/ad_report_task/{report_task_id}",
    resource="report_tasks",
    name="get",
    params=(Param("report_task_id", "report_task_id", "path"),),
    response=ReportTask,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.marketing",)),),),
    host="api",
)
_get_report_tasks: Operation[ReportTaskPagedCollection] = Operation(
    id="getReportTasks",
    method="GET",
    path="/sell/marketing/v1/ad_report_task",
    resource="report_tasks",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("report_task_statuses", "report_task_statuses", "query"),
    ),
    response=ReportTaskPagedCollection,
    returns_json=True,
    iterator="iter",
    item=_models.ReportTask,
    paging=NextLink(
        items="reportTasks",
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

OPERATIONS = (
    _create_report_task,
    _delete_report_task,
    _get_report_task,
    _get_report_tasks,
)


class ReportTasksApi(Resource):
    @checked
    def create(
        self,
        body: Union[CreateReportTask, Mapping[str, Any]],
    ) -> Error:
        """Start a task that builds a Promoted Listings report."""
        return self._call(
            _create_report_task,
            _body=body,
        )

    @checked
    def delete(
        self,
        report_task_id: StrictStr,
    ) -> Error:
        """Delete a report task."""
        return self._call(
            _delete_report_task,
            report_task_id=report_task_id,
        )

    @checked
    def get(
        self,
        report_task_id: StrictStr,
    ) -> ReportTask:
        """Get one report task."""
        return self._call(
            _get_report_task,
            report_task_id=report_task_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        report_task_statuses: Optional[StrictStr] = None,
    ) -> ReportTaskPagedCollection:
        """List one page of the seller's report tasks."""
        return self._call(
            _get_report_tasks,
            limit=limit,
            offset=offset,
            report_task_statuses=report_task_statuses,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        report_task_statuses: Optional[StrictStr] = None,
    ) -> Iterator[_models.ReportTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_report_tasks,
            limit=limit,
            offset=offset,
            report_task_statuses=report_task_statuses,
        )


class AsyncReportTasksApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Union[CreateReportTask, Mapping[str, Any]],
    ) -> Error:
        """Start a task that builds a Promoted Listings report."""
        return await self._call(
            _create_report_task,
            _body=body,
        )

    @checked
    async def delete(
        self,
        report_task_id: StrictStr,
    ) -> Error:
        """Delete a report task."""
        return await self._call(
            _delete_report_task,
            report_task_id=report_task_id,
        )

    @checked
    async def get(
        self,
        report_task_id: StrictStr,
    ) -> ReportTask:
        """Get one report task."""
        return await self._call(
            _get_report_task,
            report_task_id=report_task_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        report_task_statuses: Optional[StrictStr] = None,
    ) -> ReportTaskPagedCollection:
        """List one page of the seller's report tasks."""
        return await self._call(
            _get_report_tasks,
            limit=limit,
            offset=offset,
            report_task_statuses=report_task_statuses,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        report_task_statuses: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ReportTask]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_report_tasks,
            limit=limit,
            offset=offset,
            report_task_statuses=report_task_statuses,
        )
