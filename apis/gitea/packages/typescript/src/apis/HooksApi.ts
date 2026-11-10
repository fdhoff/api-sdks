// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, CreateHookOption, EditGitHookOption, EditHookOption, GitHook, Hook } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const orgCreateHook: Operation = {
  id: 'orgCreateHook',
  method: 'POST',
  path: '/orgs/{org}/hooks',
  resource: 'hooks',
  name: 'createForOrg',
  params: [{ wire: 'org', name: 'org', location: 'path' }],
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

const orgDeleteHook: Operation = {
  id: 'orgDeleteHook',
  method: 'DELETE',
  path: '/orgs/{org}/hooks/{id}',
  resource: 'hooks',
  name: 'deleteForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const orgEditHook: Operation = {
  id: 'orgEditHook',
  method: 'PATCH',
  path: '/orgs/{org}/hooks/{id}',
  resource: 'hooks',
  name: 'updateForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
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

const orgGetHook: Operation = {
  id: 'orgGetHook',
  method: 'GET',
  path: '/orgs/{org}/hooks/{id}',
  resource: 'hooks',
  name: 'getForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const orgListHooks: Operation = {
  id: 'orgListHooks',
  method: 'GET',
  path: '/orgs/{org}/hooks',
  resource: 'hooks',
  name: 'listForOrg',
  params: [
    { wire: 'org', name: 'org', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForOrg',
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

const repoCreateHook: Operation = {
  id: 'repoCreateHook',
  method: 'POST',
  path: '/repos/{owner}/{repo}/hooks',
  resource: 'hooks',
  name: 'create',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
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

const repoDeleteGitHook: Operation = {
  id: 'repoDeleteGitHook',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/hooks/git/{id}',
  resource: 'hooks',
  name: 'deleteGitHook',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const repoDeleteHook: Operation = {
  id: 'repoDeleteHook',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/hooks/{id}',
  resource: 'hooks',
  name: 'delete',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const repoEditGitHook: Operation = {
  id: 'repoEditGitHook',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/hooks/git/{id}',
  resource: 'hooks',
  name: 'updateGitHook',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
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

const repoEditHook: Operation = {
  id: 'repoEditHook',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/hooks/{id}',
  resource: 'hooks',
  name: 'update',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
  ],
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

const repoGetGitHook: Operation = {
  id: 'repoGetGitHook',
  method: 'GET',
  path: '/repos/{owner}/{repo}/hooks/git/{id}',
  resource: 'hooks',
  name: 'getGitHook',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const repoGetHook: Operation = {
  id: 'repoGetHook',
  method: 'GET',
  path: '/repos/{owner}/{repo}/hooks/{id}',
  resource: 'hooks',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
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

const repoListGitHooks: Operation = {
  id: 'repoListGitHooks',
  method: 'GET',
  path: '/repos/{owner}/{repo}/hooks/git',
  resource: 'hooks',
  name: 'listGitHooks',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoListHooks: Operation = {
  id: 'repoListHooks',
  method: 'GET',
  path: '/repos/{owner}/{repo}/hooks',
  resource: 'hooks',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
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

const repoTestHook: Operation = {
  id: 'repoTestHook',
  method: 'POST',
  path: '/repos/{owner}/{repo}/hooks/{id}/tests',
  resource: 'hooks',
  name: 'test',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'query' },
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

const userCreateHook: Operation = {
  id: 'userCreateHook',
  method: 'POST',
  path: '/user/hooks',
  resource: 'hooks',
  name: 'createForUser',
  params: [],
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

const userDeleteHook: Operation = {
  id: 'userDeleteHook',
  method: 'DELETE',
  path: '/user/hooks/{id}',
  resource: 'hooks',
  name: 'deleteForUser',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const userEditHook: Operation = {
  id: 'userEditHook',
  method: 'PATCH',
  path: '/user/hooks/{id}',
  resource: 'hooks',
  name: 'updateForUser',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
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

const userGetHook: Operation = {
  id: 'userGetHook',
  method: 'GET',
  path: '/user/hooks/{id}',
  resource: 'hooks',
  name: 'getForUser',
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

const userListHooks: Operation = {
  id: 'userListHooks',
  method: 'GET',
  path: '/user/hooks',
  resource: 'hooks',
  name: 'listForUser',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForUser',
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

export const OPERATIONS: readonly Operation[] = [
  orgCreateHook,
  orgDeleteHook,
  orgEditHook,
  orgGetHook,
  orgListHooks,
  repoCreateHook,
  repoDeleteGitHook,
  repoDeleteHook,
  repoEditGitHook,
  repoEditHook,
  repoGetGitHook,
  repoGetHook,
  repoListGitHooks,
  repoListHooks,
  repoTestHook,
  userCreateHook,
  userDeleteHook,
  userEditHook,
  userGetHook,
  userListHooks,
];

export class HooksApi extends Resource {
  /** Create an organization webhook (orgCreateHook). */
  createForOrg(org: string, body: CreateHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(orgCreateHook, body, { org }, options);
  }

  /** Delete an organization webhook (orgDeleteHook). */
  deleteForOrg(org: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteHook, undefined, { org, id }, options);
  }

  /** Change an organization webhook (orgEditHook). */
  updateForOrg(org: string, id: number, body?: EditHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(orgEditHook, body, { org, id }, options);
  }

  /** Get an organization webhook (orgGetHook). */
  getForOrg(org: string, id: number, options?: RequestOptions): Promise<Hook> {
    return this.call(orgGetHook, undefined, { org, id }, options);
  }

  /** List one page of an organization's webhooks (orgListHooks). */
  listForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Hook>> {
    return this.call(orgListHooks, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Hook, void, undefined> {
    return this.paginate(orgListHooks, undefined, { org, ...params }, options);
  }

  /** Create a repository webhook (repoCreateHook). */
  create(owner: string, repo: string, body?: CreateHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(repoCreateHook, body, { owner, repo }, options);
  }

  /** Clear a Git hook's content (repoDeleteGitHook). */
  deleteGitHook(owner: string, repo: string, id: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteGitHook, undefined, { owner, repo, id }, options);
  }

  /** Delete a repository webhook (repoDeleteHook). */
  delete(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteHook, undefined, { owner, repo, id }, options);
  }

  /** Change a Git hook's content (repoEditGitHook). */
  updateGitHook(
    owner: string,
    repo: string,
    id: string,
    body?: EditGitHookOption,
    options?: RequestOptions,
  ): Promise<GitHook> {
    return this.call(repoEditGitHook, body, { owner, repo, id }, options);
  }

  /** Change a repository webhook (repoEditHook). */
  update(owner: string, repo: string, id: number, body?: EditHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(repoEditHook, body, { owner, repo, id }, options);
  }

  /** Get a Git hook (repoGetGitHook). */
  getGitHook(owner: string, repo: string, id: string, options?: RequestOptions): Promise<GitHook> {
    return this.call(repoGetGitHook, undefined, { owner, repo, id }, options);
  }

  /** Get a repository webhook (repoGetHook). */
  get(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Hook> {
    return this.call(repoGetHook, undefined, { owner, repo, id }, options);
  }

  /** List a repository's Git hooks (repoListGitHooks). */
  listGitHooks(owner: string, repo: string, options?: RequestOptions): Promise<Array<GitHook>> {
    return this.call(repoListGitHooks, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's webhooks (repoListHooks). */
  list(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Hook>> {
    return this.call(repoListHooks, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Hook, void, undefined> {
    return this.paginate(repoListHooks, undefined, { owner, repo, ...params }, options);
  }

  /** Send a test push event to a repository webhook (repoTestHook). */
  test(
    owner: string,
    repo: string,
    id: number,
    params: { ref?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoTestHook, undefined, { owner, repo, id, ...params }, options);
  }

  /** Create a webhook of your own (userCreateHook). */
  createForUser(body: CreateHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(userCreateHook, body, {}, options);
  }

  /** Delete one of your webhooks (userDeleteHook). */
  deleteForUser(id: number, options?: RequestOptions): Promise<void> {
    return this.call(userDeleteHook, undefined, { id }, options);
  }

  /** Change one of your webhooks (userEditHook). */
  updateForUser(id: number, body?: EditHookOption, options?: RequestOptions): Promise<Hook> {
    return this.call(userEditHook, body, { id }, options);
  }

  /** Get one of your webhooks (userGetHook). */
  getForUser(id: number, options?: RequestOptions): Promise<Hook> {
    return this.call(userGetHook, undefined, { id }, options);
  }

  /** List one page of your own webhooks (userListHooks). */
  listForUser(params: { page?: number; limit?: number } = {}, options?: RequestOptions): Promise<Array<Hook>> {
    return this.call(userListHooks, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForUser(
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Hook, void, undefined> {
    return this.paginate(userListHooks, undefined, { ...params }, options);
  }
}
