// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetUser429Response, UserResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getUser: Operation = {
  id: 'getUser',
  method: 'GET',
  path: '/commerce/identity/v1/user/',
  resource: 'user',
  name: 'get',
  host: 'apiz',
  params: [],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/commerce.identity.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.identity.name.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.identity.address.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.identity.email.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.identity.phone.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getUser];

export class UserApi extends Resource {
  /** Get the account details of the user the token belongs to. */
  get(options?: RequestOptions): Promise<UserResponse> {
    return this.call(getUser, undefined, {}, options);
  }
}
