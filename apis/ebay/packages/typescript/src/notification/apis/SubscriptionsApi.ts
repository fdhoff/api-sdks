// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateSubscriptionFilterRequest,
  CreateSubscriptionRequest,
  GetConfig429Response,
  Subscription,
  SubscriptionFilter,
  SubscriptionSearchResponse,
  UpdateSubscriptionRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createSubscription: Operation = {
  id: 'createSubscription',
  method: 'POST',
  path: '/commerce/notification/v1/subscription',
  resource: 'subscriptions',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const createSubscriptionFilter: Operation = {
  id: 'createSubscriptionFilter',
  method: 'POST',
  path: '/commerce/notification/v1/subscription/{subscription_id}/filter',
  resource: 'subscriptions',
  name: 'createFilter',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const deleteSubscription: Operation = {
  id: 'deleteSubscription',
  method: 'DELETE',
  path: '/commerce/notification/v1/subscription/{subscription_id}',
  resource: 'subscriptions',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const deleteSubscriptionFilter: Operation = {
  id: 'deleteSubscriptionFilter',
  method: 'DELETE',
  path: '/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}',
  resource: 'subscriptions',
  name: 'deleteFilter',
  host: 'api',
  params: [
    { wire: 'filter_id', name: 'filterId', location: 'path' },
    { wire: 'subscription_id', name: 'subscriptionId', location: 'path' },
  ],
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const disableSubscription: Operation = {
  id: 'disableSubscription',
  method: 'POST',
  path: '/commerce/notification/v1/subscription/{subscription_id}/disable',
  resource: 'subscriptions',
  name: 'disable',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const enableSubscription: Operation = {
  id: 'enableSubscription',
  method: 'POST',
  path: '/commerce/notification/v1/subscription/{subscription_id}/enable',
  resource: 'subscriptions',
  name: 'enable',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const getSubscription: Operation = {
  id: 'getSubscription',
  method: 'GET',
  path: '/commerce/notification/v1/subscription/{subscription_id}',
  resource: 'subscriptions',
  name: 'get',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const getSubscriptionFilter: Operation = {
  id: 'getSubscriptionFilter',
  method: 'GET',
  path: '/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}',
  resource: 'subscriptions',
  name: 'getFilter',
  host: 'api',
  params: [
    { wire: 'filter_id', name: 'filterId', location: 'path' },
    { wire: 'subscription_id', name: 'subscriptionId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const getSubscriptions: Operation = {
  id: 'getSubscriptions',
  method: 'GET',
  path: '/commerce/notification/v1/subscription',
  resource: 'subscriptions',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'continuation_token', name: 'continuationToken', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'subscriptions',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const testSubscription: Operation = {
  id: 'testSubscription',
  method: 'POST',
  path: '/commerce/notification/v1/subscription/{subscription_id}/test',
  resource: 'subscriptions',
  name: 'test',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

const updateSubscription: Operation = {
  id: 'updateSubscription',
  method: 'PUT',
  path: '/commerce/notification/v1/subscription/{subscription_id}',
  resource: 'subscriptions',
  name: 'update',
  host: 'api',
  params: [{ wire: 'subscription_id', name: 'subscriptionId', location: 'path' }],
  hasBody: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope',
          'https://api.ebay.com/oauth/api_scope/commerce.notification.subscription',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createSubscription,
  createSubscriptionFilter,
  deleteSubscription,
  deleteSubscriptionFilter,
  disableSubscription,
  enableSubscription,
  getSubscription,
  getSubscriptionFilter,
  getSubscriptions,
  testSubscription,
  updateSubscription,
];

export class SubscriptionsApi extends Resource {
  /** Subscribe to a notification topic. */
  create(body?: CreateSubscriptionRequest, options?: RequestOptions): Promise<object> {
    return this.call(createSubscription, body, {}, options);
  }

  /** Add a filter to a subscription. */
  createFilter(
    subscriptionId: string,
    body?: CreateSubscriptionFilterRequest,
    options?: RequestOptions,
  ): Promise<object> {
    return this.call(createSubscriptionFilter, body, { subscriptionId }, options);
  }

  /** Delete a subscription. */
  delete(subscriptionId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteSubscription, undefined, { subscriptionId }, options);
  }

  /** Delete a filter from a subscription. */
  deleteFilter(filterId: string, subscriptionId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteSubscriptionFilter, undefined, { filterId, subscriptionId }, options);
  }

  /** Stop sending a subscription's notifications. */
  disable(subscriptionId: string, options?: RequestOptions): Promise<void> {
    return this.call(disableSubscription, undefined, { subscriptionId }, options);
  }

  /** Resume sending a subscription's notifications. */
  enable(subscriptionId: string, options?: RequestOptions): Promise<void> {
    return this.call(enableSubscription, undefined, { subscriptionId }, options);
  }

  /** Get one subscription. */
  get(subscriptionId: string, options?: RequestOptions): Promise<Subscription> {
    return this.call(getSubscription, undefined, { subscriptionId }, options);
  }

  /** Get one filter of a subscription. */
  getFilter(filterId: string, subscriptionId: string, options?: RequestOptions): Promise<SubscriptionFilter> {
    return this.call(getSubscriptionFilter, undefined, { filterId, subscriptionId }, options);
  }

  /** List one page of the app's subscriptions. */
  list(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): Promise<SubscriptionSearchResponse> {
    return this.call(getSubscriptions, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Subscription, void, undefined> {
    return this.paginate(getSubscriptions, undefined, { ...params }, options);
  }

  /** Send a test notification to a subscription's destination. */
  test(subscriptionId: string, options?: RequestOptions): Promise<void> {
    return this.call(testSubscription, undefined, { subscriptionId }, options);
  }

  /** Update a subscription. */
  update(subscriptionId: string, body?: UpdateSubscriptionRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateSubscription, body, { subscriptionId }, options);
  }
}
