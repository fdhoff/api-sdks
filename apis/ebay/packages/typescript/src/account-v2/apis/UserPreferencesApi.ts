// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetRateTable429Response, GetUserPreferencesResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getUserPreferences: Operation = {
  id: 'getUserPreferences',
  method: 'GET',
  path: '/sell/account/v2/user_preferences',
  resource: 'userPreferences',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account.readonly'] }]],
};

const setUserPreferences: Operation = {
  id: 'setUserPreferences',
  method: 'PATCH',
  path: '/sell/account/v2/user_preferences',
  resource: 'userPreferences',
  name: 'set',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [getUserPreferences, setUserPreferences];

export class UserPreferencesApi extends Resource {
  /** Get the seller's account preferences. */
  get(
    params: { fieldgroups?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetUserPreferencesResponse> {
    return this.call(getUserPreferences, undefined, { ...params }, options);
  }

  /** Update the seller's account preferences. */
  set(body?: { [key: string]: any }, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<void> {
    return this.call(setUserPreferences, body, { ...params }, options);
  }
}
