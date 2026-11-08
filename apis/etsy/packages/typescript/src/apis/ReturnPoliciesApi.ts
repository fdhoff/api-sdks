// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopReturnPolicies, ShopReturnPolicy } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const consolidateShopReturnPolicies: Operation = {
  id: 'consolidateShopReturnPolicies',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/policies/return/consolidate',
  resource: 'returnPolicies',
  name: 'consolidate',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'source_return_policy_id', name: 'sourceReturnPolicyId', location: 'urlencoded' },
    { wire: 'destination_return_policy_id', name: 'destinationReturnPolicyId', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const createShopReturnPolicy: Operation = {
  id: 'createShopReturnPolicy',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/policies/return',
  resource: 'returnPolicies',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'accepts_returns', name: 'acceptsReturns', location: 'urlencoded' },
    { wire: 'accepts_exchanges', name: 'acceptsExchanges', location: 'urlencoded' },
    { wire: 'return_deadline', name: 'returnDeadline', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopReturnPolicy: Operation = {
  id: 'deleteShopReturnPolicy',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/policies/return/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const getShopReturnPolicies: Operation = {
  id: 'getShopReturnPolicies',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/policies/return',
  resource: 'returnPolicies',
  name: 'list',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getShopReturnPolicy: Operation = {
  id: 'getShopReturnPolicy',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/policies/return/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateShopReturnPolicy: Operation = {
  id: 'updateShopReturnPolicy',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/policies/return/{return_policy_id}',
  resource: 'returnPolicies',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' },
    { wire: 'accepts_returns', name: 'acceptsReturns', location: 'urlencoded' },
    { wire: 'accepts_exchanges', name: 'acceptsExchanges', location: 'urlencoded' },
    { wire: 'return_deadline', name: 'returnDeadline', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  consolidateShopReturnPolicies,
  createShopReturnPolicy,
  deleteShopReturnPolicy,
  getShopReturnPolicies,
  getShopReturnPolicy,
  updateShopReturnPolicy,
];

export class ReturnPoliciesApi extends Resource {
  /** Move every listing from one return policy to another and delete the first. */
  consolidate(
    shopId: number,
    params: { sourceReturnPolicyId: number; destinationReturnPolicyId: number },
    options?: RequestOptions,
  ): Promise<ShopReturnPolicy> {
    return this.call(consolidateShopReturnPolicies, undefined, { shopId, ...params }, options);
  }

  /** Create a return policy. */
  create(
    shopId: number,
    params: { acceptsReturns: boolean; acceptsExchanges: boolean; returnDeadline?: number },
    options?: RequestOptions,
  ): Promise<ShopReturnPolicy> {
    return this.call(createShopReturnPolicy, undefined, { shopId, ...params }, options);
  }

  /** Delete a return policy. */
  delete(shopId: number, returnPolicyId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteShopReturnPolicy, undefined, { shopId, returnPolicyId }, options);
  }

  /** List a shop's return policies. */
  list(shopId: number, options?: RequestOptions): Promise<ShopReturnPolicies> {
    return this.call(getShopReturnPolicies, undefined, { shopId }, options);
  }

  /** Get one return policy. */
  get(shopId: number, returnPolicyId: number, options?: RequestOptions): Promise<ShopReturnPolicy> {
    return this.call(getShopReturnPolicy, undefined, { shopId, returnPolicyId }, options);
  }

  /** Update a return policy. */
  update(
    shopId: number,
    returnPolicyId: number,
    params: { acceptsReturns: boolean; acceptsExchanges: boolean; returnDeadline?: number },
    options?: RequestOptions,
  ): Promise<ShopReturnPolicy> {
    return this.call(updateShopReturnPolicy, undefined, { shopId, returnPolicyId, ...params }, options);
  }
}
