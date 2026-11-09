// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetCustomPolicies429Response,
  ReturnPolicy,
  ReturnPolicyRequest,
  ReturnPolicyResponse,
  SetReturnPolicyResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createReturnPolicy: Operation = {
  id: 'createReturnPolicy',
  method: 'POST',
  path: '/sell/account/v1/return_policy',
  resource: 'returnPolicies',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const deleteReturnPolicy: Operation = {
  id: 'deleteReturnPolicy',
  method: 'DELETE',
  path: '/sell/account/v1/return_policy/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getReturnPolicies: Operation = {
  id: 'getReturnPolicies',
  method: 'GET',
  path: '/sell/account/v1/return_policy',
  resource: 'returnPolicies',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'query' },
    { wire: 'Content-Language', name: 'contentLanguage', location: 'header' },
  ],
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

const getReturnPolicy: Operation = {
  id: 'getReturnPolicy',
  method: 'GET',
  path: '/sell/account/v1/return_policy/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'get',
  host: 'api',
  params: [{ wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' }],
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

const getReturnPolicyByName: Operation = {
  id: 'getReturnPolicyByName',
  method: 'GET',
  path: '/sell/account/v1/return_policy/get_by_policy_name',
  resource: 'returnPolicies',
  name: 'getByName',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'query' },
    { wire: 'name', name: 'name', location: 'query' },
    { wire: 'Content-Language', name: 'contentLanguage', location: 'header' },
  ],
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

const updateReturnPolicy: Operation = {
  id: 'updateReturnPolicy',
  method: 'PUT',
  path: '/sell/account/v1/return_policy/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'update',
  host: 'api',
  params: [{ wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createReturnPolicy,
  deleteReturnPolicy,
  getReturnPolicies,
  getReturnPolicy,
  getReturnPolicyByName,
  updateReturnPolicy,
];

export class ReturnPoliciesApi extends Resource {
  /** Create a return policy. */
  create(body: ReturnPolicyRequest, options?: RequestOptions): Promise<SetReturnPolicyResponse> {
    return this.call(createReturnPolicy, body, {}, options);
  }

  /** Delete a return policy. */
  delete(returnPolicyId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteReturnPolicy, undefined, { returnPolicyId }, options);
  }

  /** List the seller's return policies on a marketplace. */
  list(
    params: { marketplaceId: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<ReturnPolicyResponse> {
    return this.call(getReturnPolicies, undefined, { ...params }, options);
  }

  /** Get one return policy. */
  get(returnPolicyId: string, options?: RequestOptions): Promise<ReturnPolicy> {
    return this.call(getReturnPolicy, undefined, { returnPolicyId }, options);
  }

  /** Get a return policy by its name. */
  getByName(
    params: { marketplaceId: string; name: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<ReturnPolicy> {
    return this.call(getReturnPolicyByName, undefined, { ...params }, options);
  }

  /** Replace a return policy. */
  update(
    returnPolicyId: string,
    body: ReturnPolicyRequest,
    options?: RequestOptions,
  ): Promise<SetReturnPolicyResponse> {
    return this.call(updateReturnPolicy, body, { returnPolicyId }, options);
  }
}
