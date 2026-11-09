// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  ListingRecommendationsApi,
  OPERATIONS as ListingRecommendationsApiOperations,
} from './apis/ListingRecommendationsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...ListingRecommendationsApiOperations].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly listingRecommendations: ListingRecommendationsApi;

  constructor(transport: Transport) {
    this.listingRecommendations = new ListingRecommendationsApi(transport);
  }
}
