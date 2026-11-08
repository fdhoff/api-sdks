// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingVariationImages, UpdateVariationImagesRequest } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getListingVariationImages: Operation = {
  id: 'getListingVariationImages',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images',
  resource: 'listingVariationImages',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateVariationImages: Operation = {
  id: 'updateVariationImages',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images',
  resource: 'listingVariationImages',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
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

export const OPERATIONS: readonly Operation[] = [getListingVariationImages, updateVariationImages];

export class ListingVariationImagesApi extends Resource {
  /** List the images mapped to a listing's variations. */
  list(shopId: number, listingId: number, options?: RequestOptions): Promise<ListingVariationImages> {
    return this.call(getListingVariationImages, undefined, { shopId, listingId }, options);
  }

  /** Replace the images mapped to a listing's variations. */
  update(
    shopId: number,
    listingId: number,
    body?: UpdateVariationImagesRequest,
    options?: RequestOptions,
  ): Promise<ListingVariationImages> {
    return this.call(updateVariationImages, body, { shopId, listingId }, options);
  }
}
