// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  AccessToken,
  Activity,
  CreateAccessTokenOption,
  GPGKey,
  Organization,
  OrganizationPermissions,
  Project,
  PublicKey,
  Repository,
  User,
  UserHeatmapData,
  UserSearchResults,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const orgGetUserPermissions: Operation = {
  id: 'orgGetUserPermissions',
  method: 'GET',
  path: '/users/{username}/orgs/{org}/permissions',
  resource: 'users',
  name: 'getOrgPermissions',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'org', name: 'org', location: 'path' },
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

const orgListUserOrgs: Operation = {
  id: 'orgListUserOrgs',
  method: 'GET',
  path: '/users/{username}/orgs',
  resource: 'users',
  name: 'listOrgs',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterOrgs',
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

const userCheckFollowing: Operation = {
  id: 'userCheckFollowing',
  method: 'GET',
  path: '/users/{username}/following/{target}',
  resource: 'users',
  name: 'checkFollowing',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'target', name: 'target', location: 'path' },
  ],
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

const userCreateToken: Operation = {
  id: 'userCreateToken',
  method: 'POST',
  path: '/users/{username}/tokens',
  resource: 'users',
  name: 'createToken',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
  hasBody: true,
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

const userDeleteAccessToken: Operation = {
  id: 'userDeleteAccessToken',
  method: 'DELETE',
  path: '/users/{username}/tokens/{token}',
  resource: 'users',
  name: 'deleteToken',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'token', name: 'token', location: 'path' },
  ],
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

const userGet: Operation = {
  id: 'userGet',
  method: 'GET',
  path: '/users/{username}',
  resource: 'users',
  name: 'get',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userGetHeatmapData: Operation = {
  id: 'userGetHeatmapData',
  method: 'GET',
  path: '/users/{username}/heatmap',
  resource: 'users',
  name: 'getHeatmap',
  params: [{ wire: 'username', name: 'username', location: 'path' }],
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

const userGetTokens: Operation = {
  id: 'userGetTokens',
  method: 'GET',
  path: '/users/{username}/tokens',
  resource: 'users',
  name: 'listTokens',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTokens',
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

const userListActivityFeeds: Operation = {
  id: 'userListActivityFeeds',
  method: 'GET',
  path: '/users/{username}/activities/feeds',
  resource: 'users',
  name: 'listActivityFeeds',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'only-performed-by', name: 'onlyPerformedBy', location: 'query' },
    { wire: 'date', name: 'date', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterActivityFeeds',
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

const userListFollowers: Operation = {
  id: 'userListFollowers',
  method: 'GET',
  path: '/users/{username}/followers',
  resource: 'users',
  name: 'listFollowers',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFollowers',
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

const userListFollowing: Operation = {
  id: 'userListFollowing',
  method: 'GET',
  path: '/users/{username}/following',
  resource: 'users',
  name: 'listFollowing',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFollowing',
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

const userListGPGKeys: Operation = {
  id: 'userListGPGKeys',
  method: 'GET',
  path: '/users/{username}/gpg_keys',
  resource: 'users',
  name: 'listGpgKeys',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterGpgKeys',
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

const userListKeys: Operation = {
  id: 'userListKeys',
  method: 'GET',
  path: '/users/{username}/keys',
  resource: 'users',
  name: 'listKeys',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'fingerprint', name: 'fingerprint', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterKeys',
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

const userListProjects: Operation = {
  id: 'userListProjects',
  method: 'GET',
  path: '/users/{username}/projects',
  resource: 'users',
  name: 'listProjects',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterProjects',
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

const userListRepos: Operation = {
  id: 'userListRepos',
  method: 'GET',
  path: '/users/{username}/repos',
  resource: 'users',
  name: 'listRepos',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterRepos',
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

const userListStarred: Operation = {
  id: 'userListStarred',
  method: 'GET',
  path: '/users/{username}/starred',
  resource: 'users',
  name: 'listStarred',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStarred',
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

const userListSubscriptions: Operation = {
  id: 'userListSubscriptions',
  method: 'GET',
  path: '/users/{username}/subscriptions',
  resource: 'users',
  name: 'listWatched',
  params: [
    { wire: 'username', name: 'username', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterWatched',
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

const userSearch: Operation = {
  id: 'userSearch',
  method: 'GET',
  path: '/users/search',
  resource: 'users',
  name: 'search',
  params: [
    { wire: 'q', name: 'q', location: 'query' },
    { wire: 'uid', name: 'uid', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterSearch',
  paging: { style: 'link_header', items: 'data', rel: 'next', params: ['page', 'limit'] },
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
  orgGetUserPermissions,
  orgListUserOrgs,
  userCheckFollowing,
  userCreateToken,
  userDeleteAccessToken,
  userGet,
  userGetHeatmapData,
  userGetTokens,
  userListActivityFeeds,
  userListFollowers,
  userListFollowing,
  userListGPGKeys,
  userListKeys,
  userListProjects,
  userListRepos,
  userListStarred,
  userListSubscriptions,
  userSearch,
];

export class UsersApi extends Resource {
  /** Get a user's permissions in an organization (orgGetUserPermissions). */
  getOrgPermissions(username: string, org: string, options?: RequestOptions): Promise<OrganizationPermissions> {
    return this.call(orgGetUserPermissions, undefined, { username, org }, options);
  }

  /** List one page of a user's organizations (orgListUserOrgs). */
  listOrgs(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Organization>> {
    return this.call(orgListUserOrgs, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterOrgs(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Organization, void, undefined> {
    return this.paginate(orgListUserOrgs, undefined, { username, ...params }, options);
  }

  /** Check whether a user follows another (userCheckFollowing). */
  checkFollowing(username: string, target: string, options?: RequestOptions): Promise<void> {
    return this.call(userCheckFollowing, undefined, { username, target }, options);
  }

  /** Create an access token for a user (userCreateToken). */
  createToken(username: string, body?: CreateAccessTokenOption, options?: RequestOptions): Promise<AccessToken> {
    return this.call(userCreateToken, body, { username }, options);
  }

  /** Delete one of a user's access tokens (userDeleteAccessToken). */
  deleteToken(username: string, token: string, options?: RequestOptions): Promise<void> {
    return this.call(userDeleteAccessToken, undefined, { username, token }, options);
  }

  /** Get a user (userGet). */
  get(username: string, options?: RequestOptions): Promise<User> {
    return this.call(userGet, undefined, { username }, options);
  }

  /** Get a user's contribution heatmap (userGetHeatmapData). */
  getHeatmap(username: string, options?: RequestOptions): Promise<Array<UserHeatmapData>> {
    return this.call(userGetHeatmapData, undefined, { username }, options);
  }

  /** List one page of a user's access tokens (userGetTokens). */
  listTokens(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<AccessToken>> {
    return this.call(userGetTokens, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTokens(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.AccessToken, void, undefined> {
    return this.paginate(userGetTokens, undefined, { username, ...params }, options);
  }

  /** List one page of a user's activity (userListActivityFeeds). */
  listActivityFeeds(
    username: string,
    params: { onlyPerformedBy?: boolean; date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Activity>> {
    return this.call(userListActivityFeeds, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActivityFeeds(
    username: string,
    params: { onlyPerformedBy?: boolean; date?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Activity, void, undefined> {
    return this.paginate(userListActivityFeeds, undefined, { username, ...params }, options);
  }

  /** List one page of a user's followers (userListFollowers). */
  listFollowers(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(userListFollowers, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFollowers(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userListFollowers, undefined, { username, ...params }, options);
  }

  /** List one page of the users a user follows (userListFollowing). */
  listFollowing(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<User>> {
    return this.call(userListFollowing, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFollowing(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userListFollowing, undefined, { username, ...params }, options);
  }

  /** List one page of a user's GPG keys (userListGPGKeys). */
  listGpgKeys(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<GPGKey>> {
    return this.call(userListGPGKeys, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterGpgKeys(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.GPGKey, void, undefined> {
    return this.paginate(userListGPGKeys, undefined, { username, ...params }, options);
  }

  /** List one page of a user's SSH keys (userListKeys). */
  listKeys(
    username: string,
    params: { fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<PublicKey>> {
    return this.call(userListKeys, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterKeys(
    username: string,
    params: { fingerprint?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PublicKey, void, undefined> {
    return this.paginate(userListKeys, undefined, { username, ...params }, options);
  }

  /** List one page of a user's projects (userListProjects). */
  listProjects(
    username: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Project>> {
    return this.call(userListProjects, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterProjects(
    username: string,
    params: { state?: 'open' | 'closed' | 'all'; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Project, void, undefined> {
    return this.paginate(userListProjects, undefined, { username, ...params }, options);
  }

  /** List one page of a user's repositories (userListRepos). */
  listRepos(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(userListRepos, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterRepos(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userListRepos, undefined, { username, ...params }, options);
  }

  /** List one page of the repositories a user starred (userListStarred). */
  listStarred(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(userListStarred, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStarred(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userListStarred, undefined, { username, ...params }, options);
  }

  /** List one page of the repositories a user watches (userListSubscriptions). */
  listWatched(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Repository>> {
    return this.call(userListSubscriptions, undefined, { username, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterWatched(
    username: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Repository, void, undefined> {
    return this.paginate(userListSubscriptions, undefined, { username, ...params }, options);
  }

  /** Get one page of the users that match a search (userSearch). */
  search(
    params: { q?: string; uid?: number; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<UserSearchResults> {
    return this.call(userSearch, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterSearch(
    params: { q?: string; uid?: number; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.User, void, undefined> {
    return this.paginate(userSearch, undefined, { ...params }, options);
  }
}
