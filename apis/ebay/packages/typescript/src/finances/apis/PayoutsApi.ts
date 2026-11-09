// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetOrderEarnings429Response, Payout, PayoutSummaryResponse, Payouts } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPayout: Operation = {
  id: 'getPayout',
  method: 'GET',
  path: '/sell/finances/v1/payout/{payout_Id}',
  resource: 'payouts',
  name: 'get',
  host: 'apiz',
  params: [
    { wire: 'payout_Id', name: 'payoutId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

const getPayoutSummary: Operation = {
  id: 'getPayoutSummary',
  method: 'GET',
  path: '/sell/finances/v1/payout_summary',
  resource: 'payouts',
  name: 'getSummary',
  host: 'apiz',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

const getPayouts: Operation = {
  id: 'getPayouts',
  method: 'GET',
  path: '/sell/finances/v1/payout',
  resource: 'payouts',
  name: 'list',
  host: 'apiz',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'payouts', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getPayout, getPayoutSummary, getPayouts];

export class PayoutsApi extends Resource {
  /** Get one payout. */
  get(payoutId: string, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<Payout> {
    return this.call(getPayout, undefined, { payoutId, ...params }, options);
  }

  /** Sum the seller's payouts. */
  getSummary(
    params: { filter?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<PayoutSummaryResponse> {
    return this.call(getPayoutSummary, undefined, { ...params }, options);
  }

  /** List one page of the seller's payouts. */
  list(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<Payouts | undefined> {
    return this.call(getPayouts, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { filter?: string; limit?: string; offset?: string; sort?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Payout, void, undefined> {
    return this.paginate(getPayouts, undefined, { ...params }, options);
  }
}
