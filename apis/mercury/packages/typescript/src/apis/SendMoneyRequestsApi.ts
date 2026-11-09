// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { SendMoneyApprovalRequestResponse, SendMoneyApprovalRequestsPaginatedResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getSendMoneyApprovalRequest: Operation = {
  id: 'getSendMoneyApprovalRequest',
  method: 'GET',
  path: '/request-send-money/{requestId}',
  resource: 'sendMoneyRequests',
  name: 'get',
  host: 'api',
  params: [{ wire: 'requestId', name: 'requestId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listSendMoneyApprovalRequests: Operation = {
  id: 'listSendMoneyApprovalRequests',
  method: 'GET',
  path: '/request-send-money',
  resource: 'sendMoneyRequests',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'requests', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getSendMoneyApprovalRequest, listSendMoneyApprovalRequests];

export class SendMoneyRequestsApi extends Resource {
  /** Get one request to send money. */
  get(requestId: string, options?: RequestOptions): Promise<SendMoneyApprovalRequestResponse> {
    return this.call(getSendMoneyApprovalRequest, undefined, { requestId }, options);
  }

  /** List one page of requests to send money. */
  list(
    params: {
      accountId?: string;
      status?: 'pendingApproval' | 'approved' | 'rejected' | 'cancelled';
      startAfter?: string;
      endBefore?: string;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<SendMoneyApprovalRequestsPaginatedResponse> {
    return this.call(listSendMoneyApprovalRequests, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      accountId?: string;
      status?: 'pendingApproval' | 'approved' | 'rejected' | 'cancelled';
      startAfter?: string;
      endBefore?: string;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.SendMoneyApprovalRequestResponse, void, undefined> {
    return this.paginate(listSendMoneyApprovalRequests, undefined, { ...params }, options);
  }
}
