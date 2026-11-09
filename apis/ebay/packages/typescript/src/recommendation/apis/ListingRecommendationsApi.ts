// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  FindListingRecommendationRequest,
  FindListingRecommendations429Response,
  PagedListingRecommendationCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const findListingRecommendations: Operation = {
  id: 'findListingRecommendations',
  method: 'POST',
  path: '/sell/recommendation/v1/find',
  resource: 'listingRecommendations',
  name: 'find',
  host: 'api',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'listingRecommendations',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [findListingRecommendations];

export class ListingRecommendationsApi extends Resource {
  /** List one page of recommendations for the seller's listings. */
  find(
    body?: FindListingRecommendationRequest,
    params: { filter?: string; limit?: string; offset?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<PagedListingRecommendationCollection | undefined> {
    return this.call(findListingRecommendations, body, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    body?: FindListingRecommendationRequest,
    params: { filter?: string; limit?: string; offset?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ListingRecommendation, void, undefined> {
    return this.paginate(findListingRecommendations, body, { ...params }, options);
  }
}
