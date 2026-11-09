// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateDocumentFromUrlRequest,
  CreateDocumentRequest,
  CreateDocumentResponse,
  CreateImageFromFile429Response,
  DocumentResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createDocument: Operation = {
  id: 'createDocument',
  method: 'POST',
  path: '/commerce/media/v1_beta/document',
  resource: 'documents',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const createDocumentFromUrl: Operation = {
  id: 'createDocumentFromUrl',
  method: 'POST',
  path: '/commerce/media/v1_beta/document/create_document_from_url',
  resource: 'documents',
  name: 'createFromUrl',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getDocument: Operation = {
  id: 'getDocument',
  method: 'GET',
  path: '/commerce/media/v1_beta/document/{document_id}',
  resource: 'documents',
  name: 'get',
  host: 'api',
  params: [{ wire: 'document_id', name: 'documentId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const uploadDocument: Operation = {
  id: 'uploadDocument',
  method: 'POST',
  path: '/commerce/media/v1_beta/document/{document_id}/upload',
  resource: 'documents',
  name: 'upload',
  host: 'api',
  params: [
    { wire: 'document_id', name: 'documentId', location: 'path' },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [createDocument, createDocumentFromUrl, getDocument, uploadDocument];

export class DocumentsApi extends Resource {
  /** Create a document resource to upload a file to. */
  create(body?: CreateDocumentRequest, options?: RequestOptions): Promise<CreateDocumentResponse> {
    return this.call(createDocument, body, {}, options);
  }

  /** Create a document from a public URL. */
  createFromUrl(body?: CreateDocumentFromUrlRequest, options?: RequestOptions): Promise<CreateDocumentResponse> {
    return this.call(createDocumentFromUrl, body, {}, options);
  }

  /** Get one document and its status. */
  get(documentId: string, options?: RequestOptions): Promise<DocumentResponse> {
    return this.call(getDocument, undefined, { documentId }, options);
  }

  /** Upload the file of a document. */
  upload(documentId: string, params: { file: FileInput }, options?: RequestOptions): Promise<DocumentResponse> {
    return this.call(uploadDocument, undefined, { documentId, ...params }, options);
  }
}
