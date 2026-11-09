// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkSalesTaxInput,
  GetCustomPolicies429Response,
  SalesTax,
  SalesTaxBase,
  SalesTaxes,
  UpdatedSalesTaxResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateOrReplaceSalesTax: Operation = {
  id: 'bulkCreateOrReplaceSalesTax',
  method: 'POST',
  path: '/sell/account/v1/bulk_create_or_replace_sales_tax',
  resource: 'salesTaxes',
  name: 'bulkCreateOrReplace',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const createOrReplaceSalesTax: Operation = {
  id: 'createOrReplaceSalesTax',
  method: 'PUT',
  path: '/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}',
  resource: 'salesTaxes',
  name: 'createOrReplace',
  host: 'api',
  params: [
    { wire: 'countryCode', name: 'countryCode', location: 'path' },
    { wire: 'jurisdictionId', name: 'jurisdictionId', location: 'path' },
  ],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const deleteSalesTax: Operation = {
  id: 'deleteSalesTax',
  method: 'DELETE',
  path: '/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}',
  resource: 'salesTaxes',
  name: 'delete',
  host: 'api',
  params: [
    { wire: 'countryCode', name: 'countryCode', location: 'path' },
    { wire: 'jurisdictionId', name: 'jurisdictionId', location: 'path' },
  ],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getSalesTax: Operation = {
  id: 'getSalesTax',
  method: 'GET',
  path: '/sell/account/v1/sales_tax/{countryCode}/{jurisdictionId}',
  resource: 'salesTaxes',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'countryCode', name: 'countryCode', location: 'path' },
    { wire: 'jurisdictionId', name: 'jurisdictionId', location: 'path' },
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

const getSalesTaxes: Operation = {
  id: 'getSalesTaxes',
  method: 'GET',
  path: '/sell/account/v1/sales_tax',
  resource: 'salesTaxes',
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

export const OPERATIONS: readonly Operation[] = [
  bulkCreateOrReplaceSalesTax,
  createOrReplaceSalesTax,
  deleteSalesTax,
  getSalesTax,
  getSalesTaxes,
];

export class SalesTaxesApi extends Resource {
  /** Set the seller's sales tax rates for several jurisdictions. */
  bulkCreateOrReplace(body: BulkSalesTaxInput, options?: RequestOptions): Promise<UpdatedSalesTaxResponse> {
    return this.call(bulkCreateOrReplaceSalesTax, body, {}, options);
  }

  /** Set the seller's sales tax rate for one jurisdiction. */
  createOrReplace(
    countryCode: string,
    jurisdictionId: string,
    body: SalesTaxBase,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createOrReplaceSalesTax, body, { countryCode, jurisdictionId }, options);
  }

  /** Remove the seller's sales tax rate for one jurisdiction. */
  delete(countryCode: string, jurisdictionId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteSalesTax, undefined, { countryCode, jurisdictionId }, options);
  }

  /** Get the seller's sales tax rate for one jurisdiction. */
  get(countryCode: string, jurisdictionId: string, options?: RequestOptions): Promise<SalesTax | undefined> {
    return this.call(getSalesTax, undefined, { countryCode, jurisdictionId }, options);
  }

  /** List the seller's sales tax rates for a country. */
  list(params: { countryCode: string }, options?: RequestOptions): Promise<SalesTaxes> {
    return this.call(getSalesTaxes, undefined, { ...params }, options);
  }
}
