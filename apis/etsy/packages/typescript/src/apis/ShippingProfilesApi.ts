// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ErrorSchema,
  ShippingCarriers,
  ShopShippingProfile,
  ShopShippingProfileDestination,
  ShopShippingProfileDestinations,
  ShopShippingProfileUpgrade,
  ShopShippingProfileUpgrades,
  ShopShippingProfiles,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createShopShippingProfile: Operation = {
  id: 'createShopShippingProfile',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/shipping-profiles',
  resource: 'shippingProfiles',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'origin_country_iso', name: 'originCountryIso', location: 'urlencoded' },
    { wire: 'primary_cost', name: 'primaryCost', location: 'urlencoded' },
    { wire: 'secondary_cost', name: 'secondaryCost', location: 'urlencoded' },
    { wire: 'min_processing_time', name: 'minProcessingTime', location: 'urlencoded' },
    { wire: 'max_processing_time', name: 'maxProcessingTime', location: 'urlencoded' },
    { wire: 'processing_time_unit', name: 'processingTimeUnit', location: 'urlencoded' },
    { wire: 'destination_country_iso', name: 'destinationCountryIso', location: 'urlencoded' },
    { wire: 'destination_region', name: 'destinationRegion', location: 'urlencoded' },
    { wire: 'origin_postal_code', name: 'originPostalCode', location: 'urlencoded' },
    { wire: 'shipping_carrier_id', name: 'shippingCarrierId', location: 'urlencoded' },
    { wire: 'mail_class', name: 'mailClass', location: 'urlencoded' },
    { wire: 'min_delivery_days', name: 'minDeliveryDays', location: 'urlencoded' },
    { wire: 'max_delivery_days', name: 'maxDeliveryDays', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const createShopShippingProfileDestination: Operation = {
  id: 'createShopShippingProfileDestination',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations',
  resource: 'shippingProfiles',
  name: 'createDestination',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'primary_cost', name: 'primaryCost', location: 'urlencoded' },
    { wire: 'secondary_cost', name: 'secondaryCost', location: 'urlencoded' },
    { wire: 'destination_country_iso', name: 'destinationCountryIso', location: 'urlencoded' },
    { wire: 'destination_region', name: 'destinationRegion', location: 'urlencoded' },
    { wire: 'shipping_carrier_id', name: 'shippingCarrierId', location: 'urlencoded' },
    { wire: 'mail_class', name: 'mailClass', location: 'urlencoded' },
    { wire: 'min_delivery_days', name: 'minDeliveryDays', location: 'urlencoded' },
    { wire: 'max_delivery_days', name: 'maxDeliveryDays', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const createShopShippingProfileUpgrade: Operation = {
  id: 'createShopShippingProfileUpgrade',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades',
  resource: 'shippingProfiles',
  name: 'createUpgrade',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'type', name: 'type', location: 'urlencoded' },
    { wire: 'upgrade_name', name: 'upgradeName', location: 'urlencoded' },
    { wire: 'price', name: 'price', location: 'urlencoded' },
    { wire: 'secondary_price', name: 'secondaryPrice', location: 'urlencoded' },
    { wire: 'shipping_carrier_id', name: 'shippingCarrierId', location: 'urlencoded' },
    { wire: 'mail_class', name: 'mailClass', location: 'urlencoded' },
    { wire: 'min_delivery_days', name: 'minDeliveryDays', location: 'urlencoded' },
    { wire: 'max_delivery_days', name: 'maxDeliveryDays', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopShippingProfile: Operation = {
  id: 'deleteShopShippingProfile',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}',
  resource: 'shippingProfiles',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopShippingProfileDestination: Operation = {
  id: 'deleteShopShippingProfileDestination',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}',
  resource: 'shippingProfiles',
  name: 'deleteDestination',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'shipping_profile_destination_id', name: 'shippingProfileDestinationId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopShippingProfileUpgrade: Operation = {
  id: 'deleteShopShippingProfileUpgrade',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}',
  resource: 'shippingProfiles',
  name: 'deleteUpgrade',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'upgrade_id', name: 'upgradeId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const getShippingCarriers: Operation = {
  id: 'getShippingCarriers',
  method: 'GET',
  path: '/v3/application/shipping-carriers',
  resource: 'shippingProfiles',
  name: 'listCarriers',
  params: [{ wire: 'origin_country_iso', name: 'originCountryIso', location: 'query' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getShopShippingProfile: Operation = {
  id: 'getShopShippingProfile',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}',
  resource: 'shippingProfiles',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const getShopShippingProfileDestinationsByShippingProfile: Operation = {
  id: 'getShopShippingProfileDestinationsByShippingProfile',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations',
  resource: 'shippingProfiles',
  name: 'listDestinations',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDestinations',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const getShopShippingProfileUpgrades: Operation = {
  id: 'getShopShippingProfileUpgrades',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades',
  resource: 'shippingProfiles',
  name: 'listUpgrades',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const getShopShippingProfiles: Operation = {
  id: 'getShopShippingProfiles',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/shipping-profiles',
  resource: 'shippingProfiles',
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

const updateShopShippingProfile: Operation = {
  id: 'updateShopShippingProfile',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}',
  resource: 'shippingProfiles',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'origin_country_iso', name: 'originCountryIso', location: 'urlencoded' },
    { wire: 'min_processing_time', name: 'minProcessingTime', location: 'urlencoded' },
    { wire: 'max_processing_time', name: 'maxProcessingTime', location: 'urlencoded' },
    { wire: 'processing_time_unit', name: 'processingTimeUnit', location: 'urlencoded' },
    { wire: 'origin_postal_code', name: 'originPostalCode', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const updateShopShippingProfileDestination: Operation = {
  id: 'updateShopShippingProfileDestination',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id}',
  resource: 'shippingProfiles',
  name: 'updateDestination',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'shipping_profile_destination_id', name: 'shippingProfileDestinationId', location: 'path' },
    { wire: 'primary_cost', name: 'primaryCost', location: 'urlencoded' },
    { wire: 'secondary_cost', name: 'secondaryCost', location: 'urlencoded' },
    { wire: 'destination_country_iso', name: 'destinationCountryIso', location: 'urlencoded' },
    { wire: 'destination_region', name: 'destinationRegion', location: 'urlencoded' },
    { wire: 'shipping_carrier_id', name: 'shippingCarrierId', location: 'urlencoded' },
    { wire: 'mail_class', name: 'mailClass', location: 'urlencoded' },
    { wire: 'min_delivery_days', name: 'minDeliveryDays', location: 'urlencoded' },
    { wire: 'max_delivery_days', name: 'maxDeliveryDays', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const updateShopShippingProfileUpgrade: Operation = {
  id: 'updateShopShippingProfileUpgrade',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id}',
  resource: 'shippingProfiles',
  name: 'updateUpgrade',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'path' },
    { wire: 'upgrade_id', name: 'upgradeId', location: 'path' },
    { wire: 'upgrade_name', name: 'upgradeName', location: 'urlencoded' },
    { wire: 'type', name: 'type', location: 'urlencoded' },
    { wire: 'price', name: 'price', location: 'urlencoded' },
    { wire: 'secondary_price', name: 'secondaryPrice', location: 'urlencoded' },
    { wire: 'shipping_carrier_id', name: 'shippingCarrierId', location: 'urlencoded' },
    { wire: 'mail_class', name: 'mailClass', location: 'urlencoded' },
    { wire: 'min_delivery_days', name: 'minDeliveryDays', location: 'urlencoded' },
    { wire: 'max_delivery_days', name: 'maxDeliveryDays', location: 'urlencoded' },
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
  createShopShippingProfile,
  createShopShippingProfileDestination,
  createShopShippingProfileUpgrade,
  deleteShopShippingProfile,
  deleteShopShippingProfileDestination,
  deleteShopShippingProfileUpgrade,
  getShippingCarriers,
  getShopShippingProfile,
  getShopShippingProfileDestinationsByShippingProfile,
  getShopShippingProfileUpgrades,
  getShopShippingProfiles,
  updateShopShippingProfile,
  updateShopShippingProfileDestination,
  updateShopShippingProfileUpgrade,
];

export class ShippingProfilesApi extends Resource {
  /** Create a shipping profile. */
  create(
    shopId: number,
    params: {
      title: string;
      originCountryIso: string;
      primaryCost: number;
      secondaryCost: number;
      minProcessingTime?: number;
      maxProcessingTime?: number;
      processingTimeUnit?: string;
      destinationCountryIso?: string;
      destinationRegion?: string;
      originPostalCode?: string;
      shippingCarrierId?: number;
      mailClass?: string;
      minDeliveryDays?: number;
      maxDeliveryDays?: number;
    },
    options?: RequestOptions,
  ): Promise<ShopShippingProfile> {
    return this.call(createShopShippingProfile, undefined, { shopId, ...params }, options);
  }

  /** Add a destination to a shipping profile. */
  createDestination(
    shopId: number,
    shippingProfileId: number,
    params: {
      primaryCost: number;
      secondaryCost: number;
      destinationCountryIso?: string;
      destinationRegion?: string;
      shippingCarrierId?: number;
      mailClass?: string;
      minDeliveryDays?: number;
      maxDeliveryDays?: number;
    },
    options?: RequestOptions,
  ): Promise<ShopShippingProfileDestination> {
    return this.call(
      createShopShippingProfileDestination,
      undefined,
      { shopId, shippingProfileId, ...params },
      options,
    );
  }

  /** Add an upgrade to a shipping profile. */
  createUpgrade(
    shopId: number,
    shippingProfileId: number,
    params: {
      type: number;
      upgradeName: string;
      price: number;
      secondaryPrice: number;
      shippingCarrierId?: number;
      mailClass?: string;
      minDeliveryDays?: number;
      maxDeliveryDays?: number;
    },
    options?: RequestOptions,
  ): Promise<ShopShippingProfileUpgrade> {
    return this.call(createShopShippingProfileUpgrade, undefined, { shopId, shippingProfileId, ...params }, options);
  }

  /** Delete a shipping profile. */
  delete(shopId: number, shippingProfileId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteShopShippingProfile, undefined, { shopId, shippingProfileId }, options);
  }

  /** Delete a shipping profile destination. */
  deleteDestination(
    shopId: number,
    shippingProfileId: number,
    shippingProfileDestinationId: number,
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(
      deleteShopShippingProfileDestination,
      undefined,
      { shopId, shippingProfileId, shippingProfileDestinationId },
      options,
    );
  }

  /** Delete a shipping profile upgrade. */
  deleteUpgrade(shopId: number, shippingProfileId: number, upgradeId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteShopShippingProfileUpgrade, undefined, { shopId, shippingProfileId, upgradeId }, options);
  }

  /** List the shipping carriers and mail classes for an origin country. */
  listCarriers(params: { originCountryIso: string }, options?: RequestOptions): Promise<ShippingCarriers> {
    return this.call(getShippingCarriers, undefined, { ...params }, options);
  }

  /** Get one shipping profile. */
  get(shopId: number, shippingProfileId: number, options?: RequestOptions): Promise<ShopShippingProfile> {
    return this.call(getShopShippingProfile, undefined, { shopId, shippingProfileId }, options);
  }

  /** List one page of a shipping profile's destinations. */
  listDestinations(
    shopId: number,
    shippingProfileId: number,
    params: { limit?: number; offset?: number } = {},
    options?: RequestOptions,
  ): Promise<ShopShippingProfileDestinations> {
    return this.call(
      getShopShippingProfileDestinationsByShippingProfile,
      undefined,
      { shopId, shippingProfileId, ...params },
      options,
    );
  }

  /** Iterate every item across all pages. */
  iterDestinations(
    shopId: number,
    shippingProfileId: number,
    params: { limit?: number; offset?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopShippingProfileDestination, void, undefined> {
    return this.paginate(
      getShopShippingProfileDestinationsByShippingProfile,
      undefined,
      { shopId, shippingProfileId, ...params },
      options,
    );
  }

  /** List a shipping profile's upgrades. */
  listUpgrades(
    shopId: number,
    shippingProfileId: number,
    options?: RequestOptions,
  ): Promise<ShopShippingProfileUpgrades> {
    return this.call(getShopShippingProfileUpgrades, undefined, { shopId, shippingProfileId }, options);
  }

  /** List a shop's shipping profiles. */
  list(shopId: number, options?: RequestOptions): Promise<ShopShippingProfiles> {
    return this.call(getShopShippingProfiles, undefined, { shopId }, options);
  }

  /** Update a shipping profile. */
  update(
    shopId: number,
    shippingProfileId: number,
    params: {
      title?: string;
      originCountryIso?: string;
      minProcessingTime?: number;
      maxProcessingTime?: number;
      processingTimeUnit?: string;
      originPostalCode?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopShippingProfile> {
    return this.call(updateShopShippingProfile, undefined, { shopId, shippingProfileId, ...params }, options);
  }

  /** Update a shipping profile destination. */
  updateDestination(
    shopId: number,
    shippingProfileId: number,
    shippingProfileDestinationId: number,
    params: {
      primaryCost?: number;
      secondaryCost?: number;
      destinationCountryIso?: string;
      destinationRegion?: string;
      shippingCarrierId?: number;
      mailClass?: string;
      minDeliveryDays?: number;
      maxDeliveryDays?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopShippingProfileDestination> {
    return this.call(
      updateShopShippingProfileDestination,
      undefined,
      { shopId, shippingProfileId, shippingProfileDestinationId, ...params },
      options,
    );
  }

  /** Update a shipping profile upgrade. */
  updateUpgrade(
    shopId: number,
    shippingProfileId: number,
    upgradeId: number,
    params: {
      upgradeName?: string;
      type?: number;
      price?: number;
      secondaryPrice?: number;
      shippingCarrierId?: number;
      mailClass?: string;
      minDeliveryDays?: number;
      maxDeliveryDays?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopShippingProfileUpgrade> {
    return this.call(
      updateShopShippingProfileUpgrade,
      undefined,
      { shopId, shippingProfileId, upgradeId, ...params },
      options,
    );
  }
}
