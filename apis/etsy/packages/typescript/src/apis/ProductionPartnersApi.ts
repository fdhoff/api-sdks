// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopProductionPartners } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getShopProductionPartners: Operation = {
  id: 'getShopProductionPartners',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/production-partners',
  resource: 'productionPartners',
  name: 'list',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getShopProductionPartners];

export class ProductionPartnersApi extends Resource {
  /** List a shop's production partners. */
  list(shopId: number, options?: RequestOptions): Promise<ShopProductionPartners> {
    return this.call(getShopProductionPartners, undefined, { shopId }, options);
  }
}
