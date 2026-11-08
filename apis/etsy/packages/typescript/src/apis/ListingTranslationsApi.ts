// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingTranslation } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createListingTranslation: Operation = {
  id: 'createListingTranslation',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}',
  resource: 'listingTranslations',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'language', name: 'language', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'description', name: 'description', location: 'urlencoded' },
    { wire: 'tags', name: 'tags', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getListingTranslation: Operation = {
  id: 'getListingTranslation',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}',
  resource: 'listingTranslations',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'language', name: 'language', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateListingTranslation: Operation = {
  id: 'updateListingTranslation',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}',
  resource: 'listingTranslations',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'language', name: 'language', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'description', name: 'description', location: 'urlencoded' },
    { wire: 'tags', name: 'tags', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createListingTranslation,
  getListingTranslation,
  updateListingTranslation,
];

export class ListingTranslationsApi extends Resource {
  /** Add a listing's translation into one language. */
  create(
    shopId: number,
    listingId: number,
    language: string,
    params: { title: string; description: string; tags?: Array<string> },
    options?: RequestOptions,
  ): Promise<ListingTranslation> {
    return this.call(createListingTranslation, undefined, { shopId, listingId, language, ...params }, options);
  }

  /** Get a listing's translation into one language. */
  get(shopId: number, listingId: number, language: string, options?: RequestOptions): Promise<ListingTranslation> {
    return this.call(getListingTranslation, undefined, { shopId, listingId, language }, options);
  }

  /** Update a listing's translation into one language. */
  update(
    shopId: number,
    listingId: number,
    language: string,
    params: { title: string; description: string; tags?: Array<string> },
    options?: RequestOptions,
  ): Promise<ListingTranslation> {
    return this.call(updateListingTranslation, undefined, { shopId, listingId, language, ...params }, options);
  }
}
