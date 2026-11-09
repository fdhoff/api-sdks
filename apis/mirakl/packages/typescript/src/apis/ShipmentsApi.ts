// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ST01Request,
  ST01Response201,
  ST06Request,
  ST06Response200,
  ST07Request,
  ST07Response200,
  ST11Response200,
  ST12Response200,
  ST23Request,
  ST23Response200,
  ST24Request,
  ST24Response200,
  ST26Request,
  ST26Response200,
  ST31Request,
  ST31Response200,
  ST41Request,
  ST41Response200,
  ST42Response200,
  ST51Request,
  ST51Response200,
  ST52Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const sT01: Operation = {
  id: 'ST01',
  method: 'POST',
  path: '/api/shipments',
  resource: 'shipments',
  name: 'create',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIP'] }]],
};

const sT06: Operation = {
  id: 'ST06',
  method: 'PUT',
  path: '/api/shipments/delete',
  resource: 'shipments',
  name: 'delete',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_DELETE'] }]],
};

const sT07: Operation = {
  id: 'ST07',
  method: 'PUT',
  path: '/api/shipments',
  resource: 'shipments',
  name: 'updateShippingOrigin',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_WRITE'] }]],
};

const sT11: Operation = {
  id: 'ST11',
  method: 'GET',
  path: '/api/shipments',
  resource: 'shipments',
  name: 'list',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'shipment_state_code', name: 'shipmentStateCode', location: 'query' },
    { wire: 'shipment_customer_debit_state_code', name: 'shipmentCustomerDebitStateCode', location: 'query' },
    { wire: 'last_updated_from', name: 'lastUpdatedFrom', location: 'query' },
    { wire: 'last_updated_to', name: 'lastUpdatedTo', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_READ'] }]],
};

const sT12: Operation = {
  id: 'ST12',
  method: 'GET',
  path: '/api/shipments/items_to_ship',
  resource: 'shipments',
  name: 'listItemsToShip',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'fulfillment_center_code', name: 'fulfillmentCenterCode', location: 'query' },
    { wire: 'shipping_date_from', name: 'shippingDateFrom', location: 'query' },
    { wire: 'shipping_date_to', name: 'shippingDateTo', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterItemsToShip',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_READ', 'ROLE_PARTNER_ORDER_SHIPMENT_READ'],
      },
    ],
  ],
};

const sT23: Operation = {
  id: 'ST23',
  method: 'POST',
  path: '/api/shipments/tracking',
  resource: 'shipments',
  name: 'updateTracking',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_TRACKING_WRITE'] }]],
};

const sT24: Operation = {
  id: 'ST24',
  method: 'PUT',
  path: '/api/shipments/ship',
  resource: 'shipments',
  name: 'ship',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIP'] }]],
};

const sT26: Operation = {
  id: 'ST26',
  method: 'PUT',
  path: '/api/shipments/ready_for_pick_up',
  resource: 'shipments',
  name: 'markReadyForPickUp',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_ORDER_SHIPMENT_PICK_UP', 'ROLE_SHOP_ADMIN'] }]],
};

const sT31: Operation = {
  id: 'ST31',
  method: 'PUT',
  path: '/api/shipments/additional_information',
  resource: 'shipments',
  name: 'updateAdditionalInformation',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIP'] }]],
};

const sT41: Operation = {
  id: 'ST41',
  method: 'POST',
  path: '/api/shipments/shipping-labels/rates',
  resource: 'shipments',
  name: 'calculateLabelRates',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_WRITE'] }]],
};

const sT42: Operation = {
  id: 'ST42',
  method: 'GET',
  path: '/api/shipments/shipping-labels/rates',
  resource: 'shipments',
  name: 'listLabelRates',
  params: [
    { wire: 'shipment_id', name: 'shipmentId', location: 'query' },
    { wire: 'label_rate_state', name: 'labelRateState', location: 'query' },
    { wire: 'date_created_from', name: 'dateCreatedFrom', location: 'query' },
    { wire: 'date_created_to', name: 'dateCreatedTo', location: 'query' },
    { wire: 'last_updated_from', name: 'lastUpdatedFrom', location: 'query' },
    { wire: 'last_updated_to', name: 'lastUpdatedTo', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterLabelRates',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_READ'] }]],
};

const sT51: Operation = {
  id: 'ST51',
  method: 'POST',
  path: '/api/shipments/shipping-labels',
  resource: 'shipments',
  name: 'createLabels',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_WRITE'] }]],
};

const sT52: Operation = {
  id: 'ST52',
  method: 'GET',
  path: '/api/shipments/shipping-labels',
  resource: 'shipments',
  name: 'listLabels',
  params: [
    { wire: 'shipment_id', name: 'shipmentId', location: 'query' },
    { wire: 'label_state', name: 'labelState', location: 'query' },
    { wire: 'date_created_from', name: 'dateCreatedFrom', location: 'query' },
    { wire: 'date_created_to', name: 'dateCreatedTo', location: 'query' },
    { wire: 'last_updated_from', name: 'lastUpdatedFrom', location: 'query' },
    { wire: 'last_updated_to', name: 'lastUpdatedTo', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterLabels',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIPMENT_READ'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  sT01,
  sT06,
  sT07,
  sT11,
  sT12,
  sT23,
  sT24,
  sT26,
  sT31,
  sT41,
  sT42,
  sT51,
  sT52,
];

export class ShipmentsApi extends Resource {
  /** Create shipments (ST01). */
  create(body?: ST01Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<ST01Response201> {
    return this.call(sT01, body, { ...params }, options);
  }

  /** Delete shipments (ST06). */
  delete(body?: ST06Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<ST06Response200> {
    return this.call(sT06, body, { ...params }, options);
  }

  /** Update the shipping origin of shipments (ST07). */
  updateShippingOrigin(
    body?: ST07Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST07Response200> {
    return this.call(sT07, body, { ...params }, options);
  }

  /** List one page of shipments (ST11). */
  list(
    params: {
      orderId?: Array<string>;
      shipmentStateCode?: Array<string>;
      shipmentCustomerDebitStateCode?: Array<string>;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ST11Response200> {
    return this.call(sT11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      orderId?: Array<string>;
      shipmentStateCode?: Array<string>;
      shipmentCustomerDebitStateCode?: Array<string>;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ST11Response200Data, void, undefined> {
    return this.paginate(sT11, undefined, { ...params }, options);
  }

  /** List one page of items to ship (ST12). */
  listItemsToShip(
    params: {
      orderId?: Array<string>;
      fulfillmentCenterCode?: Array<string>;
      shippingDateFrom?: string;
      shippingDateTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ST12Response200> {
    return this.call(sT12, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterItemsToShip(
    params: {
      orderId?: Array<string>;
      fulfillmentCenterCode?: Array<string>;
      shippingDateFrom?: string;
      shippingDateTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ST12Response200Data, void, undefined> {
    return this.paginate(sT12, undefined, { ...params }, options);
  }

  /** Update the carrier tracking of shipments (ST23). */
  updateTracking(
    body?: ST23Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST23Response200> {
    return this.call(sT23, body, { ...params }, options);
  }

  /** Confirm that shipments have shipped (ST24). */
  ship(body?: ST24Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<ST24Response200> {
    return this.call(sT24, body, { ...params }, options);
  }

  /** Mark shipments as ready to pick up (ST26). */
  markReadyForPickUp(
    body?: ST26Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST26Response200> {
    return this.call(sT26, body, { ...params }, options);
  }

  /** Update the additional information of shipments (ST31). */
  updateAdditionalInformation(
    body?: ST31Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST31Response200> {
    return this.call(sT31, body, { ...params }, options);
  }

  /** Calculate shipping label rates (ST41). */
  calculateLabelRates(
    body?: ST41Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST41Response200> {
    return this.call(sT41, body, { ...params }, options);
  }

  /** List one page of shipping label rates (ST42). */
  listLabelRates(
    params: {
      shipmentId?: Array<string>;
      labelRateState?: Array<'PENDING' | 'CREATED' | 'FAILED'>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ST42Response200> {
    return this.call(sT42, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterLabelRates(
    params: {
      shipmentId?: Array<string>;
      labelRateState?: Array<'PENDING' | 'CREATED' | 'FAILED'>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ST42Response200Data, void, undefined> {
    return this.paginate(sT42, undefined, { ...params }, options);
  }

  /** Create shipping labels (ST51). */
  createLabels(
    body?: ST51Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<ST51Response200> {
    return this.call(sT51, body, { ...params }, options);
  }

  /** List one page of shipping labels (ST52). */
  listLabels(
    params: {
      shipmentId?: Array<string>;
      labelState?: Array<'PENDING' | 'CREATED' | 'FAILED'>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ST52Response200> {
    return this.call(sT52, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterLabels(
    params: {
      shipmentId?: Array<string>;
      labelState?: Array<'PENDING' | 'CREATED' | 'FAILED'>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ST52Response200Data, void, undefined> {
    return this.paginate(sT52, undefined, { ...params }, options);
  }
}
