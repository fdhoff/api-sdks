// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { ConfigApi, OPERATIONS as ConfigApiOperations } from './apis/ConfigApi.js';
import { DestinationsApi, OPERATIONS as DestinationsApiOperations } from './apis/DestinationsApi.js';
import { PublicKeysApi, OPERATIONS as PublicKeysApiOperations } from './apis/PublicKeysApi.js';
import { SubscriptionsApi, OPERATIONS as SubscriptionsApiOperations } from './apis/SubscriptionsApi.js';
import { TopicsApi, OPERATIONS as TopicsApiOperations } from './apis/TopicsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...ConfigApiOperations,
    ...DestinationsApiOperations,
    ...PublicKeysApiOperations,
    ...SubscriptionsApiOperations,
    ...TopicsApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly config: ConfigApi;
  readonly destinations: DestinationsApi;
  readonly publicKeys: PublicKeysApi;
  readonly subscriptions: SubscriptionsApi;
  readonly topics: TopicsApi;

  constructor(transport: Transport) {
    this.config = new ConfigApi(transport);
    this.destinations = new DestinationsApi(transport);
    this.publicKeys = new PublicKeysApi(transport);
    this.subscriptions = new SubscriptionsApi(transport);
    this.topics = new TopicsApi(transport);
  }
}
