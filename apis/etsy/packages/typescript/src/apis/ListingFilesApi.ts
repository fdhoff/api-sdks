// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ShopListingFile, ShopListingFiles } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deleteListingFile: Operation = {
  id: 'deleteListingFile',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}',
  resource: 'listingFiles',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'listing_file_id', name: 'listingFileId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getAllListingFiles: Operation = {
  id: 'getAllListingFiles',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/files',
  resource: 'listingFiles',
  name: 'list',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getListingFile: Operation = {
  id: 'getListingFile',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}',
  resource: 'listingFiles',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'listing_file_id', name: 'listingFileId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const uploadListingFile: Operation = {
  id: 'uploadListingFile',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/files',
  resource: 'listingFiles',
  name: 'upload',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'listing_file_id', name: 'listingFileId', location: 'form' },
    { wire: 'file', name: 'file', location: 'form' },
    { wire: 'name', name: 'name', location: 'form' },
    { wire: 'rank', name: 'rank', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  deleteListingFile,
  getAllListingFiles,
  getListingFile,
  uploadListingFile,
];

export class ListingFilesApi extends Resource {
  /** Delete a file from a digital listing. */
  delete(shopId: number, listingId: number, listingFileId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListingFile, undefined, { shopId, listingId, listingFileId }, options);
  }

  /** List a digital listing's files. */
  list(listingId: number, shopId: number, options?: RequestOptions): Promise<ShopListingFiles> {
    return this.call(getAllListingFiles, undefined, { listingId, shopId }, options);
  }

  /** Get one file of a digital listing. */
  get(shopId: number, listingId: number, listingFileId: number, options?: RequestOptions): Promise<ShopListingFile> {
    return this.call(getListingFile, undefined, { shopId, listingId, listingFileId }, options);
  }

  /** Upload a file to a digital listing, or attach an existing one. */
  upload(
    shopId: number,
    listingId: number,
    params: { listingFileId?: number; file?: FileInput; name?: string; rank?: number } = {},
    options?: RequestOptions,
  ): Promise<ShopListingFile> {
    return this.call(uploadListingFile, undefined, { shopId, listingId, ...params }, options);
  }
}
