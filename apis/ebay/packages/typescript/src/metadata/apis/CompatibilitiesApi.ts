// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetAutomotivePartsCompatibilityPolicies429Response,
  MultiCompatibilityPropertyValuesRequest,
  MultiCompatibilityPropertyValuesResponse,
  ProductRequest,
  ProductResponse,
  PropertyNamesRequest,
  PropertyNamesResponse,
  PropertyValuesRequest,
  PropertyValuesResponse,
  SpecificationRequest,
  SpecificationResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getCompatibilitiesBySpecification: Operation = {
  id: 'getCompatibilitiesBySpecification',
  method: 'POST',
  path: '/sell/metadata/v1/compatibilities/get_compatibilities_by_specification',
  resource: 'compatibilities',
  name: 'getBySpecification',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCompatibilityPropertyNames: Operation = {
  id: 'getCompatibilityPropertyNames',
  method: 'POST',
  path: '/sell/metadata/v1/compatibilities/get_compatibility_property_names',
  resource: 'compatibilities',
  name: 'getPropertyNames',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCompatibilityPropertyValues: Operation = {
  id: 'getCompatibilityPropertyValues',
  method: 'POST',
  path: '/sell/metadata/v1/compatibilities/get_compatibility_property_values',
  resource: 'compatibilities',
  name: 'getPropertyValues',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getMultiCompatibilityPropertyValues: Operation = {
  id: 'getMultiCompatibilityPropertyValues',
  method: 'POST',
  path: '/sell/metadata/v1/compatibilities/get_multi_compatibility_property_values',
  resource: 'compatibilities',
  name: 'getMultiPropertyValues',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getProductCompatibilities: Operation = {
  id: 'getProductCompatibilities',
  method: 'POST',
  path: '/sell/metadata/v1/compatibilities/get_product_compatibilities',
  resource: 'compatibilities',
  name: 'getProductCompatibilities',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getCompatibilitiesBySpecification,
  getCompatibilityPropertyNames,
  getCompatibilityPropertyValues,
  getMultiCompatibilityPropertyValues,
  getProductCompatibilities,
];

export class CompatibilitiesApi extends Resource {
  /** List the vehicles that match a parts specification. */
  getBySpecification(
    body?: SpecificationRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<SpecificationResponse | undefined> {
    return this.call(getCompatibilitiesBySpecification, body, { ...params }, options);
  }

  /** List the compatibility property names of a category. */
  getPropertyNames(
    body?: PropertyNamesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<PropertyNamesResponse | undefined> {
    return this.call(getCompatibilityPropertyNames, body, { ...params }, options);
  }

  /** List the values of one compatibility property. */
  getPropertyValues(
    body?: PropertyValuesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<PropertyValuesResponse | undefined> {
    return this.call(getCompatibilityPropertyValues, body, { ...params }, options);
  }

  /** List the values of several compatibility properties. */
  getMultiPropertyValues(
    body?: MultiCompatibilityPropertyValuesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<MultiCompatibilityPropertyValuesResponse | undefined> {
    return this.call(getMultiCompatibilityPropertyValues, body, { ...params }, options);
  }

  /** List the vehicles a product fits. */
  getProductCompatibilities(
    body?: ProductRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<ProductResponse | undefined> {
    return this.call(getProductCompatibilities, body, { ...params }, options);
  }
}
