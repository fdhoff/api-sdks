// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  TransferMoneyApprovalRequestAPIRequest,
  TransferMoneyApprovalRequestResponse,
  TransferMoneyApprovalRequestsPaginatedResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getTransferMoneyApprovalRequest: Operation = {
  id: 'getTransferMoneyApprovalRequest',
  method: 'GET',
  path: '/request-transfer/{requestId}',
  resource: 'transferRequests',
  name: 'get',
  host: 'api',
  params: [{ wire: 'requestId', name: 'requestId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listTransferMoneyApprovalRequests: Operation = {
  id: 'listTransferMoneyApprovalRequests',
  method: 'GET',
  path: '/request-transfer',
  resource: 'transferRequests',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'sourceAccountId', name: 'sourceAccountId', location: 'query' },
    { wire: 'destinationAccountId', name: 'destinationAccountId', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'requests', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const requestTransferMoney: Operation = {
  id: 'requestTransferMoney',
  method: 'POST',
  path: '/request-transfer',
  resource: 'transferRequests',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  idempotencyKey: 'idempotencyKey',
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getTransferMoneyApprovalRequest,
  listTransferMoneyApprovalRequests,
  requestTransferMoney,
];

export class TransferRequestsApi extends Resource {
  /** Get one request to move money between accounts. */
  get(requestId: string, options?: RequestOptions): Promise<TransferMoneyApprovalRequestResponse> {
    return this.call(getTransferMoneyApprovalRequest, undefined, { requestId }, options);
  }

  /** List one page of requests to move money between accounts. */
  list(
    params: {
      sourceAccountId?: string;
      destinationAccountId?: string;
      status?: 'pendingApproval' | 'approved' | 'rejected' | 'cancelled';
      startAt?: string;
      startAfter?: string;
      endBefore?: string;
      limit?: number;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<TransferMoneyApprovalRequestsPaginatedResponse> {
    return this.call(listTransferMoneyApprovalRequests, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      sourceAccountId?: string;
      destinationAccountId?: string;
      status?: 'pendingApproval' | 'approved' | 'rejected' | 'cancelled';
      startAt?: string;
      startAfter?: string;
      endBefore?: string;
      limit?: number;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TransferMoneyApprovalRequestResponse, void, undefined> {
    return this.paginate(listTransferMoneyApprovalRequests, undefined, { ...params }, options);
  }

  /** Ask to move money between accounts */
  create(
    body?: TransferMoneyApprovalRequestAPIRequest,
    options?: RequestOptions,
  ): Promise<TransferMoneyApprovalRequestResponse> {
    return this.call(requestTransferMoney, body, {}, options);
  }
}
