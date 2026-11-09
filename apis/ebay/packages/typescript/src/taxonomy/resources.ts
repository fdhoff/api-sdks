// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { CategoryTreesApi, OPERATIONS as CategoryTreesApiOperations } from './apis/CategoryTreesApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...CategoryTreesApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly categoryTrees: CategoryTreesApi;

  constructor(transport: Transport) {
    this.categoryTrees = new CategoryTreesApi(transport);
  }
}
