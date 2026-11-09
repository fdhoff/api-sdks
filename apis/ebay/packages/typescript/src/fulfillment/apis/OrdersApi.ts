// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetOrder429Response,
  IssueRefundRequest,
  Order,
  OrderSearchPagedCollection,
  Refund,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getOrder: Operation = {
  id: 'getOrder',
  method: 'GET',
  path: '/sell/fulfillment/v1/order/{orderId}',
  resource: 'orders',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'orderId', name: 'orderId', location: 'path' },
    { wire: 'fieldGroups', name: 'fieldGroups', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly',
        ],
      },
    ],
  ],
};

const getOrders: Operation = {
  id: 'getOrders',
  method: 'GET',
  path: '/sell/fulfillment/v1/order',
  resource: 'orders',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'fieldGroups', name: 'fieldGroups', location: 'query' },
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'orderIds', name: 'orderIds', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'orders', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
          'https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly',
        ],
      },
    ],
  ],
};

const issueRefund: Operation = {
  id: 'issueRefund',
  method: 'POST',
  path: '/sell/fulfillment/v1/order/{order_id}/issue_refund',
  resource: 'orders',
  name: 'issueRefund',
  host: 'api',
  params: [{ wire: 'order_id', name: 'orderId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getOrder, getOrders, issueRefund];

export class OrdersApi extends Resource {
  /** Get one order. */
  get(orderId: string, params: { fieldGroups?: string } = {}, options?: RequestOptions): Promise<Order> {
    return this.call(getOrder, undefined, { orderId, ...params }, options);
  }

  /** List one page of the seller's orders. */
  list(
    params: { fieldGroups?: string; filter?: string; limit?: string; offset?: string; orderIds?: string } = {},
    options?: RequestOptions,
  ): Promise<OrderSearchPagedCollection> {
    return this.call(getOrders, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { fieldGroups?: string; filter?: string; limit?: string; offset?: string; orderIds?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Order, void, undefined> {
    return this.paginate(getOrders, undefined, { ...params }, options);
  }

  /** Refund all or part of an order. */
  issueRefund(orderId: string, body?: IssueRefundRequest, options?: RequestOptions): Promise<Refund> {
    return this.call(issueRefund, body, { orderId }, options);
  }
}
