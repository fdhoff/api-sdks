// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreateTaskRequest, GetOrderTasks429Response, Task, TaskCollection } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createTask: Operation = {
  id: 'createTask',
  method: 'POST',
  path: '/sell/feed/v1/task',
  resource: 'tasks',
  name: 'create',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
          'https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.analytics.readonly',
        ],
      },
    ],
  ],
};

const getTask: Operation = {
  id: 'getTask',
  method: 'GET',
  path: '/sell/feed/v1/task/{task_id}',
  resource: 'tasks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'task_id', name: 'taskId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
          'https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.analytics.readonly',
        ],
      },
    ],
  ],
};

const getTasks: Operation = {
  id: 'getTasks',
  method: 'GET',
  path: '/sell/feed/v1/task',
  resource: 'tasks',
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
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
          'https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.analytics.readonly',
        ],
      },
    ],
  ],
};

const uploadFile: Operation = {
  id: 'uploadFile',
  method: 'POST',
  path: '/sell/feed/v1/task/{task_id}/upload_file',
  resource: 'tasks',
  name: 'uploadFile',
  host: 'api',
  params: [
    { wire: 'task_id', name: 'taskId', location: 'path' },
    { wire: 'file', name: 'file', location: 'form' },
    { wire: 'fileName', name: 'fileName', location: 'form' },
    { wire: 'name', name: 'name', location: 'form' },
    { wire: 'type', name: 'type', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
          'https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.analytics.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [createTask, getTask, getTasks, uploadFile];

export class TasksApi extends Resource {
  /** Create a feed task to upload a file to. */
  create(body: CreateTaskRequest, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<void> {
    return this.call(createTask, body, { ...params }, options);
  }

  /** Get one feed task. */
  get(taskId: string, options?: RequestOptions): Promise<Task> {
    return this.call(getTask, undefined, { taskId }, options);
  }

  /** List one page of feed tasks. */
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
  ): Promise<TaskCollection> {
    return this.call(getTasks, undefined, { ...params }, options);
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
  ): AsyncGenerator<models.Task, void, undefined> {
    return this.paginate(getTasks, undefined, { ...params }, options);
  }

  /** Upload the input file of a feed task. */
  uploadFile(
    taskId: string,
    params: { file: FileInput; fileName?: string; name?: string; type?: string },
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(uploadFile, undefined, { taskId, ...params }, options);
  }
}
