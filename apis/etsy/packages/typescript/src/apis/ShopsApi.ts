// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, Shop, Shops } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const findShops: Operation = {
  id: 'findShops',
  method: 'GET',
  path: '/v3/application/shops',
  resource: 'shops',
  name: 'find',
  params: [
    { wire: 'shop_name', name: 'shopName', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFind',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getShop: Operation = {
  id: 'getShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}',
  resource: 'shops',
  name: 'get',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getShopByOwnerUserId: Operation = {
  id: 'getShopByOwnerUserId',
  method: 'GET',
  path: '/v3/application/users/{user_id}/shops',
  resource: 'shops',
  name: 'getByOwner',
  params: [{ wire: 'user_id', name: 'userId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateShop: Operation = {
  id: 'updateShop',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}',
  resource: 'shops',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'announcement', name: 'announcement', location: 'urlencoded' },
    { wire: 'sale_message', name: 'saleMessage', location: 'urlencoded' },
    { wire: 'digital_sale_message', name: 'digitalSaleMessage', location: 'urlencoded' },
    { wire: 'policy_additional', name: 'policyAdditional', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r', 'shops_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [findShops, getShop, getShopByOwnerUserId, updateShop];

export class ShopsApi extends Resource {
  /** Search one page of shops by name. */
  find(params: { shopName: string; limit?: number; offset?: number }, options?: RequestOptions): Promise<Shops> {
    return this.call(findShops, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFind(
    params: { shopName: string; limit?: number; offset?: number },
    options?: RequestOptions,
  ): AsyncGenerator<models.Shop, void, undefined> {
    return this.paginate(findShops, undefined, { ...params }, options);
  }

  /** Get one shop. */
  get(shopId: number, options?: RequestOptions): Promise<Shop> {
    return this.call(getShop, undefined, { shopId }, options);
  }

  /** Get the shop a user owns. */
  getByOwner(userId: number, options?: RequestOptions): Promise<Shop> {
    return this.call(getShopByOwnerUserId, undefined, { userId }, options);
  }

  /** Update a shop. */
  update(
    shopId: number,
    params: {
      title?: string;
      announcement?: string;
      saleMessage?: string;
      digitalSaleMessage?: string;
      policyAdditional?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<Shop> {
    return this.call(updateShop, undefined, { shopId, ...params }, options);
  }
}
