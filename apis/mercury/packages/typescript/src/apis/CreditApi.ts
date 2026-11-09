// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreditAccountStatementsPaginatedResponse, CreditAccountsResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getCreditAccountStatements: Operation = {
  id: 'getCreditAccountStatements',
  method: 'GET',
  path: '/credit/{accountId}/statements',
  resource: 'credit',
  name: 'listStatements',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'start', name: 'start', location: 'query' },
    { wire: 'end', name: 'end', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStatements',
  paging: { style: 'cursor', items: 'statements', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listCredit: Operation = {
  id: 'listCredit',
  method: 'GET',
  path: '/credit',
  resource: 'credit',
  name: 'list',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getCreditAccountStatements, listCredit];

export class CreditApi extends Resource {
  /** List one page of a credit account's statements. */
  listStatements(
    accountId: string,
    params: {
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
      start?: string;
      end?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<CreditAccountStatementsPaginatedResponse> {
    return this.call(getCreditAccountStatements, undefined, { accountId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStatements(
    accountId: string,
    params: {
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
      start?: string;
      end?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.AccountStatement, void, undefined> {
    return this.paginate(getCreditAccountStatements, undefined, { accountId, ...params }, options);
  }

  /** List your credit accounts. */
  list(options?: RequestOptions): Promise<CreditAccountsResponse> {
    return this.call(listCredit, undefined, {}, options);
  }
}
