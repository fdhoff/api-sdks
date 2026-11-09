// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { DocumentsApi, OPERATIONS as DocumentsApiOperations } from './apis/DocumentsApi.js';
import { ImagesApi, OPERATIONS as ImagesApiOperations } from './apis/ImagesApi.js';
import { PostOrderDocumentsApi, OPERATIONS as PostOrderDocumentsApiOperations } from './apis/PostOrderDocumentsApi.js';
import { VideosApi, OPERATIONS as VideosApiOperations } from './apis/VideosApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...DocumentsApiOperations, ...ImagesApiOperations, ...PostOrderDocumentsApiOperations, ...VideosApiOperations].map(
    (operation) => [operation.id, operation],
  ),
);

export class Resources {
  readonly documents: DocumentsApi;
  readonly images: ImagesApi;
  readonly postOrderDocuments: PostOrderDocumentsApi;
  readonly videos: VideosApi;

  constructor(transport: Transport) {
    this.documents = new DocumentsApi(transport);
    this.images = new ImagesApi(transport);
    this.postOrderDocuments = new PostOrderDocumentsApi(transport);
    this.videos = new VideosApi(transport);
  }
}
