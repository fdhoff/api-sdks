// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateSigningKeyRequest,
  GetSigningKeys429Response,
  QuerySigningKeysResponse,
  SigningKey,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createSigningKey: Operation = {
  id: 'createSigningKey',
  method: 'POST',
  path: '/developer/key_management/v1/signing_key',
  resource: 'signingKeys',
  name: 'create',
  host: 'apiz',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getSigningKey: Operation = {
  id: 'getSigningKey',
  method: 'GET',
  path: '/developer/key_management/v1/signing_key/{signing_key_id}',
  resource: 'signingKeys',
  name: 'get',
  host: 'apiz',
  params: [{ wire: 'signing_key_id', name: 'signingKeyId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getSigningKeys: Operation = {
  id: 'getSigningKeys',
  method: 'GET',
  path: '/developer/key_management/v1/signing_key',
  resource: 'signingKeys',
  name: 'list',
  host: 'apiz',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [createSigningKey, getSigningKey, getSigningKeys];

export class SigningKeysApi extends Resource {
  /** Create a signing key pair and return its private key once. */
  create(body?: CreateSigningKeyRequest, options?: RequestOptions): Promise<SigningKey> {
    return this.call(createSigningKey, body, {}, options);
  }

  /** Get one signing key. */
  get(signingKeyId: string, options?: RequestOptions): Promise<SigningKey> {
    return this.call(getSigningKey, undefined, { signingKeyId }, options);
  }

  /** List the app's signing keys. */
  list(options?: RequestOptions): Promise<QuerySigningKeysResponse> {
    return this.call(getSigningKeys, undefined, {}, options);
  }
}
