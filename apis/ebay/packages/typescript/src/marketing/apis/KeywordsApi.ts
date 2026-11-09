// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  BulkCreateKeywordRequest,
  BulkCreateKeywordResponse,
  BulkUpdateKeywordRequest,
  BulkUpdateKeywordResponse,
  CreateKeywordRequest,
  Keyword,
  KeywordPagedCollectionResponse,
  UpdateKeywordRequest,
  UpdateKeywordResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateKeyword: Operation = {
  id: 'bulkCreateKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_keyword',
  resource: 'keywords',
  name: 'bulkCreate',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateKeyword: Operation = {
  id: 'bulkUpdateKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_keyword',
  resource: 'keywords',
  name: 'bulkUpdate',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const createKeyword: Operation = {
  id: 'createKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/keyword',
  resource: 'keywords',
  name: 'create',
  host: 'api',
  params: [{ wire: 'campaign_id', name: 'campaignId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getKeyword: Operation = {
  id: 'getKeyword',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}',
  resource: 'keywords',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'keyword_id', name: 'keywordId', location: 'path' },
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

const getKeywords: Operation = {
  id: 'getKeywords',
  method: 'GET',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/keyword',
  resource: 'keywords',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'ad_group_ids', name: 'adGroupIds', location: 'query' },
    { wire: 'keyword_status', name: 'keywordStatus', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'keywords', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
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

const updateKeyword: Operation = {
  id: 'updateKeyword',
  method: 'PUT',
  path: '/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}',
  resource: 'keywords',
  name: 'update',
  host: 'api',
  params: [
    { wire: 'campaign_id', name: 'campaignId', location: 'path' },
    { wire: 'keyword_id', name: 'keywordId', location: 'path' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  bulkCreateKeyword,
  bulkUpdateKeyword,
  createKeyword,
  getKeyword,
  getKeywords,
  updateKeyword,
];

export class KeywordsApi extends Resource {
  /** Create several keywords. */
  bulkCreate(
    campaignId: string,
    body: BulkCreateKeywordRequest,
    options?: RequestOptions,
  ): Promise<BulkCreateKeywordResponse> {
    return this.call(bulkCreateKeyword, body, { campaignId }, options);
  }

  /** Change the bids or status of several keywords. */
  bulkUpdate(
    campaignId: string,
    body: BulkUpdateKeywordRequest,
    options?: RequestOptions,
  ): Promise<BulkUpdateKeywordResponse> {
    return this.call(bulkUpdateKeyword, body, { campaignId }, options);
  }

  /** Create a keyword in an ad group. */
  create(campaignId: string, body: CreateKeywordRequest, options?: RequestOptions): Promise<object> {
    return this.call(createKeyword, body, { campaignId }, options);
  }

  /** Get one keyword. */
  get(campaignId: string, keywordId: string, options?: RequestOptions): Promise<Keyword> {
    return this.call(getKeyword, undefined, { campaignId, keywordId }, options);
  }

  /** List one page of a campaign's keywords. */
  list(
    campaignId: string,
    params: { adGroupIds?: string; keywordStatus?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): Promise<KeywordPagedCollectionResponse> {
    return this.call(getKeywords, undefined, { campaignId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    campaignId: string,
    params: { adGroupIds?: string; keywordStatus?: string; limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Keyword, void, undefined> {
    return this.paginate(getKeywords, undefined, { campaignId, ...params }, options);
  }

  /** Change the bid or status of a keyword. */
  update(
    campaignId: string,
    keywordId: string,
    body: UpdateKeywordRequest,
    options?: RequestOptions,
  ): Promise<UpdateKeywordResponse | undefined> {
    return this.call(updateKeyword, body, { campaignId, keywordId }, options);
  }
}
