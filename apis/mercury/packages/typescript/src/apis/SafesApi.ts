// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { APISafeRequest } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getSafeRequest: Operation = {
  id: 'getSafeRequest',
  method: 'GET',
  path: '/safes/{safeRequestId}',
  resource: 'safes',
  name: 'get',
  host: 'api',
  params: [{ wire: 'safeRequestId', name: 'safeRequestId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getSafeRequestDocument: Operation = {
  id: 'getSafeRequestDocument',
  method: 'GET',
  path: '/safes/{safeRequestId}/document',
  resource: 'safes',
  name: 'downloadDocument',
  host: 'api',
  params: [{ wire: 'safeRequestId', name: 'safeRequestId', location: 'path' }],
  returnsBinary: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getSafeRequests: Operation = {
  id: 'getSafeRequests',
  method: 'GET',
  path: '/safes',
  resource: 'safes',
  name: 'list',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getSafeRequest, getSafeRequestDocument, getSafeRequests];

export class SafesApi extends Resource {
  /** Get one SAFE request. */
  get(safeRequestId: string, options?: RequestOptions): Promise<APISafeRequest> {
    return this.call(getSafeRequest, undefined, { safeRequestId }, options);
  }

  /** Download a SAFE request's document as a PDF. */
  downloadDocument(safeRequestId: string, options?: RequestOptions): Promise<import('../runtime/index.js').Download> {
    return this.call(getSafeRequestDocument, undefined, { safeRequestId }, options);
  }

  /** List your SAFE requests. */
  list(options?: RequestOptions): Promise<Array<APISafeRequest>> {
    return this.call(getSafeRequests, undefined, {}, options);
  }
}
