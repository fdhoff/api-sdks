// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateRecipientInviteApiRequest,
  RecipientInviteApiPaginatedResponse,
  RecipientInviteApiResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createRecipientInvite: Operation = {
  id: 'createRecipientInvite',
  method: 'POST',
  path: '/recipients/invites',
  resource: 'recipientInvites',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const deleteRecipientInvite: Operation = {
  id: 'deleteRecipientInvite',
  method: 'DELETE',
  path: '/recipients/invites/{inviteId}',
  resource: 'recipientInvites',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'inviteId', name: 'inviteId', location: 'path' }],
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getRecipientInvite: Operation = {
  id: 'getRecipientInvite',
  method: 'GET',
  path: '/recipients/invites/{inviteId}',
  resource: 'recipientInvites',
  name: 'get',
  host: 'api',
  params: [{ wire: 'inviteId', name: 'inviteId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listRecipientInvites: Operation = {
  id: 'listRecipientInvites',
  method: 'GET',
  path: '/recipients/invites',
  resource: 'recipientInvites',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'invites', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createRecipientInvite,
  deleteRecipientInvite,
  getRecipientInvite,
  listRecipientInvites,
];

export class RecipientInvitesApi extends Resource {
  /** Invite someone to add their own payment details as a recipient. */
  create(body?: CreateRecipientInviteApiRequest, options?: RequestOptions): Promise<RecipientInviteApiResponse> {
    return this.call(createRecipientInvite, body, {}, options);
  }

  /** Delete a recipient invite. */
  delete(inviteId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteRecipientInvite, undefined, { inviteId }, options);
  }

  /** Get one recipient invite. */
  get(inviteId: string, options?: RequestOptions): Promise<RecipientInviteApiResponse> {
    return this.call(getRecipientInvite, undefined, { inviteId }, options);
  }

  /** List one page of recipient invites. */
  list(
    params: {
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
      status?: 'created' | 'completed' | 'expired' | 'declined';
    } = {},
    options?: RequestOptions,
  ): Promise<RecipientInviteApiPaginatedResponse> {
    return this.call(listRecipientInvites, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      limit?: number;
      startAfter?: string;
      endBefore?: string;
      order?: 'asc' | 'desc';
      status?: 'created' | 'completed' | 'expired' | 'declined';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.RecipientInviteApiResponse, void, undefined> {
    return this.paginate(listRecipientInvites, undefined, { ...params }, options);
  }
}
