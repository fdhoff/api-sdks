// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { CompatibilitiesApi, OPERATIONS as CompatibilitiesApiOperations } from './apis/CompatibilitiesApi.js';
import { CountriesApi, OPERATIONS as CountriesApiOperations } from './apis/CountriesApi.js';
import { MarketplacesApi, OPERATIONS as MarketplacesApiOperations } from './apis/MarketplacesApi.js';
import { ShippingApi, OPERATIONS as ShippingApiOperations } from './apis/ShippingApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...CompatibilitiesApiOperations,
    ...CountriesApiOperations,
    ...MarketplacesApiOperations,
    ...ShippingApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly compatibilities: CompatibilitiesApi;
  readonly countries: CountriesApi;
  readonly marketplaces: MarketplacesApi;
  readonly shipping: ShippingApi;

  constructor(transport: Transport) {
    this.compatibilities = new CompatibilitiesApi(transport);
    this.countries = new CountriesApi(transport);
    this.marketplaces = new MarketplacesApi(transport);
    this.shipping = new ShippingApi(transport);
  }
}
