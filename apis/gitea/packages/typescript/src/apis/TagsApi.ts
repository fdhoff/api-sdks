// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  CreateTagOption,
  CreateTagProtectionOption,
  EditTagProtectionOption,
  Tag,
  TagProtection,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCreateTag: Operation = {
  id: 'repoCreateTag',
  method: 'POST',
  path: '/repos/{owner}/{repo}/tags',
  resource: 'tags',
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

const repoCreateTagProtection: Operation = {
  id: 'repoCreateTagProtection',
  method: 'POST',
  path: '/repos/{owner}/{repo}/tag_protections',
  resource: 'tags',
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

const repoDeleteTag: Operation = {
  id: 'repoDeleteTag',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/tags/{tag}',
  resource: 'tags',
  name: 'delete',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'tag', name: 'tag', location: 'path' },
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

const repoDeleteTagProtection: Operation = {
  id: 'repoDeleteTagProtection',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/tag_protections/{id}',
  resource: 'tags',
  name: 'deleteProtection',
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

const repoEditTagProtection: Operation = {
  id: 'repoEditTagProtection',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/tag_protections/{id}',
  resource: 'tags',
  name: 'updateProtection',
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

const repoGetTag: Operation = {
  id: 'repoGetTag',
  method: 'GET',
  path: '/repos/{owner}/{repo}/tags/{tag}',
  resource: 'tags',
  name: 'get',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'tag', name: 'tag', location: 'path' },
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

const repoGetTagProtection: Operation = {
  id: 'repoGetTagProtection',
  method: 'GET',
  path: '/repos/{owner}/{repo}/tag_protections/{id}',
  resource: 'tags',
  name: 'getProtection',
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

const repoListTagProtection: Operation = {
  id: 'repoListTagProtection',
  method: 'GET',
  path: '/repos/{owner}/{repo}/tag_protections',
  resource: 'tags',
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

const repoListTags: Operation = {
  id: 'repoListTags',
  method: 'GET',
  path: '/repos/{owner}/{repo}/tags',
  resource: 'tags',
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

export const OPERATIONS: readonly Operation[] = [
  repoCreateTag,
  repoCreateTagProtection,
  repoDeleteTag,
  repoDeleteTagProtection,
  repoEditTagProtection,
  repoGetTag,
  repoGetTagProtection,
  repoListTagProtection,
  repoListTags,
];

export class TagsApi extends Resource {
  /** Create a tag (repoCreateTag). */
  create(owner: string, repo: string, body?: CreateTagOption, options?: RequestOptions): Promise<Tag> {
    return this.call(repoCreateTag, body, { owner, repo }, options);
  }

  /** Create a tag protection rule (repoCreateTagProtection). */
  createProtection(
    owner: string,
    repo: string,
    body?: CreateTagProtectionOption,
    options?: RequestOptions,
  ): Promise<TagProtection> {
    return this.call(repoCreateTagProtection, body, { owner, repo }, options);
  }

  /** Delete a tag (repoDeleteTag). */
  delete(owner: string, repo: string, tag: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteTag, undefined, { owner, repo, tag }, options);
  }

  /** Delete a tag protection rule (repoDeleteTagProtection). */
  deleteProtection(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteTagProtection, undefined, { owner, repo, id }, options);
  }

  /** Change a tag protection rule (repoEditTagProtection). */
  updateProtection(
    owner: string,
    repo: string,
    id: number,
    body?: EditTagProtectionOption,
    options?: RequestOptions,
  ): Promise<TagProtection> {
    return this.call(repoEditTagProtection, body, { owner, repo, id }, options);
  }

  /** Get a tag (repoGetTag). */
  get(owner: string, repo: string, tag: string, options?: RequestOptions): Promise<Tag> {
    return this.call(repoGetTag, undefined, { owner, repo, tag }, options);
  }

  /** Get a tag protection rule (repoGetTagProtection). */
  getProtection(owner: string, repo: string, id: number, options?: RequestOptions): Promise<TagProtection> {
    return this.call(repoGetTagProtection, undefined, { owner, repo, id }, options);
  }

  /** List a repository's tag protection rules (repoListTagProtection). */
  listProtections(owner: string, repo: string, options?: RequestOptions): Promise<Array<TagProtection>> {
    return this.call(repoListTagProtection, undefined, { owner, repo }, options);
  }

  /** List one page of a repository's tags (repoListTags). */
  list(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Tag>> {
    return this.call(repoListTags, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Tag, void, undefined> {
    return this.paginate(repoListTags, undefined, { owner, repo, ...params }, options);
  }
}
