// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetOrderEarnings429Response, TransactionSummaryResponse, Transactions } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getTransactionSummary: Operation = {
  id: 'getTransactionSummary',
  method: 'GET',
  path: '/sell/finances/v1/transaction_summary',
  resource: 'transactions',
  name: 'getSummary',
  host: 'apiz',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

const getTransactions: Operation = {
  id: 'getTransactions',
  method: 'GET',
  path: '/sell/finances/v1/transaction',
  resource: 'transactions',
  name: 'list',
  host: 'apiz',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'transactions',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getTransactionSummary, getTransactions];

export class TransactionsApi extends Resource {
  /** Sum the seller's monetary transactions by type. */
  getSummary(
    params: { filter?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<TransactionSummaryResponse> {
    return this.call(getTransactionSummary, undefined, { ...params }, options);
  }

  /** List one page of the seller's monetary transactions. */
  list(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<Transactions | undefined> {
    return this.call(getTransactions, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Transaction, void, undefined> {
    return this.paginate(getTransactions, undefined, { ...params }, options);
  }
}
