// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ApiV1ArAttachmentResponseData,
  ApiV1ArAttachmentsResponseData,
  ApiV1ArInvoiceCreateRequest,
  ApiV1ArInvoiceResponse,
  ApiV1ArInvoiceUpdateRequest,
  ApiV1ArInvoicesPaginatedResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const cancelInvoice: Operation = {
  id: 'cancelInvoice',
  method: 'POST',
  path: '/ar/invoices/{invoiceId}/cancel',
  resource: 'invoices',
  name: 'cancel',
  host: 'api',
  params: [{ wire: 'invoiceId', name: 'invoiceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const createInvoice: Operation = {
  id: 'createInvoice',
  method: 'POST',
  path: '/ar/invoices',
  resource: 'invoices',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getAttachment: Operation = {
  id: 'getAttachment',
  method: 'GET',
  path: '/ar/attachments/{attachmentId}',
  resource: 'invoices',
  name: 'getAttachment',
  host: 'api',
  params: [{ wire: 'attachmentId', name: 'attachmentId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getInvoice: Operation = {
  id: 'getInvoice',
  method: 'GET',
  path: '/ar/invoices/{invoiceId}',
  resource: 'invoices',
  name: 'get',
  host: 'api',
  params: [{ wire: 'invoiceId', name: 'invoiceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getInvoicePdf: Operation = {
  id: 'getInvoicePdf',
  method: 'GET',
  path: '/ar/invoices/{invoiceId}/pdf',
  resource: 'invoices',
  name: 'downloadPdf',
  host: 'api',
  params: [{ wire: 'invoiceId', name: 'invoiceId', location: 'path' }],
  returnsBinary: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listInvoiceAttachments: Operation = {
  id: 'listInvoiceAttachments',
  method: 'GET',
  path: '/ar/invoices/{invoiceId}/attachments',
  resource: 'invoices',
  name: 'listAttachments',
  host: 'api',
  params: [{ wire: 'invoiceId', name: 'invoiceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listInvoices: Operation = {
  id: 'listInvoices',
  method: 'GET',
  path: '/ar/invoices',
  resource: 'invoices',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'invoices', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateInvoice: Operation = {
  id: 'updateInvoice',
  method: 'POST',
  path: '/ar/invoices/{invoiceId}',
  resource: 'invoices',
  name: 'update',
  host: 'api',
  params: [{ wire: 'invoiceId', name: 'invoiceId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  cancelInvoice,
  createInvoice,
  getAttachment,
  getInvoice,
  getInvoicePdf,
  listInvoiceAttachments,
  listInvoices,
  updateInvoice,
];

export class InvoicesApi extends Resource {
  /** Cancel an invoice. */
  cancel(invoiceId: string, options?: RequestOptions): Promise<void> {
    return this.call(cancelInvoice, undefined, { invoiceId }, options);
  }

  /** Create an invoice. */
  create(body?: ApiV1ArInvoiceCreateRequest, options?: RequestOptions): Promise<ApiV1ArInvoiceResponse> {
    return this.call(createInvoice, body, {}, options);
  }

  /** Get one invoice attachment */
  getAttachment(attachmentId: string, options?: RequestOptions): Promise<ApiV1ArAttachmentResponseData> {
    return this.call(getAttachment, undefined, { attachmentId }, options);
  }

  /** Get one invoice. */
  get(invoiceId: string, options?: RequestOptions): Promise<ApiV1ArInvoiceResponse> {
    return this.call(getInvoice, undefined, { invoiceId }, options);
  }

  /** Download an invoice as a PDF. */
  downloadPdf(invoiceId: string, options?: RequestOptions): Promise<import('../runtime/index.js').Download> {
    return this.call(getInvoicePdf, undefined, { invoiceId }, options);
  }

  /** List an invoice's attachments. */
  listAttachments(invoiceId: string, options?: RequestOptions): Promise<ApiV1ArAttachmentsResponseData> {
    return this.call(listInvoiceAttachments, undefined, { invoiceId }, options);
  }

  /** List one page of invoices. */
  list(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): Promise<ApiV1ArInvoicesPaginatedResponse> {
    return this.call(listInvoices, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: { limit?: number; order?: 'asc' | 'desc'; startAfter?: string; endBefore?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ApiV1ArInvoicesData, void, undefined> {
    return this.paginate(listInvoices, undefined, { ...params }, options);
  }

  /** Update an invoice. */
  update(
    invoiceId: string,
    body?: ApiV1ArInvoiceUpdateRequest,
    options?: RequestOptions,
  ): Promise<ApiV1ArInvoiceResponse> {
    return this.call(updateInvoice, body, { invoiceId }, options);
  }
}
