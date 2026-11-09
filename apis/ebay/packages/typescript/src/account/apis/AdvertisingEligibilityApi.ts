// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, SellerEligibilityMultiProgramResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getAdvertisingEligibility: Operation = {
  id: 'getAdvertisingEligibility',
  method: 'GET',
  path: '/sell/account/v1/advertising_eligibility',
  resource: 'advertisingEligibility',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'program_types', name: 'programTypes', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
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

export const OPERATIONS: readonly Operation[] = [getAdvertisingEligibility];

export class AdvertisingEligibilityApi extends Resource {
  /** Get the seller's eligibility for each advertising program. */
  get(
    params: { programTypes?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<SellerEligibilityMultiProgramResponse> {
    return this.call(getAdvertisingEligibility, undefined, { ...params }, options);
  }
}
