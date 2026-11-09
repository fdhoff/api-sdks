// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  BulkCreateNegativeKeywordRequest,
  BulkCreateNegativeKeywordResponse,
  BulkUpdateNegativeKeywordRequest,
  BulkUpdateNegativeKeywordResponse,
  CreateNegativeKeywordRequest,
  NegativeKeyword,
  NegativeKeywordPagedCollectionResponse,
  UpdateNegativeKeywordRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateNegativeKeyword: Operation = {
  id: 'bulkCreateNegativeKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/bulk_create_negative_keyword',
  resource: 'negativeKeywords',
  name: 'bulkCreate',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const bulkUpdateNegativeKeyword: Operation = {
  id: 'bulkUpdateNegativeKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/bulk_update_negative_keyword',
  resource: 'negativeKeywords',
  name: 'bulkUpdate',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const createNegativeKeyword: Operation = {
  id: 'createNegativeKeyword',
  method: 'POST',
  path: '/sell/marketing/v1/negative_keyword',
  resource: 'negativeKeywords',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getNegativeKeyword: Operation = {
  id: 'getNegativeKeyword',
  method: 'GET',
  path: '/sell/marketing/v1/negative_keyword/{negative_keyword_id}',
  resource: 'negativeKeywords',
  name: 'get',
  host: 'api',
  params: [{ wire: 'negative_keyword_id', name: 'negativeKeywordId', location: 'path' }],
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

const getNegativeKeywords: Operation = {
  id: 'getNegativeKeywords',
  method: 'GET',
  path: '/sell/marketing/v1/negative_keyword',
  resource: 'negativeKeywords',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'ad_group_ids', name: 'adGroupIds', location: 'query' },
    { wire: 'campaign_ids', name: 'campaignIds', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'negative_keyword_status', name: 'negativeKeywordStatus', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'negativeKeywords',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
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

const updateNegativeKeyword: Operation = {
  id: 'updateNegativeKeyword',
  method: 'PUT',
  path: '/sell/marketing/v1/negative_keyword/{negative_keyword_id}',
  resource: 'negativeKeywords',
  name: 'update',
  host: 'api',
  params: [{ wire: 'negative_keyword_id', name: 'negativeKeywordId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  bulkCreateNegativeKeyword,
  bulkUpdateNegativeKeyword,
  createNegativeKeyword,
  getNegativeKeyword,
  getNegativeKeywords,
  updateNegativeKeyword,
];

export class NegativeKeywordsApi extends Resource {
  /** Create several negative keywords. */
  bulkCreate(
    body: BulkCreateNegativeKeywordRequest,
    options?: RequestOptions,
  ): Promise<BulkCreateNegativeKeywordResponse> {
    return this.call(bulkCreateNegativeKeyword, body, {}, options);
  }

  /** Change the status of several negative keywords. */
  bulkUpdate(
    body: BulkUpdateNegativeKeywordRequest,
    options?: RequestOptions,
  ): Promise<BulkUpdateNegativeKeywordResponse> {
    return this.call(bulkUpdateNegativeKeyword, body, {}, options);
  }

  /** Create a negative keyword. */
  create(body: CreateNegativeKeywordRequest, options?: RequestOptions): Promise<object> {
    return this.call(createNegativeKeyword, body, {}, options);
  }

  /** Get one negative keyword. */
  get(negativeKeywordId: string, options?: RequestOptions): Promise<NegativeKeyword> {
    return this.call(getNegativeKeyword, undefined, { negativeKeywordId }, options);
  }

  /** List one page of negative keywords. */
  list(
    params: {
      adGroupIds?: string;
      campaignIds?: string;
      limit?: string;
      negativeKeywordStatus?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<NegativeKeywordPagedCollectionResponse> {
    return this.call(getNegativeKeywords, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      adGroupIds?: string;
      campaignIds?: string;
      limit?: string;
      negativeKeywordStatus?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.NegativeKeyword, void, undefined> {
    return this.paginate(getNegativeKeywords, undefined, { ...params }, options);
  }

  /** Change the status of a negative keyword. */
  update(negativeKeywordId: string, body: UpdateNegativeKeywordRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateNegativeKeyword, body, { negativeKeywordId }, options);
  }
}
