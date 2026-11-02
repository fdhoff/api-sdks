# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

from pydantic import StrictInt
from backmarket_seller.models.task import Task
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource

_get_ws_task: Operation[Task] = Operation(
    id="get-ws-task",
    method="GET",
    path="/ws/tasks/{taskId}",
    resource="tasks",
    name="get",
    params=(Param("taskId", "task_id", "path"),),
    response=Task,
)

OPERATIONS = (_get_ws_task,)


class TasksApi(Resource):
    def get(
        self,
        task_id: StrictInt,
    ) -> Task:
        """Get the state of a background task."""
        return self._call(
            _get_ws_task,
            task_id=task_id,
        )


class AsyncTasksApi(AsyncResource):
    async def get(
        self,
        task_id: StrictInt,
    ) -> Task:
        """Get the state of a background task."""
        return await self._call(
            _get_ws_task,
            task_id=task_id,
        )
