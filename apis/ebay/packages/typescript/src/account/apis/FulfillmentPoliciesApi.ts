// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  FulfillmentPolicy,
  FulfillmentPolicyRequest,
  FulfillmentPolicyResponse,
  GetCustomPolicies429Response,
  SetFulfillmentPolicyResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createFulfillmentPolicy: Operation = {
  id: 'createFulfillmentPolicy',
  method: 'POST',
  path: '/sell/account/v1/fulfillment_policy/',
  resource: 'fulfillmentPolicies',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const deleteFulfillmentPolicy: Operation = {
  id: 'deleteFulfillmentPolicy',
  method: 'DELETE',
  path: '/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}',
  resource: 'fulfillmentPolicies',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'fulfillmentPolicyId', name: 'fulfillmentPolicyId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getFulfillmentPolicies: Operation = {
  id: 'getFulfillmentPolicies',
  method: 'GET',
  path: '/sell/account/v1/fulfillment_policy',
  resource: 'fulfillmentPolicies',
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

const getFulfillmentPolicy: Operation = {
  id: 'getFulfillmentPolicy',
  method: 'GET',
  path: '/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}',
  resource: 'fulfillmentPolicies',
  name: 'get',
  host: 'api',
  params: [{ wire: 'fulfillmentPolicyId', name: 'fulfillmentPolicyId', location: 'path' }],
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

const getFulfillmentPolicyByName: Operation = {
  id: 'getFulfillmentPolicyByName',
  method: 'GET',
  path: '/sell/account/v1/fulfillment_policy/get_by_policy_name',
  resource: 'fulfillmentPolicies',
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

const updateFulfillmentPolicy: Operation = {
  id: 'updateFulfillmentPolicy',
  method: 'PUT',
  path: '/sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}',
  resource: 'fulfillmentPolicies',
  name: 'update',
  host: 'api',
  params: [{ wire: 'fulfillmentPolicyId', name: 'fulfillmentPolicyId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createFulfillmentPolicy,
  deleteFulfillmentPolicy,
  getFulfillmentPolicies,
  getFulfillmentPolicy,
  getFulfillmentPolicyByName,
  updateFulfillmentPolicy,
];

export class FulfillmentPoliciesApi extends Resource {
  /** Create a fulfillment policy. */
  create(body: FulfillmentPolicyRequest, options?: RequestOptions): Promise<SetFulfillmentPolicyResponse> {
    return this.call(createFulfillmentPolicy, body, {}, options);
  }

  /** Delete a fulfillment policy. */
  delete(fulfillmentPolicyId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteFulfillmentPolicy, undefined, { fulfillmentPolicyId }, options);
  }

  /** List the seller's fulfillment policies on a marketplace. */
  list(
    params: { marketplaceId: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<FulfillmentPolicyResponse> {
    return this.call(getFulfillmentPolicies, undefined, { ...params }, options);
  }

  /** Get one fulfillment policy. */
  get(fulfillmentPolicyId: string, options?: RequestOptions): Promise<FulfillmentPolicy> {
    return this.call(getFulfillmentPolicy, undefined, { fulfillmentPolicyId }, options);
  }

  /** Get a fulfillment policy by its name. */
  getByName(
    params: { marketplaceId: string; name: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<FulfillmentPolicy> {
    return this.call(getFulfillmentPolicyByName, undefined, { ...params }, options);
  }

  /** Replace a fulfillment policy. */
  update(
    fulfillmentPolicyId: string,
    body: FulfillmentPolicyRequest,
    options?: RequestOptions,
  ): Promise<SetFulfillmentPolicyResponse> {
    return this.call(updateFulfillmentPolicy, body, { fulfillmentPolicyId }, options);
  }
}
