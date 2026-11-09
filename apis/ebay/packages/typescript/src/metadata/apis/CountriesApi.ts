// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetAutomotivePartsCompatibilityPolicies429Response, SalesTaxJurisdictions } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getSalesTaxJurisdictions: Operation = {
  id: 'getSalesTaxJurisdictions',
  method: 'GET',
  path: '/sell/metadata/v1/country/{countryCode}/sales_tax_jurisdiction',
  resource: 'countries',
  name: 'getSalesTaxJurisdictions',
  host: 'api',
  params: [{ wire: 'countryCode', name: 'countryCode', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [getSalesTaxJurisdictions];

export class CountriesApi extends Resource {
  /** List the sales tax jurisdictions of a country. */
  getSalesTaxJurisdictions(countryCode: string, options?: RequestOptions): Promise<SalesTaxJurisdictions> {
    return this.call(getSalesTaxJurisdictions, undefined, { countryCode }, options);
  }
}
