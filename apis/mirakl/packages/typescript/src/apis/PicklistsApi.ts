// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { PL11Response200 } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const pL11: Operation = {
  id: 'PL11',
  method: 'GET',
  path: '/api/picklists',
  resource: 'picklists',
  name: 'list',
  params: [
    { wire: 'pickrun_code', name: 'pickrunCode', location: 'query' },
    { wire: 'pickup_date_min', name: 'pickupDateMin', location: 'query' },
    { wire: 'pickup_date_max', name: 'pickupDateMax', location: 'query' },
    { wire: 'picklist_id', name: 'picklistId', location: 'query' },
    { wire: 'picklist_state', name: 'picklistState', location: 'query' },
    { wire: 'order_line_id', name: 'orderLineId', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PICKLIST_READ'] }]],
};

export const OPERATIONS: readonly Operation[] = [pL11];

export class PicklistsApi extends Resource {
  /** List one page of picklists (PL11). */
  list(
    params: {
      pickrunCode?: string;
      pickupDateMin?: string;
      pickupDateMax?: string;
      picklistId?: Array<string>;
      picklistState?: Array<string>;
      orderLineId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<PL11Response200> {
    return this.call(pL11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      pickrunCode?: string;
      pickupDateMin?: string;
      pickupDateMax?: string;
      picklistId?: Array<string>;
      picklistState?: Array<string>;
      orderLineId?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PL11Response200Data, void, undefined> {
    return this.paginate(pL11, undefined, { ...params }, options);
  }
}
