// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getStatementPdf: Operation = {
  id: 'getStatementPdf',
  method: 'GET',
  path: '/statements/{statementId}/pdf',
  resource: 'statements',
  name: 'downloadPdf',
  host: 'api',
  params: [{ wire: 'statementId', name: 'statementId', location: 'path' }],
  returnsBinary: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [getStatementPdf];

export class StatementsApi extends Resource {
  /** Download an account statement as a PDF. */
  downloadPdf(statementId: string, options?: RequestOptions): Promise<import('../runtime/index.js').Download> {
    return this.call(getStatementPdf, undefined, { statementId }, options);
  }
}
