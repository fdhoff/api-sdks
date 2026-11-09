// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, KycResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getKYC: Operation = {
  id: 'getKYC',
  method: 'GET',
  path: '/sell/account/v1/kyc',
  resource: 'kyc',
  name: 'get',
  host: 'api',
  params: [],
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

export const OPERATIONS: readonly Operation[] = [getKYC];

export class KycApi extends Resource {
  /** List the identity checks eBay needs from the seller. */
  get(options?: RequestOptions): Promise<KycResponse | undefined> {
    return this.call(getKYC, undefined, {}, options);
  }
}
