// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  FindSellerStandardsProfilesResponse,
  GetCustomerServiceMetric429Response,
  StandardsProfile,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const findSellerStandardsProfiles: Operation = {
  id: 'findSellerStandardsProfiles',
  method: 'GET',
  path: '/sell/analytics/v1/seller_standards_profile',
  resource: 'sellerStandardsProfiles',
  name: 'list',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

const getSellerStandardsProfile: Operation = {
  id: 'getSellerStandardsProfile',
  method: 'GET',
  path: '/sell/analytics/v1/seller_standards_profile/{program}/{cycle}',
  resource: 'sellerStandardsProfiles',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'cycle', name: 'cycle', location: 'path' },
    { wire: 'program', name: 'program', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

export const OPERATIONS: readonly Operation[] = [findSellerStandardsProfiles, getSellerStandardsProfile];

export class SellerStandardsProfilesApi extends Resource {
  /** List the seller's standards profiles. */
  list(options?: RequestOptions): Promise<FindSellerStandardsProfilesResponse> {
    return this.call(findSellerStandardsProfiles, undefined, {}, options);
  }

  /** Get one seller standards profile. */
  get(cycle: string, program: string, options?: RequestOptions): Promise<StandardsProfile | undefined> {
    return this.call(getSellerStandardsProfile, undefined, { cycle, program }, options);
  }
}
