// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ApiEventResponse, ApiEventsPaginatedResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getEvent: Operation = {
  id: 'getEvent',
  method: 'GET',
  path: '/events/{eventId}',
  resource: 'events',
  name: 'get',
  host: 'api',
  params: [{ wire: 'eventId', name: 'eventId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getEvents: Operation = {
  id: 'getEvents',
  method: 'GET',
  path: '/events',
  resource: 'events',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'resourceType', name: 'resourceType', location: 'query' },
    { wire: 'resourceId', name: 'resourceId', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'events', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getEvent, getEvents];

export class EventsApi extends Resource {
  /** Get one event. */
  get(eventId: string, options?: RequestOptions): Promise<ApiEventResponse> {
    return this.call(getEvent, undefined, { eventId }, options);
  }

  /** List one page of events. */
  list(
    params: {
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
      resourceType?:
        | 'transaction'
        | 'checkingAccount'
        | 'savingsAccount'
        | 'treasuryAccount'
        | 'investmentAccount'
        | 'creditAccount';
      resourceId?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ApiEventsPaginatedResponse> {
    return this.call(getEvents, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
      resourceType?:
        | 'transaction'
        | 'checkingAccount'
        | 'savingsAccount'
        | 'treasuryAccount'
        | 'investmentAccount'
        | 'creditAccount';
      resourceId?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiEventResponse, void, undefined> {
    return this.paginate(getEvents, undefined, { ...params }, options);
  }
}
