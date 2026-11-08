// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingImage, ListingImages } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deleteListingImage: Operation = {
  id: 'deleteListingImage',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/images/{listing_image_id}',
  resource: 'listingImages',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'listing_image_id', name: 'listingImageId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getListingImage: Operation = {
  id: 'getListingImage',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/images/{listing_image_id}',
  resource: 'listingImages',
  name: 'get',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'listing_image_id', name: 'listingImageId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingImages: Operation = {
  id: 'getListingImages',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/images',
  resource: 'listingImages',
  name: 'list',
  params: [{ wire: 'listing_id', name: 'listingId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const uploadListingImage: Operation = {
  id: 'uploadListingImage',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/images',
  resource: 'listingImages',
  name: 'upload',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'image', name: 'image', location: 'form' },
    { wire: 'listing_image_id', name: 'listingImageId', location: 'form' },
    { wire: 'rank', name: 'rank', location: 'form' },
    { wire: 'overwrite', name: 'overwrite', location: 'form' },
    { wire: 'is_watermarked', name: 'isWatermarked', location: 'form' },
    { wire: 'alt_text', name: 'altText', location: 'form' },
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
  deleteListingImage,
  getListingImage,
  getListingImages,
  uploadListingImage,
];

export class ListingImagesApi extends Resource {
  /** Delete an image from a listing. */
  delete(shopId: number, listingId: number, listingImageId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListingImage, undefined, { shopId, listingId, listingImageId }, options);
  }

  /** Get one image of a listing. */
  get(listingId: number, listingImageId: number, options?: RequestOptions): Promise<ListingImage> {
    return this.call(getListingImage, undefined, { listingId, listingImageId }, options);
  }

  /** List a listing's images. */
  list(listingId: number, options?: RequestOptions): Promise<ListingImages> {
    return this.call(getListingImages, undefined, { listingId }, options);
  }

  /** Upload an image to a listing, or attach an existing one. */
  upload(
    shopId: number,
    listingId: number,
    params: {
      image?: FileInput;
      listingImageId?: number;
      rank?: number;
      overwrite?: boolean;
      isWatermarked?: boolean;
      altText?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ListingImage> {
    return this.call(uploadListingImage, undefined, { shopId, listingId, ...params }, options);
  }
}
