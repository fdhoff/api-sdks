// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  APIError,
  Attachment,
  CreateReleaseOption,
  EditAttachmentOptions,
  EditReleaseOption,
  Release,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCreateRelease: Operation = {
  id: 'repoCreateRelease',
  method: 'POST',
  path: '/repos/{owner}/{repo}/releases',
  resource: 'releases',
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

const repoCreateReleaseAttachment: Operation = {
  id: 'repoCreateReleaseAttachment',
  method: 'POST',
  path: '/repos/{owner}/{repo}/releases/{id}/assets',
  resource: 'releases',
  name: 'uploadAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'name', name: 'name', location: 'query' },
    { wire: 'attachment', name: 'attachment', location: 'form' },
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

const repoDeleteRelease: Operation = {
  id: 'repoDeleteRelease',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/releases/{id}',
  resource: 'releases',
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

const repoDeleteReleaseAttachment: Operation = {
  id: 'repoDeleteReleaseAttachment',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}',
  resource: 'releases',
  name: 'deleteAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
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

const repoDeleteReleaseByTag: Operation = {
  id: 'repoDeleteReleaseByTag',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/releases/tags/{tag}',
  resource: 'releases',
  name: 'deleteByTag',
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

const repoEditRelease: Operation = {
  id: 'repoEditRelease',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/releases/{id}',
  resource: 'releases',
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

const repoEditReleaseAttachment: Operation = {
  id: 'repoEditReleaseAttachment',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}',
  resource: 'releases',
  name: 'updateAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
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

const repoGetLatestRelease: Operation = {
  id: 'repoGetLatestRelease',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases/latest',
  resource: 'releases',
  name: 'getLatest',
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

const repoGetRelease: Operation = {
  id: 'repoGetRelease',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases/{id}',
  resource: 'releases',
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

const repoGetReleaseAttachment: Operation = {
  id: 'repoGetReleaseAttachment',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}',
  resource: 'releases',
  name: 'getAttachment',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'id', name: 'id', location: 'path' },
    { wire: 'attachment_id', name: 'attachmentId', location: 'path' },
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

const repoGetReleaseByTag: Operation = {
  id: 'repoGetReleaseByTag',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases/tags/{tag}',
  resource: 'releases',
  name: 'getByTag',
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

const repoListReleaseAttachments: Operation = {
  id: 'repoListReleaseAttachments',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases/{id}/assets',
  resource: 'releases',
  name: 'listAttachments',
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

const repoListReleases: Operation = {
  id: 'repoListReleases',
  method: 'GET',
  path: '/repos/{owner}/{repo}/releases',
  resource: 'releases',
  name: 'list',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'draft', name: 'draft', location: 'query' },
    { wire: 'pre-release', name: 'preRelease', location: 'query' },
    { wire: 'tag_filter', name: 'tagFilter', location: 'query' },
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
  repoCreateRelease,
  repoCreateReleaseAttachment,
  repoDeleteRelease,
  repoDeleteReleaseAttachment,
  repoDeleteReleaseByTag,
  repoEditRelease,
  repoEditReleaseAttachment,
  repoGetLatestRelease,
  repoGetRelease,
  repoGetReleaseAttachment,
  repoGetReleaseByTag,
  repoListReleaseAttachments,
  repoListReleases,
];

export class ReleasesApi extends Resource {
  /** Create a release (repoCreateRelease). */
  create(owner: string, repo: string, body?: CreateReleaseOption, options?: RequestOptions): Promise<Release> {
    return this.call(repoCreateRelease, body, { owner, repo }, options);
  }

  /** Upload an attachment to a release (repoCreateReleaseAttachment). */
  uploadAttachment(
    owner: string,
    repo: string,
    id: number,
    params: { name?: string; attachment?: FileInput } = {},
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(repoCreateReleaseAttachment, undefined, { owner, repo, id, ...params }, options);
  }

  /** Delete a release (repoDeleteRelease). */
  delete(owner: string, repo: string, id: number, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteRelease, undefined, { owner, repo, id }, options);
  }

  /** Delete a release attachment (repoDeleteReleaseAttachment). */
  deleteAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(repoDeleteReleaseAttachment, undefined, { owner, repo, id, attachmentId }, options);
  }

  /** Delete a release by its tag name (repoDeleteReleaseByTag). */
  deleteByTag(owner: string, repo: string, tag: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteReleaseByTag, undefined, { owner, repo, tag }, options);
  }

  /** Change a release (repoEditRelease). */
  update(
    owner: string,
    repo: string,
    id: number,
    body?: EditReleaseOption,
    options?: RequestOptions,
  ): Promise<Release> {
    return this.call(repoEditRelease, body, { owner, repo, id }, options);
  }

  /** Rename a release attachment (repoEditReleaseAttachment). */
  updateAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    body?: EditAttachmentOptions,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(repoEditReleaseAttachment, body, { owner, repo, id, attachmentId }, options);
  }

  /** Get the latest release that is not a draft or prerelease (repoGetLatestRelease). */
  getLatest(owner: string, repo: string, options?: RequestOptions): Promise<Release> {
    return this.call(repoGetLatestRelease, undefined, { owner, repo }, options);
  }

  /** Get a release (repoGetRelease). */
  get(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Release> {
    return this.call(repoGetRelease, undefined, { owner, repo, id }, options);
  }

  /** Get a release attachment (repoGetReleaseAttachment). */
  getAttachment(
    owner: string,
    repo: string,
    id: number,
    attachmentId: number,
    options?: RequestOptions,
  ): Promise<Attachment> {
    return this.call(repoGetReleaseAttachment, undefined, { owner, repo, id, attachmentId }, options);
  }

  /** Get a release by its tag name (repoGetReleaseByTag). */
  getByTag(owner: string, repo: string, tag: string, options?: RequestOptions): Promise<Release> {
    return this.call(repoGetReleaseByTag, undefined, { owner, repo, tag }, options);
  }

  /** List a release's attachments (repoListReleaseAttachments). */
  listAttachments(owner: string, repo: string, id: number, options?: RequestOptions): Promise<Array<Attachment>> {
    return this.call(repoListReleaseAttachments, undefined, { owner, repo, id }, options);
  }

  /** List one page of a repository's releases (repoListReleases). */
  list(
    owner: string,
    repo: string,
    params: { draft?: boolean; preRelease?: boolean; tagFilter?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<Release>> {
    return this.call(repoListReleases, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    owner: string,
    repo: string,
    params: { draft?: boolean; preRelease?: boolean; tagFilter?: string; page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Release, void, undefined> {
    return this.paginate(repoListReleases, undefined, { owner, repo, ...params }, options);
  }
}
