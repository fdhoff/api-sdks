// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopEconomicOperator, ShopEconomicOperators } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createShopEconomicOperator: Operation = {
  id: 'createShopEconomicOperator',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/economic-operators',
  resource: 'economicOperators',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'operator_name', name: 'operatorName', location: 'urlencoded' },
    { wire: 'email', name: 'email', location: 'urlencoded' },
    { wire: 'first_line', name: 'firstLine', location: 'urlencoded' },
    { wire: 'city', name: 'city', location: 'urlencoded' },
    { wire: 'zip', name: 'zip', location: 'urlencoded' },
    { wire: 'country_iso', name: 'countryIso', location: 'urlencoded' },
    { wire: 'phone', name: 'phone', location: 'urlencoded' },
    { wire: 'second_line', name: 'secondLine', location: 'urlencoded' },
    { wire: 'state', name: 'state', location: 'urlencoded' },
    { wire: 'phone_country_iso', name: 'phoneCountryIso', location: 'urlencoded' },
    { wire: 'trademark_name', name: 'trademarkName', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getShopEconomicOperator: Operation = {
  id: 'getShopEconomicOperator',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/economic-operators/{economic_operator_id}',
  resource: 'economicOperators',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'economic_operator_id', name: 'economicOperatorId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getShopEconomicOperators: Operation = {
  id: 'getShopEconomicOperators',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/economic-operators',
  resource: 'economicOperators',
  name: 'list',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const updateShopEconomicOperator: Operation = {
  id: 'updateShopEconomicOperator',
  method: 'PATCH',
  path: '/v3/application/shops/{shop_id}/economic-operators/{economic_operator_id}',
  resource: 'economicOperators',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'economic_operator_id', name: 'economicOperatorId', location: 'path' },
    { wire: 'operator_name', name: 'operatorName', location: 'urlencoded' },
    { wire: 'email', name: 'email', location: 'urlencoded' },
    { wire: 'first_line', name: 'firstLine', location: 'urlencoded' },
    { wire: 'second_line', name: 'secondLine', location: 'urlencoded' },
    { wire: 'city', name: 'city', location: 'urlencoded' },
    { wire: 'state', name: 'state', location: 'urlencoded' },
    { wire: 'zip', name: 'zip', location: 'urlencoded' },
    { wire: 'country_iso', name: 'countryIso', location: 'urlencoded' },
    { wire: 'phone', name: 'phone', location: 'urlencoded' },
    { wire: 'phone_country_iso', name: 'phoneCountryIso', location: 'urlencoded' },
    { wire: 'trademark_name', name: 'trademarkName', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createShopEconomicOperator,
  getShopEconomicOperator,
  getShopEconomicOperators,
  updateShopEconomicOperator,
];

export class EconomicOperatorsApi extends Resource {
  /** Add an economic operator to a shop. */
  create(
    shopId: number,
    params: {
      operatorName: string;
      email: string;
      firstLine: string;
      city: string;
      zip: string;
      countryIso: string;
      phone: string;
      secondLine?: string;
      state?: string;
      phoneCountryIso?: string;
      trademarkName?: string;
    },
    options?: RequestOptions,
  ): Promise<ShopEconomicOperator> {
    return this.call(createShopEconomicOperator, undefined, { shopId, ...params }, options);
  }

  /** Get one economic operator. */
  get(shopId: number, economicOperatorId: number, options?: RequestOptions): Promise<ShopEconomicOperator> {
    return this.call(getShopEconomicOperator, undefined, { shopId, economicOperatorId }, options);
  }

  /** List a shop's economic operators. */
  list(shopId: number, options?: RequestOptions): Promise<ShopEconomicOperators> {
    return this.call(getShopEconomicOperators, undefined, { shopId }, options);
  }

  /** Update an economic operator. */
  update(
    shopId: number,
    economicOperatorId: number,
    params: {
      operatorName?: string;
      email?: string;
      firstLine?: string;
      secondLine?: string;
      city?: string;
      state?: string;
      zip?: string;
      countryIso?: string;
      phone?: string;
      phoneCountryIso?: string;
      trademarkName?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopEconomicOperator> {
    return this.call(updateShopEconomicOperator, undefined, { shopId, economicOperatorId, ...params }, options);
  }
}
