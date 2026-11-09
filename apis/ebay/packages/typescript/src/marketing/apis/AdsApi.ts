// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  Ad,
  AdIds,
  AdPagedCollectionResponse,
  AdReferences,
  Ads,
  BulkAdResponse,
  BulkAdUpdateResponse,
  BulkAdUpdateStatusByListingIdResponse,
  BulkAdUpdateStatusResponse,
  BulkCreateAdRequest,
  BulkCreateAdsByInventoryReference429Response,
  BulkCreateAdsByInventoryReferenceRequest,
  BulkCreateAdsByInventoryReferenceResponse,
  BulkDeleteAdRequest,
  BulkDeleteAdResponse,
  BulkDeleteAdsByInventoryReferenceRequest,
  BulkDeleteAdsByInventoryReferenceResponse,
  BulkUpdateAdStatusByListingIdRequest,
  BulkUpdateAdStatusRequest,
  BulkUpdateAdsByInventoryReferenceResponse,
  CreateAdRequest,
  CreateAdsByInventoryReferenceRequest,
  DeleteAdsByInventoryReferenceRequest,
  UpdateBidPercentageRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateAdsByInventoryReference: Operation = {
  id: 'bulkCreateAdsByInventoryReference',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference',
  resource: 'ads',
  name: 'bulkCreateByInventoryReference',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkCreateAdsByListingId: Operation = {
  id: 'bulkCreateAdsByListingId',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id',
  resource: 'ads',
  name: 'bulkCreateByListingId',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkDeleteAdsByInventoryReference: Operation = {
  id: 'bulkDeleteAdsByInventoryReference',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference',
  resource: 'ads',
  name: 'bulkDeleteByInventoryReference',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkDeleteAdsByListingId: Operation = {
  id: 'bulkDeleteAdsByListingId',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id',
  resource: 'ads',
  name: 'bulkDeleteByListingId',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateAdsBidByInventoryReference: Operation = {
  id: 'bulkUpdateAdsBidByInventoryReference',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference',
  resource: 'ads',
  name: 'bulkUpdateBidByInventoryReference',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateAdsBidByListingId: Operation = {
  id: 'bulkUpdateAdsBidByListingId',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id',
  resource: 'ads',
  name: 'bulkUpdateBidByListingId',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateAdsStatus: Operation = {
  id: 'bulkUpdateAdsStatus',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status',
  resource: 'ads',
  name: 'bulkUpdateStatus',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateAdsStatusByListingId: Operation = {
  id: 'bulkUpdateAdsStatusByListingId',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id',
  resource: 'ads',
  name: 'bulkUpdateStatusByListingId',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const createAdByListingId: Operation = {
  id: 'createAdByListingId',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad',
  resource: 'ads',
  name: 'createByListingId',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const createAdsByInventoryReference: Operation = {
  id: 'createAdsByInventoryReference',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference',
  resource: 'ads',
  name: 'createByInventoryReference',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteAd: Operation = {
  id: 'deleteAd',
  method: 'DELETE',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}',
  resource: 'ads',
  name: 'delete',
  host: 'api',
  params: [
    { wire: 'ad_id', name: 'adId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteAdsByInventoryReference: Operation = {
  id: 'deleteAdsByInventoryReference',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference',
  resource: 'ads',
  name: 'deleteByInventoryReference',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getAd: Operation = {
  id: 'getAd',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}',
  resource: 'ads',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'ad_id', name: 'adId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  returnsJson: true,
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

const getAds: Operation = {
  id: 'getAds',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad',
  resource: 'ads',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'ad_group_ids', name: 'adGroupIds', location: 'query' },
    { wire: 'ad_status', name: 'adStatus', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'listing_ids', name: 'listingIds', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'ads', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
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

const getAdsByInventoryReference: Operation = {
  id: 'getAdsByInventoryReference',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/get_ads_by_inventory_reference',
  resource: 'ads',
  name: 'getByInventoryReference',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'inventory_reference_id', name: 'inventoryReferenceId', location: 'query' },
    { wire: 'inventory_reference_type', name: 'inventoryReferenceType', location: 'query' },
  ],
  returnsJson: true,
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

const updateBid: Operation = {
  id: 'updateBid',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid',
  resource: 'ads',
  name: 'updateBid',
  host: 'api',
  params: [
    { wire: 'ad_id', name: 'adId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  bulkCreateAdsByInventoryReference,
  bulkCreateAdsByListingId,
  bulkDeleteAdsByInventoryReference,
  bulkDeleteAdsByListingId,
  bulkUpdateAdsBidByInventoryReference,
  bulkUpdateAdsBidByListingId,
  bulkUpdateAdsStatus,
  bulkUpdateAdsStatusByListingId,
  createAdByListingId,
  createAdsByInventoryReference,
  deleteAd,
  deleteAdsByInventoryReference,
  getAd,
  getAds,
  getAdsByInventoryReference,
  updateBid,
];

export class AdsApi extends Resource {
  /** Create ads for several inventory references. */
  bulkCreateByInventoryReference(
    campaignId: string,
    body: BulkCreateAdsByInventoryReferenceRequest,
    options?: RequestOptions,
  ): Promise<BulkCreateAdsByInventoryReferenceResponse> {
    return this.call(bulkCreateAdsByInventoryReference, body, { campaignId }, options);
  }

  /** Create ads for several listings. */
  bulkCreateByListingId(
    campaignId: string,
    body: BulkCreateAdRequest,
    options?: RequestOptions,
  ): Promise<BulkAdResponse> {
    return this.call(bulkCreateAdsByListingId, body, { campaignId }, options);
  }

  /** Delete the ads of several inventory references. */
  bulkDeleteByInventoryReference(
    campaignId: string,
    body: BulkDeleteAdsByInventoryReferenceRequest,
    options?: RequestOptions,
  ): Promise<BulkDeleteAdsByInventoryReferenceResponse> {
    return this.call(bulkDeleteAdsByInventoryReference, body, { campaignId }, options);
  }

  /** Delete the ads of several listings. */
  bulkDeleteByListingId(
    campaignId: string,
    body: BulkDeleteAdRequest,
    options?: RequestOptions,
  ): Promise<BulkDeleteAdResponse> {
    return this.call(bulkDeleteAdsByListingId, body, { campaignId }, options);
  }

  /** Change the bids of several inventory references' ads. */
  bulkUpdateBidByInventoryReference(
    campaignId: string,
    body: BulkCreateAdsByInventoryReferenceRequest,
    options?: RequestOptions,
  ): Promise<BulkUpdateAdsByInventoryReferenceResponse> {
    return this.call(bulkUpdateAdsBidByInventoryReference, body, { campaignId }, options);
  }

  /** Change the bids of several listings' ads. */
  bulkUpdateBidByListingId(
    campaignId: string,
    body: BulkCreateAdRequest,
    options?: RequestOptions,
  ): Promise<BulkAdUpdateResponse> {
    return this.call(bulkUpdateAdsBidByListingId, body, { campaignId }, options);
  }

  /** Change the status of several ads. */
  bulkUpdateStatus(
    campaignId: string,
    body: BulkUpdateAdStatusRequest,
    options?: RequestOptions,
  ): Promise<BulkAdUpdateStatusResponse> {
    return this.call(bulkUpdateAdsStatus, body, { campaignId }, options);
  }

  /** Change the status of several listings' ads. */
  bulkUpdateStatusByListingId(
    campaignId: string,
    body: BulkUpdateAdStatusByListingIdRequest,
    options?: RequestOptions,
  ): Promise<BulkAdUpdateStatusByListingIdResponse> {
    return this.call(bulkUpdateAdsStatusByListingId, body, { campaignId }, options);
  }

  /** Create an ad for a listing. */
  createByListingId(campaignId: string, body: CreateAdRequest, options?: RequestOptions): Promise<object> {
    return this.call(createAdByListingId, body, { campaignId }, options);
  }

  /** Create ads for an inventory reference. */
  createByInventoryReference(
    campaignId: string,
    body: CreateAdsByInventoryReferenceRequest,
    options?: RequestOptions,
  ): Promise<AdReferences> {
    return this.call(createAdsByInventoryReference, body, { campaignId }, options);
  }

  /** Delete an ad. */
  delete(adId: string, campaignId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteAd, undefined, { adId, campaignId }, options);
  }

  /** Delete a campaign's ads for one inventory reference. */
  deleteByInventoryReference(
    campaignId: string,
    body: DeleteAdsByInventoryReferenceRequest,
    options?: RequestOptions,
  ): Promise<AdIds> {
    return this.call(deleteAdsByInventoryReference, body, { campaignId }, options);
  }

  /** Get one ad. */
  get(adId: string, campaignId: string, options?: RequestOptions): Promise<Ad> {
    return this.call(getAd, undefined, { adId, campaignId }, options);
  }

  /** List one page of a campaign's ads. */
  list(
    campaignId: string,
    params: { adGroupIds?: string; adStatus?: string; limit?: string; listingIds?: string; offset?: string } = {},
    options?: RequestOptions,
  ): Promise<AdPagedCollectionResponse> {
    return this.call(getAds, undefined, { campaignId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    campaignId: string,
    params: { adGroupIds?: string; adStatus?: string; limit?: string; listingIds?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Ad, void, undefined> {
    return this.paginate(getAds, undefined, { campaignId, ...params }, options);
  }

  /** Get a campaign's ads for one inventory reference. */
  getByInventoryReference(
    campaignId: string,
    params: { inventoryReferenceId: string; inventoryReferenceType: string },
    options?: RequestOptions,
  ): Promise<Ads> {
    return this.call(getAdsByInventoryReference, undefined, { campaignId, ...params }, options);
  }

  /** Change the bid of an ad. */
  updateBid(
    adId: string,
    campaignId: string,
    body: UpdateBidPercentageRequest,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateBid, body, { adId, campaignId }, options);
  }
}
