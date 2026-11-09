// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateOrReplaceInventoryItem429Response,
  BulkEbayOfferDetailsWithKeys,
  BulkOffer,
  BulkOfferResponse,
  BulkPublishResponse,
  EbayOfferDetailsWithAll,
  EbayOfferDetailsWithId,
  EbayOfferDetailsWithKeys,
  FeesSummaryResponse,
  OfferKeysWithId,
  OfferResponse,
  Offers,
  PublishByInventoryItemGroupRequest,
  PublishResponse,
  WithdrawByInventoryItemGroupRequest,
  WithdrawResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateOffer: Operation = {
  id: 'bulkCreateOffer',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_create_offer',
  resource: 'offers',
  name: 'bulkCreate',
  host: 'api',
  params: [{ wire: 'Content-Language', name: 'contentLanguage', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const bulkPublishOffer: Operation = {
  id: 'bulkPublishOffer',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_publish_offer',
  resource: 'offers',
  name: 'bulkPublish',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const createOffer: Operation = {
  id: 'createOffer',
  method: 'POST',
  path: '/sell/inventory/v1/offer',
  resource: 'offers',
  name: 'create',
  host: 'api',
  params: [{ wire: 'Content-Language', name: 'contentLanguage', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const deleteOffer: Operation = {
  id: 'deleteOffer',
  method: 'DELETE',
  path: '/sell/inventory/v1/offer/{offerId}',
  resource: 'offers',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'offerId', name: 'offerId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getListingFees: Operation = {
  id: 'getListingFees',
  method: 'POST',
  path: '/sell/inventory/v1/offer/get_listing_fees',
  resource: 'offers',
  name: 'getListingFees',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const getOffer: Operation = {
  id: 'getOffer',
  method: 'GET',
  path: '/sell/inventory/v1/offer/{offerId}',
  resource: 'offers',
  name: 'get',
  host: 'api',
  params: [{ wire: 'offerId', name: 'offerId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const getOffers: Operation = {
  id: 'getOffers',
  method: 'GET',
  path: '/sell/inventory/v1/offer',
  resource: 'offers',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'format', name: 'format', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sku', name: 'sku', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'offers', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const publishOffer: Operation = {
  id: 'publishOffer',
  method: 'POST',
  path: '/sell/inventory/v1/offer/{offerId}/publish',
  resource: 'offers',
  name: 'publish',
  host: 'api',
  params: [{ wire: 'offerId', name: 'offerId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const publishOfferByInventoryItemGroup: Operation = {
  id: 'publishOfferByInventoryItemGroup',
  method: 'POST',
  path: '/sell/inventory/v1/offer/publish_by_inventory_item_group',
  resource: 'offers',
  name: 'publishByInventoryItemGroup',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const updateOffer: Operation = {
  id: 'updateOffer',
  method: 'PUT',
  path: '/sell/inventory/v1/offer/{offerId}',
  resource: 'offers',
  name: 'update',
  host: 'api',
  params: [
    { wire: 'offerId', name: 'offerId', location: 'path' },
    { wire: 'Content-Language', name: 'contentLanguage', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const withdrawOffer: Operation = {
  id: 'withdrawOffer',
  method: 'POST',
  path: '/sell/inventory/v1/offer/{offerId}/withdraw',
  resource: 'offers',
  name: 'withdraw',
  host: 'api',
  params: [{ wire: 'offerId', name: 'offerId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const withdrawOfferByInventoryItemGroup: Operation = {
  id: 'withdrawOfferByInventoryItemGroup',
  method: 'POST',
  path: '/sell/inventory/v1/offer/withdraw_by_inventory_item_group',
  resource: 'offers',
  name: 'withdrawByInventoryItemGroup',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  bulkCreateOffer,
  bulkPublishOffer,
  createOffer,
  deleteOffer,
  getListingFees,
  getOffer,
  getOffers,
  publishOffer,
  publishOfferByInventoryItemGroup,
  updateOffer,
  withdrawOffer,
  withdrawOfferByInventoryItemGroup,
];

export class OffersApi extends Resource {
  /** Create several unpublished offers. */
  bulkCreate(
    body: BulkEbayOfferDetailsWithKeys,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<BulkOfferResponse> {
    return this.call(bulkCreateOffer, body, { ...params }, options);
  }

  /** Publish several offers as listings. */
  bulkPublish(body: BulkOffer, options?: RequestOptions): Promise<BulkPublishResponse> {
    return this.call(bulkPublishOffer, body, {}, options);
  }

  /** Create an unpublished offer for an inventory item. */
  create(
    body: EbayOfferDetailsWithKeys,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<OfferResponse> {
    return this.call(createOffer, body, { ...params }, options);
  }

  /** Delete an offer */
  delete(offerId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteOffer, undefined, { offerId }, options);
  }

  /** Estimate the listing fees of unpublished offers. */
  getListingFees(body?: OfferKeysWithId, options?: RequestOptions): Promise<FeesSummaryResponse> {
    return this.call(getListingFees, body, {}, options);
  }

  /** Get one offer. */
  get(offerId: string, options?: RequestOptions): Promise<EbayOfferDetailsWithAll> {
    return this.call(getOffer, undefined, { offerId }, options);
  }

  /** List one page of the offers of a SKU. */
  list(
    params: { format?: string; limit?: string; marketplaceId?: string; offset?: string; sku?: string } = {},
    options?: RequestOptions,
  ): Promise<Offers> {
    return this.call(getOffers, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { format?: string; limit?: string; marketplaceId?: string; offset?: string; sku?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.EbayOfferDetailsWithAll, void, undefined> {
    return this.paginate(getOffers, undefined, { ...params }, options);
  }

  /** Publish an offer as a listing. */
  publish(offerId: string, options?: RequestOptions): Promise<PublishResponse> {
    return this.call(publishOffer, undefined, { offerId }, options);
  }

  /** Publish the offers of an inventory item group as one multi-variation listing. */
  publishByInventoryItemGroup(
    body: PublishByInventoryItemGroupRequest,
    options?: RequestOptions,
  ): Promise<PublishResponse> {
    return this.call(publishOfferByInventoryItemGroup, body, {}, options);
  }

  /** Replace an offer. */
  update(
    offerId: string,
    body: EbayOfferDetailsWithId,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<OfferResponse | undefined> {
    return this.call(updateOffer, body, { offerId, ...params }, options);
  }

  /** End the listing of an offer and keep the offer. */
  withdraw(offerId: string, options?: RequestOptions): Promise<WithdrawResponse> {
    return this.call(withdrawOffer, undefined, { offerId }, options);
  }

  /** End the multi-variation listing of an inventory item group. */
  withdrawByInventoryItemGroup(body: WithdrawByInventoryItemGroupRequest, options?: RequestOptions): Promise<void> {
    return this.call(withdrawOfferByInventoryItemGroup, body, {}, options);
  }
}
