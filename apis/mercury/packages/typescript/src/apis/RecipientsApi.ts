// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AddRecipientRequest,
  EditRecipientRequest,
  RecipientInfo,
  RecipientsAttachmentsPaginatedResponse,
  RecipientsPaginatedResponse,
  UploadedAttachment,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createRecipient: Operation = {
  id: 'createRecipient',
  method: 'POST',
  path: '/recipients',
  resource: 'recipients',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const deleteRecipient: Operation = {
  id: 'deleteRecipient',
  method: 'DELETE',
  path: '/recipient/{recipientId}',
  resource: 'recipients',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'recipientId', name: 'recipientId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getRecipient: Operation = {
  id: 'getRecipient',
  method: 'GET',
  path: '/recipient/{recipientId}',
  resource: 'recipients',
  name: 'get',
  host: 'api',
  params: [{ wire: 'recipientId', name: 'recipientId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getRecipients: Operation = {
  id: 'getRecipients',
  method: 'GET',
  path: '/recipients',
  resource: 'recipients',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'recipients', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listRecipientsAttachments: Operation = {
  id: 'listRecipientsAttachments',
  method: 'GET',
  path: '/recipients/attachments',
  resource: 'recipients',
  name: 'listAttachments',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterAttachments',
  paging: { style: 'cursor', items: 'attachments', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateRecipient: Operation = {
  id: 'updateRecipient',
  method: 'POST',
  path: '/recipient/{recipientId}',
  resource: 'recipients',
  name: 'update',
  host: 'api',
  params: [{ wire: 'recipientId', name: 'recipientId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const uploadRecipientAttachment: Operation = {
  id: 'uploadRecipientAttachment',
  method: 'POST',
  path: '/recipient/{recipientId}/attachments',
  resource: 'recipients',
  name: 'uploadAttachment',
  host: 'api',
  params: [
    { wire: 'recipientId', name: 'recipientId', location: 'path' },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createRecipient,
  deleteRecipient,
  getRecipient,
  getRecipients,
  listRecipientsAttachments,
  updateRecipient,
  uploadRecipientAttachment,
];

export class RecipientsApi extends Resource {
  /** Create a payment recipient. */
  create(body?: AddRecipientRequest, options?: RequestOptions): Promise<RecipientInfo> {
    return this.call(createRecipient, body, {}, options);
  }

  /** Delete a payment recipient. */
  delete(recipientId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteRecipient, undefined, { recipientId }, options);
  }

  /** Get one payment recipient. */
  get(recipientId: string, options?: RequestOptions): Promise<RecipientInfo> {
    return this.call(getRecipient, undefined, { recipientId }, options);
  }

  /** List one page of payment recipients. */
  list(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<RecipientsPaginatedResponse> {
    return this.call(getRecipients, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.RecipientInfo, void, undefined> {
    return this.paginate(getRecipients, undefined, { ...params }, options);
  }

  /** List one page of the files attached to recipients. */
  listAttachments(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): Promise<RecipientsAttachmentsPaginatedResponse> {
    return this.call(listRecipientsAttachments, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterAttachments(
    params: { limit?: number; startAfter?: string; endBefore?: string; order?: 'asc' | 'desc' } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.RecipientAttachmentWithId, void, undefined> {
    return this.paginate(listRecipientsAttachments, undefined, { ...params }, options);
  }

  /** Update a payment recipient. */
  update(recipientId: string, body?: EditRecipientRequest, options?: RequestOptions): Promise<RecipientInfo> {
    return this.call(updateRecipient, body, { recipientId }, options);
  }

  /** Attach a file */
  uploadAttachment(
    recipientId: string,
    params: { file: FileInput },
    options?: RequestOptions,
  ): Promise<UploadedAttachment> {
    return this.call(uploadRecipientAttachment, undefined, { recipientId, ...params }, options);
  }
}
