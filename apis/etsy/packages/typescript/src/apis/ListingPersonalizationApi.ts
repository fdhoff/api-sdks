// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingPersonalization, UpdateListingPersonalizationRequest } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deleteListingPersonalization: Operation = {
  id: 'deleteListingPersonalization',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/personalization',
  resource: 'listingPersonalization',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getListingPersonalization: Operation = {
  id: 'getListingPersonalization',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/personalization',
  resource: 'listingPersonalization',
  name: 'get',
  params: [{ wire: 'listing_id', name: 'listingId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateListingPersonalization: Operation = {
  id: 'updateListingPersonalization',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/personalization',
  resource: 'listingPersonalization',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    {
      wire: 'supports_multiple_personalization_questions',
      name: 'supportsMultiplePersonalizationQuestions',
      location: 'query',
    },
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
  deleteListingPersonalization,
  getListingPersonalization,
  updateListingPersonalization,
];

export class ListingPersonalizationApi extends Resource {
  /** Remove a listing's personalization questions. */
  delete(shopId: number, listingId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListingPersonalization, undefined, { shopId, listingId }, options);
  }

  /** Get a listing's personalization questions. */
  get(listingId: number, options?: RequestOptions): Promise<ListingPersonalization> {
    return this.call(getListingPersonalization, undefined, { listingId }, options);
  }

  /** Set a listing's personalization questions. */
  update(
    shopId: number,
    listingId: number,
    body?: UpdateListingPersonalizationRequest,
    params: { supportsMultiplePersonalizationQuestions?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ListingPersonalization> {
    return this.call(updateListingPersonalization, body, { shopId, listingId, ...params }, options);
  }
}
