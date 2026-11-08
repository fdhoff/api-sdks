// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ErrorResponseV1,
  ListingDetail,
  ListingPage,
  ListingUpdate,
  ListingsBatch,
  ListingsCatalog,
  UpdatedListing,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getWsListListing: Operation = {
  id: 'get-ws-list-listing',
  method: 'GET',
  path: '/ws/listings',
  resource: 'listings',
  name: 'list',
  params: [
    { wire: 'publication_state', name: 'publicationState', location: 'query' },
    { wire: 'min_quantity', name: 'minQuantity', location: 'query' },
    { wire: 'max_quantity', name: 'maxQuantity', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'page-size', name: 'pageSize', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'results', link: 'next', params: ['page', 'cursor'] },
};

const getWsListingDetail: Operation = {
  id: 'get-ws-listing-detail',
  method: 'GET',
  path: '/ws/listings/detail',
  resource: 'listings',
  name: 'find',
  params: [
    { wire: 'sku', name: 'sku', location: 'query' },
    { wire: 'listing_id', name: 'listingId', location: 'query' },
    { wire: 'id', name: 'id', location: 'query' },
  ],
  returnsJson: true,
};

const getWsSpecificListing: Operation = {
  id: 'get-ws-specific-listing',
  method: 'GET',
  path: '/ws/listings/{listingId}',
  resource: 'listings',
  name: 'get',
  params: [{ wire: 'listingId', name: 'listingId', location: 'path' }],
  returnsJson: true,
};

const postWsCreateOrUpdateListings: Operation = {
  id: 'post-ws-create-or-update-listings',
  method: 'POST',
  path: '/ws/listings',
  resource: 'listings',
  name: 'batchUpdate',
  params: [],
  hasBody: true,
  returnsJson: true,
};

const updateWsSpecificListing: Operation = {
  id: 'update-ws-specific-listing',
  method: 'POST',
  path: '/ws/listings/{listingId}',
  resource: 'listings',
  name: 'update',
  params: [{ wire: 'listingId', name: 'listingId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
};

export const OPERATIONS: readonly Operation[] = [
  getWsListListing,
  getWsListingDetail,
  getWsSpecificListing,
  postWsCreateOrUpdateListings,
  updateWsSpecificListing,
];

export class ListingsApi extends Resource {
  /** List one page of listings. */
  list(
    params: {
      publicationState?: 0 | 1 | 2 | 3 | 4;
      minQuantity?: number;
      maxQuantity?: number;
      page?: number;
      pageSize?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ListingPage> {
    return this.call(getWsListListing, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      publicationState?: 0 | 1 | 2 | 3 | 4;
      minQuantity?: number;
      maxQuantity?: number;
      page?: number;
      pageSize?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ListingPublic, void, undefined> {
    return this.paginate(getWsListListing, undefined, { ...params }, options);
  }

  /** Find one listing by SKU or identifier. */
  find(
    params: { sku?: string; listingId?: number; id?: string } = {},
    options?: RequestOptions,
  ): Promise<ListingDetail> {
    return this.call(getWsListingDetail, undefined, { ...params }, options);
  }

  /** Get one listing. */
  get(listingId: string, options?: RequestOptions): Promise<ListingDetail> {
    return this.call(getWsSpecificListing, undefined, { listingId }, options);
  }

  /** Create or update listings from a CSV catalog. */
  batchUpdate(body?: ListingsCatalog, options?: RequestOptions): Promise<ListingsBatch> {
    return this.call(postWsCreateOrUpdateListings, body, {}, options);
  }

  /** Update one listing. */
  update(listingId: string, body?: ListingUpdate, options?: RequestOptions): Promise<UpdatedListing> {
    return this.call(updateWsSpecificListing, body, { listingId }, options);
  }
}
