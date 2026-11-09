// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, SellingPrivileges } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPrivileges: Operation = {
  id: 'getPrivileges',
  method: 'GET',
  path: '/sell/account/v1/privilege',
  resource: 'privileges',
  name: 'get',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.account',
          'https://api.ebay.com/oauth/api_scope/sell.account.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getPrivileges];

export class PrivilegesApi extends Resource {
  /** Get the seller's selling limits and registration status. */
  get(options?: RequestOptions): Promise<SellingPrivileges> {
    return this.call(getPrivileges, undefined, {}, options);
  }
}
