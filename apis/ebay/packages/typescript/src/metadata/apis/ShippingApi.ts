// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetAutomotivePartsCompatibilityPolicies429Response,
  ShippingCarrierResponse,
  ShippingExcludeLocationResponse,
  ShippingHandlingTimeResponse,
  ShippingLocationResponse,
  ShippingServiceResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getExcludeShippingLocations: Operation = {
  id: 'getExcludeShippingLocations',
  method: 'GET',
  path: '/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_exclude_shipping_locations',
  resource: 'shipping',
  name: 'getExcludedLocations',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getHandlingTimes: Operation = {
  id: 'getHandlingTimes',
  method: 'GET',
  path: '/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_handling_times',
  resource: 'shipping',
  name: 'getHandlingTimes',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getShippingCarriers: Operation = {
  id: 'getShippingCarriers',
  method: 'GET',
  path: '/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_carriers',
  resource: 'shipping',
  name: 'getCarriers',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getShippingLocations: Operation = {
  id: 'getShippingLocations',
  method: 'GET',
  path: '/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_locations',
  resource: 'shipping',
  name: 'getLocations',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getShippingServices: Operation = {
  id: 'getShippingServices',
  method: 'GET',
  path: '/sell/metadata/v1/shipping/marketplace/{marketplace_id}/get_shipping_services',
  resource: 'shipping',
  name: 'getServices',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getExcludeShippingLocations,
  getHandlingTimes,
  getShippingCarriers,
  getShippingLocations,
  getShippingServices,
];

export class ShippingApi extends Resource {
  /** List the regions and countries a seller can exclude from shipping. */
  getExcludedLocations(marketplaceId: string, options?: RequestOptions): Promise<ShippingExcludeLocationResponse> {
    return this.call(getExcludeShippingLocations, undefined, { marketplaceId }, options);
  }

  /** List the handling times a marketplace accepts. */
  getHandlingTimes(marketplaceId: string, options?: RequestOptions): Promise<ShippingHandlingTimeResponse> {
    return this.call(getHandlingTimes, undefined, { marketplaceId }, options);
  }

  /** List the shipping carriers of a marketplace. */
  getCarriers(marketplaceId: string, options?: RequestOptions): Promise<ShippingCarrierResponse> {
    return this.call(getShippingCarriers, undefined, { marketplaceId }, options);
  }

  /** List the shipping locations of a marketplace. */
  getLocations(marketplaceId: string, options?: RequestOptions): Promise<ShippingLocationResponse> {
    return this.call(getShippingLocations, undefined, { marketplaceId }, options);
  }

  /** List the shipping services of a marketplace. */
  getServices(marketplaceId: string, options?: RequestOptions): Promise<ShippingServiceResponse> {
    return this.call(getShippingServices, undefined, { marketplaceId }, options);
  }
}
