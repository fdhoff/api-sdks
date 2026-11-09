// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiWebhookResponse,
  ApiWebhooksPaginatedResponse,
  CreateWebhookParams,
  UpdateWebhookParams,
  VerifyWebhookParams,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createWebhook: Operation = {
  id: 'createWebhook',
  method: 'POST',
  path: '/webhooks',
  resource: 'webhooks',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const deleteWebhook: Operation = {
  id: 'deleteWebhook',
  method: 'DELETE',
  path: '/webhooks/{webhookEndpointId}',
  resource: 'webhooks',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'webhookEndpointId', name: 'webhookEndpointId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getWebhook: Operation = {
  id: 'getWebhook',
  method: 'GET',
  path: '/webhooks/{webhookEndpointId}',
  resource: 'webhooks',
  name: 'get',
  host: 'api',
  params: [{ wire: 'webhookEndpointId', name: 'webhookEndpointId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getWebhooks: Operation = {
  id: 'getWebhooks',
  method: 'GET',
  path: '/webhooks',
  resource: 'webhooks',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'webhooks', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateWebhook: Operation = {
  id: 'updateWebhook',
  method: 'POST',
  path: '/webhooks/{webhookEndpointId}',
  resource: 'webhooks',
  name: 'update',
  host: 'api',
  params: [{ wire: 'webhookEndpointId', name: 'webhookEndpointId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const verifyWebhook: Operation = {
  id: 'verifyWebhook',
  method: 'POST',
  path: '/webhooks/{webhookEndpointId}/verify',
  resource: 'webhooks',
  name: 'sendTestEvent',
  host: 'api',
  params: [{ wire: 'webhookEndpointId', name: 'webhookEndpointId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createWebhook,
  deleteWebhook,
  getWebhook,
  getWebhooks,
  updateWebhook,
  verifyWebhook,
];

export class WebhooksApi extends Resource {
  /** Register a webhook endpoint. */
  create(body?: CreateWebhookParams, options?: RequestOptions): Promise<ApiWebhookResponse> {
    return this.call(createWebhook, body, {}, options);
  }

  /** Delete a webhook endpoint. */
  delete(webhookEndpointId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteWebhook, undefined, { webhookEndpointId }, options);
  }

  /** Get one webhook endpoint. */
  get(webhookEndpointId: string, options?: RequestOptions): Promise<ApiWebhookResponse> {
    return this.call(getWebhook, undefined, { webhookEndpointId }, options);
  }

  /** List one page of webhook endpoints. */
  list(
    params: {
      status?: Array<'active' | 'paused' | 'disabled' | 'deleted'>;
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<ApiWebhooksPaginatedResponse> {
    return this.call(getWebhooks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      status?: Array<'active' | 'paused' | 'disabled' | 'deleted'>;
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiWebhookResponse, void, undefined> {
    return this.paginate(getWebhooks, undefined, { ...params }, options);
  }

  /** Update a webhook endpoint. */
  update(webhookEndpointId: string, body?: UpdateWebhookParams, options?: RequestOptions): Promise<ApiWebhookResponse> {
    return this.call(updateWebhook, body, { webhookEndpointId }, options);
  }

  /** Send a test event to a webhook endpoint. */
  sendTestEvent(webhookEndpointId: string, body?: VerifyWebhookParams, options?: RequestOptions): Promise<void> {
    return this.call(verifyWebhook, body, { webhookEndpointId }, options);
  }
}
