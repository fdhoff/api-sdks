// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  RT01Request,
  RT01Response200,
  RT04Request,
  RT04Response200,
  RT11Response200,
  RT12Response200,
  RT21Request,
  RT21Response200,
  RT25Request,
  RT25Response200,
  RT26Request,
  RT26Response200,
  RT27Request,
  RT27Response200,
  RT29Request,
  RT29Response200,
  RT51Request,
  RT51Response200,
  RT52Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const rT01: Operation = {
  id: 'RT01',
  method: 'POST',
  path: '/api/returns',
  resource: 'returns',
  name: 'create',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_ORDER_RETURN_WRITE', 'ROLE_SHOP_ADMIN'] }]],
};

const rT04: Operation = {
  id: 'RT04',
  method: 'PUT',
  path: '/api/returns',
  resource: 'returns',
  name: 'update',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT11: Operation = {
  id: 'RT11',
  method: 'GET',
  path: '/api/returns',
  resource: 'returns',
  name: 'list',
  params: [
    { wire: 'return_id', name: 'returnId', location: 'query' },
    { wire: 'return_state', name: 'returnState', location: 'query' },
    { wire: 'return_creation_date_from', name: 'returnCreationDateFrom', location: 'query' },
    { wire: 'return_creation_date_to', name: 'returnCreationDateTo', location: 'query' },
    { wire: 'return_last_updated_from', name: 'returnLastUpdatedFrom', location: 'query' },
    { wire: 'return_last_updated_to', name: 'returnLastUpdatedTo', location: 'query' },
    { wire: 'order_commercial_id', name: 'orderCommercialId', location: 'query' },
    { wire: 'order_line_id', name: 'orderLineId', location: 'query' },
    { wire: 'return_rma', name: 'returnRma', location: 'query' },
    { wire: 'customer_id', name: 'customerId', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_ORDER_RETURN_READ', 'ROLE_SHOP_ADMIN'] }]],
};

const rT12: Operation = {
  id: 'RT12',
  method: 'GET',
  path: '/api/returns/items_to_return',
  resource: 'returns',
  name: 'listItemsToReturn',
  params: [
    { wire: 'order_commercial_id', name: 'orderCommercialId', location: 'query' },
    { wire: 'order_line_id', name: 'orderLineId', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterItemsToReturn',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_ORDER_RETURN_READ', 'ROLE_SHOP_ADMIN'] }]],
};

const rT21: Operation = {
  id: 'RT21',
  method: 'PUT',
  path: '/api/returns/accept',
  resource: 'returns',
  name: 'accept',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT25: Operation = {
  id: 'RT25',
  method: 'PUT',
  path: '/api/returns/receive',
  resource: 'returns',
  name: 'receive',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_ORDER_RETURN_WRITE', 'ROLE_SHOP_ADMIN'] }]],
};

const rT26: Operation = {
  id: 'RT26',
  method: 'PUT',
  path: '/api/returns/compliance',
  resource: 'returns',
  name: 'setCompliance',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT27: Operation = {
  id: 'RT27',
  method: 'PUT',
  path: '/api/returns/close',
  resource: 'returns',
  name: 'close',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT29: Operation = {
  id: 'RT29',
  method: 'PUT',
  path: '/api/returns/cancel',
  resource: 'returns',
  name: 'cancel',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT51: Operation = {
  id: 'RT51',
  method: 'POST',
  path: '/api/returns/return-labels',
  resource: 'returns',
  name: 'createLabels',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_WRITE'] }]],
};

const rT52: Operation = {
  id: 'RT52',
  method: 'GET',
  path: '/api/returns/return-labels',
  resource: 'returns',
  name: 'listLabels',
  params: [
    { wire: 'return_id', name: 'returnId', location: 'query' },
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
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_RETURN_READ'] }]],
};

export const OPERATIONS: readonly Operation[] = [rT01, rT04, rT11, rT12, rT21, rT25, rT26, rT27, rT29, rT51, rT52];

export class ReturnsApi extends Resource {
  /** Create returns (RT01). */
  create(body?: RT01Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT01Response200> {
    return this.call(rT01, body, { ...params }, options);
  }

  /** Update fields on several returns (RT04). */
  update(body?: RT04Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT04Response200> {
    return this.call(rT04, body, { ...params }, options);
  }

  /** List one page of returns (RT11). */
  list(
    params: {
      returnId?: Array<string>;
      returnState?: Array<string>;
      returnCreationDateFrom?: string;
      returnCreationDateTo?: string;
      returnLastUpdatedFrom?: string;
      returnLastUpdatedTo?: string;
      orderCommercialId?: Array<string>;
      orderLineId?: Array<string>;
      returnRma?: Array<string>;
      customerId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<RT11Response200> {
    return this.call(rT11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      returnId?: Array<string>;
      returnState?: Array<string>;
      returnCreationDateFrom?: string;
      returnCreationDateTo?: string;
      returnLastUpdatedFrom?: string;
      returnLastUpdatedTo?: string;
      orderCommercialId?: Array<string>;
      orderLineId?: Array<string>;
      returnRma?: Array<string>;
      customerId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.RT11Response200Data, void, undefined> {
    return this.paginate(rT11, undefined, { ...params }, options);
  }

  /** List one page of items to return (RT12). */
  listItemsToReturn(
    params: {
      orderCommercialId?: Array<string>;
      orderLineId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<RT12Response200> {
    return this.call(rT12, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterItemsToReturn(
    params: {
      orderCommercialId?: Array<string>;
      orderLineId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.RT12Response200Data, void, undefined> {
    return this.paginate(rT12, undefined, { ...params }, options);
  }

  /** Accept or refuse return requests (RT21). */
  accept(body?: RT21Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT21Response200> {
    return this.call(rT21, body, { ...params }, options);
  }

  /** Confirm that returns were received (RT25). */
  receive(body?: RT25Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT25Response200> {
    return this.call(rT25, body, { ...params }, options);
  }

  /** Mark returns as compliant or not (RT26). */
  setCompliance(
    body?: RT26Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<RT26Response200> {
    return this.call(rT26, body, { ...params }, options);
  }

  /** Close returns (RT27). */
  close(body?: RT27Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT27Response200> {
    return this.call(rT27, body, { ...params }, options);
  }

  /** Cancel returns (RT29). */
  cancel(body?: RT29Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<RT29Response200> {
    return this.call(rT29, body, { ...params }, options);
  }

  /** Create return labels (RT51). */
  createLabels(
    body?: RT51Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<RT51Response200> {
    return this.call(rT51, body, { ...params }, options);
  }

  /** List one page of return labels (RT52). */
  listLabels(
    params: {
      returnId?: Array<string>;
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
  ): Promise<RT52Response200> {
    return this.call(rT52, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterLabels(
    params: {
      returnId?: Array<string>;
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
  ): AsyncGenerator<models.RT52Response200Data, void, undefined> {
    return this.paginate(rT52, undefined, { ...params }, options);
  }
}
