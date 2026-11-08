// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingReviews, TransactionReviews } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getReviewsByListing: Operation = {
  id: 'getReviewsByListing',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/reviews',
  resource: 'reviews',
  name: 'listByListing',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'min_created', name: 'minCreated', location: 'query' },
    { wire: 'max_created', name: 'maxCreated', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterByListing',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getReviewsByShop: Operation = {
  id: 'getReviewsByShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/reviews',
  resource: 'reviews',
  name: 'listByShop',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'min_created', name: 'minCreated', location: 'query' },
    { wire: 'max_created', name: 'maxCreated', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterByShop',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getReviewsByListing, getReviewsByShop];

export class ReviewsApi extends Resource {
  /** List one page of a listing's reviews. */
  listByListing(
    listingId: number,
    params: { limit?: number; offset?: number; minCreated?: number; maxCreated?: number } = {},
    options?: RequestOptions,
  ): Promise<ListingReviews> {
    return this.call(getReviewsByListing, undefined, { listingId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterByListing(
    listingId: number,
    params: { limit?: number; offset?: number; minCreated?: number; maxCreated?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ListingReview, void, undefined> {
    return this.paginate(getReviewsByListing, undefined, { listingId, ...params }, options);
  }

  /** List one page of a shop's reviews. */
  listByShop(
    shopId: number,
    params: { limit?: number; offset?: number; minCreated?: number; maxCreated?: number } = {},
    options?: RequestOptions,
  ): Promise<TransactionReviews> {
    return this.call(getReviewsByShop, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterByShop(
    shopId: number,
    params: { limit?: number; offset?: number; minCreated?: number; maxCreated?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TransactionReview, void, undefined> {
    return this.paginate(getReviewsByShop, undefined, { shopId, ...params }, options);
  }
}
