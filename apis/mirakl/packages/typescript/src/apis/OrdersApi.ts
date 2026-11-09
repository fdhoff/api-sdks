// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  OR04Request,
  OR04Response200,
  OR07Request,
  OR07Response200,
  OR11Response200,
  OR13Request,
  OR13Response200,
  OR14Response200,
  OR21Request,
  OR23Request,
  OR28Request,
  OR28Response200,
  OR30Request,
  OR30Response200,
  OR31Request,
  OR31Response200,
  OR32Request,
  OR32Response200,
  OR33Request,
  OR43RequestMultipartFormDataThreadInput,
  OR43Response201,
  OR51Response200,
  OR64Request,
  OR72Response200,
  OR74RequestMultipartFormDataOrderDocuments,
  OR74Response200,
  OR75Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const oR04: Operation = {
  id: 'OR04',
  method: 'PUT',
  path: '/api/orders',
  resource: 'orders',
  name: 'update',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_EDIT'] }]],
};

const oR07: Operation = {
  id: 'OR07',
  method: 'PUT',
  path: '/api/orders/shipping_from',
  resource: 'orders',
  name: 'updateShippingOrigin',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIP'] }]],
};

const oR11: Operation = {
  id: 'OR11',
  method: 'GET',
  path: '/api/orders',
  resource: 'orders',
  name: 'list',
  params: [
    { wire: 'order_ids', name: 'orderIds', location: 'query' },
    { wire: 'order_references_for_customer', name: 'orderReferencesForCustomer', location: 'query' },
    { wire: 'order_references_for_seller', name: 'orderReferencesForSeller', location: 'query' },
    { wire: 'order_state_codes', name: 'orderStateCodes', location: 'query' },
    { wire: 'channel_codes', name: 'channelCodes', location: 'query' },
    { wire: 'only_null_channel', name: 'onlyNullChannel', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'start_update_date', name: 'startUpdateDate', location: 'query' },
    { wire: 'end_update_date', name: 'endUpdateDate', location: 'query' },
    { wire: 'customer_debited', name: 'customerDebited', location: 'query' },
    { wire: 'payment_workflow', name: 'paymentWorkflow', location: 'query' },
    { wire: 'has_incident', name: 'hasIncident', location: 'query' },
    { wire: 'fulfillment_center_code', name: 'fulfillmentCenterCode', location: 'query' },
    { wire: 'order_tax_mode', name: 'orderTaxMode', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'orders', total: 'total_count', offset: 'offset' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_READ'] }]],
};

const oR13: Operation = {
  id: 'OR13',
  method: 'POST',
  path: '/api/orders/async-export',
  resource: 'orders',
  name: 'export',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_READ'] }]],
};

const oR14: Operation = {
  id: 'OR14',
  method: 'GET',
  path: '/api/orders/async-export/status/{tracking_id}',
  resource: 'orders',
  name: 'getExport',
  params: [
    { wire: 'tracking_id', name: 'trackingId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'status', done: ['COMPLETED'], failed: ['FAILED'] },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_READ'] }]],
};

const oR21: Operation = {
  id: 'OR21',
  method: 'PUT',
  path: '/api/orders/{order_id}/accept',
  resource: 'orders',
  name: 'accept',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_ACCEPT'] }]],
};

const oR23: Operation = {
  id: 'OR23',
  method: 'PUT',
  path: '/api/orders/{order_id}/tracking',
  resource: 'orders',
  name: 'updateTracking',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_TRACKING_WRITE'] }]],
};

const oR24: Operation = {
  id: 'OR24',
  method: 'PUT',
  path: '/api/orders/{order_id}/ship',
  resource: 'orders',
  name: 'ship',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SHIP'] }]],
};

const oR28: Operation = {
  id: 'OR28',
  method: 'PUT',
  path: '/api/orders/refund',
  resource: 'orders',
  name: 'refund',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_REFUND_REQUEST', 'ROLE_PARTNER_ORDER_REFUND'],
      },
    ],
  ],
};

const oR29: Operation = {
  id: 'OR29',
  method: 'PUT',
  path: '/api/orders/{order_id}/cancel',
  resource: 'orders',
  name: 'cancel',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_CANCEL'] }]],
};

const oR30: Operation = {
  id: 'OR30',
  method: 'PUT',
  path: '/api/orders/cancel',
  resource: 'orders',
  name: 'cancelLines',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_CANCEL'] }]],
};

const oR31: Operation = {
  id: 'OR31',
  method: 'PUT',
  path: '/api/orders/{order_id}/additional_fields',
  resource: 'orders',
  name: 'updateCustomFields',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_ADDITIONAL_FIELD_UPDATE'] }]],
};

const oR32: Operation = {
  id: 'OR32',
  method: 'PUT',
  path: '/api/orders/adjust',
  resource: 'orders',
  name: 'adjustLines',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_ADJUST'] }]],
};

const oR33: Operation = {
  id: 'OR33',
  method: 'PUT',
  path: '/api/orders/{order_id}/cancel-order-lines',
  resource: 'orders',
  name: 'fullyCancelLines',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_CANCEL'] }]],
};

const oR43: Operation = {
  id: 'OR43',
  method: 'POST',
  path: '/api/orders/{order_id}/threads',
  resource: 'orders',
  name: 'createThread',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'files', name: 'files', location: 'form' },
    { wire: 'thread_input', name: 'threadInput', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_MESSAGE_WRITE'] }]],
};

const oR51: Operation = {
  id: 'OR51',
  method: 'GET',
  path: '/api/orders/{order_id}/evaluation',
  resource: 'orders',
  name: 'getEvaluation',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_EVALUATION_READ'] }]],
};

const oR64: Operation = {
  id: 'OR64',
  method: 'PUT',
  path: '/api/orders/{order_id}/lines/{line}/resolve_incident',
  resource: 'orders',
  name: 'resolveIncident',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'line', name: 'line', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_INCIDENT_RESOLVE'] }]],
};

const oR72: Operation = {
  id: 'OR72',
  method: 'GET',
  path: '/api/orders/documents',
  resource: 'orders',
  name: 'listDocuments',
  params: [
    { wire: 'order_ids', name: 'orderIds', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_DOCUMENT_READ'] }]],
};

const oR73: Operation = {
  id: 'OR73',
  method: 'GET',
  path: '/api/orders/documents/download',
  resource: 'orders',
  name: 'downloadDocuments',
  params: [
    { wire: 'order_ids', name: 'orderIds', location: 'query' },
    { wire: 'document_ids', name: 'documentIds', location: 'query' },
    { wire: 'document_codes', name: 'documentCodes', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_DOCUMENT_READ'] }]],
};

const oR74: Operation = {
  id: 'OR74',
  method: 'POST',
  path: '/api/orders/{order_id}/documents',
  resource: 'orders',
  name: 'uploadDocuments',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'files', name: 'files', location: 'form' },
    { wire: 'order_documents', name: 'orderDocuments', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_DOCUMENT_WRITE'] }]],
};

const oR75: Operation = {
  id: 'OR75',
  method: 'GET',
  path: '/api/orders/taxes',
  resource: 'orders',
  name: 'listTaxes',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SETTINGS_READ'] }]],
};

const oR76: Operation = {
  id: 'OR76',
  method: 'DELETE',
  path: '/api/orders/documents/{document_id}',
  resource: 'orders',
  name: 'deleteDocument',
  params: [
    { wire: 'document_id', name: 'documentId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_DOCUMENT_DELETE'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  oR04,
  oR07,
  oR11,
  oR13,
  oR14,
  oR21,
  oR23,
  oR24,
  oR28,
  oR29,
  oR30,
  oR31,
  oR32,
  oR33,
  oR43,
  oR51,
  oR64,
  oR72,
  oR73,
  oR74,
  oR75,
  oR76,
];

export class OrdersApi extends Resource {
  /** Update fields on several orders (OR04). */
  update(body?: OR04Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR04Response200> {
    return this.call(oR04, body, { ...params }, options);
  }

  /** Update the shipping origin of order lines (OR07). */
  updateShippingOrigin(
    body?: OR07Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<OR07Response200> {
    return this.call(oR07, body, { ...params }, options);
  }

  /** List one page of orders (OR11). */
  list(
    params: {
      orderIds?: string;
      orderReferencesForCustomer?: string;
      orderReferencesForSeller?: string;
      orderStateCodes?:
        | 'STAGING'
        | 'WAITING_ACCEPTANCE'
        | 'WAITING_DEBIT'
        | 'WAITING_DEBIT_PAYMENT'
        | 'SHIPPING'
        | 'SHIPPED'
        | 'TO_COLLECT'
        | 'RECEIVED'
        | 'CLOSED'
        | 'REFUSED'
        | 'CANCELED';
      channelCodes?: string;
      onlyNullChannel?: boolean;
      startDate?: string;
      endDate?: string;
      startUpdateDate?: string;
      endUpdateDate?: string;
      customerDebited?: boolean;
      paymentWorkflow?:
        | 'PAY_ON_ACCEPTANCE'
        | 'PAY_ON_DELIVERY'
        | 'PAY_ON_DUE_DATE'
        | 'PAY_ON_SHIPMENT'
        | 'NO_CUSTOMER_PAYMENT_CONFIRMATION';
      hasIncident?: boolean;
      fulfillmentCenterCode?: Array<string>;
      orderTaxMode?: 'TAX_INCLUDED' | 'TAX_EXCLUDED';
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<OR11Response200> {
    return this.call(oR11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      orderIds?: string;
      orderReferencesForCustomer?: string;
      orderReferencesForSeller?: string;
      orderStateCodes?:
        | 'STAGING'
        | 'WAITING_ACCEPTANCE'
        | 'WAITING_DEBIT'
        | 'WAITING_DEBIT_PAYMENT'
        | 'SHIPPING'
        | 'SHIPPED'
        | 'TO_COLLECT'
        | 'RECEIVED'
        | 'CLOSED'
        | 'REFUSED'
        | 'CANCELED';
      channelCodes?: string;
      onlyNullChannel?: boolean;
      startDate?: string;
      endDate?: string;
      startUpdateDate?: string;
      endUpdateDate?: string;
      customerDebited?: boolean;
      paymentWorkflow?:
        | 'PAY_ON_ACCEPTANCE'
        | 'PAY_ON_DELIVERY'
        | 'PAY_ON_DUE_DATE'
        | 'PAY_ON_SHIPMENT'
        | 'NO_CUSTOMER_PAYMENT_CONFIRMATION';
      hasIncident?: boolean;
      fulfillmentCenterCode?: Array<string>;
      orderTaxMode?: 'TAX_INCLUDED' | 'TAX_EXCLUDED';
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OR11Response200Orders, void, undefined> {
    return this.paginate(oR11, undefined, { ...params }, options);
  }

  /** Start an export of orders as JSON files (OR13). */
  export(body?: OR13Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR13Response200> {
    return this.call(oR13, body, { ...params }, options);
  }

  /** Get the status of an order export (OR14). */
  getExport(trackingId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR14Response200> {
    return this.call(oR14, undefined, { trackingId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `export` started ends, and return its last status, done or
   * failed. Pass the `tracking_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForExport(trackingId: string, options?: import('../runtime/index.js').WaitOptions): Promise<OR14Response200> {
    return this.pollJob(oR14, { trackingId }, options);
  }

  /** Accept or refuse an order's lines (OR21). */
  accept(
    orderId: string,
    body?: OR21Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(oR21, body, { orderId, ...params }, options);
  }

  /** Update an order's carrier tracking (OR23). */
  updateTracking(
    orderId: string,
    body?: OR23Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(oR23, body, { orderId, ...params }, options);
  }

  /** Confirm that an order has shipped (OR24). */
  ship(orderId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(oR24, undefined, { orderId, ...params }, options);
  }

  /** Refund order lines (OR28). */
  refund(body?: OR28Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR28Response200> {
    return this.call(oR28, body, { ...params }, options);
  }

  /** Cancel a whole order (OR29). */
  cancel(orderId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(oR29, undefined, { orderId, ...params }, options);
  }

  /** Cancel quantities or amounts on order lines (OR30). */
  cancelLines(
    body?: OR30Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<OR30Response200> {
    return this.call(oR30, body, { ...params }, options);
  }

  /** Update the custom fields of an order and its lines (OR31). */
  updateCustomFields(
    orderId: string,
    body?: OR31Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<OR31Response200> {
    return this.call(oR31, body, { orderId, ...params }, options);
  }

  /** Adjust order lines (OR32). */
  adjustLines(
    body?: OR32Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<OR32Response200> {
    return this.call(oR32, body, { ...params }, options);
  }

  /** Fully cancel some of an order's lines (OR33). */
  fullyCancelLines(
    orderId: string,
    body?: OR33Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(oR33, body, { orderId, ...params }, options);
  }

  /** Start a message thread on an order (OR43). */
  createThread(
    orderId: string,
    params: { shopId?: number; files?: FileInput[]; threadInput: OR43RequestMultipartFormDataThreadInput },
    options?: RequestOptions,
  ): Promise<OR43Response201> {
    return this.call(oR43, undefined, { orderId, ...params }, options);
  }

  /** Get an order's evaluation (OR51). */
  getEvaluation(orderId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR51Response200> {
    return this.call(oR51, undefined, { orderId, ...params }, options);
  }

  /** Mark an order line's incident as resolved (OR64). */
  resolveIncident(
    orderId: string,
    line: string,
    body?: OR64Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(oR64, body, { orderId, line, ...params }, options);
  }

  /** List the documents on orders (OR72). */
  listDocuments(params: { orderIds: string; shopId?: number }, options?: RequestOptions): Promise<OR72Response200> {
    return this.call(oR72, undefined, { ...params }, options);
  }

  /** Download one or more order documents (OR73). */
  downloadDocuments(
    params: { orderIds?: string; documentIds?: string; documentCodes?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(oR73, undefined, { ...params }, options);
  }

  /** Upload documents to an order (OR74). */
  uploadDocuments(
    orderId: string,
    params: { shopId?: number; files: FileInput[]; orderDocuments: OR74RequestMultipartFormDataOrderDocuments },
    options?: RequestOptions,
  ): Promise<OR74Response200> {
    return this.call(oR74, undefined, { orderId, ...params }, options);
  }

  /** List the order taxes the platform uses (OR75). */
  listTaxes(params: { shopId?: number } = {}, options?: RequestOptions): Promise<OR75Response200> {
    return this.call(oR75, undefined, { ...params }, options);
  }

  /** Delete an order document (OR76). */
  deleteDocument(documentId: number, params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(oR76, undefined, { documentId, ...params }, options);
  }
}
