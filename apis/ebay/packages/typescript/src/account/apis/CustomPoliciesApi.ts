// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CustomPolicy,
  CustomPolicyCreateRequest,
  CustomPolicyRequest,
  CustomPolicyResponse,
  GetCustomPolicies429Response,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createCustomPolicy: Operation = {
  id: 'createCustomPolicy',
  method: 'POST',
  path: '/sell/account/v1/custom_policy/',
  resource: 'customPolicies',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getCustomPolicies: Operation = {
  id: 'getCustomPolicies',
  method: 'GET',
  path: '/sell/account/v1/custom_policy/',
  resource: 'customPolicies',
  name: 'list',
  host: 'api',
  params: [{ wire: 'policy_types', name: 'policyTypes', location: 'query' }],
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

const getCustomPolicy: Operation = {
  id: 'getCustomPolicy',
  method: 'GET',
  path: '/sell/account/v1/custom_policy/{custom_policy_id}',
  resource: 'customPolicies',
  name: 'get',
  host: 'api',
  params: [{ wire: 'custom_policy_id', name: 'customPolicyId', location: 'path' }],
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

const updateCustomPolicy: Operation = {
  id: 'updateCustomPolicy',
  method: 'PUT',
  path: '/sell/account/v1/custom_policy/{custom_policy_id}',
  resource: 'customPolicies',
  name: 'update',
  host: 'api',
  params: [{ wire: 'custom_policy_id', name: 'customPolicyId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createCustomPolicy,
  getCustomPolicies,
  getCustomPolicy,
  updateCustomPolicy,
];

export class CustomPoliciesApi extends Resource {
  /** Create a custom policy. */
  create(body: CustomPolicyCreateRequest, options?: RequestOptions): Promise<object> {
    return this.call(createCustomPolicy, body, {}, options);
  }

  /** List the seller's custom policies. */
  list(params: { policyTypes?: string } = {}, options?: RequestOptions): Promise<CustomPolicyResponse> {
    return this.call(getCustomPolicies, undefined, { ...params }, options);
  }

  /** Get one custom policy. */
  get(customPolicyId: string, options?: RequestOptions): Promise<CustomPolicy> {
    return this.call(getCustomPolicy, undefined, { customPolicyId }, options);
  }

  /** Update a custom policy. */
  update(customPolicyId: string, body: CustomPolicyRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateCustomPolicy, body, { customPolicyId }, options);
  }
}
