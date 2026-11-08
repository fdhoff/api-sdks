// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopReceiptTransaction, ShopReceiptTransactions } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getShopReceiptTransaction: Operation = {
  id: 'getShopReceiptTransaction',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/transactions/{transaction_id}',
  resource: 'transactions',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'transaction_id', name: 'transactionId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getShopReceiptTransactionsByListing: Operation = {
  id: 'getShopReceiptTransactionsByListing',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/transactions',
  resource: 'transactions',
  name: 'listByListing',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterByListing',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getShopReceiptTransactionsByReceipt: Operation = {
  id: 'getShopReceiptTransactionsByReceipt',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}/transactions',
  resource: 'transactions',
  name: 'listByReceipt',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'receipt_id', name: 'receiptId', location: 'path' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getShopReceiptTransactionsByShop: Operation = {
  id: 'getShopReceiptTransactionsByShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/transactions',
  resource: 'transactions',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  getShopReceiptTransaction,
  getShopReceiptTransactionsByListing,
  getShopReceiptTransactionsByReceipt,
  getShopReceiptTransactionsByShop,
];

export class TransactionsApi extends Resource {
  /** Get one transaction. */
  get(shopId: number, transactionId: number, options?: RequestOptions): Promise<ShopReceiptTransaction> {
    return this.call(getShopReceiptTransaction, undefined, { shopId, transactionId }, options);
  }

  /** List one page of a listing's transactions. */
  listByListing(
    shopId: number,
    listingId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceiptTransactions> {
    return this.call(getShopReceiptTransactionsByListing, undefined, { shopId, listingId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterByListing(
    shopId: number,
    listingId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopReceiptTransaction, void, undefined> {
    return this.paginate(getShopReceiptTransactionsByListing, undefined, { shopId, listingId, ...params }, options);
  }

  /** List the transactions on a receipt. */
  listByReceipt(
    shopId: number,
    receiptId: number,
    params: { legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceiptTransactions> {
    return this.call(getShopReceiptTransactionsByReceipt, undefined, { shopId, receiptId, ...params }, options);
  }

  /** List one page of a shop's transactions. */
  list(
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceiptTransactions> {
    return this.call(getShopReceiptTransactionsByShop, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopReceiptTransaction, void, undefined> {
    return this.paginate(getShopReceiptTransactionsByShop, undefined, { shopId, ...params }, options);
  }
}
