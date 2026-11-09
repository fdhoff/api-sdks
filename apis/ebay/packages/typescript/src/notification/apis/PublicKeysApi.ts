// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetConfig429Response, PublicKey } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPublicKey: Operation = {
  id: 'getPublicKey',
  method: 'GET',
  path: '/commerce/notification/v1/public_key/{public_key_id}',
  resource: 'publicKeys',
  name: 'get',
  host: 'api',
  params: [{ wire: 'public_key_id', name: 'publicKeyId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [getPublicKey];

export class PublicKeysApi extends Resource {
  /** Get the public key that verifies a notification's signature. */
  get(publicKeyId: string, options?: RequestOptions): Promise<PublicKey> {
    return this.call(getPublicKey, undefined, { publicKeyId }, options);
  }
}
