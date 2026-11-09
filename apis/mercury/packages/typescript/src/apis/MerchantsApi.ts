// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { MerchantsResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const listMerchants: Operation = {
  id: 'listMerchants',
  method: 'GET',
  path: '/merchants',
  resource: 'merchants',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'search', name: 'search', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'data', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [listMerchants];

export class MerchantsApi extends Resource {
  /** List one page of merchants you have paid. */
  list(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string; search?: string } = {},
    options?: RequestOptions,
  ): Promise<MerchantsResponse> {
    return this.call(listMerchants, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string; search?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.MerchantInfo, void, undefined> {
    return this.paginate(listMerchants, undefined, { ...params }, options);
  }
}
