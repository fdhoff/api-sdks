// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { Config, GetConfig429Response } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getConfig: Operation = {
  id: 'getConfig',
  method: 'GET',
  path: '/commerce/notification/v1/config',
  resource: 'config',
  name: 'get',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const updateConfig: Operation = {
  id: 'updateConfig',
  method: 'PUT',
  path: '/commerce/notification/v1/config',
  resource: 'config',
  name: 'update',
  host: 'api',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [getConfig, updateConfig];

export class ConfigApi extends Resource {
  /** Get the app's notification settings. */
  get(options?: RequestOptions): Promise<Config> {
    return this.call(getConfig, undefined, {}, options);
  }

  /** Update the app's notification settings. */
  update(body?: Config, options?: RequestOptions): Promise<void> {
    return this.call(updateConfig, body, {}, options);
  }
}
