// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomerServiceMetric429Response, GetCustomerServiceMetricResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getCustomerServiceMetric: Operation = {
  id: 'getCustomerServiceMetric',
  method: 'GET',
  path: '/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}',
  resource: 'customerServiceMetrics',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'customer_service_metric_type', name: 'customerServiceMetricType', location: 'path' },
    { wire: 'evaluation_type', name: 'evaluationType', location: 'path' },
    { wire: 'evaluation_marketplace_id', name: 'evaluationMarketplaceId', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.analytics.readonly'] }]],
};

export const OPERATIONS: readonly Operation[] = [getCustomerServiceMetric];

export class CustomerServiceMetricsApi extends Resource {
  /** Get the seller's rating for one customer service metric. */
  get(
    customerServiceMetricType: string,
    evaluationType: string,
    params: { evaluationMarketplaceId: string },
    options?: RequestOptions,
  ): Promise<GetCustomerServiceMetricResponse> {
    return this.call(
      getCustomerServiceMetric,
      undefined,
      { customerServiceMetricType, evaluationType, ...params },
      options,
    );
  }
}
