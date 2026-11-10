// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, CreateLabelOption, EditLabelOption, Label } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const issueCreateLabel: Operation = {
  id: 'issueCreateLabel',
  method: 'POST',
  path: '/repos/{owner}/{repo}/labels',
  resource: 'labels',
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

const issueDeleteLabel: Operation = {
  id: 'issueDeleteLabel',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/labels/{id}',
  resource: 'labels',
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

const issueEditLabel: Operation = {
  id: 'issueEditLabel',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/labels/{id}',
  resource: 'labels',
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

const issueGetLabel: Operation = {
  id: 'issueGetLabel',
  method: 'GET',
  path: '/repos/{owner}/{repo}/labels/{id}',
  resource: 'labels',
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

const issueListLabels: Operation = {
  id: 'issueListLabels',
  method: 'GET',
  path: '/repos/{owner}/{repo}/labels',
  resource: 'labels',
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

const orgCreateLabel: Operation = {
  id: 'orgCreateLabel',
  method: 'POST',
  path: '/orgs/{org}/labels',
  resource: 'labels',
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

const orgDeleteLabel: Operation = {
  id: 'orgDeleteLabel',
  method: 'DELETE',
  path: '/orgs/{org}/labels/{id}',
  resource: 'labels',
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

const orgEditLabel: Operation = {
  id: 'orgEditLabel',
  method: 'PATCH',
  path: '/orgs/{org}/labels/{id}',
  resource: 'labels',
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

const orgGetLabel: Operation = {
  id: 'orgGetLabel',
  method: 'GET',
  path: '/orgs/{org}/labels/{id}',
  resource: 'labels',
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

const orgListLabels: Operation = {
  id: 'orgListLabels',
  method: 'GET',
  path: '/orgs/{org}/labels',
  resource: 'labels',
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

export const OPERATIONS: readonly Operation[] = [
  issueCreateLabel,
  issueDeleteLabel,
  issueEditLabel,
  issueGetLabel,
  issueListLabels,
  orgCreateLabel,
  orgDeleteLabel,
  orgEditLabel,
  orgGetLabel,
  orgListLabels,
];

export class LabelsApi extends Resource {
  /** Create a repository label (issueCreateLabel). */
  create(owner: string, repo: string, body?: CreateLabelOption, options?: RequestOptions): Promise<Label> {
    return this.call(issueCreateLabel, body, { owner, repo }, options);
  }

  /** Delete a repository label (issueDeleteLabel). */
  delete(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteLabel, undefined, { owner, repo, id }, options);
  }

  /** Change a repository label (issueEditLabel). */
  update(owner: string, repo: string, id: number, body?: EditLabelOption, options?: RequestOptions): Promise<Label> {
    return this.call(issueEditLabel, body, { owner, repo, id }, options);
  }

  /** Get a repository label (issueGetLabel). */
  get(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Label> {
    return this.call(issueGetLabel, undefined, { owner, repo, id }, options);
  }

  /** List one page of a repository's labels (issueListLabels). */
  list(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Label>> {
    return this.call(issueListLabels, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Label, void, undefined> {
    return this.paginate(issueListLabels, undefined, { owner, repo, ...params }, options);
  }

  /** Create an organization label (orgCreateLabel). */
  createForOrg(org: string, body?: CreateLabelOption, options?: RequestOptions): Promise<Label> {
    return this.call(orgCreateLabel, body, { org }, options);
  }

  /** Delete an organization label (orgDeleteLabel). */
  deleteForOrg(org: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(orgDeleteLabel, undefined, { org, id }, options);
  }

  /** Change an organization label (orgEditLabel). */
  updateForOrg(org: string, id: number, body?: EditLabelOption, options?: RequestOptions): Promise<Label> {
    return this.call(orgEditLabel, body, { org, id }, options);
  }

  /** Get an organization label (orgGetLabel). */
  getForOrg(org: string, id: number, options?: RequestOptions): Promise<Label> {
    return this.call(orgGetLabel, undefined, { org, id }, options);
  }

  /** List one page of an organization's labels (orgListLabels). */
  listForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Label>> {
    return this.call(orgListLabels, undefined, { org, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForOrg(
    org: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Label, void, undefined> {
    return this.paginate(orgListLabels, undefined, { org, ...params }, options);
  }
}
