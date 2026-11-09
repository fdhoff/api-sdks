// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  InventoryItemGroupsApi,
  OPERATIONS as InventoryItemGroupsApiOperations,
} from './apis/InventoryItemGroupsApi.js';
import { InventoryItemsApi, OPERATIONS as InventoryItemsApiOperations } from './apis/InventoryItemsApi.js';
import { ListingsApi, OPERATIONS as ListingsApiOperations } from './apis/ListingsApi.js';
import { LocationsApi, OPERATIONS as LocationsApiOperations } from './apis/LocationsApi.js';
import { OffersApi, OPERATIONS as OffersApiOperations } from './apis/OffersApi.js';
import {
  ProductCompatibilityApi,
  OPERATIONS as ProductCompatibilityApiOperations,
} from './apis/ProductCompatibilityApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...InventoryItemGroupsApiOperations,
    ...InventoryItemsApiOperations,
    ...ListingsApiOperations,
    ...LocationsApiOperations,
    ...OffersApiOperations,
    ...ProductCompatibilityApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly inventoryItemGroups: InventoryItemGroupsApi;
  readonly inventoryItems: InventoryItemsApi;
  readonly listings: ListingsApi;
  readonly locations: LocationsApi;
  readonly offers: OffersApi;
  readonly productCompatibility: ProductCompatibilityApi;

  constructor(transport: Transport) {
    this.inventoryItemGroups = new InventoryItemGroupsApi(transport);
    this.inventoryItems = new InventoryItemsApi(transport);
    this.listings = new ListingsApi(transport);
    this.locations = new LocationsApi(transport);
    this.offers = new OffersApi(transport);
    this.productCompatibility = new ProductCompatibilityApi(transport);
  }
}
