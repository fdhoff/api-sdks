// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { UserApi, OPERATIONS as UserApiOperations } from './apis/UserApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...UserApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly user: UserApi;

  constructor(transport: Transport) {
    this.user = new UserApi(transport);
  }
}
