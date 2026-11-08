// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BackboxPage, Competitor, ErrorResponseV3 } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getBackboxData: Operation = {
  id: 'GetBackboxData',
  method: 'GET',
  path: '/ws/listings_bi',
  resource: 'backbox',
  name: 'list',
  params: [
    { wire: 'page', name: 'page', location: 'query' },
    { wire: 'page-size', name: 'pageSize', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'results', link: 'next', params: ['page', 'cursor'] },
  security: [[{ scheme: 'ApiKeyAuth', scopes: [] }]],
};

const getWsBackboxV1Competitors: Operation = {
  id: 'get-ws-backbox-v1-competitors',
  method: 'GET',
  path: '/ws/backbox/v1/competitors/{listingId}',
  resource: 'backbox',
  name: 'listCompetitors',
  params: [{ wire: 'listingId', name: 'listingId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'ApiKeyAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getBackboxData, getWsBackboxV1Competitors];

export class BackboxApi extends Resource {
  /** List one page of Backbox data. */
  list(params: { page?: number; pageSize?: number } = {}, options?: RequestOptions): Promise<BackboxPage> {
    return this.call(getBackboxData, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { page?: number; pageSize?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Backbox, void, undefined> {
    return this.paginate(getBackboxData, undefined, { ...params }, options);
  }

  /** List competitors for a listing. */
  listCompetitors(listingId: string, options?: RequestOptions): Promise<Array<Competitor>> {
    return this.call(getWsBackboxV1Competitors, undefined, { listingId }, options);
  }
}
