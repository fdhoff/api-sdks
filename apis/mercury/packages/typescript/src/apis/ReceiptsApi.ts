// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiV1ReceiptResponse,
  ApiV1ReceiptUploadUrlRequest,
  ApiV1ReceiptUploadUrlResponse,
  ApiV1ReceiptsPaginatedResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createReceiptUploadUrl: Operation = {
  id: 'createReceiptUploadUrl',
  method: 'POST',
  path: '/spend/receipts',
  resource: 'receipts',
  name: 'createUploadUrl',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getReceipt: Operation = {
  id: 'getReceipt',
  method: 'GET',
  path: '/spend/receipts/{receiptId}',
  resource: 'receipts',
  name: 'get',
  host: 'api',
  params: [{ wire: 'receiptId', name: 'receiptId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listReceipts: Operation = {
  id: 'listReceipts',
  method: 'GET',
  path: '/spend/receipts',
  resource: 'receipts',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'receipts', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const matchReceipt: Operation = {
  id: 'matchReceipt',
  method: 'POST',
  path: '/spend/receipts/{receiptId}/match',
  resource: 'receipts',
  name: 'match',
  host: 'api',
  params: [{ wire: 'receiptId', name: 'receiptId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [createReceiptUploadUrl, getReceipt, listReceipts, matchReceipt];

export class ReceiptsApi extends Resource {
  /** Get a short-lived URL to upload a receipt file to. */
  createUploadUrl(
    body?: ApiV1ReceiptUploadUrlRequest,
    options?: RequestOptions,
  ): Promise<ApiV1ReceiptUploadUrlResponse> {
    return this.call(createReceiptUploadUrl, body, {}, options);
  }

  /** Get one receipt. */
  get(receiptId: string, options?: RequestOptions): Promise<ApiV1ReceiptResponse> {
    return this.call(getReceipt, undefined, { receiptId }, options);
  }

  /** List one page of receipts. */
  list(
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1ReceiptsPaginatedResponse> {
    return this.call(listReceipts, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1ReceiptResponse, void, undefined> {
    return this.paginate(listReceipts, undefined, { ...params }, options);
  }

  /** Start matching an uploaded receipt to a transaction. */
  match(receiptId: string, options?: RequestOptions): Promise<void> {
    return this.call(matchReceipt, undefined, { receiptId }, options);
  }
}
