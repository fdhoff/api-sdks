// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { RateLimitsApi, OPERATIONS as RateLimitsApiOperations } from './apis/RateLimitsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...RateLimitsApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly rateLimits: RateLimitsApi;

  constructor(transport: Transport) {
    this.rateLimits = new RateLimitsApi(transport);
  }
}
