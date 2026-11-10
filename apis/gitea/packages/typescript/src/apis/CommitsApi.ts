// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  CombinedStatus,
  Commit,
  CommitStatus,
  Compare,
  CreateStatusOption,
  PullRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCompareDiff: Operation = {
  id: 'repoCompareDiff',
  method: 'GET',
  path: '/repos/{owner}/{repo}/compare/{basehead}',
  resource: 'commits',
  name: 'compare',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'basehead', name: 'basehead', location: 'path' },
    { wire: 'output', name: 'output', location: 'query' },
    { wire: 'verification', name: 'verification', location: 'query' },
    { wire: 'files', name: 'files', location: 'query' },
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

const repoCreateStatus: Operation = {
  id: 'repoCreateStatus',
  method: 'POST',
  path: '/repos/{owner}/{repo}/statuses/{sha}',
  resource: 'commits',
  name: 'createStatus',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
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

const repoDownloadCommitDiffOrPatch: Operation = {
  id: 'repoDownloadCommitDiffOrPatch',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/commits/{sha}.{diffType}',
  resource: 'commits',
  name: 'getDiff',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
    { wire: 'diffType', name: 'diffType', location: 'path' },
  ],
  returnsText: true,
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

const repoGetAllCommits: Operation = {
  id: 'repoGetAllCommits',
  method: 'GET',
  path: '/repos/{owner}/{repo}/commits',
  resource: 'commits',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'query' },
    { wire: 'path', name: 'path', location: 'query' },
    { wire: 'since', name: 'since', location: 'query' },
    { wire: 'until', name: 'until', location: 'query' },
    { wire: 'stat', name: 'stat', location: 'query' },
    { wire: 'verification', name: 'verification', location: 'query' },
    { wire: 'files', name: 'files', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'not', name: 'not', location: 'query' },
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

const repoGetCombinedStatusByRef: Operation = {
  id: 'repoGetCombinedStatusByRef',
  method: 'GET',
  path: '/repos/{owner}/{repo}/commits/{ref}/status',
  resource: 'commits',
  name: 'getCombinedStatus',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterCombinedStatus',
  paging: { style: 'link_header', items: 'statuses', rel: 'next', params: ['page', 'limit'] },
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

const repoGetCommitPullRequest: Operation = {
  id: 'repoGetCommitPullRequest',
  method: 'GET',
  path: '/repos/{owner}/{repo}/commits/{sha}/pull',
  resource: 'commits',
  name: 'getPullRequest',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
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

const repoGetSingleCommit: Operation = {
  id: 'repoGetSingleCommit',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/commits/{sha}',
  resource: 'commits',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
    { wire: 'stat', name: 'stat', location: 'query' },
    { wire: 'verification', name: 'verification', location: 'query' },
    { wire: 'files', name: 'files', location: 'query' },
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

const repoListStatuses: Operation = {
  id: 'repoListStatuses',
  method: 'GET',
  path: '/repos/{owner}/{repo}/statuses/{sha}',
  resource: 'commits',
  name: 'listStatuses',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStatuses',
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

const repoListStatusesByRef: Operation = {
  id: 'repoListStatusesByRef',
  method: 'GET',
  path: '/repos/{owner}/{repo}/commits/{ref}/statuses',
  resource: 'commits',
  name: 'listStatusesForRef',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'path' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStatusesForRef',
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
  repoCompareDiff,
  repoCreateStatus,
  repoDownloadCommitDiffOrPatch,
  repoGetAllCommits,
  repoGetCombinedStatusByRef,
  repoGetCommitPullRequest,
  repoGetSingleCommit,
  repoListStatuses,
  repoListStatusesByRef,
];

export class CommitsApi extends Resource {
  /** Compare two refs (repoCompareDiff). */
  compare(
    owner: string,
    repo: string,
    basehead: string,
    params: { output?: 'diff' | 'patch'; verification?: boolean; files?: boolean } = {},
    options?: RequestOptions,
  ): Promise<Compare> {
    return this.call(repoCompareDiff, undefined, { owner, repo, basehead, ...params }, options);
  }

  /** Set a commit status (repoCreateStatus). */
  createStatus(
    owner: string,
    repo: string,
    sha: string,
    body?: CreateStatusOption,
    options?: RequestOptions,
  ): Promise<CommitStatus> {
    return this.call(repoCreateStatus, body, { owner, repo, sha }, options);
  }

  /** Get a commit's diff or patch as text (repoDownloadCommitDiffOrPatch). */
  getDiff(
    owner: string,
    repo: string,
    sha: string,
    diffType: 'diff' | 'patch',
    options?: RequestOptions,
  ): Promise<string> {
    return this.call(repoDownloadCommitDiffOrPatch, undefined, { owner, repo, sha, diffType }, options);
  }

  /** List one page of a repository's commits (repoGetAllCommits). */
  list(
    owner: string,
    repo: string,
    params: {
      sha?: string;
      path?: string;
      since?: string;
      until?: string;
      stat?: boolean;
      verification?: boolean;
      files?: boolean;
      page?: number;
      limit?: number;
      not?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<Commit>> {
    return this.call(repoGetAllCommits, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: {
      sha?: string;
      path?: string;
      since?: string;
      until?: string;
      stat?: boolean;
      verification?: boolean;
      files?: boolean;
      page?: number;
      limit?: number;
      not?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Commit, void, undefined> {
    return this.paginate(repoGetAllCommits, undefined, { owner, repo, ...params }, options);
  }

  /** Get the combined status of a branch, tag or commit, with one page of its statuses (repoGetCombinedStatusByRef). */
  getCombinedStatus(
    owner: string,
    repo: string,
    ref: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<CombinedStatus> {
    return this.call(repoGetCombinedStatusByRef, undefined, { owner, repo, ref, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterCombinedStatus(
    owner: string,
    repo: string,
    ref: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CommitStatus, void, undefined> {
    return this.paginate(repoGetCombinedStatusByRef, undefined, { owner, repo, ref, ...params }, options);
  }

  /** Get the pull request that a commit was merged in (repoGetCommitPullRequest). */
  getPullRequest(owner: string, repo: string, sha: string, options?: RequestOptions): Promise<PullRequest> {
    return this.call(repoGetCommitPullRequest, undefined, { owner, repo, sha }, options);
  }

  /** Get a commit (repoGetSingleCommit). */
  get(
    owner: string,
    repo: string,
    sha: string,
    params: { stat?: boolean; verification?: boolean; files?: boolean } = {},
    options?: RequestOptions,
  ): Promise<Commit> {
    return this.call(repoGetSingleCommit, undefined, { owner, repo, sha, ...params }, options);
  }

  /** List one page of a commit's statuses (repoListStatuses). */
  listStatuses(
    owner: string,
    repo: string,
    sha: string,
    params: {
      sort?: 'oldest' | 'recentupdate' | 'leastupdate' | 'leastindex' | 'highestindex';
      state?: 'pending' | 'success' | 'error' | 'failure' | 'warning';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<CommitStatus>> {
    return this.call(repoListStatuses, undefined, { owner, repo, sha, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStatuses(
    owner: string,
    repo: string,
    sha: string,
    params: {
      sort?: 'oldest' | 'recentupdate' | 'leastupdate' | 'leastindex' | 'highestindex';
      state?: 'pending' | 'success' | 'error' | 'failure' | 'warning';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CommitStatus, void, undefined> {
    return this.paginate(repoListStatuses, undefined, { owner, repo, sha, ...params }, options);
  }

  /** List one page of the statuses of a branch, tag or commit (repoListStatusesByRef). */
  listStatusesForRef(
    owner: string,
    repo: string,
    ref: string,
    params: {
      sort?: 'oldest' | 'recentupdate' | 'leastupdate' | 'leastindex' | 'highestindex';
      state?: 'pending' | 'success' | 'error' | 'failure' | 'warning';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<Array<CommitStatus>> {
    return this.call(repoListStatusesByRef, undefined, { owner, repo, ref, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStatusesForRef(
    owner: string,
    repo: string,
    ref: string,
    params: {
      sort?: 'oldest' | 'recentupdate' | 'leastupdate' | 'leastindex' | 'highestindex';
      state?: 'pending' | 'success' | 'error' | 'failure' | 'warning';
      page?: number;
      limit?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CommitStatus, void, undefined> {
    return this.paginate(repoListStatusesByRef, undefined, { owner, repo, ref, ...params }, options);
  }
}
