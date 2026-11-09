// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { ConversationsApi, OPERATIONS as ConversationsApiOperations } from './apis/ConversationsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...ConversationsApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly conversations: ConversationsApi;

  constructor(transport: Transport) {
    this.conversations = new ConversationsApi(transport);
  }
}
