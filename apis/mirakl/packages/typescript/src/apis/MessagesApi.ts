// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  M10Response200,
  M11Response200,
  M12RequestMultipartFormDataMessageInput,
  M12Response201,
  M14RequestMultipartFormDataThreadInput,
  M14Response201,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const m10: Operation = {
  id: 'M10',
  method: 'GET',
  path: '/api/inbox/threads/{thread_id}',
  resource: 'messages',
  name: 'getThread',
  params: [
    { wire: 'thread_id', name: 'threadId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_MESSAGE_READ', 'ROLE_PARTNER_MESSAGE_READ'],
      },
    ],
  ],
};

const m11: Operation = {
  id: 'M11',
  method: 'GET',
  path: '/api/inbox/threads',
  resource: 'messages',
  name: 'listThreads',
  params: [
    { wire: 'entity_type', name: 'entityType', location: 'query' },
    { wire: 'entity_id', name: 'entityId', location: 'query' },
    { wire: 'updated_since', name: 'updatedSince', location: 'query' },
    { wire: 'with_messages', name: 'withMessages', location: 'query' },
    { wire: 'channel_codes', name: 'channelCodes', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterThreads',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_MESSAGE_READ', 'ROLE_PARTNER_MESSAGE_READ'],
      },
    ],
  ],
};

const m12: Operation = {
  id: 'M12',
  method: 'POST',
  path: '/api/inbox/threads/{thread_id}/message',
  resource: 'messages',
  name: 'reply',
  params: [
    { wire: 'thread_id', name: 'threadId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'files', name: 'files', location: 'form' },
    { wire: 'message_input', name: 'messageInput', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_MESSAGE_WRITE', 'ROLE_PARTNER_MESSAGE_WRITE'],
      },
    ],
  ],
};

const m13: Operation = {
  id: 'M13',
  method: 'GET',
  path: '/api/inbox/threads/{attachment_id}/download',
  resource: 'messages',
  name: 'downloadAttachment',
  params: [
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_MESSAGE_READ', 'ROLE_PARTNER_MESSAGE_READ'],
      },
    ],
  ],
};

const m14: Operation = {
  id: 'M14',
  method: 'POST',
  path: '/api/inbox/threads',
  resource: 'messages',
  name: 'createThread',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'files', name: 'files', location: 'form' },
    { wire: 'thread_input', name: 'threadInput', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

export const OPERATIONS: readonly Operation[] = [m10, m11, m12, m13, m14];

export class MessagesApi extends Resource {
  /** Get a message thread (M10). */
  getThread(threadId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<M10Response200> {
    return this.call(m10, undefined, { threadId, ...params }, options);
  }

  /** List one page of message threads (M11). */
  listThreads(
    params: {
      entityType?: string;
      entityId?: Array<string>;
      updatedSince?: string;
      withMessages?: boolean;
      channelCodes?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<M11Response200> {
    return this.call(m11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterThreads(
    params: {
      entityType?: string;
      entityId?: Array<string>;
      updatedSince?: string;
      withMessages?: boolean;
      channelCodes?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.M11Response200Data, void, undefined> {
    return this.paginate(m11, undefined, { ...params }, options);
  }

  /** Reply to a message thread (M12). */
  reply(
    threadId: string,
    params: { shopId?: number; files?: FileInput[]; messageInput: M12RequestMultipartFormDataMessageInput },
    options?: RequestOptions,
  ): Promise<M12Response201> {
    return this.call(m12, undefined, { threadId, ...params }, options);
  }

  /** Download a message attachment (M13). */
  downloadAttachment(
    attachmentId: string,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(m13, undefined, { attachmentId, ...params }, options);
  }

  /** Start a message thread with the operator (M14). */
  createThread(
    params: { shopId?: number; files?: FileInput[]; threadInput: M14RequestMultipartFormDataThreadInput },
    options?: RequestOptions,
  ): Promise<M14Response201> {
    return this.call(m14, undefined, { ...params }, options);
  }
}
