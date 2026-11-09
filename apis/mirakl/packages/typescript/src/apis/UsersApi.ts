// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { RO02Response200 } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const rO02: Operation = {
  id: 'RO02',
  method: 'GET',
  path: '/api/users/shops/roles',
  resource: 'users',
  name: 'listShopRoles',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_SHOP_USER_CREATE', 'ROLE_SHOP_ADMIN'] }]],
};

export const OPERATIONS: readonly Operation[] = [rO02];

export class UsersApi extends Resource {
  /** List the shop roles (RO02). */
  listShopRoles(params: { shopId?: number } = {}, options?: RequestOptions): Promise<RO02Response200> {
    return this.call(rO02, undefined, { ...params }, options);
  }
}
