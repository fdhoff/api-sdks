# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictInt

from backmarket_seller._runtime import (
    AsyncResource,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from backmarket_seller.models.background_task import BackgroundTask

_get_ws_task: Operation[BackgroundTask] = Operation(
    id="get-ws-task",
    method="GET",
    path="/ws/tasks/{taskId}",
    resource="tasks",
    name="get",
    params=(Param("taskId", "task_id", "path"),),
    response=BackgroundTask,
    returns_json=True,
    security=((Scheme("ApiKeyAuth", ()),),),
)

OPERATIONS = (_get_ws_task,)


class TasksApi(Resource):
    @checked
    def get(
        self,
        task_id: StrictInt,
    ) -> BackgroundTask:
        """Get the state of a background task."""
        return self._call(
            _get_ws_task,
            task_id=task_id,
        )


class AsyncTasksApi(AsyncResource):
    @checked
    async def get(
        self,
        task_id: StrictInt,
    ) -> BackgroundTask:
        """Get the state of a background task."""
        return await self._call(
            _get_ws_task,
            task_id=task_id,
        )
