// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateAdsByInventoryReference429Response,
  PromotionsReportPagedCollection,
  SummaryReportResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPromotionReports: Operation = {
  id: 'getPromotionReports',
  method: 'GET',
  path: '/sell/marketing/v1/promotion_report',
  resource: 'promotionReports',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'promotion_status', name: 'promotionStatus', location: 'query' },
    { wire: 'promotion_type', name: 'promotionType', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'promotionReports',
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

const getPromotionSummaryReport: Operation = {
  id: 'getPromotionSummaryReport',
  method: 'GET',
  path: '/sell/marketing/v1/promotion_summary_report',
  resource: 'promotionReports',
  name: 'getSummary',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'query' }],
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

export const OPERATIONS: readonly Operation[] = [getPromotionReports, getPromotionSummaryReport];

export class PromotionReportsApi extends Resource {
  /** List one page of promotion performance reports. */
  list(
    params: {
      limit?: string;
      marketplaceId: string;
      offset?: string;
      promotionStatus?: string;
      promotionType?: string;
      q?: string;
    },
    options?: RequestOptions,
  ): Promise<PromotionsReportPagedCollection> {
    return this.call(getPromotionReports, undefined, { ...params }, options);
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
    },
    options?: RequestOptions,
  ): AsyncGenerator<models.PromotionReportDetail, void, undefined> {
    return this.paginate(getPromotionReports, undefined, { ...params }, options);
  }

  /** Get a summary of the seller's promotion performance. */
  getSummary(params: { marketplaceId: string }, options?: RequestOptions): Promise<SummaryReportResponse> {
    return this.call(getPromotionSummaryReport, undefined, { ...params }, options);
  }
}
