// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkUpdateConversation429Response,
  BulkUpdateConversationsRequest,
  BulkUpdateConversationsResponse,
  GetAllMyConversationsResponse,
  GetMessagesByConversationIdResponse,
  SendMessageRequest,
  SendMessageResponse,
  UpdateConversationRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkUpdateConversation: Operation = {
  id: 'bulkUpdateConversation',
  method: 'POST',
  path: '/commerce/message/v1/bulk_update_conversation',
  resource: 'conversations',
  name: 'bulkUpdate',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.message'] }]],
};

const getConversation: Operation = {
  id: 'getConversation',
  method: 'GET',
  path: '/commerce/message/v1/conversation/{conversation_id}',
  resource: 'conversations',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'conversation_id', name: 'conversationId', location: 'path' },
    { wire: 'conversation_type', name: 'conversationType', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterMessages',
  paging: { style: 'next_link', items: 'messages', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.message'] }]],
};

const getConversations: Operation = {
  id: 'getConversations',
  method: 'GET',
  path: '/commerce/message/v1/conversation',
  resource: 'conversations',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'conversation_status', name: 'conversationStatus', location: 'query' },
    { wire: 'conversation_type', name: 'conversationType', location: 'query' },
    { wire: 'end_time', name: 'endTime', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'other_party_username', name: 'otherPartyUsername', location: 'query' },
    { wire: 'reference_id', name: 'referenceId', location: 'query' },
    { wire: 'reference_type', name: 'referenceType', location: 'query' },
    { wire: 'start_time', name: 'startTime', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'conversations',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.message'] }]],
};

const sendMessage: Operation = {
  id: 'sendMessage',
  method: 'POST',
  path: '/commerce/message/v1/send_message',
  resource: 'conversations',
  name: 'send',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.message'] }]],
};

const updateConversation: Operation = {
  id: 'updateConversation',
  method: 'POST',
  path: '/commerce/message/v1/update_conversation',
  resource: 'conversations',
  name: 'update',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.message'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  bulkUpdateConversation,
  getConversation,
  getConversations,
  sendMessage,
  updateConversation,
];

export class ConversationsApi extends Resource {
  /** Update the status of several conversations. */
  bulkUpdate(
    body?: BulkUpdateConversationsRequest,
    options?: RequestOptions,
  ): Promise<BulkUpdateConversationsResponse> {
    return this.call(bulkUpdateConversation, body, {}, options);
  }

  /** Get one conversation with one page of its messages. */
  get(
    conversationId: string,
    params: { conversationType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): Promise<GetMessagesByConversationIdResponse> {
    return this.call(getConversation, undefined, { conversationId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterMessages(
    conversationId: string,
    params: { conversationType: string; limit?: string; offset?: string },
    options?: RequestOptions,
  ): AsyncGenerator<models.MessageDetail, void, undefined> {
    return this.paginate(getConversation, undefined, { conversationId, ...params }, options);
  }

  /** List one page of conversations. */
  list(
    params: {
      conversationStatus?: string;
      conversationType: string;
      endTime?: string;
      limit?: string;
      offset?: string;
      otherPartyUsername?: string;
      referenceId?: string;
      referenceType?: string;
      startTime?: string;
    },
    options?: RequestOptions,
  ): Promise<GetAllMyConversationsResponse> {
    return this.call(getConversations, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      conversationStatus?: string;
      conversationType: string;
      endTime?: string;
      limit?: string;
      offset?: string;
      otherPartyUsername?: string;
      referenceId?: string;
      referenceType?: string;
      startTime?: string;
    },
    options?: RequestOptions,
  ): AsyncGenerator<models.ConversationDetail, void, undefined> {
    return this.paginate(getConversations, undefined, { ...params }, options);
  }

  /** Send a message */
  send(body?: SendMessageRequest, options?: RequestOptions): Promise<SendMessageResponse> {
    return this.call(sendMessage, body, {}, options);
  }

  /** Update the status of one conversation. */
  update(body?: UpdateConversationRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateConversation, body, {}, options);
  }
}
