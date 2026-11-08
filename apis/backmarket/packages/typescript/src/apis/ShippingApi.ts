// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { Delivery, DeliveryPage, OrderIdValidationError, ReturnPage, ReturnShipment } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getDeliveries: Operation = {
  id: 'GetDeliveries',
  method: 'GET',
  path: '/ws/shipping/v1/deliveries',
  resource: 'shipping',
  name: 'listDeliveries',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'pickup_start_date', name: 'pickupStartDate', location: 'query' },
    { wire: 'pickup_end_date', name: 'pickupEndDate', location: 'query' },
    { wire: 'order_state', name: 'orderState', location: 'query' },
    { wire: 'hub_scanned', name: 'hubScanned', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDeliveries',
  paging: { style: 'next_link', items: 'results', link: 'next', params: ['page', 'cursor'] },
};

const getDelivery: Operation = {
  id: 'GetDelivery',
  method: 'GET',
  path: '/ws/shipping/v1/deliveries/{id}',
  resource: 'shipping',
  name: 'getDelivery',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsJson: true,
};

const getReturn: Operation = {
  id: 'GetReturn',
  method: 'GET',
  path: '/ws/shipping/v1/returns/{id}',
  resource: 'shipping',
  name: 'getReturn',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsJson: true,
};

const getReturns: Operation = {
  id: 'GetReturns',
  method: 'GET',
  path: '/ws/shipping/v1/returns',
  resource: 'shipping',
  name: 'listReturns',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'pickup_start_date', name: 'pickupStartDate', location: 'query' },
    { wire: 'pickup_end_date', name: 'pickupEndDate', location: 'query' },
    { wire: 'order_state', name: 'orderState', location: 'query' },
    { wire: 'hub_scanned', name: 'hubScanned', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterReturns',
  paging: { style: 'next_link', items: 'results', link: 'next', params: ['page', 'cursor'] },
};

export const OPERATIONS: readonly Operation[] = [getDeliveries, getDelivery, getReturn, getReturns];

export class ShippingApi extends Resource {
  /** List one page of deliveries. */
  listDeliveries(
    params: {
      page?: number;
      orderId?: number;
      startDate?: string;
      endDate?: string;
      pickupStartDate?: string;
      pickupEndDate?: string;
      orderState?: 0 | 1 | 3 | 8 | 9;
      hubScanned?: boolean;
    } = {},
    options?: RequestOptions,
  ): Promise<DeliveryPage> {
    return this.call(getDeliveries, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterDeliveries(
    params: {
      page?: number;
      orderId?: number;
      startDate?: string;
      endDate?: string;
      pickupStartDate?: string;
      pickupEndDate?: string;
      orderState?: 0 | 1 | 3 | 8 | 9;
      hubScanned?: boolean;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Delivery, void, undefined> {
    return this.paginate(getDeliveries, undefined, { ...params }, options);
  }

  /** Get one delivery. */
  getDelivery(id: number, options?: RequestOptions): Promise<Delivery> {
    return this.call(getDelivery, undefined, { id }, options);
  }

  /** Get one return. */
  getReturn(id: number, options?: RequestOptions): Promise<ReturnShipment> {
    return this.call(getReturn, undefined, { id }, options);
  }

  /** List one page of returns. */
  listReturns(
    params: {
      page?: number;
      orderId?: number;
      startDate?: string;
      endDate?: string;
      pickupStartDate?: string;
      pickupEndDate?: string;
      orderState?: 0 | 1 | 3 | 8 | 9;
      hubScanned?: boolean;
    } = {},
    options?: RequestOptions,
  ): Promise<ReturnPage> {
    return this.call(getReturns, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterReturns(
    params: {
      page?: number;
      orderId?: number;
      startDate?: string;
      endDate?: string;
      pickupStartDate?: string;
      pickupEndDate?: string;
      orderState?: 0 | 1 | 3 | 8 | 9;
      hubScanned?: boolean;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ReturnShipment, void, undefined> {
    return this.paginate(getReturns, undefined, { ...params }, options);
  }
}
