// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetOrderEarnings429Response,
  OrderEarning,
  OrderEarnings,
  OrderEarningsSummary,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getOrderEarnings: Operation = {
  id: 'getOrderEarnings',
  method: 'GET',
  path: '/sell/finances/v1/order_earnings',
  resource: 'orderEarnings',
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
  paging: { style: 'next_link', items: 'orders', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read'] }]],
};

const getOrderEarningsById: Operation = {
  id: 'getOrderEarningsById',
  method: 'GET',
  path: '/sell/finances/v1/order_earnings/{order_id}',
  resource: 'orderEarnings',
  name: 'get',
  host: 'apiz',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read'] }]],
};

const getOrderEarningsSummary: Operation = {
  id: 'getOrderEarningsSummary',
  method: 'GET',
  path: '/sell/finances/v1/order_earnings_summary',
  resource: 'orderEarnings',
  name: 'getSummary',
  host: 'apiz',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read'] }]],
};

export const OPERATIONS: readonly Operation[] = [getOrderEarnings, getOrderEarningsById, getOrderEarningsSummary];

export class OrderEarningsApi extends Resource {
  /** List one page of the seller's earnings by order. */
  list(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<OrderEarnings> {
    return this.call(getOrderEarnings, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OrderEarning, void, undefined> {
    return this.paginate(getOrderEarnings, undefined, { ...params }, options);
  }

  /** Get the seller's earnings from one order. */
  get(orderId: string, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<OrderEarning> {
    return this.call(getOrderEarningsById, undefined, { orderId, ...params }, options);
  }

  /** Sum the seller's earnings across orders. */
  getSummary(
    params: { filter?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<OrderEarningsSummary> {
    return this.call(getOrderEarningsSummary, undefined, { ...params }, options);
  }
}
