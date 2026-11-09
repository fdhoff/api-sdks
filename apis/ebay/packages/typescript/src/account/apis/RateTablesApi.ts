// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, RateTableResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getRateTables: Operation = {
  id: 'getRateTables',
  method: 'GET',
  path: '/sell/account/v1/rate_table',
  resource: 'rateTables',
  name: 'list',
  host: 'api',
  params: [{ wire: 'country_code', name: 'countryCode', location: 'query' }],
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

export const OPERATIONS: readonly Operation[] = [getRateTables];

export class RateTablesApi extends Resource {
  /** List the seller's shipping rate tables. */
  list(params: { countryCode?: string } = {}, options?: RequestOptions): Promise<RateTableResponse> {
    return this.call(getRateTables, undefined, { ...params }, options);
  }
}
