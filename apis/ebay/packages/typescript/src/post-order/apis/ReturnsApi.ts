// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CheckCancellationEligibility429Response,
  CreateReturnRequest,
  CreateReturnResponse,
  DecideReturnRequest,
  DecideReturnResponse,
  EscalateRequest,
  EscalateResponse,
  GetDetailResponse,
  GetFileResponse,
  GetSummaryResponse,
  GetTrackingHistoryResponse,
  IssueRefundRequest,
  IssueRefundResponse,
  MarkAsReceivedRequest,
  ProvideLabelRequest,
  ProvideLabelResponse,
  SendMessageRequest,
  UploadFileRequest,
  UploadFileResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const addShippingLabelInfo: Operation = {
  id: 'addShippingLabelInfo',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/add_shipping_label',
  resource: 'returns',
  name: 'addShippingLabel',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const createReturnRequest: Operation = {
  id: 'createReturnRequest',
  method: 'POST',
  path: '/post-order/v2/return',
  resource: 'returns',
  name: 'create',
  host: 'api',
  params: [
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const escalateReturn: Operation = {
  id: 'escalateReturn',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/escalate',
  resource: 'returns',
  name: 'escalate',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getReturn: Operation = {
  id: 'getReturn',
  method: 'GET',
  path: '/post-order/v2/return/{returnId}',
  resource: 'returns',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getReturnFiles: Operation = {
  id: 'getReturnFiles',
  method: 'GET',
  path: '/post-order/v2/return/{returnId}/files',
  resource: 'returns',
  name: 'listFiles',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getShipmentTrackingInfo: Operation = {
  id: 'getShipmentTrackingInfo',
  method: 'GET',
  path: '/post-order/v2/return/{returnId}/tracking',
  resource: 'returns',
  name: 'getTracking',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'carrier_used', name: 'carrierUsed', location: 'query' },
    { wire: 'tracking_number', name: 'trackingNumber', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const issueReturnRefund: Operation = {
  id: 'issueReturnRefund',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/issue_refund',
  resource: 'returns',
  name: 'issueRefund',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const markItemReceived: Operation = {
  id: 'markItemReceived',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/mark_as_received',
  resource: 'returns',
  name: 'markReceived',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const processReturnRequest: Operation = {
  id: 'processReturnRequest',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/decide',
  resource: 'returns',
  name: 'decide',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const searchReturns: Operation = {
  id: 'searchReturns',
  method: 'GET',
  path: '/post-order/v2/return/search',
  resource: 'returns',
  name: 'search',
  host: 'api',
  params: [
    { wire: 'creation_date_range_from', name: 'creationDateRangeFrom', location: 'query' },
    { wire: 'creation_date_range_to', name: 'creationDateRangeTo', location: 'query' },
    { wire: 'item_id', name: 'itemId', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'return_id', name: 'returnId', location: 'query' },
    { wire: 'return_state', name: 'returnState', location: 'query' },
    { wire: 'role', name: 'role', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'states', name: 'states', location: 'query' },
    { wire: 'transaction_id', name: 'transactionId', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const sendReturnMessage: Operation = {
  id: 'sendReturnMessage',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/send_message',
  resource: 'returns',
  name: 'sendMessage',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const uploadReturnFile: Operation = {
  id: 'uploadReturnFile',
  method: 'POST',
  path: '/post-order/v2/return/{returnId}/file/upload',
  resource: 'returns',
  name: 'uploadFile',
  host: 'api',
  params: [
    { wire: 'returnId', name: 'returnId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  addShippingLabelInfo,
  createReturnRequest,
  escalateReturn,
  getReturn,
  getReturnFiles,
  getShipmentTrackingInfo,
  issueReturnRefund,
  markItemReceived,
  processReturnRequest,
  searchReturns,
  sendReturnMessage,
  uploadReturnFile,
];

export class ReturnsApi extends Resource {
  /** Give the buyer a return shipping label, or say why there is none. */
  addShippingLabel(
    returnId: string,
    body: ProvideLabelRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<ProvideLabelResponse> {
    return this.call(addShippingLabelInfo, body, { returnId, ...params }, options);
  }

  /** Create a return request. */
  create(
    body: CreateReturnRequest,
    params: { fieldgroups?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<CreateReturnResponse> {
    return this.call(createReturnRequest, body, { ...params }, options);
  }

  /** Escalate a return request to a case. */
  escalate(
    returnId: string,
    body: EscalateRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<EscalateResponse> {
    return this.call(escalateReturn, body, { returnId, ...params }, options);
  }

  /** Get one return request. */
  get(
    returnId: string,
    params: { fieldgroups?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetDetailResponse> {
    return this.call(getReturn, undefined, { returnId, ...params }, options);
  }

  /** List the files attached to a return request. */
  listFiles(
    returnId: string,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetFileResponse> {
    return this.call(getReturnFiles, undefined, { returnId, ...params }, options);
  }

  /** Get the tracking of a return shipment. */
  getTracking(
    returnId: string,
    params: { carrierUsed?: string; trackingNumber?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetTrackingHistoryResponse> {
    return this.call(getShipmentTrackingInfo, undefined, { returnId, ...params }, options);
  }

  /** Refund the buyer for a return. */
  issueRefund(
    returnId: string,
    body: IssueRefundRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<IssueRefundResponse> {
    return this.call(issueReturnRefund, body, { returnId, ...params }, options);
  }

  /** Mark a returned item received. */
  markReceived(
    returnId: string,
    body?: MarkAsReceivedRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(markItemReceived, body, { returnId, ...params }, options);
  }

  /** Accept or decline a return request, or offer a partial refund. */
  decide(
    returnId: string,
    body: DecideReturnRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<DecideReturnResponse> {
    return this.call(processReturnRequest, body, { returnId, ...params }, options);
  }

  /** Search one page of return requests. */
  search(
    params: {
      creationDateRangeFrom?: string;
      creationDateRangeTo?: string;
      itemId?: string;
      limit?: string;
      offset?: string;
      orderId?: string;
      returnId?: string;
      returnState?: string;
      role?: string;
      sort?: string;
      states?: string;
      transactionId?: string;
      marketplaceId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<GetSummaryResponse> {
    return this.call(searchReturns, undefined, { ...params }, options);
  }

  /** Send the buyer a message about a return. */
  sendMessage(
    returnId: string,
    body: SendMessageRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(sendReturnMessage, body, { returnId, ...params }, options);
  }

  /** Attach a base64-encoded file to a return request. */
  uploadFile(
    returnId: string,
    body: UploadFileRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<UploadFileResponse> {
    return this.call(uploadReturnFile, body, { returnId, ...params }, options);
  }
}
