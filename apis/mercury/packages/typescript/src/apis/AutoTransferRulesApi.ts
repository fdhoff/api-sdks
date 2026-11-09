// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { AutoTransferRulesResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getAutoTransferRules: Operation = {
  id: 'getAutoTransferRules',
  method: 'GET',
  path: '/auto-transfer-rules',
  resource: 'autoTransferRules',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'rules', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getAutoTransferRules];

export class AutoTransferRulesApi extends Resource {
  /** List one page of automatic transfer rules. */
  list(
    params: {
      accountId?: string;
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<AutoTransferRulesResponse> {
    return this.call(getAutoTransferRules, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      accountId?: string;
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.AutoTransferRule, void, undefined> {
    return this.paginate(getAutoTransferRules, undefined, { ...params }, options);
  }
}
