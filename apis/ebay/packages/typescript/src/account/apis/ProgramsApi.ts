// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetCustomPolicies429Response, Program, Programs } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getOptedInPrograms: Operation = {
  id: 'getOptedInPrograms',
  method: 'GET',
  path: '/sell/account/v1/program/get_opted_in_programs',
  resource: 'programs',
  name: 'listOptedIn',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.account',
          'https://api.ebay.com/oauth/api_scope/sell.account.readonly',
        ],
      },
    ],
  ],
};

const optInToProgram: Operation = {
  id: 'optInToProgram',
  method: 'POST',
  path: '/sell/account/v1/program/opt_in',
  resource: 'programs',
  name: 'optIn',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const optOutOfProgram: Operation = {
  id: 'optOutOfProgram',
  method: 'POST',
  path: '/sell/account/v1/program/opt_out',
  resource: 'programs',
  name: 'optOut',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [getOptedInPrograms, optInToProgram, optOutOfProgram];

export class ProgramsApi extends Resource {
  /** List the seller programs the seller has joined. */
  listOptedIn(options?: RequestOptions): Promise<Programs> {
    return this.call(getOptedInPrograms, undefined, {}, options);
  }

  /** Join a seller program. */
  optIn(body: Program, options?: RequestOptions): Promise<object> {
    return this.call(optInToProgram, body, {}, options);
  }

  /** Leave a seller program. */
  optOut(body: Program, options?: RequestOptions): Promise<object> {
    return this.call(optOutOfProgram, body, {}, options);
  }
}
