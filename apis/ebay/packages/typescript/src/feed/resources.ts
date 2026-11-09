// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  CustomerServiceMetricTasksApi,
  OPERATIONS as CustomerServiceMetricTasksApiOperations,
} from './apis/CustomerServiceMetricTasksApi.js';
import { InventoryTasksApi, OPERATIONS as InventoryTasksApiOperations } from './apis/InventoryTasksApi.js';
import { OrderTasksApi, OPERATIONS as OrderTasksApiOperations } from './apis/OrderTasksApi.js';
import { SchedulesApi, OPERATIONS as SchedulesApiOperations } from './apis/SchedulesApi.js';
import { TasksApi, OPERATIONS as TasksApiOperations } from './apis/TasksApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...CustomerServiceMetricTasksApiOperations,
    ...InventoryTasksApiOperations,
    ...OrderTasksApiOperations,
    ...SchedulesApiOperations,
    ...TasksApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly customerServiceMetricTasks: CustomerServiceMetricTasksApi;
  readonly inventoryTasks: InventoryTasksApi;
  readonly orderTasks: OrderTasksApi;
  readonly schedules: SchedulesApi;
  readonly tasks: TasksApi;

  constructor(transport: Transport) {
    this.customerServiceMetricTasks = new CustomerServiceMetricTasksApi(transport);
    this.inventoryTasks = new InventoryTasksApi(transport);
    this.orderTasks = new OrderTasksApi(transport);
    this.schedules = new SchedulesApi(transport);
    this.tasks = new TasksApi(transport);
  }
}
