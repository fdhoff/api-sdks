// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BaseResponse,
  BulkCreateOrReplaceInventoryItem429Response,
  BulkGetInventoryItem,
  BulkGetInventoryItemResponse,
  BulkInventoryItem,
  BulkInventoryItemResponse,
  BulkPriceQuantity,
  BulkPriceQuantityResponse,
  InventoryItem,
  InventoryItemWithSkuLocaleGroupid,
  InventoryItems,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const bulkCreateOrReplaceInventoryItem: Operation = {
  id: 'bulkCreateOrReplaceInventoryItem',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_create_or_replace_inventory_item',
  resource: 'inventoryItems',
  name: 'bulkCreateOrReplace',
  host: 'api',
  params: [{ wire: 'Content-Language', name: 'contentLanguage', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const bulkGetInventoryItem: Operation = {
  id: 'bulkGetInventoryItem',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_get_inventory_item',
  resource: 'inventoryItems',
  name: 'bulkGet',
  host: 'api',
  params: [],
  hasBody: true,
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

const bulkUpdatePriceQuantity: Operation = {
  id: 'bulkUpdatePriceQuantity',
  method: 'POST',
  path: '/sell/inventory/v1/bulk_update_price_quantity',
  resource: 'inventoryItems',
  name: 'bulkUpdatePriceQuantity',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const createOrReplaceInventoryItem: Operation = {
  id: 'createOrReplaceInventoryItem',
  method: 'PUT',
  path: '/sell/inventory/v1/inventory_item/{sku}',
  resource: 'inventoryItems',
  name: 'createOrReplace',
  host: 'api',
  params: [
    { wire: 'sku', name: 'sku', location: 'path' },
    { wire: 'Content-Language', name: 'contentLanguage', location: 'header' },
  ],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const deleteInventoryItem: Operation = {
  id: 'deleteInventoryItem',
  method: 'DELETE',
  path: '/sell/inventory/v1/inventory_item/{sku}',
  resource: 'inventoryItems',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'sku', name: 'sku', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getInventoryItem: Operation = {
  id: 'getInventoryItem',
  method: 'GET',
  path: '/sell/inventory/v1/inventory_item/{sku}',
  resource: 'inventoryItems',
  name: 'get',
  host: 'api',
  params: [{ wire: 'sku', name: 'sku', location: 'path' }],
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

const getInventoryItems: Operation = {
  id: 'getInventoryItems',
  method: 'GET',
  path: '/sell/inventory/v1/inventory_item',
  resource: 'inventoryItems',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'inventoryItems',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
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
  bulkCreateOrReplaceInventoryItem,
  bulkGetInventoryItem,
  bulkUpdatePriceQuantity,
  createOrReplaceInventoryItem,
  deleteInventoryItem,
  getInventoryItem,
  getInventoryItems,
];

export class InventoryItemsApi extends Resource {
  /** Create or replace several inventory items. */
  bulkCreateOrReplace(
    body: BulkInventoryItem,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<BulkInventoryItemResponse> {
    return this.call(bulkCreateOrReplaceInventoryItem, body, { ...params }, options);
  }

  /** Get several inventory items by SKU. */
  bulkGet(body: BulkGetInventoryItem, options?: RequestOptions): Promise<BulkGetInventoryItemResponse> {
    return this.call(bulkGetInventoryItem, body, {}, options);
  }

  /** Update the price and quantity of several inventory items and their offers. */
  bulkUpdatePriceQuantity(body: BulkPriceQuantity, options?: RequestOptions): Promise<BulkPriceQuantityResponse> {
    return this.call(bulkUpdatePriceQuantity, body, {}, options);
  }

  /** Create or replace an inventory item. */
  createOrReplace(
    sku: string,
    body: InventoryItem,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<BaseResponse | undefined> {
    return this.call(createOrReplaceInventoryItem, body, { sku, ...params }, options);
  }

  /** Delete an inventory item and its offers. */
  delete(sku: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteInventoryItem, undefined, { sku }, options);
  }

  /** Get one inventory item by SKU. */
  get(sku: string, options?: RequestOptions): Promise<InventoryItemWithSkuLocaleGroupid> {
    return this.call(getInventoryItem, undefined, { sku }, options);
  }

  /** List one page of the seller's inventory items. */
  list(params: { limit?: string; offset?: string } = {}, options?: RequestOptions): Promise<InventoryItems> {
    return this.call(getInventoryItems, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.InventoryItemWithSkuLocaleGroupid, void, undefined> {
    return this.paginate(getInventoryItems, undefined, { ...params }, options);
  }
}
