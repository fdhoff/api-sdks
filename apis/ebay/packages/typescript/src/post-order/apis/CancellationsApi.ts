// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CheckCancellationEligibility429Response,
  CreateCancelRequest,
  CreateCancelResponse,
  FindCancelResponse,
  GetCancelDetailResponse,
  OrderEligibilityCheckInfo,
  OrderEligibilityResult,
  RejectCancelRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const approveCancellation: Operation = {
  id: 'approveCancellation',
  method: 'POST',
  path: '/post-order/v2/cancellation/{cancelId}/approve',
  resource: 'cancellations',
  name: 'approve',
  host: 'api',
  params: [
    { wire: 'cancelId', name: 'cancelId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const checkCancellationEligibility: Operation = {
  id: 'checkCancellationEligibility',
  method: 'POST',
  path: '/post-order/v2/cancellation/check_eligibility',
  resource: 'cancellations',
  name: 'checkEligibility',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const createCancellationRequest: Operation = {
  id: 'createCancellationRequest',
  method: 'POST',
  path: '/post-order/v2/cancellation',
  resource: 'cancellations',
  name: 'create',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getCancellation: Operation = {
  id: 'getCancellation',
  method: 'GET',
  path: '/post-order/v2/cancellation/{cancelId}',
  resource: 'cancellations',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'cancelId', name: 'cancelId', location: 'path' },
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const rejectCancellation: Operation = {
  id: 'rejectCancellation',
  method: 'POST',
  path: '/post-order/v2/cancellation/{cancelId}/reject',
  resource: 'cancellations',
  name: 'reject',
  host: 'api',
  params: [
    { wire: 'cancelId', name: 'cancelId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const searchCancellations: Operation = {
  id: 'searchCancellations',
  method: 'GET',
  path: '/post-order/v2/cancellation/search',
  resource: 'cancellations',
  name: 'search',
  host: 'api',
  params: [
    { wire: 'cancel_id', name: 'cancelId', location: 'query' },
    { wire: 'creation_date_range_from', name: 'creationDateRangeFrom', location: 'query' },
    { wire: 'creation_date_range_to', name: 'creationDateRangeTo', location: 'query' },
    { wire: 'item_id', name: 'itemId', location: 'query' },
    { wire: 'legacy_order_id', name: 'legacyOrderId', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'role', name: 'role', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'transaction_id', name: 'transactionId', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  approveCancellation,
  checkCancellationEligibility,
  createCancellationRequest,
  getCancellation,
  rejectCancellation,
  searchCancellations,
];

export class CancellationsApi extends Resource {
  /** Approve a buyer's cancellation request. */
  approve(cancelId: string, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<object> {
    return this.call(approveCancellation, undefined, { cancelId, ...params }, options);
  }

  /** Check whether an order can be cancelled. */
  checkEligibility(
    body: OrderEligibilityCheckInfo,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<OrderEligibilityResult> {
    return this.call(checkCancellationEligibility, body, { ...params }, options);
  }

  /** Ask to cancel an order. */
  create(
    body: CreateCancelRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<CreateCancelResponse> {
    return this.call(createCancellationRequest, body, { ...params }, options);
  }

  /** Get one cancellation request. */
  get(
    cancelId: string,
    params: { fieldgroups?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetCancelDetailResponse> {
    return this.call(getCancellation, undefined, { cancelId, ...params }, options);
  }

  /** Reject a buyer's cancellation request. */
  reject(
    cancelId: string,
    body?: RejectCancelRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(rejectCancellation, body, { cancelId, ...params }, options);
  }

  /** Search one page of cancellation requests. */
  search(
    params: {
      cancelId?: string;
      creationDateRangeFrom?: string;
      creationDateRangeTo?: string;
      itemId?: string;
      legacyOrderId?: string;
      limit?: string;
      offset?: string;
      role?: string;
      sort?: string;
      transactionId?: string;
      marketplaceId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<FindCancelResponse> {
    return this.call(searchCancellations, undefined, { ...params }, options);
  }
}
