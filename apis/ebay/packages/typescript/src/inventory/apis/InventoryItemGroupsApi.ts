// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BaseResponse, BulkCreateOrReplaceInventoryItem429Response, InventoryItemGroup } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createOrReplaceInventoryItemGroup: Operation = {
  id: 'createOrReplaceInventoryItemGroup',
  method: 'PUT',
  path: '/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}',
  resource: 'inventoryItemGroups',
  name: 'createOrReplace',
  host: 'api',
  params: [
    { wire: 'inventoryItemGroupKey', name: 'inventoryItemGroupKey', location: 'path' },
    { wire: 'Content-Language', name: 'contentLanguage', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const deleteInventoryItemGroup: Operation = {
  id: 'deleteInventoryItemGroup',
  method: 'DELETE',
  path: '/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}',
  resource: 'inventoryItemGroups',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'inventoryItemGroupKey', name: 'inventoryItemGroupKey', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getInventoryItemGroup: Operation = {
  id: 'getInventoryItemGroup',
  method: 'GET',
  path: '/sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}',
  resource: 'inventoryItemGroups',
  name: 'get',
  host: 'api',
  params: [{ wire: 'inventoryItemGroupKey', name: 'inventoryItemGroupKey', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createOrReplaceInventoryItemGroup,
  deleteInventoryItemGroup,
  getInventoryItemGroup,
];

export class InventoryItemGroupsApi extends Resource {
  /** Create or replace an inventory item group for a multi-variation listing. */
  createOrReplace(
    inventoryItemGroupKey: string,
    body: InventoryItemGroup,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<BaseResponse | undefined> {
    return this.call(createOrReplaceInventoryItemGroup, body, { inventoryItemGroupKey, ...params }, options);
  }

  /** Delete an inventory item group. */
  delete(inventoryItemGroupKey: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(deleteInventoryItemGroup, undefined, { inventoryItemGroupKey }, options);
  }

  /** Get one inventory item group. */
  get(inventoryItemGroupKey: string, options?: RequestOptions): Promise<InventoryItemGroup> {
    return this.call(getInventoryItemGroup, undefined, { inventoryItemGroupKey }, options);
  }
}
