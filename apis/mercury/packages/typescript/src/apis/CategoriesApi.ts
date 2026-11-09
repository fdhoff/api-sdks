// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CategoriesPaginatedResponse,
  CategoryData,
  CreateCategoryApiRequest,
  EditCategoryApiRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createCategory: Operation = {
  id: 'createCategory',
  method: 'POST',
  path: '/categories',
  resource: 'categories',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const deleteCategory: Operation = {
  id: 'deleteCategory',
  method: 'DELETE',
  path: '/categories/{expenseCategoryId}',
  resource: 'categories',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'expenseCategoryId', name: 'expenseCategoryId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const editCategory: Operation = {
  id: 'editCategory',
  method: 'POST',
  path: '/categories/{expenseCategoryId}',
  resource: 'categories',
  name: 'update',
  host: 'api',
  params: [{ wire: 'expenseCategoryId', name: 'expenseCategoryId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listCategories: Operation = {
  id: 'listCategories',
  method: 'GET',
  path: '/categories',
  resource: 'categories',
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
  paging: { style: 'cursor', items: 'categories', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [createCategory, deleteCategory, editCategory, listCategories];

export class CategoriesApi extends Resource {
  /** Create an expense category. */
  create(body?: CreateCategoryApiRequest, options?: RequestOptions): Promise<CategoryData> {
    return this.call(createCategory, body, {}, options);
  }

  /** Delete an expense category. */
  delete(expenseCategoryId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteCategory, undefined, { expenseCategoryId }, options);
  }

  /** Update an expense category. */
  update(expenseCategoryId: string, body?: EditCategoryApiRequest, options?: RequestOptions): Promise<CategoryData> {
    return this.call(editCategory, body, { expenseCategoryId }, options);
  }

  /** List one page of expense categories. */
  list(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): Promise<CategoriesPaginatedResponse> {
    return this.call(listCategories, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CategoryData, void, undefined> {
    return this.paginate(listCategories, undefined, { ...params }, options);
  }
}
