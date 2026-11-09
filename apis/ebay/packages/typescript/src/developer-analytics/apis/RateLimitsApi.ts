// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetRateLimits429Response, RateLimitsResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getRateLimits: Operation = {
  id: 'getRateLimits',
  method: 'GET',
  path: '/developer/analytics/v1_beta/rate_limit/',
  resource: 'rateLimits',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'api_context', name: 'apiContext', location: 'query' },
    { wire: 'api_name', name: 'apiName', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getUserRateLimits: Operation = {
  id: 'getUserRateLimits',
  method: 'GET',
  path: '/developer/analytics/v1_beta/user_rate_limit/',
  resource: 'rateLimits',
  name: 'listForUser',
  host: 'api',
  params: [
    { wire: 'api_context', name: 'apiContext', location: 'query' },
    { wire: 'api_name', name: 'apiName', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.marketplace.insights.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
          'https://api.ebay.com/oauth/api_scope/sell.marketing.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getRateLimits, getUserRateLimits];

export class RateLimitsApi extends Resource {
  /** List the app's call limits and current usage. */
  list(
    params: { apiContext?: string; apiName?: string } = {},
    options?: RequestOptions,
  ): Promise<RateLimitsResponse | undefined> {
    return this.call(getRateLimits, undefined, { ...params }, options);
  }

  /** List the call limits and current usage of the user the token belongs to. */
  listForUser(
    params: { apiContext?: string; apiName?: string } = {},
    options?: RequestOptions,
  ): Promise<RateLimitsResponse | undefined> {
    return this.call(getUserRateLimits, undefined, { ...params }, options);
  }
}
