// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { CancellationsApi, OPERATIONS as CancellationsApiOperations } from './apis/CancellationsApi.js';
import { CasesApi, OPERATIONS as CasesApiOperations } from './apis/CasesApi.js';
import { InquiriesApi, OPERATIONS as InquiriesApiOperations } from './apis/InquiriesApi.js';
import { ReturnPreferencesApi, OPERATIONS as ReturnPreferencesApiOperations } from './apis/ReturnPreferencesApi.js';
import { ReturnsApi, OPERATIONS as ReturnsApiOperations } from './apis/ReturnsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...CancellationsApiOperations,
    ...CasesApiOperations,
    ...InquiriesApiOperations,
    ...ReturnPreferencesApiOperations,
    ...ReturnsApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly cancellations: CancellationsApi;
  readonly cases: CasesApi;
  readonly inquiries: InquiriesApi;
  readonly returnPreferences: ReturnPreferencesApi;
  readonly returns: ReturnsApi;

  constructor(transport: Transport) {
    this.cancellations = new CancellationsApi(transport);
    this.cases = new CasesApi(transport);
    this.inquiries = new InquiriesApi(transport);
    this.returnPreferences = new ReturnPreferencesApi(transport);
    this.returns = new ReturnsApi(transport);
  }
}
