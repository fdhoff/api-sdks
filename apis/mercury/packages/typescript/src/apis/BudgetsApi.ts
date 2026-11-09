// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiV1AssignTransactionRequest,
  ApiV1BudgetExpendituresResponse,
  ApiV1BudgetIdResponse,
  ApiV1BudgetMembersResponse,
  ApiV1CreateBudgetRequest,
  ApiV1SpendBudgetResponse,
  ApiV1SpendBudgetsResponse,
  ApiV1UpdateBudgetRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const archiveBudget: Operation = {
  id: 'archiveBudget',
  method: 'POST',
  path: '/spend/budgets/{budgetId}/archive',
  resource: 'budgets',
  name: 'archive',
  host: 'api',
  params: [{ wire: 'budgetId', name: 'budgetId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const assignTransactionToBudget: Operation = {
  id: 'assignTransactionToBudget',
  method: 'POST',
  path: '/spend/budgets/{budgetId}/assign-transaction',
  resource: 'budgets',
  name: 'assignTransaction',
  host: 'api',
  params: [{ wire: 'budgetId', name: 'budgetId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const createBudget: Operation = {
  id: 'createBudget',
  method: 'POST',
  path: '/spend/budgets',
  resource: 'budgets',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getBudget: Operation = {
  id: 'getBudget',
  method: 'GET',
  path: '/spend/budgets/{budgetId}',
  resource: 'budgets',
  name: 'get',
  host: 'api',
  params: [{ wire: 'budgetId', name: 'budgetId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getBudgetExpenditures: Operation = {
  id: 'getBudgetExpenditures',
  method: 'GET',
  path: '/spend/budgets/{budgetId}/expenditures',
  resource: 'budgets',
  name: 'listExpenditures',
  host: 'api',
  params: [
    { wire: 'budgetId', name: 'budgetId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterExpenditures',
  paging: { style: 'cursor', items: 'expenditures', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getBudgetMembers: Operation = {
  id: 'getBudgetMembers',
  method: 'GET',
  path: '/spend/budgets/{budgetId}/members',
  resource: 'budgets',
  name: 'listMembers',
  host: 'api',
  params: [
    { wire: 'budgetId', name: 'budgetId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterMembers',
  paging: { style: 'cursor', items: 'members', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listBudgets: Operation = {
  id: 'listBudgets',
  method: 'GET',
  path: '/spend/budgets',
  resource: 'budgets',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_at', name: 'startAt', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'budgets', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateBudget: Operation = {
  id: 'updateBudget',
  method: 'POST',
  path: '/spend/budgets/{budgetId}',
  resource: 'budgets',
  name: 'update',
  host: 'api',
  params: [{ wire: 'budgetId', name: 'budgetId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  archiveBudget,
  assignTransactionToBudget,
  createBudget,
  getBudget,
  getBudgetExpenditures,
  getBudgetMembers,
  listBudgets,
  updateBudget,
];

export class BudgetsApi extends Resource {
  /** Archive a published budget */
  archive(budgetId: string, options?: RequestOptions): Promise<void> {
    return this.call(archiveBudget, undefined, { budgetId }, options);
  }

  /** Count a transaction against a budget. */
  assignTransaction(budgetId: string, body?: ApiV1AssignTransactionRequest, options?: RequestOptions): Promise<void> {
    return this.call(assignTransactionToBudget, body, { budgetId }, options);
  }

  /** Create a budget. */
  create(body?: ApiV1CreateBudgetRequest, options?: RequestOptions): Promise<ApiV1BudgetIdResponse> {
    return this.call(createBudget, body, {}, options);
  }

  /** Get one budget. */
  get(budgetId: string, options?: RequestOptions): Promise<ApiV1SpendBudgetResponse> {
    return this.call(getBudget, undefined, { budgetId }, options);
  }

  /** List one page of a budget's spending. */
  listExpenditures(
    budgetId: string,
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1BudgetExpendituresResponse> {
    return this.call(getBudgetExpenditures, undefined, { budgetId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterExpenditures(
    budgetId: string,
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1BudgetExpenditure, void, undefined> {
    return this.paginate(getBudgetExpenditures, undefined, { budgetId, ...params }, options);
  }

  /** List one page of a budget's members. */
  listMembers(
    budgetId: string,
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1BudgetMembersResponse> {
    return this.call(getBudgetMembers, undefined, { budgetId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterMembers(
    budgetId: string,
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1BudgetMember, void, undefined> {
    return this.paginate(getBudgetMembers, undefined, { budgetId, ...params }, options);
  }

  /** List one page of budgets. */
  list(
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<ApiV1SpendBudgetsResponse> {
    return this.call(listBudgets, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAt?: string; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1SpendBudgetResponse, void, undefined> {
    return this.paginate(listBudgets, undefined, { ...params }, options);
  }

  /** Update a budget. */
  update(budgetId: string, body?: ApiV1UpdateBudgetRequest, options?: RequestOptions): Promise<ApiV1BudgetIdResponse> {
    return this.call(updateBudget, body, { budgetId }, options);
  }
}
