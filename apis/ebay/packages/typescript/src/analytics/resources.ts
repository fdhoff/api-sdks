// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  CustomerServiceMetricsApi,
  OPERATIONS as CustomerServiceMetricsApiOperations,
} from './apis/CustomerServiceMetricsApi.js';
import {
  SellerStandardsProfilesApi,
  OPERATIONS as SellerStandardsProfilesApiOperations,
} from './apis/SellerStandardsProfilesApi.js';
import { TrafficReportsApi, OPERATIONS as TrafficReportsApiOperations } from './apis/TrafficReportsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...CustomerServiceMetricsApiOperations, ...SellerStandardsProfilesApiOperations, ...TrafficReportsApiOperations].map(
    (operation) => [operation.id, operation],
  ),
);

export class Resources {
  readonly customerServiceMetrics: CustomerServiceMetricsApi;
  readonly sellerStandardsProfiles: SellerStandardsProfilesApi;
  readonly trafficReports: TrafficReportsApi;

  constructor(transport: Transport) {
    this.customerServiceMetrics = new CustomerServiceMetricsApi(transport);
    this.sellerStandardsProfiles = new SellerStandardsProfilesApi(transport);
    this.trafficReports = new TrafficReportsApi(transport);
  }
}
