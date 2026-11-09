// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { OffersApi, OPERATIONS as OffersApiOperations } from './apis/OffersApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...OffersApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly offers: OffersApi;

  constructor(transport: Transport) {
    this.offers = new OffersApi(transport);
  }
}
