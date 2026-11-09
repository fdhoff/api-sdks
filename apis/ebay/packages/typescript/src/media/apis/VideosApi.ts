// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { CreateImageFromFile429Response, CreateVideoRequest, Video } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createVideo: Operation = {
  id: 'createVideo',
  method: 'POST',
  path: '/commerce/media/v1_beta/video',
  resource: 'videos',
  name: 'create',
  host: 'apim',
  params: [],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

const getVideo: Operation = {
  id: 'getVideo',
  method: 'GET',
  path: '/commerce/media/v1_beta/video/{video_id}',
  resource: 'videos',
  name: 'get',
  host: 'apim',
  params: [{ wire: 'video_id', name: 'videoId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [createVideo, getVideo];

export class VideosApi extends Resource {
  /** Create a video resource to upload content to. */
  create(body?: CreateVideoRequest, options?: RequestOptions): Promise<void> {
    return this.call(createVideo, body, {}, options);
  }

  /** Get one video and its status. */
  get(videoId: string, options?: RequestOptions): Promise<Video> {
    return this.call(getVideo, undefined, { videoId }, options);
  }
}
