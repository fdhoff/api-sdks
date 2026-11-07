// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetCareFolderDetailsResponse,
  GetCareFolderListResponse,
  PostItemTransferCreateRequest,
  PostMessageResponse,
  PostNoteRequest,
  PostNoteResponse,
  PostRefundCreateRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getCareFolderDetails: Operation = {
  id: 'getCareFolderDetails',
  method: 'GET',
  path: '/ws/sav/{careFolderId}',
  resource: 'care',
  name: 'getFolder',
  params: [{ wire: 'careFolderId', name: 'careFolderId', location: 'path' }],
  returnsJson: true,
};

const getCareFolderList: Operation = {
  id: 'getCareFolderList',
  method: 'GET',
  path: '/ws/sav',
  resource: 'care',
  name: 'listFolders',
  params: [
    { wire: 'last_id', name: 'lastId', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'orderline', name: 'orderline', location: 'query' },
    { wire: 'last_modification_date', name: 'lastModificationDate', location: 'query' },
    { wire: 'last_message_date', name: 'lastMessageDate', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFolders',
};

const postItemTransfer: Operation = {
  id: 'postItemTransfer',
  method: 'POST',
  path: '/ws/sav/{careFolderId}/item-transfer',
  resource: 'care',
  name: 'transferItem',
  params: [{ wire: 'careFolderId', name: 'careFolderId', location: 'path' }],
  hasBody: true,
};

const postMessage: Operation = {
  id: 'postMessage',
  method: 'POST',
  path: '/ws/sav/{careFolderId}/msg',
  resource: 'care',
  name: 'sendMessage',
  params: [
    { wire: 'careFolderId', name: 'careFolderId', location: 'path' },
    { wire: 'attachment', name: 'attachment', location: 'form' },
    { wire: 'message', name: 'message', location: 'form' },
  ],
  returnsJson: true,
};

const postNote: Operation = {
  id: 'postNote',
  method: 'POST',
  path: '/ws/sav/{careFolderId}/note',
  resource: 'care',
  name: 'addNote',
  params: [{ wire: 'careFolderId', name: 'careFolderId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
};

const postProblem: Operation = {
  id: 'postProblem',
  method: 'POST',
  path: '/ws/sav/{careFolderId}/problem',
  resource: 'care',
  name: 'reportProblem',
  params: [
    { wire: 'careFolderId', name: 'careFolderId', location: 'path' },
    { wire: 'problem_type', name: 'problemType', location: 'form' },
    { wire: 'message', name: 'message', location: 'form' },
    { wire: 'attachment', name: 'attachment', location: 'form' },
  ],
};

const postRefundCreate: Operation = {
  id: 'postRefundCreate',
  method: 'POST',
  path: '/ws/sav/refund',
  resource: 'care',
  name: 'createRefund',
  params: [],
  hasBody: true,
};

export const OPERATIONS: readonly Operation[] = [
  getCareFolderDetails,
  getCareFolderList,
  postItemTransfer,
  postMessage,
  postNote,
  postProblem,
  postRefundCreate,
];

export class CareApi extends Resource {
  /** Get one care folder. */
  getFolder(careFolderId: number, options?: RequestOptions): Promise<GetCareFolderDetailsResponse> {
    return this.call(getCareFolderDetails, undefined, { careFolderId }, options);
  }

  /** List one page of care folders. */
  listFolders(
    params: {
      lastId?: number;
      state?: 0 | 9;
      orderline?: number;
      lastModificationDate?: string;
      lastMessageDate?: string;
      page?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<GetCareFolderListResponse> {
    return this.call(getCareFolderList, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFolders(
    params: {
      lastId?: number;
      state?: 0 | 9;
      orderline?: number;
      lastModificationDate?: string;
      lastMessageDate?: string;
      page?: number;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.CareFolder, void, undefined> {
    return this.paginate(getCareFolderList, undefined, { ...params }, options);
  }

  /** Transfer an item on a care folder. */
  transferItem(careFolderId: number, body: PostItemTransferCreateRequest, options?: RequestOptions): Promise<void> {
    return this.call(postItemTransfer, body, { careFolderId }, options);
  }

  /** Send a message on a care folder. */
  sendMessage(
    careFolderId: number,
    params: { attachment?: FileInput[]; message: string },
    options?: RequestOptions,
  ): Promise<PostMessageResponse> {
    return this.call(postMessage, undefined, { careFolderId, ...params }, options);
  }

  /** Add a note to a care folder. */
  addNote(careFolderId: number, body: PostNoteRequest, options?: RequestOptions): Promise<PostNoteResponse> {
    return this.call(postNote, body, { careFolderId }, options);
  }

  /** Report a problem on a care folder. */
  reportProblem(
    careFolderId: number,
    params: { problemType?: string; message?: string; attachment?: FileInput[] } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(postProblem, undefined, { careFolderId, ...params }, options);
  }

  /** Create a refund. Never retried on failure. */
  createRefund(body?: PostRefundCreateRequest, options?: RequestOptions): Promise<string> {
    return this.call(postRefundCreate, body, {}, options);
  }
}
