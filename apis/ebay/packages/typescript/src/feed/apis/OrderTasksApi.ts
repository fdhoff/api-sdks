// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateOrderTaskRequest,
  GetOrderTasks429Response,
  OrderTask,
  OrderTaskCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createOrderTask: Operation = {
  id: 'createOrderTask',
  method: 'POST',
  path: '/sell/feed/v1/order_task',
  resource: 'orderTasks',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.fulfillment'] }]],
};

const getOrderTask: Operation = {
  id: 'getOrderTask',
  method: 'GET',
  path: '/sell/feed/v1/order_task/{task_id}',
  resource: 'orderTasks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'task_id', name: 'taskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.fulfillment'] }]],
};

const getOrderTasks: Operation = {
  id: 'getOrderTasks',
  method: 'GET',
  path: '/sell/feed/v1/order_task',
  resource: 'orderTasks',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'date_range', name: 'dateRange', location: 'query' },
    { wire: 'feed_type', name: 'feedType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'look_back_days', name: 'lookBackDays', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'schedule_id', name: 'scheduleId', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'tasks', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.fulfillment'] }]],
};

export const OPERATIONS: readonly Operation[] = [createOrderTask, getOrderTask, getOrderTasks];

export class OrderTasksApi extends Resource {
  /** Start a task that builds an order report. */
  create(body: CreateOrderTaskRequest, options?: RequestOptions): Promise<void> {
    return this.call(createOrderTask, body, {}, options);
  }

  /** Get one order report task. */
  get(taskId: string, options?: RequestOptions): Promise<OrderTask> {
    return this.call(getOrderTask, undefined, { taskId }, options);
  }

  /** List one page of order report tasks. */
  list(
    params: {
      dateRange?: string;
      feedType?: string;
      limit?: string;
      lookBackDays?: string;
      offset?: string;
      scheduleId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<OrderTaskCollection> {
    return this.call(getOrderTasks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      dateRange?: string;
      feedType?: string;
      limit?: string;
      lookBackDays?: string;
      offset?: string;
      scheduleId?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OrderTask, void, undefined> {
    return this.paginate(getOrderTasks, undefined, { ...params }, options);
  }
}
