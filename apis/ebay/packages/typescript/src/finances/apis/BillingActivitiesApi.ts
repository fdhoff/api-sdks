// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BillingActivityResponse, GetOrderEarnings429Response } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getBillingActivities: Operation = {
  id: 'getBillingActivities',
  method: 'GET',
  path: '/sell/finances/v1/billing_activity',
  resource: 'billingActivities',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'billingActivities',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getBillingActivities];

export class BillingActivitiesApi extends Resource {
  /** List one page of the seller's billing activities. */
  list(
    params: { filter?: string; limit?: string; offset?: string; sort?: string } = {},
    options?: RequestOptions,
  ): Promise<BillingActivityResponse> {
    return this.call(getBillingActivities, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { filter?: string; limit?: string; offset?: string; sort?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.BillingActivityLineItem, void, undefined> {
    return this.paginate(getBillingActivities, undefined, { ...params }, options);
  }
}
