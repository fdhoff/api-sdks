// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CheckCancellationEligibility429Response,
  EscalateInquiryRequest,
  InquiryDetailsResponse,
  InquirySearchResponse,
  InquiryVoluntaryRefundRequest,
  SendMessageRequest,
  ShipmentInfoRequest,
  VoluntaryRefundResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const escalateInquiry: Operation = {
  id: 'escalateInquiry',
  method: 'POST',
  path: '/post-order/v2/inquiry/{inquiryId}/escalate',
  resource: 'inquiries',
  name: 'escalate',
  host: 'api',
  params: [
    { wire: 'inquiryId', name: 'inquiryId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const getInquiry: Operation = {
  id: 'getInquiry',
  method: 'GET',
  path: '/post-order/v2/inquiry/{inquiryId}',
  resource: 'inquiries',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'inquiryId', name: 'inquiryId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const issueInquiryRefund: Operation = {
  id: 'issueInquiryRefund',
  method: 'POST',
  path: '/post-order/v2/inquiry/{inquiryId}/issue_refund',
  resource: 'inquiries',
  name: 'issueRefund',
  host: 'api',
  params: [
    { wire: 'inquiryId', name: 'inquiryId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const provideInquiryShipmentInfo: Operation = {
  id: 'provideInquiryShipmentInfo',
  method: 'POST',
  path: '/post-order/v2/inquiry/{inquiryId}/provide_shipment_info',
  resource: 'inquiries',
  name: 'provideShipmentInfo',
  host: 'api',
  params: [
    { wire: 'inquiryId', name: 'inquiryId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const searchInquiries: Operation = {
  id: 'searchInquiries',
  method: 'GET',
  path: '/post-order/v2/inquiry/search',
  resource: 'inquiries',
  name: 'search',
  host: 'api',
  params: [
    { wire: 'fieldgroups', name: 'fieldgroups', location: 'query' },
    { wire: 'inquiry_creation_date_range_from', name: 'inquiryCreationDateRangeFrom', location: 'query' },
    { wire: 'inquiry_creation_date_range_to', name: 'inquiryCreationDateRangeTo', location: 'query' },
    { wire: 'inquiry_status', name: 'inquiryStatus', location: 'query' },
    { wire: 'item_id', name: 'itemId', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'transaction_id', name: 'transactionId', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

const sendInquiryMessage: Operation = {
  id: 'sendInquiryMessage',
  method: 'POST',
  path: '/post-order/v2/inquiry/{inquiryId}/send_message',
  resource: 'inquiries',
  name: 'sendMessage',
  host: 'api',
  params: [
    { wire: 'inquiryId', name: 'inquiryId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  escalateInquiry,
  getInquiry,
  issueInquiryRefund,
  provideInquiryShipmentInfo,
  searchInquiries,
  sendInquiryMessage,
];

export class InquiriesApi extends Resource {
  /** Escalate an inquiry to a case. */
  escalate(
    inquiryId: string,
    body: EscalateInquiryRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(escalateInquiry, body, { inquiryId, ...params }, options);
  }

  /** Get one item-not-received inquiry. */
  get(
    inquiryId: string,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<InquiryDetailsResponse> {
    return this.call(getInquiry, undefined, { inquiryId, ...params }, options);
  }

  /** Refund the buyer to settle an inquiry. */
  issueRefund(
    inquiryId: string,
    body?: InquiryVoluntaryRefundRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<VoluntaryRefundResponse> {
    return this.call(issueInquiryRefund, body, { inquiryId, ...params }, options);
  }

  /** Give the shipment tracking for an inquiry. */
  provideShipmentInfo(
    inquiryId: string,
    body: ShipmentInfoRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(provideInquiryShipmentInfo, body, { inquiryId, ...params }, options);
  }

  /** Search one page of inquiries. */
  search(
    params: {
      fieldgroups?: string;
      inquiryCreationDateRangeFrom?: string;
      inquiryCreationDateRangeTo?: string;
      inquiryStatus?: string;
      itemId?: string;
      limit?: string;
      offset?: string;
      orderId?: string;
      sort?: string;
      transactionId?: string;
      marketplaceId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<InquirySearchResponse> {
    return this.call(searchInquiries, undefined, { ...params }, options);
  }

  /** Send the buyer a message about an inquiry. */
  sendMessage(
    inquiryId: string,
    body: SendMessageRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(sendInquiryMessage, body, { inquiryId, ...params }, options);
  }
}
