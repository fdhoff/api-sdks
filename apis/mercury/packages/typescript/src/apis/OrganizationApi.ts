// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { OrganizationResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getOrganization: Operation = {
  id: 'getOrganization',
  method: 'GET',
  path: '/organization',
  resource: 'organization',
  name: 'get',
  host: 'api',
  params: [],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getOrganization];

export class OrganizationApi extends Resource {
  /** Get your organization. */
  get(options?: RequestOptions): Promise<OrganizationResponse> {
    return this.call(getOrganization, undefined, {}, options);
  }
}
