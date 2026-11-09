// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  ItemsPagedCollection,
  PromotionsPagedCollection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getListingSet: Operation = {
  id: 'getListingSet',
  method: 'GET',
  path: '/sell/marketing/v1/promotion/{promotion_id}/get_listing_set',
  resource: 'promotions',
  name: 'getListingSet',
  host: 'api',
  params: [
    { wire: 'promotion_id', name: 'promotionId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterListingSet',
  paging: { style: 'next_link', items: 'listings', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getPromotions: Operation = {
  id: 'getPromotions',
  method: 'GET',
  path: '/sell/marketing/v1/promotion',
  resource: 'promotions',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'promotion_status', name: 'promotionStatus', location: 'query' },
    { wire: 'promotion_type', name: 'promotionType', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'promotions', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.marketing.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
        ],
      },
    ],
  ],
};

const pausePromotion: Operation = {
  id: 'pausePromotion',
  method: 'POST',
  path: '/sell/marketing/v1/promotion/{promotion_id}/pause',
  resource: 'promotions',
  name: 'pause',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const resumePromotion: Operation = {
  id: 'resumePromotion',
  method: 'POST',
  path: '/sell/marketing/v1/promotion/{promotion_id}/resume',
  resource: 'promotions',
  name: 'resume',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [getListingSet, getPromotions, pausePromotion, resumePromotion];

export class PromotionsApi extends Resource {
  /** List one page of the listings in a promotion. */
  getListingSet(
    promotionId: string,
    params: { limit?: string; offset?: string; q?: string; sort?: string; status?: string } = {},
    options?: RequestOptions,
  ): Promise<ItemsPagedCollection> {
    return this.call(getListingSet, undefined, { promotionId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterListingSet(
    promotionId: string,
    params: { limit?: string; offset?: string; q?: string; sort?: string; status?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ListingDetail, void, undefined> {
    return this.paginate(getListingSet, undefined, { promotionId, ...params }, options);
  }

  /** List one page of the seller's promotions on a marketplace. */
  list(
    params: {
      limit?: string;
      marketplaceId: string;
      offset?: string;
      promotionStatus?: string;
      promotionType?: string;
      q?: string;
      sort?: string;
    },
    options?: RequestOptions,
  ): Promise<PromotionsPagedCollection> {
    return this.call(getPromotions, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      limit?: string;
      marketplaceId: string;
      offset?: string;
      promotionStatus?: string;
      promotionType?: string;
      q?: string;
      sort?: string;
    },
    options?: RequestOptions,
  ): AsyncGenerator<models.PromotionDetail, void, undefined> {
    return this.paginate(getPromotions, undefined, { ...params }, options);
  }

  /** Pause a promotion. */
  pause(promotionId: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(pausePromotion, undefined, { promotionId }, options);
  }

  /** Resume a paused promotion. */
  resume(promotionId: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(resumePromotion, undefined, { promotionId }, options);
  }
}
