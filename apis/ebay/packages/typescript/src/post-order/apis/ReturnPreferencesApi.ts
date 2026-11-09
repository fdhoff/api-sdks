// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CheckCancellationEligibility429Response,
  GetSellerReturnPreferenceResponse,
  SetSellerReturnPreferenceRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getReturnPreferences: Operation = {
  id: 'getReturnPreferences',
  method: 'GET',
  path: '/post-order/v2/return/preference',
  resource: 'returnPreferences',
  name: 'get',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const setReturnPreferences: Operation = {
  id: 'setReturnPreferences',
  method: 'POST',
  path: '/post-order/v2/return/preference',
  resource: 'returnPreferences',
  name: 'set',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getReturnPreferences, setReturnPreferences];

export class ReturnPreferencesApi extends Resource {
  /** Get the seller's return preferences. */
  get(params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<GetSellerReturnPreferenceResponse> {
    return this.call(getReturnPreferences, undefined, { ...params }, options);
  }

  /** Set the seller's return preferences. */
  set(
    body: SetSellerReturnPreferenceRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(setReturnPreferences, body, { ...params }, options);
  }
}
