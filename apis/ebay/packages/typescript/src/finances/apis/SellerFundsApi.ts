// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetOrderEarnings429Response, SellerFundsSummaryResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getSellerFundsSummary: Operation = {
  id: 'getSellerFundsSummary',
  method: 'GET',
  path: '/sell/finances/v1/seller_funds_summary',
  resource: 'sellerFunds',
  name: 'getSummary',
  host: 'apiz',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getSellerFundsSummary];

export class SellerFundsApi extends Resource {
  /** Get the seller's funds that are not yet paid out. */
  getSummary(
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<SellerFundsSummaryResponse | undefined> {
    return this.call(getSellerFundsSummary, undefined, { ...params }, options);
  }
}
