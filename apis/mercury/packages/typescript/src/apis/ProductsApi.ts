// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiV1ArProductCreateRequest,
  ApiV1ArProductPaginatedResponseData,
  ApiV1ArProductResponseData,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createProduct: Operation = {
  id: 'createProduct',
  method: 'POST',
  path: '/ar/products',
  resource: 'products',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listProducts: Operation = {
  id: 'listProducts',
  method: 'GET',
  path: '/ar/products',
  resource: 'products',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'products', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [createProduct, listProducts];

export class ProductsApi extends Resource {
  /** Create an invoicing product. */
  create(body?: ApiV1ArProductCreateRequest, options?: RequestOptions): Promise<ApiV1ArProductResponseData> {
    return this.call(createProduct, body, {}, options);
  }

  /** List one page of invoicing products. */
  list(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1ArProductPaginatedResponseData> {
    return this.call(listProducts, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1ArProductResponseData, void, undefined> {
    return this.paginate(listProducts, undefined, { ...params }, options);
  }
}
