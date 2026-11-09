// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  Campaign,
  CampaignPagedCollectionResponse,
  Campaigns,
  CloneCampaignRequest,
  CreateCampaignRequest,
  SuggestBudgetResponse,
  SuggestMaxCpcRequest,
  SuggestMaxCpcResponse,
  TargetedAdsPagedCollection,
  UpdateAdrateStrategyRequest,
  UpdateBiddingStrategyRequest,
  UpdateCampaignBudgetRequest,
  UpdateCampaignIdentificationRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const cloneCampaign: Operation = {
  id: 'cloneCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/clone',
  resource: 'campaigns',
  name: 'clone',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const createCampaign: Operation = {
  id: 'createCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign',
  resource: 'campaigns',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteCampaign: Operation = {
  id: 'deleteCampaign',
  method: 'DELETE',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}',
  resource: 'campaigns',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const endCampaign: Operation = {
  id: 'endCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/end',
  resource: 'campaigns',
  name: 'end',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const findCampaignByAdReference: Operation = {
  id: 'findCampaignByAdReference',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/find_campaign_by_ad_reference',
  resource: 'campaigns',
  name: 'findByAdReference',
  host: 'api',
  params: [
    { wire: 'inventory_reference_id', name: 'inventoryReferenceId', location: 'query' },
    { wire: 'inventory_reference_type', name: 'inventoryReferenceType', location: 'query' },
    { wire: 'listing_id', name: 'listingId', location: 'query' },
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

const getCampaign: Operation = {
  id: 'getCampaign',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}',
  resource: 'campaigns',
  name: 'get',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
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

const getCampaignByName: Operation = {
  id: 'getCampaignByName',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/get_campaign_by_name',
  resource: 'campaigns',
  name: 'getByName',
  host: 'api',
  params: [{ wire: 'campaign_name', name: 'campaignName', location: 'query' }],
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

const getCampaigns: Operation = {
  id: 'getCampaigns',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign',
  resource: 'campaigns',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'campaign_name', name: 'campaignName', location: 'query' },
    { wire: 'campaign_status', name: 'campaignStatus', location: 'query' },
    { wire: 'campaign_targeting_types', name: 'campaignTargetingTypes', location: 'query' },
    { wire: 'channels', name: 'channels', location: 'query' },
    { wire: 'end_date_range', name: 'endDateRange', location: 'query' },
    { wire: 'funding_strategy', name: 'fundingStrategy', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'start_date_range', name: 'startDateRange', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'campaigns', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
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

const pauseCampaign: Operation = {
  id: 'pauseCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/pause',
  resource: 'campaigns',
  name: 'pause',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const resumeCampaign: Operation = {
  id: 'resumeCampaign',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/resume',
  resource: 'campaigns',
  name: 'resume',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const suggestBudget: Operation = {
  id: 'suggestBudget',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/suggest_budget',
  resource: 'campaigns',
  name: 'suggestBudget',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const suggestItems: Operation = {
  id: 'suggestItems',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/suggest_items',
  resource: 'campaigns',
  name: 'suggestItems',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'category_ids', name: 'categoryIds', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSuggestedItems',
  paging: {
    style: 'next_link',
    items: 'suggestedItems',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const suggestMaxCpc: Operation = {
  id: 'suggestMaxCpc',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/suggest_max_cpc',
  resource: 'campaigns',
  name: 'suggestMaxCpc',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateAdRateStrategy: Operation = {
  id: 'updateAdRateStrategy',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/update_ad_rate_strategy',
  resource: 'campaigns',
  name: 'updateAdRateStrategy',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateBiddingStrategy: Operation = {
  id: 'updateBiddingStrategy',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/update_bidding_strategy',
  resource: 'campaigns',
  name: 'updateBiddingStrategy',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateCampaignBudget: Operation = {
  id: 'updateCampaignBudget',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_budget',
  resource: 'campaigns',
  name: 'updateBudget',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateCampaignIdentification: Operation = {
  id: 'updateCampaignIdentification',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/update_campaign_identification',
  resource: 'campaigns',
  name: 'updateIdentification',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  cloneCampaign,
  createCampaign,
  deleteCampaign,
  endCampaign,
  findCampaignByAdReference,
  getCampaign,
  getCampaignByName,
  getCampaigns,
  pauseCampaign,
  resumeCampaign,
  suggestBudget,
  suggestItems,
  suggestMaxCpc,
  updateAdRateStrategy,
  updateBiddingStrategy,
  updateCampaignBudget,
  updateCampaignIdentification,
];

export class CampaignsApi extends Resource {
  /** Copy an ended campaign into a new one. */
  clone(campaignId: string, body: CloneCampaignRequest, options?: RequestOptions): Promise<object> {
    return this.call(cloneCampaign, body, { campaignId }, options);
  }

  /** Create a Promoted Listings campaign. */
  create(body: CreateCampaignRequest, options?: RequestOptions): Promise<object> {
    return this.call(createCampaign, body, {}, options);
  }

  /** Delete a campaign. */
  delete(campaignId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteCampaign, undefined, { campaignId }, options);
  }

  /** End a campaign. */
  end(campaignId: string, options?: RequestOptions): Promise<void> {
    return this.call(endCampaign, undefined, { campaignId }, options);
  }

  /** Find the campaigns that hold a listing or inventory reference. */
  findByAdReference(
    params: { inventoryReferenceId?: string; inventoryReferenceType?: string; listingId?: string } = {},
    options?: RequestOptions,
  ): Promise<Campaigns> {
    return this.call(findCampaignByAdReference, undefined, { ...params }, options);
  }

  /** Get one campaign. */
  get(campaignId: string, options?: RequestOptions): Promise<Campaign> {
    return this.call(getCampaign, undefined, { campaignId }, options);
  }

  /** Get a campaign by its name. */
  getByName(params: { campaignName: string }, options?: RequestOptions): Promise<Campaign> {
    return this.call(getCampaignByName, undefined, { ...params }, options);
  }

  /** List one page of the seller's Promoted Listings campaigns. */
  list(
    params: {
      campaignName?: string;
      campaignStatus?: string;
      campaignTargetingTypes?: string;
      channels?: string;
      endDateRange?: string;
      fundingStrategy?: string;
      limit?: string;
      offset?: string;
      startDateRange?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<CampaignPagedCollectionResponse> {
    return this.call(getCampaigns, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      campaignName?: string;
      campaignStatus?: string;
      campaignTargetingTypes?: string;
      channels?: string;
      endDateRange?: string;
      fundingStrategy?: string;
      limit?: string;
      offset?: string;
      startDateRange?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Campaign, void, undefined> {
    return this.paginate(getCampaigns, undefined, { ...params }, options);
  }

  /** Pause a campaign. */
  pause(campaignId: string, options?: RequestOptions): Promise<void> {
    return this.call(pauseCampaign, undefined, { campaignId }, options);
  }

  /** Resume a paused campaign. */
  resume(campaignId: string, options?: RequestOptions): Promise<void> {
    return this.call(resumeCampaign, undefined, { campaignId }, options);
  }

  /** Suggest a daily budget for a new campaign. */
  suggestBudget(params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<SuggestBudgetResponse> {
    return this.call(suggestBudget, undefined, { ...params }, options);
  }

  /** List one page of listings suggested for a campaign. */
  suggestItems(
    campaignId: string,
    params: { categoryIds?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): Promise<TargetedAdsPagedCollection> {
    return this.call(suggestItems, undefined, { campaignId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSuggestedItems(
    campaignId: string,
    params: { categoryIds?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TargetingItems, void, undefined> {
    return this.paginate(suggestItems, undefined, { campaignId, ...params }, options);
  }

  /** Suggest a maximum cost per click for a campaign. */
  suggestMaxCpc(body: SuggestMaxCpcRequest, options?: RequestOptions): Promise<SuggestMaxCpcResponse> {
    return this.call(suggestMaxCpc, body, {}, options);
  }

  /** Change how a campaign sets its ad rates. */
  updateAdRateStrategy(campaignId: string, body: UpdateAdrateStrategyRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateAdRateStrategy, body, { campaignId }, options);
  }

  /** Change the bidding strategy of a campaign. */
  updateBiddingStrategy(
    campaignId: string,
    body: UpdateBiddingStrategyRequest,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateBiddingStrategy, body, { campaignId }, options);
  }

  /** Change the daily budget of a campaign. */
  updateBudget(
    campaignId: string,
    body: UpdateCampaignBudgetRequest,
    options?: RequestOptions,
  ): Promise<object | undefined> {
    return this.call(updateCampaignBudget, body, { campaignId }, options);
  }

  /** Rename a campaign or change its dates. */
  updateIdentification(
    campaignId: string,
    body: UpdateCampaignIdentificationRequest,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateCampaignIdentification, body, { campaignId }, options);
  }
}
