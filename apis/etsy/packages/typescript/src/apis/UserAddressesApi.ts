// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, UserAddress, UserAddresses } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getUserAddress: Operation = {
  id: 'getUserAddress',
  method: 'GET',
  path: '/v3/application/user/addresses/{user_address_id}',
  resource: 'userAddresses',
  name: 'get',
  params: [{ wire: 'user_address_id', name: 'userAddressId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['address_r'] },
    ],
  ],
};

const getUserAddresses: Operation = {
  id: 'getUserAddresses',
  method: 'GET',
  path: '/v3/application/user/addresses',
  resource: 'userAddresses',
  name: 'list',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['address_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getUserAddress, getUserAddresses];

export class UserAddressesApi extends Resource {
  /** Get one of the user's addresses. */
  get(userAddressId: number, options?: RequestOptions): Promise<UserAddress> {
    return this.call(getUserAddress, undefined, { userAddressId }, options);
  }

  /** List one page of the user's addresses. */
  list(params: { limit?: number; offset?: number } = {}, options?: RequestOptions): Promise<UserAddresses> {
    return this.call(getUserAddresses, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; offset?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.UserAddress, void, undefined> {
    return this.paginate(getUserAddresses, undefined, { ...params }, options);
  }
}
