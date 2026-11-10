// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  Branch,
  BranchProtection,
  CreateBranchProtectionOption,
  CreateBranchRepoOption,
  EditBranchProtectionOption,
  RenameBranchRepoOption,
  UpdateBranchProtectionPriories,
  UpdateBranchRepoOption,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCreateBranch: Operation = {
  id: 'repoCreateBranch',
  method: 'POST',
  path: '/repos/{owner}/{repo}/branches',
  resource: 'branches',
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

const repoCreateBranchProtection: Operation = {
  id: 'repoCreateBranchProtection',
  method: 'POST',
  path: '/repos/{owner}/{repo}/branch_protections',
  resource: 'branches',
  name: 'createProtection',
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

const repoDeleteBranch: Operation = {
  id: 'repoDeleteBranch',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/branches/{branch}',
  resource: 'branches',
  name: 'delete',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'branch', name: 'branch', location: 'path' },
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

const repoDeleteBranchProtection: Operation = {
  id: 'repoDeleteBranchProtection',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/branch_protections/{name}',
  resource: 'branches',
  name: 'deleteProtection',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const repoEditBranchProtection: Operation = {
  id: 'repoEditBranchProtection',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/branch_protections/{name}',
  resource: 'branches',
  name: 'updateProtection',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const repoGetBranch: Operation = {
  id: 'repoGetBranch',
  method: 'GET',
  path: '/repos/{owner}/{repo}/branches/{branch}',
  resource: 'branches',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'branch', name: 'branch', location: 'path' },
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

const repoGetBranchProtection: Operation = {
  id: 'repoGetBranchProtection',
  method: 'GET',
  path: '/repos/{owner}/{repo}/branch_protections/{name}',
  resource: 'branches',
  name: 'getProtection',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'name', name: 'name', location: 'path' },
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

const repoListBranchProtection: Operation = {
  id: 'repoListBranchProtection',
  method: 'GET',
  path: '/repos/{owner}/{repo}/branch_protections',
  resource: 'branches',
  name: 'listProtections',
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

const repoListBranches: Operation = {
  id: 'repoListBranches',
  method: 'GET',
  path: '/repos/{owner}/{repo}/branches',
  resource: 'branches',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'q', name: 'q', location: 'query' },
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

const repoRenameBranch: Operation = {
  id: 'repoRenameBranch',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/branches/{branch}',
  resource: 'branches',
  name: 'rename',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'branch', name: 'branch', location: 'path' },
  ],
  hasBody: true,
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

const repoUpdateBranch: Operation = {
  id: 'repoUpdateBranch',
  method: 'PUT',
  path: '/repos/{owner}/{repo}/branches/{branch}',
  resource: 'branches',
  name: 'update',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'branch', name: 'branch', location: 'path' },
  ],
  hasBody: true,
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

const repoUpdateBranchProtectionPriories: Operation = {
  id: 'repoUpdateBranchProtectionPriories',
  method: 'POST',
  path: '/repos/{owner}/{repo}/branch_protections/priority',
  resource: 'branches',
  name: 'reorderProtections',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
  ],
  hasBody: true,
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
  repoCreateBranch,
  repoCreateBranchProtection,
  repoDeleteBranch,
  repoDeleteBranchProtection,
  repoEditBranchProtection,
  repoGetBranch,
  repoGetBranchProtection,
  repoListBranchProtection,
  repoListBranches,
  repoRenameBranch,
  repoUpdateBranch,
  repoUpdateBranchProtectionPriories,
];

export class BranchesApi extends Resource {
  /** Create a branch (repoCreateBranch). */
  create(owner: string, repo: string, body?: CreateBranchRepoOption, options?: RequestOptions): Promise<Branch> {
    return this.call(repoCreateBranch, body, { owner, repo }, options);
  }

  /** Create a branch protection rule (repoCreateBranchProtection). */
  createProtection(
    owner: string,
    repo: string,
    body?: CreateBranchProtectionOption,
    options?: RequestOptions,
  ): Promise<BranchProtection> {
    return this.call(repoCreateBranchProtection, body, { owner, repo }, options);
  }

  /** Delete a branch (repoDeleteBranch). */
  delete(owner: string, repo: string, branch: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteBranch, undefined, { owner, repo, branch }, options);
  }

  /** Delete a branch protection rule (repoDeleteBranchProtection). */
  deleteProtection(owner: string, repo: string, name: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteBranchProtection, undefined, { owner, repo, name }, options);
  }

  /** Change a branch protection rule (repoEditBranchProtection). */
  updateProtection(
    owner: string,
    repo: string,
    name: string,
    body?: EditBranchProtectionOption,
    options?: RequestOptions,
  ): Promise<BranchProtection> {
    return this.call(repoEditBranchProtection, body, { owner, repo, name }, options);
  }

  /** Get a branch (repoGetBranch). */
  get(owner: string, repo: string, branch: string, options?: RequestOptions): Promise<Branch> {
    return this.call(repoGetBranch, undefined, { owner, repo, branch }, options);
  }

  /** Get a branch protection rule (repoGetBranchProtection). */
  getProtection(owner: string, repo: string, name: string, options?: RequestOptions): Promise<BranchProtection> {
    return this.call(repoGetBranchProtection, undefined, { owner, repo, name }, options);
  }

  /** List a repository's branch protection rules (repoListBranchProtection). */
  listProtections(owner: string, repo: string, options?: RequestOptions): Promise<Array<BranchProtection>> {
    return this.call(repoListBranchProtection, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's branches (repoListBranches). */
  list(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number; q?: string } = {},
    options?: RequestOptions,
  ): Promise<Array<Branch>> {
    return this.call(repoListBranches, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number; q?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Branch, void, undefined> {
    return this.paginate(repoListBranches, undefined, { owner, repo, ...params }, options);
  }

  /** Rename a branch (repoRenameBranch). */
  rename(
    owner: string,
    repo: string,
    branch: string,
    body?: RenameBranchRepoOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoRenameBranch, body, { owner, repo, branch }, options);
  }

  /** Point a branch at another commit (repoUpdateBranch). */
  update(
    owner: string,
    repo: string,
    branch: string,
    body?: UpdateBranchRepoOption,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoUpdateBranch, body, { owner, repo, branch }, options);
  }

  /** Set the order in which branch protection rules apply (repoUpdateBranchProtectionPriories). */
  reorderProtections(
    owner: string,
    repo: string,
    body?: UpdateBranchProtectionPriories,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoUpdateBranchProtectionPriories, body, { owner, repo }, options);
  }
}
