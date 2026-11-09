// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiV1ArCustomerCreateRequest,
  ApiV1ArCustomerPaginatedResponseData,
  ApiV1ArCustomerResponseData,
  ApiV1ArCustomerUpdateRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createCustomer: Operation = {
  id: 'createCustomer',
  method: 'POST',
  path: '/ar/customers',
  resource: 'customers',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const deleteCustomer: Operation = {
  id: 'deleteCustomer',
  method: 'DELETE',
  path: '/ar/customers/{customerId}',
  resource: 'customers',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'customerId', name: 'customerId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getCustomer: Operation = {
  id: 'getCustomer',
  method: 'GET',
  path: '/ar/customers/{customerId}',
  resource: 'customers',
  name: 'get',
  host: 'api',
  params: [{ wire: 'customerId', name: 'customerId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listCustomers: Operation = {
  id: 'listCustomers',
  method: 'GET',
  path: '/ar/customers',
  resource: 'customers',
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
  paging: { style: 'cursor', items: 'customers', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateCustomer: Operation = {
  id: 'updateCustomer',
  method: 'POST',
  path: '/ar/customers/{customerId}',
  resource: 'customers',
  name: 'update',
  host: 'api',
  params: [{ wire: 'customerId', name: 'customerId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createCustomer,
  deleteCustomer,
  getCustomer,
  listCustomers,
  updateCustomer,
];

export class CustomersApi extends Resource {
  /** Create an invoicing customer. */
  create(body?: ApiV1ArCustomerCreateRequest, options?: RequestOptions): Promise<ApiV1ArCustomerResponseData> {
    return this.call(createCustomer, body, {}, options);
  }

  /** Delete an invoicing customer. */
  delete(customerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteCustomer, undefined, { customerId }, options);
  }

  /** Get one invoicing customer. */
  get(customerId: string, options?: RequestOptions): Promise<ApiV1ArCustomerResponseData> {
    return this.call(getCustomer, undefined, { customerId }, options);
  }

  /** List one page of invoicing customers. */
  list(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1ArCustomerPaginatedResponseData> {
    return this.call(listCustomers, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1ArCustomerResponseData, void, undefined> {
    return this.paginate(listCustomers, undefined, { ...params }, options);
  }

  /** Update an invoicing customer. */
  update(
    customerId: string,
    body?: ApiV1ArCustomerUpdateRequest,
    options?: RequestOptions,
  ): Promise<ApiV1ArCustomerResponseData> {
    return this.call(updateCustomer, body, { customerId }, options);
  }
}
