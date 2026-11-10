// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APIError, CreateWikiPageOptions, WikiCommitList, WikiPage, WikiPageMetaData } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const repoCreateWikiPage: Operation = {
  id: 'repoCreateWikiPage',
  method: 'POST',
  path: '/repos/{owner}/{repo}/wiki/new',
  resource: 'wiki',
  name: 'createPage',
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

const repoDeleteWikiPage: Operation = {
  id: 'repoDeleteWikiPage',
  method: 'DELETE',
  path: '/repos/{owner}/{repo}/wiki/page/{pageName}',
  resource: 'wiki',
  name: 'deletePage',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'pageName', name: 'pageName', location: 'path' },
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

const repoEditWikiPage: Operation = {
  id: 'repoEditWikiPage',
  method: 'PATCH',
  path: '/repos/{owner}/{repo}/wiki/page/{pageName}',
  resource: 'wiki',
  name: 'updatePage',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'pageName', name: 'pageName', location: 'path' },
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

const repoGetWikiPage: Operation = {
  id: 'repoGetWikiPage',
  method: 'GET',
  path: '/repos/{owner}/{repo}/wiki/page/{pageName}',
  resource: 'wiki',
  name: 'getPage',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'pageName', name: 'pageName', location: 'path' },
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

const repoGetWikiPageRevisions: Operation = {
  id: 'repoGetWikiPageRevisions',
  method: 'GET',
  path: '/repos/{owner}/{repo}/wiki/revisions/{pageName}',
  resource: 'wiki',
  name: 'listPageRevisions',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'pageName', name: 'pageName', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
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

const repoGetWikiPages: Operation = {
  id: 'repoGetWikiPages',
  method: 'GET',
  path: '/repos/{owner}/{repo}/wiki/pages',
  resource: 'wiki',
  name: 'listPages',
  params: [
    { wire: 'owner', name: 'owner', location: 'path' },
    { wire: 'repo', name: 'repo', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterPages',
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
  repoCreateWikiPage,
  repoDeleteWikiPage,
  repoEditWikiPage,
  repoGetWikiPage,
  repoGetWikiPageRevisions,
  repoGetWikiPages,
];

export class WikiApi extends Resource {
  /** Create a wiki page (repoCreateWikiPage). */
  createPage(owner: string, repo: string, body?: CreateWikiPageOptions, options?: RequestOptions): Promise<WikiPage> {
    return this.call(repoCreateWikiPage, body, { owner, repo }, options);
  }

  /** Delete a wiki page (repoDeleteWikiPage). */
  deletePage(owner: string, repo: string, pageName: string, options?: RequestOptions): Promise<void> {
    return this.call(repoDeleteWikiPage, undefined, { owner, repo, pageName }, options);
  }

  /** Change a wiki page (repoEditWikiPage). */
  updatePage(
    owner: string,
    repo: string,
    pageName: string,
    body?: CreateWikiPageOptions,
    options?: RequestOptions,
  ): Promise<WikiPage> {
    return this.call(repoEditWikiPage, body, { owner, repo, pageName }, options);
  }

  /** Get a wiki page (repoGetWikiPage). */
  getPage(owner: string, repo: string, pageName: string, options?: RequestOptions): Promise<WikiPage> {
    return this.call(repoGetWikiPage, undefined, { owner, repo, pageName }, options);
  }

  /** List a wiki page's revisions (repoGetWikiPageRevisions). */
  listPageRevisions(
    owner: string,
    repo: string,
    pageName: string,
    params: { page?: number } = {},
    options?: RequestOptions,
  ): Promise<WikiCommitList> {
    return this.call(repoGetWikiPageRevisions, undefined, { owner, repo, pageName, ...params }, options);
  }

  /** List one page of a repository's wiki pages (repoGetWikiPages). */
  listPages(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): Promise<Array<WikiPageMetaData>> {
    return this.call(repoGetWikiPages, undefined, { owner, repo, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterPages(
    owner: string,
    repo: string,
    params: { page?: number; limit?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.WikiPageMetaData, void, undefined> {
    return this.paginate(repoGetWikiPages, undefined, { owner, repo, ...params }, options);
  }
}
