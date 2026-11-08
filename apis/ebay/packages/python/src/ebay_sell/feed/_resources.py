# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Dict

from ebay_sell._runtime import AsyncTransport, Operation, SyncTransport
from ebay_sell.feed.api import (
    customer_service_metric_tasks_api,
    inventory_tasks_api,
    order_tasks_api,
    schedules_api,
    tasks_api,
)

OPERATIONS: Dict[str, Operation[Any]] = {
    operation.id: operation
    for operations in (
        customer_service_metric_tasks_api.OPERATIONS,
        inventory_tasks_api.OPERATIONS,
        order_tasks_api.OPERATIONS,
        schedules_api.OPERATIONS,
        tasks_api.OPERATIONS,
    )
    for operation in operations
}


class Resources:
    def __init__(self, transport: SyncTransport) -> None:
        self.customer_service_metric_tasks = customer_service_metric_tasks_api.CustomerServiceMetricTasksApi(transport)
        self.inventory_tasks = inventory_tasks_api.InventoryTasksApi(transport)
        self.order_tasks = order_tasks_api.OrderTasksApi(transport)
        self.schedules = schedules_api.SchedulesApi(transport)
        self.tasks = tasks_api.TasksApi(transport)


class AsyncResources:
    def __init__(self, transport: AsyncTransport) -> None:
        self.customer_service_metric_tasks = customer_service_metric_tasks_api.AsyncCustomerServiceMetricTasksApi(
            transport
        )
        self.inventory_tasks = inventory_tasks_api.AsyncInventoryTasksApi(transport)
        self.order_tasks = order_tasks_api.AsyncOrderTasksApi(transport)
        self.schedules = schedules_api.AsyncSchedulesApi(transport)
        self.tasks = tasks_api.AsyncTasksApi(transport)
