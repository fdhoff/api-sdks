// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateUserScheduleRequest,
  GetOrderTasks429Response,
  ScheduleTemplateCollection,
  ScheduleTemplateResponse,
  UpdateUserScheduleRequest,
  UserScheduleCollection,
  UserScheduleResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createSchedule: Operation = {
  id: 'createSchedule',
  method: 'POST',
  path: '/sell/feed/v1/schedule',
  resource: 'schedules',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
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

const deleteSchedule: Operation = {
  id: 'deleteSchedule',
  method: 'DELETE',
  path: '/sell/feed/v1/schedule/{schedule_id}',
  resource: 'schedules',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'schedule_id', name: 'scheduleId', location: 'path' }],
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

const getSchedule: Operation = {
  id: 'getSchedule',
  method: 'GET',
  path: '/sell/feed/v1/schedule/{schedule_id}',
  resource: 'schedules',
  name: 'get',
  host: 'api',
  params: [{ wire: 'schedule_id', name: 'scheduleId', location: 'path' }],
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

const getScheduleTemplate: Operation = {
  id: 'getScheduleTemplate',
  method: 'GET',
  path: '/sell/feed/v1/schedule_template/{schedule_template_id}',
  resource: 'schedules',
  name: 'getTemplate',
  host: 'api',
  params: [{ wire: 'schedule_template_id', name: 'scheduleTemplateId', location: 'path' }],
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

const getScheduleTemplates: Operation = {
  id: 'getScheduleTemplates',
  method: 'GET',
  path: '/sell/feed/v1/schedule_template',
  resource: 'schedules',
  name: 'listTemplates',
  host: 'api',
  params: [
    { wire: 'feed_type', name: 'feedType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTemplates',
  paging: {
    style: 'next_link',
    items: 'scheduleTemplates',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
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

const getSchedules: Operation = {
  id: 'getSchedules',
  method: 'GET',
  path: '/sell/feed/v1/schedule',
  resource: 'schedules',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'feed_type', name: 'feedType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'schedules', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
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

const updateSchedule: Operation = {
  id: 'updateSchedule',
  method: 'PUT',
  path: '/sell/feed/v1/schedule/{schedule_id}',
  resource: 'schedules',
  name: 'update',
  host: 'api',
  params: [{ wire: 'schedule_id', name: 'scheduleId', location: 'path' }],
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

export const OPERATIONS: readonly Operation[] = [
  createSchedule,
  deleteSchedule,
  getSchedule,
  getScheduleTemplate,
  getScheduleTemplates,
  getSchedules,
  updateSchedule,
];

export class SchedulesApi extends Resource {
  /** Create a schedule that builds a report regularly. */
  create(body: CreateUserScheduleRequest, options?: RequestOptions): Promise<object> {
    return this.call(createSchedule, body, {}, options);
  }

  /** Delete a schedule. */
  delete(scheduleId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteSchedule, undefined, { scheduleId }, options);
  }

  /** Get one schedule. */
  get(scheduleId: string, options?: RequestOptions): Promise<UserScheduleResponse> {
    return this.call(getSchedule, undefined, { scheduleId }, options);
  }

  /** Get one schedule template. */
  getTemplate(scheduleTemplateId: string, options?: RequestOptions): Promise<ScheduleTemplateResponse> {
    return this.call(getScheduleTemplate, undefined, { scheduleTemplateId }, options);
  }

  /** List one page of schedule templates. */
  listTemplates(
    params: { feedType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): Promise<ScheduleTemplateCollection> {
    return this.call(getScheduleTemplates, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTemplates(
    params: { feedType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): AsyncGenerator<models.ScheduleTemplateResponse, void, undefined> {
    return this.paginate(getScheduleTemplates, undefined, { ...params }, options);
  }

  /** List one page of report schedules. */
  list(
    params: { feedType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): Promise<UserScheduleCollection> {
    return this.call(getSchedules, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { feedType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): AsyncGenerator<models.UserScheduleResponse, void, undefined> {
    return this.paginate(getSchedules, undefined, { ...params }, options);
  }

  /** Update a schedule. */
  update(scheduleId: string, body: UpdateUserScheduleRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateSchedule, body, { scheduleId }, options);
  }
}
