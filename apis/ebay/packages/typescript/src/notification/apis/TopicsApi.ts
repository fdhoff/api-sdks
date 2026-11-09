// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetConfig429Response, Topic, TopicSearchResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getTopic: Operation = {
  id: 'getTopic',
  method: 'GET',
  path: '/commerce/notification/v1/topic/{topic_id}',
  resource: 'topics',
  name: 'get',
  host: 'api',
  params: [{ wire: 'topic_id', name: 'topicId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getTopics: Operation = {
  id: 'getTopics',
  method: 'GET',
  path: '/commerce/notification/v1/topic',
  resource: 'topics',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'continuation_token', name: 'continuationToken', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'topics', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [getTopic, getTopics];

export class TopicsApi extends Resource {
  /** Get one notification topic. */
  get(topicId: string, options?: RequestOptions): Promise<Topic> {
    return this.call(getTopic, undefined, { topicId }, options);
  }

  /** List one page of notification topics. */
  list(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): Promise<TopicSearchResponse> {
    return this.call(getTopics, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Topic, void, undefined> {
    return this.paginate(getTopics, undefined, { ...params }, options);
  }
}
