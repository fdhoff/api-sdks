// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  TreasuryAccountsPaginatedResponse,
  TreasuryStatementsPaginatedResponse,
  TreasuryTransactionsResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getTreasury: Operation = {
  id: 'getTreasury',
  method: 'GET',
  path: '/treasury',
  resource: 'treasury',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'accounts', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getTreasuryStatements: Operation = {
  id: 'getTreasuryStatements',
  method: 'GET',
  path: '/treasury/{treasuryId}/statements',
  resource: 'treasury',
  name: 'listStatements',
  host: 'api',
  params: [
    { wire: 'treasuryId', name: 'treasuryId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'documentType', name: 'documentType', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterStatements',
  paging: { style: 'cursor', items: 'statements', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getTreasuryTransactions: Operation = {
  id: 'getTreasuryTransactions',
  method: 'GET',
  path: '/treasury/{treasuryId}/transactions',
  resource: 'treasury',
  name: 'listTransactions',
  host: 'api',
  params: [
    { wire: 'treasuryId', name: 'treasuryId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'cursor', name: 'cursor', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTransactions',
  paging: { style: 'cursor', items: 'transactions', next: 'cursor', param: 'cursor' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getTreasury, getTreasuryStatements, getTreasuryTransactions];

export class TreasuryApi extends Resource {
  /** List one page of treasury accounts. */
  list(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<TreasuryAccountsPaginatedResponse> {
    return this.call(getTreasury, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TreasuryAccount, void, undefined> {
    return this.paginate(getTreasury, undefined, { ...params }, options);
  }

  /** List one page of a treasury account's statements. */
  listStatements(
    treasuryId: string,
    params: {
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
      documentType?:
        | 'MonthlyStatement'
        | 'TradeConfirmation'
        | '1099'
        | '1099R'
        | '1042S'
        | '5498'
        | '5498ESA'
        | '1099Q'
        | 'FMV'
        | 'SDIRA';
    } = {},
    options?: RequestOptions,
  ): Promise<TreasuryStatementsPaginatedResponse> {
    return this.call(getTreasuryStatements, undefined, { treasuryId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterStatements(
    treasuryId: string,
    params: {
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
      documentType?:
        | 'MonthlyStatement'
        | 'TradeConfirmation'
        | '1099'
        | '1099R'
        | '1042S'
        | '5498'
        | '5498ESA'
        | '1099Q'
        | 'FMV'
        | 'SDIRA';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TreasuryStatement, void, undefined> {
    return this.paginate(getTreasuryStatements, undefined, { treasuryId, ...params }, options);
  }

  /** List one page of a treasury account's transactions. */
  listTransactions(
    treasuryId: string,
    params: { limit?: number; order?: 'asc' | 'desc'; cursor?: number } = {},
    options?: RequestOptions,
  ): Promise<TreasuryTransactionsResponse> {
    return this.call(getTreasuryTransactions, undefined, { treasuryId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTransactions(
    treasuryId: string,
    params: { limit?: number; order?: 'asc' | 'desc'; cursor?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TreasuryTxn, void, undefined> {
    return this.paginate(getTreasuryTransactions, undefined, { treasuryId, ...params }, options);
  }
}
