// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CategoryTree, ErrorResponseV1, ErrorResponseV2 } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation } from '../runtime/index.js';

const getBmCatalogCategory: Operation = {
  id: 'get-bm-catalog-category',
  method: 'GET',
  path: '/ws/category/tree',
  resource: 'categories',
  name: 'list',
  params: [],
};

const getBmCatalogCategoryBranch: Operation = {
  id: 'get-bm-catalog-category-branch',
  method: 'GET',
  path: '/ws/category/tree/{categoryId}',
  resource: 'categories',
  name: 'get',
  params: [{ wire: 'categoryId', name: 'categoryId', location: 'path' }],
};

export const OPERATIONS: readonly Operation[] = [getBmCatalogCategory, getBmCatalogCategoryBranch];

export class CategoriesApi extends Resource {
  /** List the category tree. */
  list(): Promise<Array<CategoryTree>> {
    return this.call(getBmCatalogCategory, undefined, {});
  }

  /** Get one branch of the category tree. */
  get(categoryId: number): Promise<CategoryTree> {
    return this.call(getBmCatalogCategoryBranch, undefined, { categoryId });
  }
}
