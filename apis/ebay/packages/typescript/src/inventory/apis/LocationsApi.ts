// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BulkCreateOrReplaceInventoryItem429Response,
  InventoryLocation,
  InventoryLocationFull,
  InventoryLocationResponse,
  LocationResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createInventoryLocation: Operation = {
  id: 'createInventoryLocation',
  method: 'POST',
  path: '/sell/inventory/v1/location/{merchantLocationKey}',
  resource: 'locations',
  name: 'create',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const deleteInventoryLocation: Operation = {
  id: 'deleteInventoryLocation',
  method: 'DELETE',
  path: '/sell/inventory/v1/location/{merchantLocationKey}',
  resource: 'locations',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const disableInventoryLocation: Operation = {
  id: 'disableInventoryLocation',
  method: 'POST',
  path: '/sell/inventory/v1/location/{merchantLocationKey}/disable',
  resource: 'locations',
  name: 'disable',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const enableInventoryLocation: Operation = {
  id: 'enableInventoryLocation',
  method: 'POST',
  path: '/sell/inventory/v1/location/{merchantLocationKey}/enable',
  resource: 'locations',
  name: 'enable',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getInventoryLocation: Operation = {
  id: 'getInventoryLocation',
  method: 'GET',
  path: '/sell/inventory/v1/location/{merchantLocationKey}',
  resource: 'locations',
  name: 'get',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const getInventoryLocations: Operation = {
  id: 'getInventoryLocations',
  method: 'GET',
  path: '/sell/inventory/v1/location',
  resource: 'locations',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'next_link', items: 'locations', link: 'next', params: ['offset', 'limit', 'continuation_token'] },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const updateInventoryLocation: Operation = {
  id: 'updateInventoryLocation',
  method: 'POST',
  path: '/sell/inventory/v1/location/{merchantLocationKey}/update_location_details',
  resource: 'locations',
  name: 'update',
  host: 'api',
  params: [{ wire: 'merchantLocationKey', name: 'merchantLocationKey', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createInventoryLocation,
  deleteInventoryLocation,
  disableInventoryLocation,
  enableInventoryLocation,
  getInventoryLocation,
  getInventoryLocations,
  updateInventoryLocation,
];

export class LocationsApi extends Resource {
  /** Create an inventory location. */
  create(
    merchantLocationKey: string,
    body: InventoryLocationFull,
    options?: RequestOptions,
  ): Promise<Error | undefined> {
    return this.call(createInventoryLocation, body, { merchantLocationKey }, options);
  }

  /** Delete an inventory location. */
  delete(merchantLocationKey: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(deleteInventoryLocation, undefined, { merchantLocationKey }, options);
  }

  /** Disable an inventory location. */
  disable(merchantLocationKey: string, options?: RequestOptions): Promise<object> {
    return this.call(disableInventoryLocation, undefined, { merchantLocationKey }, options);
  }

  /** Enable a disabled inventory location. */
  enable(merchantLocationKey: string, options?: RequestOptions): Promise<object> {
    return this.call(enableInventoryLocation, undefined, { merchantLocationKey }, options);
  }

  /** Get one inventory location. */
  get(merchantLocationKey: string, options?: RequestOptions): Promise<InventoryLocationResponse> {
    return this.call(getInventoryLocation, undefined, { merchantLocationKey }, options);
  }

  /** List one page of the seller's inventory locations. */
  list(params: { limit?: string; offset?: string } = {}, options?: RequestOptions): Promise<LocationResponse> {
    return this.call(getInventoryLocations, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: string; offset?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.InventoryLocationResponse, void, undefined> {
    return this.paginate(getInventoryLocations, undefined, { ...params }, options);
  }

  /** Update the details of an inventory location. */
  update(merchantLocationKey: string, body: InventoryLocation, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(updateInventoryLocation, body, { merchantLocationKey }, options);
  }
}
