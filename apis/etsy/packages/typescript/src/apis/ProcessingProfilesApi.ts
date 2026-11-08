// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopProcessingProfile, ShopProcessingProfiles } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createShopReadinessStateDefinition: Operation = {
  id: 'createShopReadinessStateDefinition',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/readiness-state-definitions',
  resource: 'processingProfiles',
  name: 'create',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'readiness_state', name: 'readinessState', location: 'urlencoded' },
    { wire: 'min_processing_time', name: 'minProcessingTime', location: 'urlencoded' },
    { wire: 'max_processing_time', name: 'maxProcessingTime', location: 'urlencoded' },
    { wire: 'processing_time_unit', name: 'processingTimeUnit', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const deleteShopReadinessStateDefinition: Operation = {
  id: 'deleteShopReadinessStateDefinition',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}',
  resource: 'processingProfiles',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'readiness_state_definition_id', name: 'readinessStateDefinitionId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_w'] },
    ],
  ],
};

const getShopReadinessStateDefinition: Operation = {
  id: 'getShopReadinessStateDefinition',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}',
  resource: 'processingProfiles',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'readiness_state_definition_id', name: 'readinessStateDefinitionId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const getShopReadinessStateDefinitions: Operation = {
  id: 'getShopReadinessStateDefinitions',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/readiness-state-definitions',
  resource: 'processingProfiles',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const updateShopReadinessStateDefinition: Operation = {
  id: 'updateShopReadinessStateDefinition',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/readiness-state-definitions/{readiness_state_definition_id}',
  resource: 'processingProfiles',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'readiness_state_definition_id', name: 'readinessStateDefinitionId', location: 'path' },
    { wire: 'readiness_state', name: 'readinessState', location: 'urlencoded' },
    { wire: 'min_processing_time', name: 'minProcessingTime', location: 'urlencoded' },
    { wire: 'max_processing_time', name: 'maxProcessingTime', location: 'urlencoded' },
    { wire: 'processing_time_unit', name: 'processingTimeUnit', location: 'urlencoded' },
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
  createShopReadinessStateDefinition,
  deleteShopReadinessStateDefinition,
  getShopReadinessStateDefinition,
  getShopReadinessStateDefinitions,
  updateShopReadinessStateDefinition,
];

export class ProcessingProfilesApi extends Resource {
  /** Create a processing profile. */
  create(
    shopId: number,
    params: {
      readinessState: string;
      minProcessingTime: number;
      maxProcessingTime: number;
      processingTimeUnit?: string;
    },
    options?: RequestOptions,
  ): Promise<ShopProcessingProfile> {
    return this.call(createShopReadinessStateDefinition, undefined, { shopId, ...params }, options);
  }

  /** Delete a processing profile. */
  delete(shopId: number, readinessStateDefinitionId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteShopReadinessStateDefinition, undefined, { shopId, readinessStateDefinitionId }, options);
  }

  /** Get one processing profile. */
  get(shopId: number, readinessStateDefinitionId: number, options?: RequestOptions): Promise<ShopProcessingProfile> {
    return this.call(getShopReadinessStateDefinition, undefined, { shopId, readinessStateDefinitionId }, options);
  }

  /** List one page of a shop's processing profiles. */
  list(
    shopId: number,
    params: { limit?: number; offset?: number } = {},
    options?: RequestOptions,
  ): Promise<ShopProcessingProfiles> {
    return this.call(getShopReadinessStateDefinitions, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    shopId: number,
    params: { limit?: number; offset?: number } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopProcessingProfile, void, undefined> {
    return this.paginate(getShopReadinessStateDefinitions, undefined, { shopId, ...params }, options);
  }

  /** Update a processing profile. */
  update(
    shopId: number,
    readinessStateDefinitionId: number,
    params: {
      readinessState?: string;
      minProcessingTime?: number;
      maxProcessingTime?: number;
      processingTimeUnit?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopProcessingProfile> {
    return this.call(
      updateShopReadinessStateDefinition,
      undefined,
      { shopId, readinessStateDefinitionId, ...params },
      options,
    );
  }
}
