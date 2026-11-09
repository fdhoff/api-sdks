// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateServiceMetricsTaskRequest,
  CustomerServiceMetricTaskCollection,
  GetOrderTasks429Response,
  ServiceMetricsTask,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createCustomerServiceMetricTask: Operation = {
  id: 'createCustomerServiceMetricTask',
  method: 'POST',
  path: '/sell/feed/v1/customer_service_metric_task',
  resource: 'customerServiceMetricTasks',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

const getCustomerServiceMetricTask: Operation = {
  id: 'getCustomerServiceMetricTask',
  method: 'GET',
  path: '/sell/feed/v1/customer_service_metric_task/{task_id}',
  resource: 'customerServiceMetricTasks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'task_id', name: 'taskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

const getCustomerServiceMetricTasks: Operation = {
  id: 'getCustomerServiceMetricTasks',
  method: 'GET',
  path: '/sell/feed/v1/customer_service_metric_task',
  resource: 'customerServiceMetricTasks',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'date_range', name: 'dateRange', location: 'query' },
    { wire: 'feed_type', name: 'feedType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'look_back_days', name: 'lookBackDays', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'tasks', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createCustomerServiceMetricTask,
  getCustomerServiceMetricTask,
  getCustomerServiceMetricTasks,
];

export class CustomerServiceMetricTasksApi extends Resource {
  /** Start a task that builds a customer service metric report. */
  create(body: CreateServiceMetricsTaskRequest, options?: RequestOptions): Promise<void> {
    return this.call(createCustomerServiceMetricTask, body, {}, options);
  }

  /** Get one customer service metric task. */
  get(taskId: string, options?: RequestOptions): Promise<ServiceMetricsTask> {
    return this.call(getCustomerServiceMetricTask, undefined, { taskId }, options);
  }

  /** List one page of customer service metric tasks. */
  list(
    params: { dateRange?: string; feedType?: string; limit?: string; lookBackDays?: string; offset?: string } = {},
    options?: RequestOptions,
  ): Promise<CustomerServiceMetricTaskCollection> {
    return this.call(getCustomerServiceMetricTasks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { dateRange?: string; feedType?: string; limit?: string; lookBackDays?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ServiceMetricsTask, void, undefined> {
    return this.paginate(getCustomerServiceMetricTasks, undefined, { ...params }, options);
  }
}
