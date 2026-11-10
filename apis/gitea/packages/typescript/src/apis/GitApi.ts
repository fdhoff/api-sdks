// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, AnnotatedTag, GitBlobResponse, GitTreeResponse, Note, Reference } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getAnnotatedTag: Operation = {
  id: 'GetAnnotatedTag',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/tags/{sha}',
  resource: 'git',
  name: 'getTag',
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

const getBlob: Operation = {
  id: 'GetBlob',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/blobs/{sha}',
  resource: 'git',
  name: 'getBlob',
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

const getTree: Operation = {
  id: 'GetTree',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/trees/{sha}',
  resource: 'git',
  name: 'getTree',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
    { wire: 'recursive', name: 'recursive', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'per_page', name: 'perPage', location: 'query' },
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

const repoGetNote: Operation = {
  id: 'repoGetNote',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/notes/{sha}',
  resource: 'git',
  name: 'getNote',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'sha', name: 'sha', location: 'path' },
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

const repoListAllGitRefs: Operation = {
  id: 'repoListAllGitRefs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/refs',
  resource: 'git',
  name: 'listRefs',
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

const repoListGitRefs: Operation = {
  id: 'repoListGitRefs',
  method: 'GET',
  path: '/repos/{owner}/{repo}/git/refs/{ref}',
  resource: 'git',
  name: 'listRefsMatching',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'ref', name: 'ref', location: 'path' },
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
  getAnnotatedTag,
  getBlob,
  getTree,
  repoGetNote,
  repoListAllGitRefs,
  repoListGitRefs,
];

export class GitApi extends Resource {
  /** Get an annotated tag object (GetAnnotatedTag). */
  getTag(owner: string, repo: string, sha: string, options?: RequestOptions): Promise<AnnotatedTag> {
    return this.call(getAnnotatedTag, undefined, { owner, repo, sha }, options);
  }

  /** Get a blob (GetBlob). */
  getBlob(owner: string, repo: string, sha: string, options?: RequestOptions): Promise<GitBlobResponse> {
    return this.call(getBlob, undefined, { owner, repo, sha }, options);
  }

  /** Get a tree (GetTree). */
  getTree(
    owner: string,
    repo: string,
    sha: string,
    params: { recursive?: boolean; page?: number; perPage?: number } = {},
    options?: RequestOptions,
  ): Promise<GitTreeResponse> {
    return this.call(getTree, undefined, { owner, repo, sha, ...params }, options);
  }

  /** Get the note attached to a commit (repoGetNote). */
  getNote(
    owner: string,
    repo: string,
    sha: string,
    params: { verification?: boolean; files?: boolean } = {},
    options?: RequestOptions,
  ): Promise<Note> {
    return this.call(repoGetNote, undefined, { owner, repo, sha, ...params }, options);
  }

  /** List a repository's refs (repoListAllGitRefs). */
  listRefs(owner: string, repo: string, options?: RequestOptions): Promise<Array<Reference>> {
    return this.call(repoListAllGitRefs, undefined, { owner, repo }, options);
  }

  /** List the refs that start with a prefix, such as heads (repoListGitRefs). */
  listRefsMatching(owner: string, repo: string, ref: string, options?: RequestOptions): Promise<Array<Reference>> {
    return this.call(repoListGitRefs, undefined, { owner, repo, ref }, options);
  }
}
