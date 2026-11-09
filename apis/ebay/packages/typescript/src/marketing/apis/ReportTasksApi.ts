// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  CreateReportTask,
  ReportTask,
  ReportTaskPagedCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createReportTask: Operation = {
  id: 'createReportTask',
  method: 'POST',
  path: '/sell/marketing/v1/ad_report_task',
  resource: 'reportTasks',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteReportTask: Operation = {
  id: 'deleteReportTask',
  method: 'DELETE',
  path: '/sell/marketing/v1/ad_report_task/{report_task_id}',
  resource: 'reportTasks',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'report_task_id', name: 'reportTaskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getReportTask: Operation = {
  id: 'getReportTask',
  method: 'GET',
  path: '/sell/marketing/v1/ad_report_task/{report_task_id}',
  resource: 'reportTasks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'report_task_id', name: 'reportTaskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getReportTasks: Operation = {
  id: 'getReportTasks',
  method: 'GET',
  path: '/sell/marketing/v1/ad_report_task',
  resource: 'reportTasks',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'report_task_statuses', name: 'reportTaskStatuses', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'reportTasks', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [createReportTask, deleteReportTask, getReportTask, getReportTasks];

export class ReportTasksApi extends Resource {
  /** Start a task that builds a Promoted Listings report. */
  create(body: CreateReportTask, options?: RequestOptions): Promise<Error> {
    return this.call(createReportTask, body, {}, options);
  }

  /** Delete a report task. */
  delete(reportTaskId: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(deleteReportTask, undefined, { reportTaskId }, options);
  }

  /** Get one report task. */
  get(reportTaskId: string, options?: RequestOptions): Promise<ReportTask> {
    return this.call(getReportTask, undefined, { reportTaskId }, options);
  }

  /** List one page of the seller's report tasks. */
  list(
    params: { limit?: string; offset?: string; reportTaskStatuses?: string } = {},
    options?: RequestOptions,
  ): Promise<ReportTaskPagedCollection> {
    return this.call(getReportTasks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: string; offset?: string; reportTaskStatuses?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ReportTask, void, undefined> {
    return this.paginate(getReportTasks, undefined, { ...params }, options);
  }
}
