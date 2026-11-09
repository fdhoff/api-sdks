// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreateImageFromFile429Response, CreateImageFromUrlRequest, ImageResponse } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createImageFromFile: Operation = {
  id: 'createImageFromFile',
  method: 'POST',
  path: '/commerce/media/v1_beta/image/create_image_from_file',
  resource: 'images',
  name: 'upload',
  host: 'apim',
  params: [{ wire: 'image', name: 'image', location: 'form' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const createImageFromUrl: Operation = {
  id: 'createImageFromUrl',
  method: 'POST',
  path: '/commerce/media/v1_beta/image/create_image_from_url',
  resource: 'images',
  name: 'createFromUrl',
  host: 'apim',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getImage: Operation = {
  id: 'getImage',
  method: 'GET',
  path: '/commerce/media/v1_beta/image/{image_id}',
  resource: 'images',
  name: 'get',
  host: 'apim',
  params: [{ wire: 'image_id', name: 'imageId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [createImageFromFile, createImageFromUrl, getImage];

export class ImagesApi extends Resource {
  /** Upload an image file to eBay's picture service. */
  upload(params: { image: FileInput }, options?: RequestOptions): Promise<ImageResponse> {
    return this.call(createImageFromFile, undefined, { ...params }, options);
  }

  /** Create an image on eBay's picture service from a public URL. */
  createFromUrl(body: CreateImageFromUrlRequest, options?: RequestOptions): Promise<ImageResponse> {
    return this.call(createImageFromUrl, body, {}, options);
  }

  /** Get one image. */
  get(imageId: string, options?: RequestOptions): Promise<ImageResponse> {
    return this.call(getImage, undefined, { imageId }, options);
  }
}
