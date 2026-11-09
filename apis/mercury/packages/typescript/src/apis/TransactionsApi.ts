// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiUpdateTransactionRequest,
  Transaction,
  TransactionsPaginatedResponse,
  UploadedAttachment,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getTransactionById: Operation = {
  id: 'getTransactionById',
  method: 'GET',
  path: '/transaction/{transactionId}',
  resource: 'transactions',
  name: 'get',
  host: 'api',
  params: [{ wire: 'transactionId', name: 'transactionId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listTransactions: Operation = {
  id: 'listTransactions',
  method: 'GET',
  path: '/transactions',
  resource: 'transactions',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'search', name: 'search', location: 'query' },
    { wire: 'start', name: 'start', location: 'query' },
    { wire: 'end', name: 'end', location: 'query' },
    { wire: 'postedStart', name: 'postedStart', location: 'query' },
    { wire: 'postedEnd', name: 'postedEnd', location: 'query' },
    { wire: 'accountId', name: 'accountId', location: 'query' },
    { wire: 'cardId', name: 'cardId', location: 'query' },
    { wire: 'mercuryCategory', name: 'mercuryCategory', location: 'query' },
    { wire: 'categoryId', name: 'categoryId', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'transactions', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateTransaction: Operation = {
  id: 'updateTransaction',
  method: 'PATCH',
  path: '/transaction/{transactionId}',
  resource: 'transactions',
  name: 'update',
  host: 'api',
  params: [{ wire: 'transactionId', name: 'transactionId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const uploadTransactionAttachment: Operation = {
  id: 'uploadTransactionAttachment',
  method: 'POST',
  path: '/transaction/{transactionId}/attachments',
  resource: 'transactions',
  name: 'uploadAttachment',
  host: 'api',
  params: [
    { wire: 'transactionId', name: 'transactionId', location: 'path' },
    { wire: 'attachmentType', name: 'attachmentType', location: 'form' },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getTransactionById,
  listTransactions,
  updateTransaction,
  uploadTransactionAttachment,
];

export class TransactionsApi extends Resource {
  /** Get one transaction. */
  get(transactionId: string, options?: RequestOptions): Promise<Transaction> {
    return this.call(getTransactionById, undefined, { transactionId }, options);
  }

  /** List one page of transactions across your accounts. */
  list(
    params: {
      status?: Array<'pending' | 'sent' | 'cancelled' | 'failed' | 'reversed' | 'blocked'>;
      search?: string;
      start?: string;
      end?: string;
      postedStart?: string;
      postedEnd?: string;
      accountId?: Array<string>;
      cardId?: Array<string>;
      mercuryCategory?: string;
      categoryId?: string;
      startAt?: string;
      startAfter?: string;
      endBefore?: string;
      limit?: number;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<TransactionsPaginatedResponse> {
    return this.call(listTransactions, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      status?: Array<'pending' | 'sent' | 'cancelled' | 'failed' | 'reversed' | 'blocked'>;
      search?: string;
      start?: string;
      end?: string;
      postedStart?: string;
      postedEnd?: string;
      accountId?: Array<string>;
      cardId?: Array<string>;
      mercuryCategory?: string;
      categoryId?: string;
      startAt?: string;
      startAfter?: string;
      endBefore?: string;
      limit?: number;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Transaction, void, undefined> {
    return this.paginate(listTransactions, undefined, { ...params }, options);
  }

  /** Update a transaction's note or category. */
  update(transactionId: string, body?: ApiUpdateTransactionRequest, options?: RequestOptions): Promise<Transaction> {
    return this.call(updateTransaction, body, { transactionId }, options);
  }

  /** Attach a file */
  uploadAttachment(
    transactionId: string,
    params: { attachmentType?: string; file: FileInput },
    options?: RequestOptions,
  ): Promise<UploadedAttachment> {
    return this.call(uploadTransactionAttachment, undefined, { transactionId, ...params }, options);
  }
}
