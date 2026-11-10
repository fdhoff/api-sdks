// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, NotificationCount, NotificationThread } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const notifyGetList: Operation = {
  id: 'notifyGetList',
  method: 'GET',
  path: '/notifications',
  resource: 'notifications',
  name: 'list',
  params: [
    { wire: 'all', name: 'all', location: 'query' },
    { wire: 'status-types', name: 'statusTypes', location: 'query' },
    { wire: 'subject-type', name: 'subjectType', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyGetRepoList: Operation = {
  id: 'notifyGetRepoList',
  method: 'GET',
  path: '/repos/{owner}/{repo}/notifications',
  resource: 'notifications',
  name: 'listForRepo',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'all', name: 'all', location: 'query' },
    { wire: 'status-types', name: 'statusTypes', location: 'query' },
    { wire: 'subject-type', name: 'subjectType', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'before', name: 'before', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForRepo',
  paging: { style: 'link_header', items: '$', rel: 'next', params: ['page', 'limit'] },
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyGetThread: Operation = {
  id: 'notifyGetThread',
  method: 'GET',
  path: '/notifications/threads/{id}',
  resource: 'notifications',
  name: 'getThread',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyNewAvailable: Operation = {
  id: 'notifyNewAvailable',
  method: 'GET',
  path: '/notifications/new',
  resource: 'notifications',
  name: 'countUnread',
  params: [],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyReadList: Operation = {
  id: 'notifyReadList',
  method: 'PUT',
  path: '/notifications',
  resource: 'notifications',
  name: 'markRead',
  params: [
    { wire: 'last_read_at', name: 'lastReadAt', location: 'query' },
    { wire: 'all', name: 'all', location: 'query' },
    { wire: 'status-types', name: 'statusTypes', location: 'query' },
    { wire: 'to-status', name: 'toStatus', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyReadRepoList: Operation = {
  id: 'notifyReadRepoList',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/notifications',
  resource: 'notifications',
  name: 'markRepoRead',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'all', name: 'all', location: 'query' },
    { wire: 'status-types', name: 'statusTypes', location: 'query' },
    { wire: 'to-status', name: 'toStatus', location: 'query' },
    { wire: 'last_read_at', name: 'lastReadAt', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

const notifyReadThread: Operation = {
  id: 'notifyReadThread',
  method: 'PATCH',
  path: '/notifications/threads/{id}',
  resource: 'notifications',
  name: 'markThreadRead',
  params: [
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'to-status', name: 'toStatus', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'AuthorizationHeaderToken', scopes: [] }],
    [
      { scheme: 'AuthorizationHeaderToken', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [{ scheme: 'BasicAuth', scopes: [] }],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
    [
      { scheme: 'BasicAuth', scopes: [] },
      { scheme: 'TOTPHeader', scopes: [] },
      { scheme: 'SudoHeader', scopes: [] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  notifyGetList,
  notifyGetRepoList,
  notifyGetThread,
  notifyNewAvailable,
  notifyReadList,
  notifyReadRepoList,
  notifyReadThread,
];

export class NotificationsApi extends Resource {
  /** List one page of your notification threads (notifyGetList). */
  list(
    params: {
      all?: boolean;
      statusTypes?: Array<string>;
      subjectType?: Array<'issue' | 'pull' | 'commit' | 'repository'>;
      since?: string;
      before?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<NotificationThread>> {
    return this.call(notifyGetList, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      all?: boolean;
      statusTypes?: Array<string>;
      subjectType?: Array<'issue' | 'pull' | 'commit' | 'repository'>;
      since?: string;
      before?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.NotificationThread, void, undefined> {
    return this.paginate(notifyGetList, undefined, { ...params }, options);
  }

  /** List one page of your notification threads on a repository (notifyGetRepoList). */
  listForRepo(
    owner: string,
    repo: string,
    params: {
      all?: boolean;
      statusTypes?: Array<string>;
      subjectType?: Array<'issue' | 'pull' | 'commit' | 'repository'>;
      since?: string;
      before?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<NotificationThread>> {
    return this.call(notifyGetRepoList, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForRepo(
    owner: string,
    repo: string,
    params: {
      all?: boolean;
      statusTypes?: Array<string>;
      subjectType?: Array<'issue' | 'pull' | 'commit' | 'repository'>;
      since?: string;
      before?: string;
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.NotificationThread, void, undefined> {
    return this.paginate(notifyGetRepoList, undefined, { owner, repo, ...params }, options);
  }

  /** Get a notification thread (notifyGetThread). */
  getThread(id: string, options?: RequestOptions): Promise<NotificationThread> {
    return this.call(notifyGetThread, undefined, { id }, options);
  }

  /** Count your unread notification threads (notifyNewAvailable). */
  countUnread(options?: RequestOptions): Promise<NotificationCount> {
    return this.call(notifyNewAvailable, undefined, {}, options);
  }

  /** Mark your notification threads read (notifyReadList). */
  markRead(
    params: { lastReadAt?: string; all?: string; statusTypes?: Array<string>; toStatus?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<NotificationThread>> {
    return this.call(notifyReadList, undefined, { ...params }, options);
  }

  /** Mark your notification threads on a repository read (notifyReadRepoList). */
  markRepoRead(
    owner: string,
    repo: string,
    params: { all?: string; statusTypes?: Array<string>; toStatus?: string; lastReadAt?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<NotificationThread>> {
    return this.call(notifyReadRepoList, undefined, { owner, repo, ...params }, options);
  }

  /** Mark a notification thread read (notifyReadThread). */
  markThreadRead(
    id: string,
    params: { toStatus?: string } = {},
    options?: RequestOptions,
  ): Promise<NotificationThread> {
    return this.call(notifyReadThread, undefined, { id, ...params }, options);
  }
}
