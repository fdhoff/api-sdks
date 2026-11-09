// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  Card,
  CardListResponse,
  CardRevealResponse,
  CreateCardRequest,
  UpdateCardRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const cancelCard: Operation = {
  id: 'cancelCard',
  method: 'POST',
  path: '/cards/{cardId}/cancel',
  resource: 'cards',
  name: 'cancel',
  host: 'api',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const createCard: Operation = {
  id: 'createCard',
  method: 'POST',
  path: '/cards',
  resource: 'cards',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const freezeCard: Operation = {
  id: 'freezeCard',
  method: 'POST',
  path: '/cards/{cardId}/freeze',
  resource: 'cards',
  name: 'freeze',
  host: 'api',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const getCard: Operation = {
  id: 'getCard',
  method: 'GET',
  path: '/cards/{cardId}',
  resource: 'cards',
  name: 'get',
  host: 'api',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const listCards: Operation = {
  id: 'listCards',
  method: 'GET',
  path: '/cards',
  resource: 'cards',
  name: 'list',
  host: 'api',
  params: [
    { wire: 'accountId', name: 'accountId', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'kind', name: 'kind', location: 'query' },
    { wire: 'userId', name: 'userId', location: 'query' },
    { wire: 'isAgentCard', name: 'isAgentCard', location: 'query' },
    { wire: 'isSingleUse', name: 'isSingleUse', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
    { wire: 'start_after', name: 'startAfter', location: 'query' },
    { wire: 'end_before', name: 'endBefore', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'cursor', items: 'cards', next: 'page.nextPage', param: 'start_after' },
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const revealCardPan: Operation = {
  id: 'revealCardPan',
  method: 'GET',
  path: '/cards/{cardId}/reveal',
  resource: 'cards',
  name: 'reveal',
  host: 'vault',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const unfreezeCard: Operation = {
  id: 'unfreezeCard',
  method: 'POST',
  path: '/cards/{cardId}/unfreeze',
  resource: 'cards',
  name: 'unfreeze',
  host: 'api',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

const updateCard: Operation = {
  id: 'updateCard',
  method: 'POST',
  path: '/cards/{cardId}',
  resource: 'cards',
  name: 'update',
  host: 'api',
  params: [{ wire: 'cardId', name: 'cardId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'bearerAuth', scopes: [] }]],
};

export const OPERATIONS: readonly Operation[] = [
  cancelCard,
  createCard,
  freezeCard,
  getCard,
  listCards,
  revealCardPan,
  unfreezeCard,
  updateCard,
];

export class CardsApi extends Resource {
  /** Cancel a card for good. */
  cancel(cardId: string, options?: RequestOptions): Promise<Card> {
    return this.call(cancelCard, undefined, { cardId }, options);
  }

  /** Issue a card. */
  create(body?: CreateCardRequest, options?: RequestOptions): Promise<Card> {
    return this.call(createCard, body, {}, options);
  }

  /** Freeze a card. */
  freeze(cardId: string, options?: RequestOptions): Promise<Card> {
    return this.call(freezeCard, undefined, { cardId }, options);
  }

  /** Get one card. */
  get(cardId: string, options?: RequestOptions): Promise<Card> {
    return this.call(getCard, undefined, { cardId }, options);
  }

  /** List one page of cards. */
  list(
    params: {
      accountId?: Array<string>;
      status?: Array<'active' | 'frozen' | 'cancelled' | 'inactive' | 'expired' | 'suspended' | 'singleUseConsumed'>;
      type?: Array<'virtual' | 'physical'>;
      kind?: Array<'debit' | 'credit'>;
      userId?: string;
      isAgentCard?: boolean;
      isSingleUse?: boolean;
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<CardListResponse> {
    return this.call(listCards, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      accountId?: Array<string>;
      status?: Array<'active' | 'frozen' | 'cancelled' | 'inactive' | 'expired' | 'suspended' | 'singleUseConsumed'>;
      type?: Array<'virtual' | 'physical'>;
      kind?: Array<'debit' | 'credit'>;
      userId?: string;
      isAgentCard?: boolean;
      isSingleUse?: boolean;
      limit?: number;
      order?: 'asc' | 'desc';
      startAfter?: string;
      endBefore?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.Card, void, undefined> {
    return this.paginate(listCards, undefined, { ...params }, options);
  }

  /** Get a card's full number and security code. Never log the result. */
  reveal(cardId: string, options?: RequestOptions): Promise<CardRevealResponse> {
    return this.call(revealCardPan, undefined, { cardId }, options);
  }

  /** Unfreeze a card. */
  unfreeze(cardId: string, options?: RequestOptions): Promise<Card> {
    return this.call(unfreezeCard, undefined, { cardId }, options);
  }

  /** Update a card. */
  update(cardId: string, body?: UpdateCardRequest, options?: RequestOptions): Promise<Card> {
    return this.call(updateCard, body, { cardId }, options);
  }
}
