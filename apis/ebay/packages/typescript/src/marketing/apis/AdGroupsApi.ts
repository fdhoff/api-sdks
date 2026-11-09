// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AdGroup,
  AdGroupPagedCollectionResponse,
  BulkCreateAdsByInventoryReference429Response,
  CreateAdGroupRequest,
  TargetedBidRequest,
  TargetedBidsPagedCollection,
  TargetedKeywordRequest,
  TargetedKeywordsPagedCollection,
  UpdateAdGroupRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createAdGroup: Operation = {
  id: 'createAdGroup',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group',
  resource: 'adGroups',
  name: 'create',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getAdGroup: Operation = {
  id: 'getAdGroup',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}',
  resource: 'adGroups',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'ad_group_id', name: 'adGroupId', location: 'path' },
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

const getAdGroups: Operation = {
  id: 'getAdGroups',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group',
  resource: 'adGroups',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'ad_group_status', name: 'adGroupStatus', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'adGroups', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
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

const suggestBids: Operation = {
  id: 'suggestBids',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids',
  resource: 'adGroups',
  name: 'suggestBids',
  host: 'api',
  params: [
    { wire: 'ad_group_id', name: 'adGroupId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const suggestKeywords: Operation = {
  id: 'suggestKeywords',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords',
  resource: 'adGroups',
  name: 'suggestKeywords',
  host: 'api',
  params: [
    { wire: 'ad_group_id', name: 'adGroupId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateAdGroup: Operation = {
  id: 'updateAdGroup',
  method: 'PUT',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}',
  resource: 'adGroups',
  name: 'update',
  host: 'api',
  params: [
    { wire: 'ad_group_id', name: 'adGroupId', location: 'path' },
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createAdGroup,
  getAdGroup,
  getAdGroups,
  suggestBids,
  suggestKeywords,
  updateAdGroup,
];

export class AdGroupsApi extends Resource {
  /** Create an ad group in a campaign. */
  create(campaignId: string, body: CreateAdGroupRequest, options?: RequestOptions): Promise<object> {
    return this.call(createAdGroup, body, { campaignId }, options);
  }

  /** Get one ad group. */
  get(adGroupId: string, campaignId: string, options?: RequestOptions): Promise<AdGroup> {
    return this.call(getAdGroup, undefined, { adGroupId, campaignId }, options);
  }

  /** List one page of a campaign's ad groups. */
  list(
    campaignId: string,
    params: { adGroupStatus?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): Promise<AdGroupPagedCollectionResponse> {
    return this.call(getAdGroups, undefined, { campaignId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    campaignId: string,
    params: { adGroupStatus?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.AdGroup, void, undefined> {
    return this.paginate(getAdGroups, undefined, { campaignId, ...params }, options);
  }

  /** Suggest bids for keywords in an ad group. */
  suggestBids(
    adGroupId: string,
    campaignId: string,
    body: TargetedBidRequest,
    options?: RequestOptions,
  ): Promise<TargetedBidsPagedCollection> {
    return this.call(suggestBids, body, { adGroupId, campaignId }, options);
  }

  /** Suggest keywords for an ad group. */
  suggestKeywords(
    adGroupId: string,
    campaignId: string,
    body?: TargetedKeywordRequest,
    options?: RequestOptions,
  ): Promise<TargetedKeywordsPagedCollection> {
    return this.call(suggestKeywords, body, { adGroupId, campaignId }, options);
  }

  /** Update an ad group. */
  update(
    adGroupId: string,
    campaignId: string,
    body: UpdateAdGroupRequest,
    options?: RequestOptions,
  ): Promise<Error | undefined> {
    return this.call(updateAdGroup, body, { adGroupId, campaignId }, options);
  }
}
