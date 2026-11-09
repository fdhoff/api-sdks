// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { StoreApi, OPERATIONS as StoreApiOperations } from './apis/StoreApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...StoreApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly store: StoreApi;

  constructor(transport: Transport) {
    this.store = new StoreApi(transport);
  }
}
