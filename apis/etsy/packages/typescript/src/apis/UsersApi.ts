// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, Me, User } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getMe: Operation = {
  id: 'getMe',
  method: 'GET',
  path: '/v3/application/users/me',
  resource: 'users',
  name: 'getMe',
  params: [],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const getUser: Operation = {
  id: 'getUser',
  method: 'GET',
  path: '/v3/application/users/{user_id}',
  resource: 'users',
  name: 'get',
  params: [{ wire: 'user_id', name: 'userId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['email_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getMe, getUser];

export class UsersApi extends Resource {
  /** Get the user and shop IDs the access token belongs to. */
  getMe(options?: RequestOptions): Promise<Me> {
    return this.call(getMe, undefined, {}, options);
  }

  /** Get one user. */
  get(userId: number, options?: RequestOptions): Promise<User> {
    return this.call(getUser, undefined, { userId }, options);
  }
}
