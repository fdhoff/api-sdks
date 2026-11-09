// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BaseResponse, BulkCreateOrReplaceInventoryItem429Response, Compatibility } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createOrReplaceProductCompatibility: Operation = {
  id: 'createOrReplaceProductCompatibility',
  method: 'PUT',
  path: '/sell/inventory/v1/inventory_item/{sku}/product_compatibility',
  resource: 'productCompatibility',
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

const deleteProductCompatibility: Operation = {
  id: 'deleteProductCompatibility',
  method: 'DELETE',
  path: '/sell/inventory/v1/inventory_item/{sku}/product_compatibility',
  resource: 'productCompatibility',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'sku', name: 'sku', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getProductCompatibility: Operation = {
  id: 'getProductCompatibility',
  method: 'GET',
  path: '/sell/inventory/v1/inventory_item/{sku}/product_compatibility',
  resource: 'productCompatibility',
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

export const OPERATIONS: readonly Operation[] = [
  createOrReplaceProductCompatibility,
  deleteProductCompatibility,
  getProductCompatibility,
];

export class ProductCompatibilityApi extends Resource {
  /** Set the vehicles an inventory item fits. */
  createOrReplace(
    sku: string,
    body: Compatibility,
    params: { contentLanguage?: string } = {},
    options?: RequestOptions,
  ): Promise<BaseResponse | undefined> {
    return this.call(createOrReplaceProductCompatibility, body, { sku, ...params }, options);
  }

  /** Remove the vehicle list of an inventory item. */
  delete(sku: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteProductCompatibility, undefined, { sku }, options);
  }

  /** Get the vehicles an inventory item fits. */
  get(sku: string, options?: RequestOptions): Promise<Compatibility> {
    return this.call(getProductCompatibility, undefined, { sku }, options);
  }
}
