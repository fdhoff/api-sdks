// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AF01Response200,
  CH11Response200,
  CUR01Response200,
  DO01Response200,
  L01Response200,
  OF61Response200,
  PC01Response200,
  RE01Response200,
  SH11Response200,
  SH12Response200,
  SH21Response200,
  SH31Response200,
  SH42Response200,
  SH52Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const aF01: Operation = {
  id: 'AF01',
  method: 'GET',
  path: '/api/additional_fields',
  resource: 'platform',
  name: 'listCustomFields',
  params: [
    { wire: 'entities', name: 'entities', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_ORDER_SETTINGS_READ',
          'ROLE_PARTNER_OFFER_SETTINGS_READ',
          'ROLE_PARTNER_SHOP_SETTINGS_READ',
        ],
      },
    ],
  ],
};

const cH11: Operation = {
  id: 'CH11',
  method: 'GET',
  path: '/api/channels',
  resource: 'platform',
  name: 'listChannels',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_CHANNEL_READ'] }]],
};

const cUR01: Operation = {
  id: 'CUR01',
  method: 'GET',
  path: '/api/currencies',
  resource: 'platform',
  name: 'listCurrencies',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_CURRENCY_SETTINGS_READ'] }]],
};

const dO01: Operation = {
  id: 'DO01',
  method: 'GET',
  path: '/api/documents',
  resource: 'platform',
  name: 'listDocumentTypes',
  params: [
    { wire: 'entities', name: 'entities', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SETTINGS_READ'] }]],
};

const l01: Operation = {
  id: 'L01',
  method: 'GET',
  path: '/api/locales',
  resource: 'platform',
  name: 'listLocales',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_I18N_SETTINGS_READ'] }]],
};

const oF61: Operation = {
  id: 'OF61',
  method: 'GET',
  path: '/api/offers/states',
  resource: 'platform',
  name: 'listOfferConditions',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_SETTINGS_READ'] }]],
};

const pC01: Operation = {
  id: 'PC01',
  method: 'GET',
  path: '/api/platform/configuration',
  resource: 'platform',
  name: 'getConfiguration',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

const rE01: Operation = {
  id: 'RE01',
  method: 'GET',
  path: '/api/reasons',
  resource: 'platform',
  name: 'listReasons',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_ORDER_SETTINGS_READ'] }]],
};

const sH11: Operation = {
  id: 'SH11',
  method: 'GET',
  path: '/api/shipping/zones',
  resource: 'platform',
  name: 'listShippingZones',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHIPPING_SETTINGS_READ'] }]],
};

const sH12: Operation = {
  id: 'SH12',
  method: 'GET',
  path: '/api/shipping/types',
  resource: 'platform',
  name: 'listShippingMethods',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHIPPING_SETTINGS_READ'] }]],
};

const sH21: Operation = {
  id: 'SH21',
  method: 'GET',
  path: '/api/shipping/carriers',
  resource: 'platform',
  name: 'listCarriers',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHIPPING_SETTINGS_READ'] }]],
};

const sH31: Operation = {
  id: 'SH31',
  method: 'GET',
  path: '/api/shipping/logistic_classes',
  resource: 'platform',
  name: 'listLogisticClasses',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHIPPING_SETTINGS_READ'] }]],
};

const sH42: Operation = {
  id: 'SH42',
  method: 'GET',
  path: '/api/shipping/configuration/shop',
  resource: 'platform',
  name: 'getShippingConfiguration',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

const sH52: Operation = {
  id: 'SH52',
  method: 'GET',
  path: '/api/shipping/charges/shop',
  resource: 'platform',
  name: 'getShippingCharges',
  params: [
    { wire: 'overridden_by_shop', name: 'overriddenByShop', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

const v01: Operation = {
  id: 'V01',
  method: 'GET',
  path: '/api/version',
  resource: 'platform',
  name: 'healthCheck',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  security: [],
};

export const OPERATIONS: readonly Operation[] = [
  aF01,
  cH11,
  cUR01,
  dO01,
  l01,
  oF61,
  pC01,
  rE01,
  sH11,
  sH12,
  sH21,
  sH31,
  sH42,
  sH52,
  v01,
];

export class PlatformApi extends Resource {
  /** List the operator's custom fields (AF01). */
  listCustomFields(
    params: { entities?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<AF01Response200> {
    return this.call(aF01, undefined, { ...params }, options);
  }

  /** List the enabled sales channels (CH11). */
  listChannels(params: { shopId?: number } = {}, options?: RequestOptions): Promise<CH11Response200> {
    return this.call(cH11, undefined, { ...params }, options);
  }

  /** List currency codes and labels (CUR01). */
  listCurrencies(params: { shopId?: number } = {}, options?: RequestOptions): Promise<CUR01Response200> {
    return this.call(cUR01, undefined, { ...params }, options);
  }

  /** List the document types (DO01). */
  listDocumentTypes(
    params: { entities?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<DO01Response200> {
    return this.call(dO01, undefined, { ...params }, options);
  }

  /** List locale codes and labels (L01). */
  listLocales(params: { shopId?: number } = {}, options?: RequestOptions): Promise<L01Response200> {
    return this.call(l01, undefined, { ...params }, options);
  }

  /** List the offer conditions (OF61). */
  listOfferConditions(params: { shopId?: number } = {}, options?: RequestOptions): Promise<OF61Response200> {
    return this.call(oF61, undefined, { ...params }, options);
  }

  /** Get the platform configuration (PC01). */
  getConfiguration(params: { shopId?: number } = {}, options?: RequestOptions): Promise<PC01Response200> {
    return this.call(pC01, undefined, { ...params }, options);
  }

  /** List the reasons for incidents, refunds and other actions (RE01). */
  listReasons(params: { shopId?: number } = {}, options?: RequestOptions): Promise<RE01Response200> {
    return this.call(rE01, undefined, { ...params }, options);
  }

  /** List the active shipping zones (SH11). */
  listShippingZones(params: { shopId?: number } = {}, options?: RequestOptions): Promise<SH11Response200> {
    return this.call(sH11, undefined, { ...params }, options);
  }

  /** List the active shipping methods (SH12). */
  listShippingMethods(params: { shopId?: number } = {}, options?: RequestOptions): Promise<SH12Response200> {
    return this.call(sH12, undefined, { ...params }, options);
  }

  /** List the carriers (SH21). */
  listCarriers(params: { shopId?: number } = {}, options?: RequestOptions): Promise<SH21Response200> {
    return this.call(sH21, undefined, { ...params }, options);
  }

  /** List the logistic classes (SH31). */
  listLogisticClasses(params: { shopId?: number } = {}, options?: RequestOptions): Promise<SH31Response200> {
    return this.call(sH31, undefined, { ...params }, options);
  }

  /** Get your shop's shipping configuration (SH42). */
  getShippingConfiguration(params: { shopId?: number } = {}, options?: RequestOptions): Promise<SH42Response200> {
    return this.call(sH42, undefined, { ...params }, options);
  }

  /** Get the shipping charges set for your shop (SH52). */
  getShippingCharges(
    params: { overriddenByShop?: boolean; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<SH52Response200> {
    return this.call(sH52, undefined, { ...params }, options);
  }

  /** Check that the instance is up. Needs no key (V01). */
  healthCheck(params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(v01, undefined, { ...params }, options);
  }
}
