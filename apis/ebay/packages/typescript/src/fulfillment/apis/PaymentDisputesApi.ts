// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AcceptPaymentDisputeRequest,
  AddEvidencePaymentDisputeRequest,
  AddEvidencePaymentDisputeResponse,
  ContestPaymentDisputeRequest,
  DisputeSummaryResponse,
  FileEvidence,
  GetOrder429Response,
  PaymentDispute,
  PaymentDisputeActivityHistory,
  UpdateEvidencePaymentDisputeRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const acceptPaymentDispute: Operation = {
  id: 'acceptPaymentDispute',
  method: 'POST',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/accept',
  resource: 'paymentDisputes',
  name: 'accept',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const addEvidence: Operation = {
  id: 'addEvidence',
  method: 'POST',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/add_evidence',
  resource: 'paymentDisputes',
  name: 'addEvidence',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const contestPaymentDispute: Operation = {
  id: 'contestPaymentDispute',
  method: 'POST',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/contest',
  resource: 'paymentDisputes',
  name: 'contest',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const getActivities: Operation = {
  id: 'getActivities',
  method: 'GET',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/activity',
  resource: 'paymentDisputes',
  name: 'listActivities',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const getPaymentDispute: Operation = {
  id: 'getPaymentDispute',
  method: 'GET',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}',
  resource: 'paymentDisputes',
  name: 'get',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const getPaymentDisputeSummaries: Operation = {
  id: 'getPaymentDisputeSummaries',
  method: 'GET',
  path: '/sell/fulfillment/v1/payment_dispute_summary',
  resource: 'paymentDisputes',
  name: 'listSummaries',
  host: 'apiz',
  params: [
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'buyer_username', name: 'buyerUsername', location: 'query' },
    { wire: 'open_date_from', name: 'openDateFrom', location: 'query' },
    { wire: 'open_date_to', name: 'openDateTo', location: 'query' },
    { wire: 'payment_dispute_status', name: 'paymentDisputeStatus', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSummaries',
  paging: {
    style: 'next_link',
    items: 'paymentDisputeSummaries',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const updateEvidence: Operation = {
  id: 'updateEvidence',
  method: 'POST',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/update_evidence',
  resource: 'paymentDisputes',
  name: 'updateEvidence',
  host: 'apiz',
  params: [{ wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

const uploadEvidenceFile: Operation = {
  id: 'uploadEvidenceFile',
  method: 'POST',
  path: '/sell/fulfillment/v1/payment_dispute/{payment_dispute_id}/upload_evidence_file',
  resource: 'paymentDisputes',
  name: 'uploadEvidenceFile',
  host: 'apiz',
  params: [
    { wire: 'payment_dispute_id', name: 'paymentDisputeId', location: 'path' },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.payment.dispute'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  acceptPaymentDispute,
  addEvidence,
  contestPaymentDispute,
  getActivities,
  getPaymentDispute,
  getPaymentDisputeSummaries,
  updateEvidence,
  uploadEvidenceFile,
];

export class PaymentDisputesApi extends Resource {
  /** Accept a payment dispute. */
  accept(paymentDisputeId: string, body?: AcceptPaymentDisputeRequest, options?: RequestOptions): Promise<void> {
    return this.call(acceptPaymentDispute, body, { paymentDisputeId }, options);
  }

  /** Add a set of uploaded evidence files to a payment dispute. */
  addEvidence(
    paymentDisputeId: string,
    body?: AddEvidencePaymentDisputeRequest,
    options?: RequestOptions,
  ): Promise<AddEvidencePaymentDisputeResponse> {
    return this.call(addEvidence, body, { paymentDisputeId }, options);
  }

  /** Contest a payment dispute. */
  contest(paymentDisputeId: string, body?: ContestPaymentDisputeRequest, options?: RequestOptions): Promise<void> {
    return this.call(contestPaymentDispute, body, { paymentDisputeId }, options);
  }

  /** List the activity on a payment dispute. */
  listActivities(paymentDisputeId: string, options?: RequestOptions): Promise<PaymentDisputeActivityHistory> {
    return this.call(getActivities, undefined, { paymentDisputeId }, options);
  }

  /** Get one payment dispute. */
  get(paymentDisputeId: string, options?: RequestOptions): Promise<PaymentDispute> {
    return this.call(getPaymentDispute, undefined, { paymentDisputeId }, options);
  }

  /** List one page of the seller's payment disputes. */
  listSummaries(
    params: {
      orderId?: string;
      buyerUsername?: string;
      openDateFrom?: string;
      openDateTo?: string;
      paymentDisputeStatus?: string;
      limit?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<DisputeSummaryResponse> {
    return this.call(getPaymentDisputeSummaries, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSummaries(
    params: {
      orderId?: string;
      buyerUsername?: string;
      openDateFrom?: string;
      openDateTo?: string;
      paymentDisputeStatus?: string;
      limit?: string;
      offset?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PaymentDisputeSummary, void, undefined> {
    return this.paginate(getPaymentDisputeSummaries, undefined, { ...params }, options);
  }

  /** Add uploaded files to an existing set of evidence. */
  updateEvidence(
    paymentDisputeId: string,
    body?: UpdateEvidencePaymentDisputeRequest,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateEvidence, body, { paymentDisputeId }, options);
  }

  /** Upload a file to use as evidence in a payment dispute. */
  uploadEvidenceFile(
    paymentDisputeId: string,
    params: { file: FileInput },
    options?: RequestOptions,
  ): Promise<FileEvidence> {
    return this.call(uploadEvidenceFile, undefined, { paymentDisputeId, ...params }, options);
  }
}
