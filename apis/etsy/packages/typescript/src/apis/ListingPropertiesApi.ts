// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingPropertyValue, ListingPropertyValues } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deleteListingProperty: Operation = {
  id: 'deleteListingProperty',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}',
  resource: 'listingProperties',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'property_id', name: 'propertyId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getListingProperties: Operation = {
  id: 'getListingProperties',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/properties',
  resource: 'listingProperties',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingProperty: Operation = {
  id: 'getListingProperty',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/properties/{property_id}',
  resource: 'listingProperties',
  name: 'get',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'property_id', name: 'propertyId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const updateListingProperty: Operation = {
  id: 'updateListingProperty',
  method: 'PUT',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id}',
  resource: 'listingProperties',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'property_id', name: 'propertyId', location: 'path' },
    { wire: 'value_ids', name: 'valueIds', location: 'urlencoded' },
    { wire: 'values', name: 'values', location: 'urlencoded' },
    { wire: 'scale_id', name: 'scaleId', location: 'urlencoded' },
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
  deleteListingProperty,
  getListingProperties,
  getListingProperty,
  updateListingProperty,
];

export class ListingPropertiesApi extends Resource {
  /** Remove one property value from a listing. */
  delete(shopId: number, listingId: number, propertyId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListingProperty, undefined, { shopId, listingId, propertyId }, options);
  }

  /** List a listing's property values. */
  list(shopId: number, listingId: number, options?: RequestOptions): Promise<ListingPropertyValues> {
    return this.call(getListingProperties, undefined, { shopId, listingId }, options);
  }

  /** Get one property value of a listing. */
  get(listingId: number, propertyId: number, options?: RequestOptions): Promise<ListingPropertyValue> {
    return this.call(getListingProperty, undefined, { listingId, propertyId }, options);
  }

  /** Set one property value of a listing. */
  update(
    shopId: number,
    listingId: number,
    propertyId: number,
    params: { valueIds: Array<number>; values: Array<string>; scaleId?: number },
    options?: RequestOptions,
  ): Promise<ListingPropertyValue> {
    return this.call(updateListingProperty, undefined, { shopId, listingId, propertyId, ...params }, options);
  }
}
