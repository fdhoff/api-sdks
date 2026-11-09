// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateOrReplaceInventoryItem429Response,
  BulkMigrateListing,
  BulkMigrateListingResponse,
  LocationMapping,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkMigrateListing: Operation = {
  id: 'bulkMigrateListing',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_migrate_listing',
  resource: 'listings',
  name: 'bulkMigrate',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const createOrReplaceSkuLocationMapping: Operation = {
  id: 'createOrReplaceSkuLocationMapping',
  method: 'PUT',
  path: '/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations',
  resource: 'listings',
  name: 'setSkuLocations',
  host: 'api',
  params: [
    { wire: 'listingId', name: 'listingId', location: 'path' },
    { wire: 'sku', name: 'sku', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const deleteSkuLocationMapping: Operation = {
  id: 'deleteSkuLocationMapping',
  method: 'DELETE',
  path: '/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations',
  resource: 'listings',
  name: 'deleteSkuLocations',
  host: 'api',
  params: [
    { wire: 'listingId', name: 'listingId', location: 'path' },
    { wire: 'sku', name: 'sku', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getSkuLocationMapping: Operation = {
  id: 'getSkuLocationMapping',
  method: 'GET',
  path: '/sell/inventory/v1/listing/{listingId}/sku/{sku}/locations',
  resource: 'listings',
  name: 'getSkuLocations',
  host: 'api',
  params: [
    { wire: 'listingId', name: 'listingId', location: 'path' },
    { wire: 'sku', name: 'sku', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  bulkMigrateListing,
  createOrReplaceSkuLocationMapping,
  deleteSkuLocationMapping,
  getSkuLocationMapping,
];

export class ListingsApi extends Resource {
  /** Move existing listings into the Inventory API. */
  bulkMigrate(body: BulkMigrateListing, options?: RequestOptions): Promise<BulkMigrateListingResponse> {
    return this.call(bulkMigrateListing, body, {}, options);
  }

  /** Set the fulfillment locations of a SKU in a listing. */
  setSkuLocations(
    listingId: string,
    sku: string,
    body: LocationMapping,
    options?: RequestOptions,
  ): Promise<Error | undefined> {
    return this.call(createOrReplaceSkuLocationMapping, body, { listingId, sku }, options);
  }

  /** Remove the fulfillment locations of a SKU in a listing. */
  deleteSkuLocations(listingId: string, sku: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(deleteSkuLocationMapping, undefined, { listingId, sku }, options);
  }

  /** Get the fulfillment locations of a SKU in a listing. */
  getSkuLocations(listingId: string, sku: string, options?: RequestOptions): Promise<LocationMapping> {
    return this.call(getSkuLocationMapping, undefined, { listingId, sku }, options);
  }
}
