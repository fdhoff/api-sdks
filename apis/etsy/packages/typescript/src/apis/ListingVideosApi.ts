// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, ListingVideo, ListingVideos } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const deleteListingVideo: Operation = {
  id: 'deleteListingVideo',
  method: 'DELETE',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/videos/{video_id}',
  resource: 'listingVideos',
  name: 'delete',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'video_id', name: 'videoId', location: 'path' },
  ],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const getListingVideo: Operation = {
  id: 'getListingVideo',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/videos/{video_id}',
  resource: 'listingVideos',
  name: 'get',
  params: [
    { wire: 'video_id', name: 'videoId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingVideos: Operation = {
  id: 'getListingVideos',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}/videos',
  resource: 'listingVideos',
  name: 'list',
  params: [{ wire: 'listing_id', name: 'listingId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const uploadListingVideo: Operation = {
  id: 'uploadListingVideo',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}/videos',
  resource: 'listingVideos',
  name: 'upload',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'video_id', name: 'videoId', location: 'form' },
    { wire: 'video', name: 'video', location: 'form' },
    { wire: 'name', name: 'name', location: 'form' },
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
  deleteListingVideo,
  getListingVideo,
  getListingVideos,
  uploadListingVideo,
];

export class ListingVideosApi extends Resource {
  /** Delete a video from a listing. */
  delete(shopId: number, listingId: number, videoId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListingVideo, undefined, { shopId, listingId, videoId }, options);
  }

  /** Get one video of a listing. */
  get(videoId: number, listingId: number, options?: RequestOptions): Promise<ListingVideo> {
    return this.call(getListingVideo, undefined, { videoId, listingId }, options);
  }

  /** List a listing's videos. */
  list(listingId: number, options?: RequestOptions): Promise<ListingVideos> {
    return this.call(getListingVideos, undefined, { listingId }, options);
  }

  /** Upload a video to a listing, or attach an existing one. */
  upload(
    shopId: number,
    listingId: number,
    params: { videoId?: number; video?: FileInput; name?: string } = {},
    options?: RequestOptions,
  ): Promise<ListingVideo> {
    return this.call(uploadListingVideo, undefined, { shopId, listingId, ...params }, options);
  }
}
