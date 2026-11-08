// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ErrorSchema,
  ListingInventory,
  ListingInventoryProduct,
  ListingInventoryWithAssociations,
  ShopListingsWithAssociations,
  UpdateListingInventoryRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getListingInventory: Operation = {
  id: 'getListingInventory',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/inventory',
  resource: 'listingInventory',
  name: 'get',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'show_deleted', name: 'showDeleted', location: 'query' },
    { wire: 'includes', name: 'includes', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getListingProduct: Operation = {
  id: 'getListingProduct',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/inventory/products/{product_id}',
  resource: 'listingInventory',
  name: 'getProduct',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'product_id', name: 'productId', location: 'path' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getListingsInventoryByListingIds: Operation = {
  id: 'getListingsInventoryByListingIds',
  method: 'GET',
  path: '/v3/application/listings/batch/inventory',
  resource: 'listingInventory',
  name: 'listByIds',
  params: [{ wire: 'listing_ids', name: 'listingIds', location: 'query' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const updateListingInventory: Operation = {
  id: 'updateListingInventory',
  method: 'PUT',
  path: '/v3/application/listings/{listing_id}/inventory',
  resource: 'listingInventory',
  name: 'update',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'max_variations_supported', name: 'maxVariationsSupported', location: 'query' },
    { wire: 'enable_scale_validation', name: 'enableScaleValidation', location: 'query' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  getListingInventory,
  getListingProduct,
  getListingsInventoryByListingIds,
  updateListingInventory,
];

export class ListingInventoryApi extends Resource {
  /** Get a listing's inventory. */
  get(
    listingId: number,
    params: { showDeleted?: boolean; includes?: 'Listing' } = {},
    options?: RequestOptions,
  ): Promise<ListingInventoryWithAssociations> {
    return this.call(getListingInventory, undefined, { listingId, ...params }, options);
  }

  /** Get one product of a listing's inventory. */
  getProduct(
    listingId: number,
    productId: number,
    params: { legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ListingInventoryProduct> {
    return this.call(getListingProduct, undefined, { listingId, productId, ...params }, options);
  }

  /** Get the inventory of several listings by ID. */
  listByIds(params: { listingIds: Array<number> }, options?: RequestOptions): Promise<ShopListingsWithAssociations> {
    return this.call(getListingsInventoryByListingIds, undefined, { ...params }, options);
  }

  /** Replace a listing's inventory. */
  update(
    listingId: number,
    body?: UpdateListingInventoryRequest,
    params: { maxVariationsSupported?: '2' | '3'; enableScaleValidation?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ListingInventory> {
    return this.call(updateListingInventory, body, { listingId, ...params }, options);
  }
}
