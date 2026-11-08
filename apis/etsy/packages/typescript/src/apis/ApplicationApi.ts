// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, Pong } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const ping: Operation = {
  id: 'ping',
  method: 'GET',
  path: '/v3/application/openapi-ping',
  resource: 'application',
  name: 'ping',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const tokenScopes: Operation = {
  id: 'tokenScopes',
  method: 'POST',
  path: '/v3/application/scopes',
  resource: 'application',
  name: 'getTokenScopes',
  params: [{ wire: 'token', name: 'token', location: 'urlencoded' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [ping, tokenScopes];

export class ApplicationApi extends Resource {
  /** Check that the API key works. */
  ping(options?: RequestOptions): Promise<Pong> {
    return this.call(ping, undefined, {}, options);
  }

  /** List the scopes an access token grants. */
  getTokenScopes(params: { token: string }, options?: RequestOptions): Promise<object> {
    return this.call(tokenScopes, undefined, { ...params }, options);
  }
}
