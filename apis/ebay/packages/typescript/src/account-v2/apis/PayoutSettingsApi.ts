// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetRateTable429Response,
  PayoutSettingsResponse,
  UpdatePayoutPercentageRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPayoutSettings: Operation = {
  id: 'getPayoutSettings',
  method: 'GET',
  path: '/sell/account/v2/payout_settings',
  resource: 'payoutSettings',
  name: 'get',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

const updatePayoutPercentage: Operation = {
  id: 'updatePayoutPercentage',
  method: 'POST',
  path: '/sell/account/v2/payout_settings/update_percentage',
  resource: 'payoutSettings',
  name: 'updatePercentage',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getPayoutSettings, updatePayoutPercentage];

export class PayoutSettingsApi extends Resource {
  /** Get the seller's payout settings. */
  get(options?: RequestOptions): Promise<PayoutSettingsResponse> {
    return this.call(getPayoutSettings, undefined, {}, options);
  }

  /** Split payouts between the seller's payout accounts. */
  updatePercentage(body?: UpdatePayoutPercentageRequest, options?: RequestOptions): Promise<void> {
    return this.call(updatePayoutPercentage, body, {}, options);
  }
}
