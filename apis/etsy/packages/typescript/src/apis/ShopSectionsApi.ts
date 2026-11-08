// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopSection, ShopSections } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createShopSection: Operation = {
  id: 'createShopSection',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/sections',
  resource: 'shopSections',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopSection: Operation = {
  id: 'deleteShopSection',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/sections/{shop_section_id}',
  resource: 'shopSections',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shop_section_id', name: 'shopSectionId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const getShopSection: Operation = {
  id: 'getShopSection',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/sections/{shop_section_id}',
  resource: 'shopSections',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shop_section_id', name: 'shopSectionId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getShopSections: Operation = {
  id: 'getShopSections',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/sections',
  resource: 'shopSections',
  name: 'list',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateShopSection: Operation = {
  id: 'updateShopSection',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/sections/{shop_section_id}',
  resource: 'shopSections',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shop_section_id', name: 'shopSectionId', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createShopSection,
  deleteShopSection,
  getShopSection,
  getShopSections,
  updateShopSection,
];

export class ShopSectionsApi extends Resource {
  /** Create a shop section. */
  create(shopId: number, params: { title: string }, options?: RequestOptions): Promise<ShopSection> {
    return this.call(createShopSection, undefined, { shopId, ...params }, options);
  }

  /** Delete a shop section. */
  delete(shopId: number, shopSectionId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteShopSection, undefined, { shopId, shopSectionId }, options);
  }

  /** Get one shop section. */
  get(shopId: number, shopSectionId: number, options?: RequestOptions): Promise<ShopSection> {
    return this.call(getShopSection, undefined, { shopId, shopSectionId }, options);
  }

  /** List a shop's sections. */
  list(shopId: number, options?: RequestOptions): Promise<ShopSections> {
    return this.call(getShopSections, undefined, { shopId }, options);
  }

  /** Rename a shop section. */
  update(
    shopId: number,
    shopSectionId: number,
    params: { title: string },
    options?: RequestOptions,
  ): Promise<ShopSection> {
    return this.call(updateShopSection, undefined, { shopId, shopSectionId, ...params }, options);
  }
}
