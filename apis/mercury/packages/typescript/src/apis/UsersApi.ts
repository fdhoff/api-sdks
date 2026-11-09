// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { UserDetails, UsersPaginatedResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getUser: Operation = {
  id: 'getUser',
  method: 'GET',
  path: '/users/{userId}',
  resource: 'users',
  name: 'get',
  host: 'api',
  params: [{ wire: 'userId', name: 'userId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getUsers: Operation = {
  id: 'getUsers',
  method: 'GET',
  path: '/users',
  resource: 'users',
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
  paging: { style: 'cursor', items: 'users', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getUser, getUsers];

export class UsersApi extends Resource {
  /** Get one user. */
  get(userId: string, options?: RequestOptions): Promise<UserDetails> {
    return this.call(getUser, undefined, { userId }, options);
  }

  /** List one page of your organization's users. */
  list(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<UsersPaginatedResponse> {
    return this.call(getUsers, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.UserDetails, void, undefined> {
    return this.paginate(getUsers, undefined, { ...params }, options);
  }
}
