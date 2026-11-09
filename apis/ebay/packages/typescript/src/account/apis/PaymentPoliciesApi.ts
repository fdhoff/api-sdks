// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetCustomPolicies429Response,
  PaymentPolicy,
  PaymentPolicyRequest,
  PaymentPolicyResponse,
  SetPaymentPolicyResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createPaymentPolicy: Operation = {
  id: 'createPaymentPolicy',
  method: 'POST',
  path: '/sell/account/v1/payment_policy',
  resource: 'paymentPolicies',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const deletePaymentPolicy: Operation = {
  id: 'deletePaymentPolicy',
  method: 'DELETE',
  path: '/sell/account/v1/payment_policy/{payment_policy_id}',
  resource: 'paymentPolicies',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'payment_policy_id', name: 'paymentPolicyId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getPaymentPolicies: Operation = {
  id: 'getPaymentPolicies',
  method: 'GET',
  path: '/sell/account/v1/payment_policy',
  resource: 'paymentPolicies',
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

const getPaymentPolicy: Operation = {
  id: 'getPaymentPolicy',
  method: 'GET',
  path: '/sell/account/v1/payment_policy/{payment_policy_id}',
  resource: 'paymentPolicies',
  name: 'get',
  host: 'api',
  params: [{ wire: 'payment_policy_id', name: 'paymentPolicyId', location: 'path' }],
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

const getPaymentPolicyByName: Operation = {
  id: 'getPaymentPolicyByName',
  method: 'GET',
  path: '/sell/account/v1/payment_policy/get_by_policy_name',
  resource: 'paymentPolicies',
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

const updatePaymentPolicy: Operation = {
  id: 'updatePaymentPolicy',
  method: 'PUT',
  path: '/sell/account/v1/payment_policy/{payment_policy_id}',
  resource: 'paymentPolicies',
  name: 'update',
  host: 'api',
  params: [{ wire: 'payment_policy_id', name: 'paymentPolicyId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createPaymentPolicy,
  deletePaymentPolicy,
  getPaymentPolicies,
  getPaymentPolicy,
  getPaymentPolicyByName,
  updatePaymentPolicy,
];

export class PaymentPoliciesApi extends Resource {
  /** Create a payment policy. */
  create(body: PaymentPolicyRequest, options?: RequestOptions): Promise<SetPaymentPolicyResponse> {
    return this.call(createPaymentPolicy, body, {}, options);
  }

  /** Delete a payment policy. */
  delete(paymentPolicyId: string, options?: RequestOptions): Promise<void> {
    return this.call(deletePaymentPolicy, undefined, { paymentPolicyId }, options);
  }

  /** List the seller's payment policies on a marketplace. */
  list(
    params: { marketplaceId: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<PaymentPolicyResponse> {
    return this.call(getPaymentPolicies, undefined, { ...params }, options);
  }

  /** Get one payment policy. */
  get(paymentPolicyId: string, options?: RequestOptions): Promise<PaymentPolicy> {
    return this.call(getPaymentPolicy, undefined, { paymentPolicyId }, options);
  }

  /** Get a payment policy by its name. */
  getByName(
    params: { marketplaceId: string; name: string; contentLanguage?: string },
    options?: RequestOptions,
  ): Promise<PaymentPolicy> {
    return this.call(getPaymentPolicyByName, undefined, { ...params }, options);
  }

  /** Replace a payment policy. */
  update(
    paymentPolicyId: string,
    body: PaymentPolicyRequest,
    options?: RequestOptions,
  ): Promise<SetPaymentPolicyResponse> {
    return this.call(updatePaymentPolicy, body, { paymentPolicyId }, options);
  }
}
