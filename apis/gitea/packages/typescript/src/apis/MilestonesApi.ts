// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, CreateMilestoneOption, EditMilestoneOption, Milestone } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const issueCreateMilestone: Operation = {
  id: 'issueCreateMilestone',
  method: 'POST',
  path: '/repos/{owner}/{repo}/milestones',
  resource: 'milestones',
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

const issueDeleteMilestone: Operation = {
  id: 'issueDeleteMilestone',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/milestones/{id}',
  resource: 'milestones',
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

const issueEditMilestone: Operation = {
  id: 'issueEditMilestone',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/milestones/{id}',
  resource: 'milestones',
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

const issueGetMilestone: Operation = {
  id: 'issueGetMilestone',
  method: 'GET',
  path: '/repos/{owner}/{repo}/milestones/{id}',
  resource: 'milestones',
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

const issueGetMilestonesList: Operation = {
  id: 'issueGetMilestonesList',
  method: 'GET',
  path: '/repos/{owner}/{repo}/milestones',
  resource: 'milestones',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'name', name: 'name', location: 'query' },
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

export const OPERATIONS: readonly Operation[] = [
  issueCreateMilestone,
  issueDeleteMilestone,
  issueEditMilestone,
  issueGetMilestone,
  issueGetMilestonesList,
];

export class MilestonesApi extends Resource {
  /** Create a milestone (issueCreateMilestone). */
  create(owner: string, repo: string, body?: CreateMilestoneOption, options?: RequestOptions): Promise<Milestone> {
    return this.call(issueCreateMilestone, body, { owner, repo }, options);
  }

  /** Delete a milestone (issueDeleteMilestone). */
  delete(owner: string, repo: string, id: string, options?: RequestOptions): Promise<void> {
    return this.call(issueDeleteMilestone, undefined, { owner, repo, id }, options);
  }

  /** Change a milestone (issueEditMilestone). */
  update(
    owner: string,
    repo: string,
    id: string,
    body?: EditMilestoneOption,
    options?: RequestOptions,
  ): Promise<Milestone> {
    return this.call(issueEditMilestone, body, { owner, repo, id }, options);
  }

  /** Get a milestone (issueGetMilestone). */
  get(owner: string, repo: string, id: string, options?: RequestOptions): Promise<Milestone> {
    return this.call(issueGetMilestone, undefined, { owner, repo, id }, options);
  }

  /** List one page of a repository's milestones (issueGetMilestonesList). */
  list(
    owner: string,
    repo: string,
    params: { state?: string; name?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Milestone>> {
    return this.call(issueGetMilestonesList, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { state?: string; name?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Milestone, void, undefined> {
    return this.paginate(issueGetMilestonesList, undefined, { owner, repo, ...params }, options);
  }
}
