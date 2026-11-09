// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BulkCreateAdsByInventoryReference429Response, ReportMetadata, ReportMetadatas } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getReportMetadata: Operation = {
  id: 'getReportMetadata',
  method: 'GET',
  path: '/sell/marketing/v1/ad_report_metadata',
  resource: 'reportMetadata',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'funding_model', name: 'fundingModel', location: 'query' },
    { wire: 'channel', name: 'channel', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getReportMetadataForReportType: Operation = {
  id: 'getReportMetadataForReportType',
  method: 'GET',
  path: '/sell/marketing/v1/ad_report_metadata/{report_type}',
  resource: 'reportMetadata',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'report_type', name: 'reportType', location: 'path' },
    { wire: 'funding_model', name: 'fundingModel', location: 'query' },
    { wire: 'channel', name: 'channel', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [getReportMetadata, getReportMetadataForReportType];

export class ReportMetadataApi extends Resource {
  /** List the fields of every Promoted Listings report type. */
  list(params: { fundingModel?: string; channel?: string } = {}, options?: RequestOptions): Promise<ReportMetadatas> {
    return this.call(getReportMetadata, undefined, { ...params }, options);
  }

  /** List the fields of one report type. */
  get(
    reportType: string,
    params: { fundingModel?: string; channel?: string } = {},
    options?: RequestOptions,
  ): Promise<ReportMetadata> {
    return this.call(getReportMetadataForReportType, undefined, { reportType, ...params }, options);
  }
}
