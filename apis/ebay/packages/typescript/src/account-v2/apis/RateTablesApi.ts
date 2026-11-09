// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetRateTable429Response, RateTableDetails, RateTableUpdate } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getRateTable: Operation = {
  id: 'getRateTable',
  method: 'GET',
  path: '/sell/account/v2/rate_table/{rate_table_id}',
  resource: 'rateTables',
  name: 'get',
  host: 'api',
  params: [{ wire: 'rate_table_id', name: 'rateTableId', location: 'path' }],
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

const updateShippingCost: Operation = {
  id: 'updateShippingCost',
  method: 'POST',
  path: '/sell/account/v2/rate_table/{rate_table_id}/update_shipping_cost',
  resource: 'rateTables',
  name: 'updateShippingCost',
  host: 'api',
  params: [{ wire: 'rate_table_id', name: 'rateTableId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [getRateTable, updateShippingCost];

export class RateTablesApi extends Resource {
  /** Get one shipping rate table. */
  get(rateTableId: string, options?: RequestOptions): Promise<RateTableDetails> {
    return this.call(getRateTable, undefined, { rateTableId }, options);
  }

  /** Update the shipping costs in a rate table. */
  updateShippingCost(rateTableId: string, body?: RateTableUpdate, options?: RequestOptions): Promise<void> {
    return this.call(updateShippingCost, body, { rateTableId }, options);
  }
}
