// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  Destination,
  DestinationRequest,
  DestinationSearchResponse,
  GetConfig429Response,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createDestination: Operation = {
  id: 'createDestination',
  method: 'POST',
  path: '/commerce/notification/v1/destination',
  resource: 'destinations',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const deleteDestination: Operation = {
  id: 'deleteDestination',
  method: 'DELETE',
  path: '/commerce/notification/v1/destination/{destination_id}',
  resource: 'destinations',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'destination_id', name: 'destinationId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getDestination: Operation = {
  id: 'getDestination',
  method: 'GET',
  path: '/commerce/notification/v1/destination/{destination_id}',
  resource: 'destinations',
  name: 'get',
  host: 'api',
  params: [{ wire: 'destination_id', name: 'destinationId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getDestinations: Operation = {
  id: 'getDestinations',
  method: 'GET',
  path: '/commerce/notification/v1/destination',
  resource: 'destinations',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'continuation_token', name: 'continuationToken', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: {
    style: 'next_link',
    items: 'destinations',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const updateDestination: Operation = {
  id: 'updateDestination',
  method: 'PUT',
  path: '/commerce/notification/v1/destination/{destination_id}',
  resource: 'destinations',
  name: 'update',
  host: 'api',
  params: [{ wire: 'destination_id', name: 'destinationId', location: 'path' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createDestination,
  deleteDestination,
  getDestination,
  getDestinations,
  updateDestination,
];

export class DestinationsApi extends Resource {
  /** Create a destination endpoint for notifications. */
  create(body?: DestinationRequest, options?: RequestOptions): Promise<object> {
    return this.call(createDestination, body, {}, options);
  }

  /** Delete a destination. */
  delete(destinationId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteDestination, undefined, { destinationId }, options);
  }

  /** Get one destination. */
  get(destinationId: string, options?: RequestOptions): Promise<Destination> {
    return this.call(getDestination, undefined, { destinationId }, options);
  }

  /** List one page of the app's notification destinations. */
  list(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): Promise<DestinationSearchResponse> {
    return this.call(getDestinations, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { continuationToken?: string; limit?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Destination, void, undefined> {
    return this.paginate(getDestinations, undefined, { ...params }, options);
  }

  /** Update a destination. */
  update(destinationId: string, body?: DestinationRequest, options?: RequestOptions): Promise<void> {
    return this.call(updateDestination, body, { destinationId }, options);
  }
}
