// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AddStoreCategoryRequestType,
  DeleteStoreCategoryRequestType,
  GetStoreCategories429Response,
  GetStoreCategoriesResponseType,
  GetStoreResponseType,
  GetStoreTaskResponseType,
  GetStoreTasksResponseType,
  MoveStoreCategoryRequestType,
  RenameStoreCategoryRequestType,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const addStoreCategory: Operation = {
  id: 'addStoreCategory',
  method: 'POST',
  path: '/sell/stores/v1/store/categories',
  resource: 'store',
  name: 'addCategory',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const deleteStoreCategory: Operation = {
  id: 'deleteStoreCategory',
  method: 'DELETE',
  path: '/sell/stores/v1/store/categories/{category_id}',
  resource: 'store',
  name: 'deleteCategory',
  host: 'api',
  params: [{ wire: 'category_id', name: 'categoryId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const getStore: Operation = {
  id: 'getStore',
  method: 'GET',
  path: '/sell/stores/v1/store',
  resource: 'store',
  name: 'get',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const getStoreCategories: Operation = {
  id: 'getStoreCategories',
  method: 'GET',
  path: '/sell/stores/v1/store/categories',
  resource: 'store',
  name: 'listCategories',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const getStoreTask: Operation = {
  id: 'getStoreTask',
  method: 'GET',
  path: '/sell/stores/v1/store/tasks/{task_id}',
  resource: 'store',
  name: 'getTask',
  host: 'api',
  params: [{ wire: 'task_id', name: 'taskId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const getStoreTasks: Operation = {
  id: 'getStoreTasks',
  method: 'GET',
  path: '/sell/stores/v1/store/tasks',
  resource: 'store',
  name: 'listTasks',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const moveStoreCategory: Operation = {
  id: 'moveStoreCategory',
  method: 'POST',
  path: '/sell/stores/v1/store/categories/move_category',
  resource: 'store',
  name: 'moveCategory',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

const renameStoreCategory: Operation = {
  id: 'renameStoreCategory',
  method: 'PUT',
  path: '/sell/stores/v1/store/categories/{category_id}',
  resource: 'store',
  name: 'renameCategory',
  host: 'api',
  params: [{ wire: 'category_id', name: 'categoryId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.stores'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  addStoreCategory,
  deleteStoreCategory,
  getStore,
  getStoreCategories,
  getStoreTask,
  getStoreTasks,
  moveStoreCategory,
  renameStoreCategory,
];

export class StoreApi extends Resource {
  /** Start a task that adds a store category. */
  addCategory(body?: AddStoreCategoryRequestType, options?: RequestOptions): Promise<void> {
    return this.call(addStoreCategory, body, {}, options);
  }

  /** Start a task that deletes a store category. */
  deleteCategory(categoryId: string, body?: DeleteStoreCategoryRequestType, options?: RequestOptions): Promise<void> {
    return this.call(deleteStoreCategory, body, { categoryId }, options);
  }

  /** Get the seller's eBay store. */
  get(options?: RequestOptions): Promise<GetStoreResponseType> {
    return this.call(getStore, undefined, {}, options);
  }

  /** List the categories of the seller's store. */
  listCategories(options?: RequestOptions): Promise<GetStoreCategoriesResponseType> {
    return this.call(getStoreCategories, undefined, {}, options);
  }

  /** Get one store category task. */
  getTask(taskId: string, options?: RequestOptions): Promise<GetStoreTaskResponseType> {
    return this.call(getStoreTask, undefined, { taskId }, options);
  }

  /** List the seller's store category tasks. */
  listTasks(options?: RequestOptions): Promise<GetStoreTasksResponseType> {
    return this.call(getStoreTasks, undefined, {}, options);
  }

  /** Start a task that moves a store category. */
  moveCategory(body: MoveStoreCategoryRequestType, options?: RequestOptions): Promise<void> {
    return this.call(moveStoreCategory, body, {}, options);
  }

  /** Rename a store category. */
  renameCategory(categoryId: string, body?: RenameStoreCategoryRequestType, options?: RequestOptions): Promise<void> {
    return this.call(renameStoreCategory, body, { categoryId }, options);
  }
}
