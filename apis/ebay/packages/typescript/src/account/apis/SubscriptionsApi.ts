// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, SubscriptionResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getSubscription: Operation = {
  id: 'getSubscription',
  method: 'GET',
  path: '/sell/account/v1/subscription',
  resource: 'subscriptions',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'continuation_token', name: 'continuationToken', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'subscriptions',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
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

export const OPERATIONS: readonly Operation[] = [getSubscription];

export class SubscriptionsApi extends Resource {
  /** List one page of the seller's eBay subscriptions */
  list(
    params: { limit?: string; continuationToken?: string } = {},
    options?: RequestOptions,
  ): Promise<SubscriptionResponse> {
    return this.call(getSubscription, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: string; continuationToken?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Subscription, void, undefined> {
    return this.paginate(getSubscription, undefined, { ...params }, options);
  }
}
