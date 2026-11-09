// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetOrder429Response,
  ShippingFulfillment,
  ShippingFulfillmentDetails,
  ShippingFulfillmentPagedCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createShippingFulfillment: Operation = {
  id: 'createShippingFulfillment',
  method: 'POST',
  path: '/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment',
  resource: 'shippingFulfillments',
  name: 'create',
  host: 'api',
  params: [{ wire: 'orderId', name: 'orderId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.fulfillment'] }]],
};

const getShippingFulfillment: Operation = {
  id: 'getShippingFulfillment',
  method: 'GET',
  path: '/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment/{fulfillmentId}',
  resource: 'shippingFulfillments',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'fulfillmentId', name: 'fulfillmentId', location: 'path' },
    { wire: 'orderId', name: 'orderId', location: 'path' },
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

const getShippingFulfillments: Operation = {
  id: 'getShippingFulfillments',
  method: 'GET',
  path: '/sell/fulfillment/v1/order/{orderId}/shipping_fulfillment',
  resource: 'shippingFulfillments',
  name: 'list',
  host: 'api',
  params: [{ wire: 'orderId', name: 'orderId', location: 'path' }],
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

export const OPERATIONS: readonly Operation[] = [
  createShippingFulfillment,
  getShippingFulfillment,
  getShippingFulfillments,
];

export class ShippingFulfillmentsApi extends Resource {
  /** Mark line items of an order shipped */
  create(orderId: string, body: ShippingFulfillmentDetails, options?: RequestOptions): Promise<object> {
    return this.call(createShippingFulfillment, body, { orderId }, options);
  }

  /** Get one shipping fulfillment. */
  get(fulfillmentId: string, orderId: string, options?: RequestOptions): Promise<ShippingFulfillment> {
    return this.call(getShippingFulfillment, undefined, { fulfillmentId, orderId }, options);
  }

  /** List the shipping fulfillments of an order. */
  list(orderId: string, options?: RequestOptions): Promise<ShippingFulfillmentPagedCollection> {
    return this.call(getShippingFulfillments, undefined, { orderId }, options);
  }
}
