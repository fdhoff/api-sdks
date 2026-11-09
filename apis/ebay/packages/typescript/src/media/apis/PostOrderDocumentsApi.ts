// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreateImageFromFile429Response } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const removePostOrderDocument: Operation = {
  id: 'removePostOrderDocument',
  method: 'DELETE',
  path: '/commerce/media/v1_beta/post_order/document/{document_id}',
  resource: 'postOrderDocuments',
  name: 'delete',
  host: 'apiz',
  params: [{ wire: 'document_id', name: 'documentId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.post_order.document'] }]],
};

const uploadPostOrderDocument: Operation = {
  id: 'uploadPostOrderDocument',
  method: 'POST',
  path: '/commerce/media/v1_beta/post_order/document',
  resource: 'postOrderDocuments',
  name: 'upload',
  host: 'apiz',
  params: [
    { wire: 'file', name: 'file', location: 'form' },
    { wire: 'documentUsageType', name: 'documentUsageType', location: 'form' },
    { wire: 'entityType', name: 'entityType', location: 'form' },
    { wire: 'entityId', name: 'entityId', location: 'form' },
  ],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/commerce.post_order.document'] }]],
};

export const OPERATIONS: readonly Operation[] = [removePostOrderDocument, uploadPostOrderDocument];

export class PostOrderDocumentsApi extends Resource {
  /** Delete a post-order document. */
  delete(documentId: string, options?: RequestOptions): Promise<void> {
    return this.call(removePostOrderDocument, undefined, { documentId }, options);
  }

  /** Upload a document for a return */
  upload(
    params: { file: FileInput; documentUsageType: string; entityType: string; entityId: string },
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(uploadPostOrderDocument, undefined, { ...params }, options);
  }
}
