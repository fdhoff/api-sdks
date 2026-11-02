// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CountryCode,
  Order,
  OrderLineUpdate,
  OrderPage,
  OrderState,
  UpdateOrder,
  UpdatedOrderLine,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation } from '../runtime/index.js';

const getWsListOrder: Operation = {
  id: 'get-ws-list-order',
  method: 'GET',
  path: '/ws/orders',
  resource: 'orders',
  name: 'list',
  params: [
    { wire: 'date_creation', name: 'dateCreation', location: 'query' },
    { wire: 'date_modification', name: 'dateModification', location: 'query' },
    { wire: 'country_code', name: 'countryCode', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'page-size', name: 'pageSize', location: 'query' },
  ],
  iterator: 'iter',
};

const getWsSpecificOrder: Operation = {
  id: 'get-ws-specific-order',
  method: 'GET',
  path: '/ws/orders/{order_id}',
  resource: 'orders',
  name: 'get',
  params: [{ wire: 'order_id', name: 'orderId', location: 'path' }],
};

const postWsSpecificOrderInvoice: Operation = {
  id: 'post-ws-specific-order-invoice',
  method: 'POST',
  path: '/ws/orders/{order_id}/invoice',
  resource: 'orders',
  name: 'uploadInvoice',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'invoice', name: 'invoice', location: 'form' },
  ],
};

const updateWsSpecificOrder: Operation = {
  id: 'update-ws-specific-order',
  method: 'POST',
  path: '/ws/orders/{order_id}',
  resource: 'orders',
  name: 'update',
  params: [{ wire: 'order_id', name: 'orderId', location: 'path' }],
  hasBody: true,
};

const updateWsSpecificOrderline: Operation = {
  id: 'update-ws-specific-orderline',
  method: 'PATCH',
  path: '/ws/orderlines/{orderline_id}',
  resource: 'orders',
  name: 'updateLine',
  params: [{ wire: 'orderline_id', name: 'orderlineId', location: 'path' }],
  hasBody: true,
};

export const OPERATIONS: readonly Operation[] = [
  getWsListOrder,
  getWsSpecificOrder,
  postWsSpecificOrderInvoice,
  updateWsSpecificOrder,
  updateWsSpecificOrderline,
];

export class OrdersApi extends Resource {
  /** List one page of orders. */
  list(
    params: {
      dateCreation?: string;
      dateModification?: string;
      countryCode?: CountryCode;
      state?: OrderState;
      page?: number;
      pageSize?: number;
    } = {},
  ): Promise<OrderPage> {
    return this.call(getWsListOrder, undefined, { ...params });
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      dateCreation?: string;
      dateModification?: string;
      countryCode?: CountryCode;
      state?: OrderState;
      page?: number;
      pageSize?: number;
    } = {},
  ): AsyncGenerator<models.Order, void, undefined> {
    return this.paginate(getWsListOrder, undefined, { ...params });
  }

  /** Get one order. */
  get(orderId: number): Promise<Order> {
    return this.call(getWsSpecificOrder, undefined, { orderId });
  }

  /** Upload invoices for an order. */
  uploadInvoice(orderId: number, params: { invoice?: FileInput[] } = {}): Promise<void> {
    return this.call(postWsSpecificOrderInvoice, undefined, { orderId, ...params });
  }

  /** Update one order. */
  update(orderId: number, body?: UpdateOrder): Promise<Order> {
    return this.call(updateWsSpecificOrder, body, { orderId });
  }

  /** Update one order line. */
  updateLine(orderlineId: number, body?: OrderLineUpdate): Promise<UpdatedOrderLine> {
    return this.call(updateWsSpecificOrderline, body, { orderlineId });
  }
}
