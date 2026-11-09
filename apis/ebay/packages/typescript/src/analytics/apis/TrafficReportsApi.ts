// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomerServiceMetric429Response, Report } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getTrafficReport: Operation = {
  id: 'getTrafficReport',
  method: 'GET',
  path: '/sell/analytics/v1/traffic_report',
  resource: 'trafficReports',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'dimension', name: 'dimension', location: 'query' },
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'metric', name: 'metric', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

export const OPERATIONS: readonly Operation[] = [getTrafficReport];

export class TrafficReportsApi extends Resource {
  /** Get a traffic report of the seller's listings. */
  get(
    params: { dimension?: string; filter?: string; metric?: string; sort?: string } = {},
    options?: RequestOptions,
  ): Promise<Report> {
    return this.call(getTrafficReport, undefined, { ...params }, options);
  }
}
