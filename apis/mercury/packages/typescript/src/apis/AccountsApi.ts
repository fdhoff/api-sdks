// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AccountCardsResponse,
  AccountsPaginatedResponse,
  DepositoryAccountStatementsPaginatedResponse,
  InternalTransferAPIRequest,
  InternalTransferAPIResponse,
  PostTransactionAPIRequest,
  SendMoneyAPIRequest,
  SendMoneyApprovalRequestResponse,
  Transaction,
  TransactionsResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createInternalTransfer: Operation = {
  id: 'createInternalTransfer',
  method: 'POST',
  path: '/transfer',
  resource: 'accounts',
  name: 'transfer',
  host: 'api',
  params: [],
  hasBody: true,
  idempotencyKey: 'idempotencyKey',
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const createTransaction: Operation = {
  id: 'createTransaction',
  method: 'POST',
  path: '/account/{accountId}/transactions',
  resource: 'accounts',
  name: 'sendMoney',
  host: 'api',
  params: [{ wire: 'accountId', name: 'accountId', location: 'path' }],
  hasBody: true,
  idempotencyKey: 'idempotencyKey',
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getAccountCards: Operation = {
  id: 'getAccountCards',
  method: 'GET',
  path: '/account/{accountId}/cards',
  resource: 'accounts',
  name: 'listCards',
  host: 'api',
  params: [{ wire: 'accountId', name: 'accountId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getAccountStatements: Operation = {
  id: 'getAccountStatements',
  method: 'GET',
  path: '/account/{accountId}/statements',
  resource: 'accounts',
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

const getAccounts: Operation = {
  id: 'getAccounts',
  method: 'GET',
  path: '/accounts',
  resource: 'accounts',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'accounts', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getTransaction: Operation = {
  id: 'getTransaction',
  method: 'GET',
  path: '/account/{accountId}/transaction/{transactionId}',
  resource: 'accounts',
  name: 'getTransaction',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'path' },
    { wire: 'transactionId', name: 'transactionId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listAccountTransactions: Operation = {
  id: 'listAccountTransactions',
  method: 'GET',
  path: '/account/{accountId}/transactions',
  resource: 'accounts',
  name: 'listTransactions',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start', name: 'start', location: 'query' },
    { wire: 'end', name: 'end', location: 'query' },
    { wire: 'search', name: 'search', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'requestId', name: 'requestId', location: 'query' },
    { wire: 'mercuryCategory', name: 'mercuryCategory', location: 'query' },
    { wire: 'categoryId', name: 'categoryId', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTransactions',
  paging: { style: 'offset', items: 'transactions', total: 'total', offset: 'offset' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const requestSendMoney: Operation = {
  id: 'requestSendMoney',
  method: 'POST',
  path: '/account/{accountId}/request-send-money',
  resource: 'accounts',
  name: 'requestSendMoney',
  host: 'api',
  params: [{ wire: 'accountId', name: 'accountId', location: 'path' }],
  hasBody: true,
  idempotencyKey: 'idempotencyKey',
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createInternalTransfer,
  createTransaction,
  getAccountCards,
  getAccountStatements,
  getAccounts,
  getTransaction,
  listAccountTransactions,
  requestSendMoney,
];

export class AccountsApi extends Resource {
  /** Move money between two of your accounts. */
  transfer(body?: InternalTransferAPIRequest, options?: RequestOptions): Promise<InternalTransferAPIResponse> {
    return this.call(createInternalTransfer, body, {}, options);
  }

  /** Send money from an account to a recipient. */
  sendMoney(accountId: string, body?: PostTransactionAPIRequest, options?: RequestOptions): Promise<Transaction> {
    return this.call(createTransaction, body, { accountId }, options);
  }

  /** List the cards issued on an account. */
  listCards(accountId: string, options?: RequestOptions): Promise<AccountCardsResponse> {
    return this.call(getAccountCards, undefined, { accountId }, options);
  }

  /** List one page of an account's statements. */
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
  ): Promise<DepositoryAccountStatementsPaginatedResponse> {
    return this.call(getAccountStatements, undefined, { accountId, ...params }, options);
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
  ): AsyncGenerator<models.DepositoryAccountStatement, void, undefined> {
    return this.paginate(getAccountStatements, undefined, { accountId, ...params }, options);
  }

  /** List one page of your accounts. */
  list(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): Promise<AccountsPaginatedResponse> {
    return this.call(getAccounts, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Account, void, undefined> {
    return this.paginate(getAccounts, undefined, { ...params }, options);
  }

  /** Get one transaction of an account. */
  getTransaction(accountId: string, transactionId: string, options?: RequestOptions): Promise<Transaction> {
    return this.call(getTransaction, undefined, { accountId, transactionId }, options);
  }

  /** List one page of an account's transactions. */
  listTransactions(
    accountId: string,
    params: {
      limit?: number;
      start?: string;
      end?: string;
      search?: string;
      status?: 'pending' | 'sent' | 'cancelled' | 'failed' | 'reversed' | 'blocked';
      offset?: number;
      order?: 'asc' | 'desc';
      requestId?: string;
      mercuryCategory?: string;
      categoryId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<TransactionsResponse> {
    return this.call(listAccountTransactions, undefined, { accountId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTransactions(
    accountId: string,
    params: {
      limit?: number;
      start?: string;
      end?: string;
      search?: string;
      status?: 'pending' | 'sent' | 'cancelled' | 'failed' | 'reversed' | 'blocked';
      offset?: number;
      order?: 'asc' | 'desc';
      requestId?: string;
      mercuryCategory?: string;
      categoryId?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Transaction, void, undefined> {
    return this.paginate(listAccountTransactions, undefined, { accountId, ...params }, options);
  }

  /** Ask to send money from an account */
  requestSendMoney(
    accountId: string,
    body?: SendMoneyAPIRequest,
    options?: RequestOptions,
  ): Promise<SendMoneyApprovalRequestResponse> {
    return this.call(requestSendMoney, body, { accountId }, options);
  }
}
