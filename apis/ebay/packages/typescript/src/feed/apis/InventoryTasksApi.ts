// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateInventoryTaskRequest,
  GetOrderTasks429Response,
  InventoryTask,
  InventoryTaskCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createInventoryTask: Operation = {
  id: 'createInventoryTask',
  method: 'POST',
  path: '/sell/feed/v1/inventory_task',
  resource: 'inventoryTasks',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getInventoryTask: Operation = {
  id: 'getInventoryTask',
  method: 'GET',
  path: '/sell/feed/v1/inventory_task/{task_id}',
  resource: 'inventoryTasks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'task_id', name: 'taskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getInventoryTasks: Operation = {
  id: 'getInventoryTasks',
  method: 'GET',
  path: '/sell/feed/v1/inventory_task',
  resource: 'inventoryTasks',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'feed_type', name: 'feedType', location: 'query' },
    { wire: 'schedule_id', name: 'scheduleId', location: 'query' },
    { wire: 'look_back_days', name: 'lookBackDays', location: 'query' },
    { wire: 'date_range', name: 'dateRange', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'tasks', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [createInventoryTask, getInventoryTask, getInventoryTasks];

export class InventoryTasksApi extends Resource {
  /** Start a task that builds an inventory report. */
  create(body: CreateInventoryTaskRequest, options?: RequestOptions): Promise<void> {
    return this.call(createInventoryTask, body, {}, options);
  }

  /** Get one inventory report task. */
  get(taskId: string, options?: RequestOptions): Promise<InventoryTask> {
    return this.call(getInventoryTask, undefined, { taskId }, options);
  }

  /** List one page of inventory report tasks. */
  list(
    params: {
      feedType?: string;
      scheduleId?: string;
      lookBackDays?: string;
      dateRange?: string;
      limit?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<InventoryTaskCollection> {
    return this.call(getInventoryTasks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      feedType?: string;
      scheduleId?: string;
      lookBackDays?: string;
      dateRange?: string;
      limit?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.InventoryTask, void, undefined> {
    return this.paginate(getInventoryTasks, undefined, { ...params }, options);
  }
}
