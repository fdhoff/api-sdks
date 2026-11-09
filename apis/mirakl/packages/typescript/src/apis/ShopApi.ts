// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  A01Response200,
  A02Request,
  A02Response200,
  A21Response200,
  S30Response200,
  S32RequestMultipartFormDataShopDocuments,
  S32Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const a01: Operation = {
  id: 'A01',
  method: 'GET',
  path: '/api/account',
  resource: 'shop',
  name: 'get',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_READ'] }]],
};

const a02: Operation = {
  id: 'A02',
  method: 'PUT',
  path: '/api/account',
  resource: 'shop',
  name: 'update',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_UPDATE'] }]],
};

const a21: Operation = {
  id: 'A21',
  method: 'GET',
  path: '/api/account/statistics',
  resource: 'shop',
  name: 'getStatistics',
  params: [
    { wire: 'periods', name: 'periods', location: 'query' },
    { wire: 'channel_code', name: 'channelCode', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_READ'] }]],
};

const s30: Operation = {
  id: 'S30',
  method: 'GET',
  path: '/api/shops/documents',
  resource: 'shop',
  name: 'listDocuments',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_DOCUMENT_READ'] }]],
};

const s31: Operation = {
  id: 'S31',
  method: 'GET',
  path: '/api/shops/documents/download',
  resource: 'shop',
  name: 'downloadDocuments',
  params: [
    { wire: 'document_ids', name: 'documentIds', location: 'query' },
    { wire: 'type_codes', name: 'typeCodes', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_DOCUMENT_READ'] }]],
};

const s32: Operation = {
  id: 'S32',
  method: 'POST',
  path: '/api/shops/documents',
  resource: 'shop',
  name: 'uploadDocuments',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'files', name: 'files', location: 'form' },
    { wire: 'shop_documents', name: 'shopDocuments', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_DOCUMENT_WRITE'] }]],
};

const s33: Operation = {
  id: 'S33',
  method: 'DELETE',
  path: '/api/shops/documents/{document_id}',
  resource: 'shop',
  name: 'deleteDocument',
  params: [
    { wire: 'document_id', name: 'documentId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SHOP_DOCUMENT_DELETE'] }]],
};

export const OPERATIONS: readonly Operation[] = [a01, a02, a21, s30, s31, s32, s33];

export class ShopApi extends Resource {
  /** Get your shop's information (A01). */
  get(params: { shopId?: number } = {}, options?: RequestOptions): Promise<A01Response200> {
    return this.call(a01, undefined, { ...params }, options);
  }

  /** Update your shop's information (A02). */
  update(body?: A02Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<A02Response200> {
    return this.call(a02, body, { ...params }, options);
  }

  /** Get your shop's statistics (A21). */
  getStatistics(
    params: { periods?: string; channelCode?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<A21Response200> {
    return this.call(a21, undefined, { ...params }, options);
  }

  /** List your shop's documents (S30). */
  listDocuments(params: { shopId?: number } = {}, options?: RequestOptions): Promise<S30Response200> {
    return this.call(s30, undefined, { ...params }, options);
  }

  /** Download one or more shop documents (S31). */
  downloadDocuments(
    params: { documentIds?: string; typeCodes?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(s31, undefined, { ...params }, options);
  }

  /** Upload business documents to your shop (S32). */
  uploadDocuments(
    params: { shopId?: number; files: FileInput[]; shopDocuments: S32RequestMultipartFormDataShopDocuments },
    options?: RequestOptions,
  ): Promise<S32Response200> {
    return this.call(s32, undefined, { ...params }, options);
  }

  /** Delete a shop document (S33). */
  deleteDocument(documentId: number, params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(s33, undefined, { documentId, ...params }, options);
  }
}
