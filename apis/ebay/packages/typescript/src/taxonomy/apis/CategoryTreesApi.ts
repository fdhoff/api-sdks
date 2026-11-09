// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AspectMetadata,
  BaseCategoryTree,
  CategorySubtree,
  CategorySuggestionResponse,
  CategoryTree,
  ExpiredCategories,
  FetchItemAspects429Response,
  GetCategoriesAspectResponse,
  GetCompatibilityMetadataResponse,
  GetCompatibilityPropertyValuesResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const fetchItemAspects: Operation = {
  id: 'fetchItemAspects',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects',
  resource: 'categoryTrees',
  name: 'fetchItemAspects',
  host: 'api',
  params: [{ wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: ['https://api.ebay.com/oauth/api_scope', 'https://api.ebay.com/oauth/api_scope/metadata.insights'],
      },
    ],
  ],
};

const getCategorySubtree: Operation = {
  id: 'getCategorySubtree',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree',
  resource: 'categoryTrees',
  name: 'getSubtree',
  host: 'api',
  params: [
    { wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' },
    { wire: 'category_id', name: 'categoryId', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCategorySuggestions: Operation = {
  id: 'getCategorySuggestions',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions',
  resource: 'categoryTrees',
  name: 'getSuggestions',
  host: 'api',
  params: [
    { wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' },
    { wire: 'q', name: 'q', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCategoryTree: Operation = {
  id: 'getCategoryTree',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}',
  resource: 'categoryTrees',
  name: 'get',
  host: 'api',
  params: [{ wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCompatibilityProperties: Operation = {
  id: 'getCompatibilityProperties',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties',
  resource: 'categoryTrees',
  name: 'getCompatibilityProperties',
  host: 'api',
  params: [
    { wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' },
    { wire: 'category_id', name: 'categoryId', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCompatibilityPropertyValues: Operation = {
  id: 'getCompatibilityPropertyValues',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values',
  resource: 'categoryTrees',
  name: 'getCompatibilityPropertyValues',
  host: 'api',
  params: [
    { wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' },
    { wire: 'compatibility_property', name: 'compatibilityProperty', location: 'query' },
    { wire: 'category_id', name: 'categoryId', location: 'query' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getDefaultCategoryTreeId: Operation = {
  id: 'getDefaultCategoryTreeId',
  method: 'GET',
  path: '/commerce/taxonomy/v1/get_default_category_tree_id',
  resource: 'categoryTrees',
  name: 'getDefaultId',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'query' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getExpiredCategories: Operation = {
  id: 'getExpiredCategories',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories',
  resource: 'categoryTrees',
  name: 'getExpiredCategories',
  host: 'api',
  params: [{ wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getItemAspectsForCategory: Operation = {
  id: 'getItemAspectsForCategory',
  method: 'GET',
  path: '/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category',
  resource: 'categoryTrees',
  name: 'getItemAspects',
  host: 'api',
  params: [
    { wire: 'category_tree_id', name: 'categoryTreeId', location: 'path' },
    { wire: 'category_id', name: 'categoryId', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: ['https://api.ebay.com/oauth/api_scope', 'https://api.ebay.com/oauth/api_scope/metadata.insights'],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  fetchItemAspects,
  getCategorySubtree,
  getCategorySuggestions,
  getCategoryTree,
  getCompatibilityProperties,
  getCompatibilityPropertyValues,
  getDefaultCategoryTreeId,
  getExpiredCategories,
  getItemAspectsForCategory,
];

export class CategoryTreesApi extends Resource {
  /** Get the item aspects of every leaf category in a tree */
  fetchItemAspects(categoryTreeId: string, options?: RequestOptions): Promise<GetCategoriesAspectResponse> {
    return this.call(fetchItemAspects, undefined, { categoryTreeId }, options);
  }

  /** Get the part of a category tree under one category. */
  getSubtree(
    categoryTreeId: string,
    params: { categoryId: string },
    options?: RequestOptions,
  ): Promise<CategorySubtree> {
    return this.call(getCategorySubtree, undefined, { categoryTreeId, ...params }, options);
  }

  /** Suggest leaf categories for a search phrase. */
  getSuggestions(
    categoryTreeId: string,
    params: { q: string },
    options?: RequestOptions,
  ): Promise<CategorySuggestionResponse | undefined> {
    return this.call(getCategorySuggestions, undefined, { categoryTreeId, ...params }, options);
  }

  /** Get a whole category tree. */
  get(categoryTreeId: string, options?: RequestOptions): Promise<CategoryTree> {
    return this.call(getCategoryTree, undefined, { categoryTreeId }, options);
  }

  /** List the parts compatibility properties of a category. */
  getCompatibilityProperties(
    categoryTreeId: string,
    params: { categoryId: string },
    options?: RequestOptions,
  ): Promise<GetCompatibilityMetadataResponse | undefined> {
    return this.call(getCompatibilityProperties, undefined, { categoryTreeId, ...params }, options);
  }

  /** List the values of one parts compatibility property. */
  getCompatibilityPropertyValues(
    categoryTreeId: string,
    params: { compatibilityProperty: string; categoryId: string; filter?: string },
    options?: RequestOptions,
  ): Promise<GetCompatibilityPropertyValuesResponse | undefined> {
    return this.call(getCompatibilityPropertyValues, undefined, { categoryTreeId, ...params }, options);
  }

  /** Get the ID of a marketplace's default category tree. */
  getDefaultId(params: { marketplaceId: string }, options?: RequestOptions): Promise<BaseCategoryTree | undefined> {
    return this.call(getDefaultCategoryTreeId, undefined, { ...params }, options);
  }

  /** List the leaf categories that expired and what replaced them. */
  getExpiredCategories(categoryTreeId: string, options?: RequestOptions): Promise<ExpiredCategories | undefined> {
    return this.call(getExpiredCategories, undefined, { categoryTreeId }, options);
  }

  /** List the item aspects of one leaf category. */
  getItemAspects(
    categoryTreeId: string,
    params: { categoryId: string },
    options?: RequestOptions,
  ): Promise<AspectMetadata | undefined> {
    return this.call(getItemAspectsForCategory, undefined, { categoryTreeId, ...params }, options);
  }
}
