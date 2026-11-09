// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { SigningKeysApi, OPERATIONS as SigningKeysApiOperations } from './apis/SigningKeysApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...SigningKeysApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly signingKeys: SigningKeysApi;

  constructor(transport: Transport) {
    this.signingKeys = new SigningKeysApi(transport);
  }
}
