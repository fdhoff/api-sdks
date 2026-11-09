// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AwaitingFeedbackResponse,
  GetFeedbackRatingSummaryResponse,
  GetFeedbackResponse,
  GetItemsAwaitingFeedback429Response,
  LeaveFeedbackRequest,
  LeaveFeedbackResponse,
  RespondToFeedbackRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getFeedback: Operation = {
  id: 'getFeedback',
  method: 'GET',
  path: '/commerce/feedback/v1/feedback',
  resource: 'feedback',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'feedback_id', name: 'feedbackId', location: 'query' },
    { wire: 'feedback_type', name: 'feedbackType', location: 'query' },
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'listing_id', name: 'listingId', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'order_line_item_id', name: 'orderLineItemId', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'transaction_id', name: 'transactionId', location: 'query' },
    { wire: 'user_id', name: 'userId', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/commerce.feedback',
          'https://api.ebay.com/oauth/api_scope/commerce.feedback.readonly',
        ],
      },
    ],
  ],
};

const getFeedbackRatingSummary: Operation = {
  id: 'getFeedbackRatingSummary',
  method: 'GET',
  path: '/commerce/feedback/v1/feedback_rating_summary',
  resource: 'feedback',
  name: 'getRatingSummary',
  host: 'api',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'user_id', name: 'userId', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/commerce.feedback',
          'https://api.ebay.com/oauth/api_scope/commerce.feedback.readonly',
        ],
      },
    ],
  ],
};

const getItemsAwaitingFeedback: Operation = {
  id: 'getItemsAwaitingFeedback',
  method: 'GET',
  path: '/commerce/feedback/v1/awaiting_feedback',
  resource: 'feedback',
  name: 'listAwaiting',
  host: 'api',
  params: [
    { wire: 'filter', name: 'filter', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.feedback'] }]],
};

const leaveFeedback: Operation = {
  id: 'leaveFeedback',
  method: 'POST',
  path: '/commerce/feedback/v1/feedback',
  resource: 'feedback',
  name: 'leave',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.feedback'] }]],
};

const respondToFeedback: Operation = {
  id: 'respondToFeedback',
  method: 'POST',
  path: '/commerce/feedback/v1/respond_to_feedback',
  resource: 'feedback',
  name: 'respond',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.feedback'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getFeedback,
  getFeedbackRatingSummary,
  getItemsAwaitingFeedback,
  leaveFeedback,
  respondToFeedback,
];

export class FeedbackApi extends Resource {
  /** List one page of feedback a user left or received. */
  list(
    params: {
      feedbackId?: string;
      feedbackType: string;
      filter?: string;
      limit?: string;
      listingId?: string;
      offset?: string;
      orderLineItemId?: string;
      sort?: string;
      transactionId?: string;
      userId: string;
    },
    options?: RequestOptions,
  ): Promise<GetFeedbackResponse> {
    return this.call(getFeedback, undefined, { ...params }, options);
  }

  /** Get a user's feedback rating summary. */
  getRatingSummary(
    params: { filter: string; userId: string },
    options?: RequestOptions,
  ): Promise<GetFeedbackRatingSummaryResponse> {
    return this.call(getFeedbackRatingSummary, undefined, { ...params }, options);
  }

  /** List one page of the order line items still waiting for feedback. */
  listAwaiting(
    params: { filter?: string; limit?: string; offset?: string; sort?: string } = {},
    options?: RequestOptions,
  ): Promise<AwaitingFeedbackResponse> {
    return this.call(getItemsAwaitingFeedback, undefined, { ...params }, options);
  }

  /** Leave feedback for the other party of an order line item. */
  leave(body?: LeaveFeedbackRequest, options?: RequestOptions): Promise<LeaveFeedbackResponse> {
    return this.call(leaveFeedback, body, {}, options);
  }

  /** Reply to feedback */
  respond(body?: RespondToFeedbackRequest, options?: RequestOptions): Promise<object> {
    return this.call(respondToFeedback, body, {}, options);
  }
}
