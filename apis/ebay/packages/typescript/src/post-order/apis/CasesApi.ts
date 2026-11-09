// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AppealRequest,
  CaseDetailsResponse,
  CaseSearchResponse,
  CheckCancellationEligibility429Response,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const appealCaseDecision: Operation = {
  id: 'appealCaseDecision',
  method: 'POST',
  path: '/post-order/v2/casemanagement/{caseId}/appeal',
  resource: 'cases',
  name: 'appeal',
  host: 'api',
  params: [
    { wire: 'caseId', name: 'caseId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getCase: Operation = {
  id: 'getCase',
  method: 'GET',
  path: '/post-order/v2/casemanagement/{caseId}',
  resource: 'cases',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'caseId', name: 'caseId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const searchCases: Operation = {
  id: 'searchCases',
  method: 'GET',
  path: '/post-order/v2/casemanagement/search',
  resource: 'cases',
  name: 'search',
  host: 'api',
  params: [
    { wire: 'case_creation_date_range_from', name: 'caseCreationDateRangeFrom', location: 'query' },
    { wire: 'case_creation_date_range_to', name: 'caseCreationDateRangeTo', location: 'query' },
    { wire: 'case_status_filter', name: 'caseStatusFilter', location: 'query' },
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'item_id', name: 'itemId', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'return_id', name: 'returnId', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'transaction_id', name: 'transactionId', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [appealCaseDecision, getCase, searchCases];

export class CasesApi extends Resource {
  /** Appeal the decision on a case. */
  appeal(
    caseId: string,
    body?: AppealRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(appealCaseDecision, body, { caseId, ...params }, options);
  }

  /** Get one case. */
  get(caseId: string, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<CaseDetailsResponse> {
    return this.call(getCase, undefined, { caseId, ...params }, options);
  }

  /** Search one page of cases. */
  search(
    params: {
      caseCreationDateRangeFrom?: string;
      caseCreationDateRangeTo?: string;
      caseStatusFilter?: string;
      fieldgroups?: string;
      itemId?: string;
      limit?: string;
      offset?: string;
      orderId?: string;
      returnId?: string;
      sort?: string;
      transactionId?: string;
      marketplaceId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<CaseSearchResponse> {
    return this.call(searchCases, undefined, { ...params }, options);
  }
}
