// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { FeedbackApi, OPERATIONS as FeedbackApiOperations } from './apis/FeedbackApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...FeedbackApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly feedback: FeedbackApi;

  constructor(transport: Transport) {
    this.feedback = new FeedbackApi(transport);
  }
}
