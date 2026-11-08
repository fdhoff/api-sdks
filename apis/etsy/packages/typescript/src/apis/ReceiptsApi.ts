// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreateReceiptShipmentRequest, ErrorSchema, ShopReceipt, ShopReceipts } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createReceiptShipment: Operation = {
  id: 'createReceiptShipment',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking',
  resource: 'receipts',
  name: 'createShipment',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'receipt_id', name: 'receiptId', location: 'path' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_w'] },
    ],
  ],
};

const getShopReceipt: Operation = {
  id: 'getShopReceipt',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}',
  resource: 'receipts',
  name: 'get',
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

const getShopReceipts: Operation = {
  id: 'getShopReceipts',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/receipts',
  resource: 'receipts',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'min_created', name: 'minCreated', location: 'query' },
    { wire: 'max_created', name: 'maxCreated', location: 'query' },
    { wire: 'min_last_modified', name: 'minLastModified', location: 'query' },
    { wire: 'max_last_modified', name: 'maxLastModified', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort_on', name: 'sortOn', location: 'query' },
    { wire: 'sort_order', name: 'sortOrder', location: 'query' },
    { wire: 'was_paid', name: 'wasPaid', location: 'query' },
    { wire: 'was_shipped', name: 'wasShipped', location: 'query' },
    { wire: 'was_delivered', name: 'wasDelivered', location: 'query' },
    { wire: 'was_canceled', name: 'wasCanceled', location: 'query' },
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

const updateShopReceipt: Operation = {
  id: 'updateShopReceipt',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}',
  resource: 'receipts',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'receipt_id', name: 'receiptId', location: 'path' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
    { wire: 'was_shipped', name: 'wasShipped', location: 'urlencoded' },
    { wire: 'was_paid', name: 'wasPaid', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createReceiptShipment,
  getShopReceipt,
  getShopReceipts,
  updateShopReceipt,
];

export class ReceiptsApi extends Resource {
  /** Add tracking to a receipt and mark it shipped. */
  createShipment(
    shopId: number,
    receiptId: number,
    body?: CreateReceiptShipmentRequest,
    params: { legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceipt> {
    return this.call(createReceiptShipment, body, { shopId, receiptId, ...params }, options);
  }

  /** Get one receipt. */
  get(
    shopId: number,
    receiptId: number,
    params: { legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceipt> {
    return this.call(getShopReceipt, undefined, { shopId, receiptId, ...params }, options);
  }

  /** List one page of a shop's receipts. */
  list(
    shopId: number,
    params: {
      minCreated?: number;
      maxCreated?: number;
      minLastModified?: number;
      maxLastModified?: number;
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'updated' | 'receipt_id';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      wasPaid?: boolean;
      wasShipped?: boolean;
      wasDelivered?: boolean;
      wasCanceled?: boolean;
      legacy?: boolean;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopReceipts> {
    return this.call(getShopReceipts, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    shopId: number,
    params: {
      minCreated?: number;
      maxCreated?: number;
      minLastModified?: number;
      maxLastModified?: number;
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'updated' | 'receipt_id';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      wasPaid?: boolean;
      wasShipped?: boolean;
      wasDelivered?: boolean;
      wasCanceled?: boolean;
      legacy?: boolean;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopReceipt, void, undefined> {
    return this.paginate(getShopReceipts, undefined, { shopId, ...params }, options);
  }

  /** Update a receipt's shipped or paid state. */
  update(
    shopId: number,
    receiptId: number,
    params: { legacy?: boolean; wasShipped?: boolean; wasPaid?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopReceipt> {
    return this.call(updateShopReceipt, undefined, { shopId, receiptId, ...params }, options);
  }
}
