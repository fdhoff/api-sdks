// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { PR01Response200, PR03Request, PR04Request } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const pR01: Operation = {
  id: 'PR01',
  method: 'GET',
  path: '/api/promotions',
  resource: 'promotions',
  name: 'list',
  params: [
    { wire: 'ids', name: 'ids', location: 'query' },
    { wire: 'types', name: 'types', location: 'query' },
    { wire: 'states', name: 'states', location: 'query' },
    { wire: 'ending_after', name: 'endingAfter', location: 'query' },
    { wire: 'starting_before', name: 'startingBefore', location: 'query' },
    { wire: 'date_created_from', name: 'dateCreatedFrom', location: 'query' },
    { wire: 'date_created_to', name: 'dateCreatedTo', location: 'query' },
    { wire: 'last_request_date', name: 'lastRequestDate', location: 'query' },
    { wire: 'locale', name: 'locale', location: 'query' },
    { wire: 'trigger_offer_ids', name: 'triggerOfferIds', location: 'query' },
    { wire: 'reward_offer_ids', name: 'rewardOfferIds', location: 'query' },
    { wire: 'channel_codes', name: 'channelCodes', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'promotions', total: 'total_count', offset: 'offset' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PROMOTION_READ'] }]],
};

const pR03: Operation = {
  id: 'PR03',
  method: 'POST',
  path: '/api/promotions',
  resource: 'promotions',
  name: 'create',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

const pR04: Operation = {
  id: 'PR04',
  method: 'PUT',
  path: '/api/promotions/{promotion_internal_id}',
  resource: 'promotions',
  name: 'update',
  params: [
    { wire: 'promotion_internal_id', name: 'promotionInternalId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  hasBody: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN'] }]],
};

export const OPERATIONS: readonly Operation[] = [pR01, pR03, pR04];

export class PromotionsApi extends Resource {
  /** List one page of promotions (PR01). */
  list(
    params: {
      ids?: string;
      types?: string;
      states?: string;
      endingAfter?: string;
      startingBefore?: string;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastRequestDate?: string;
      locale?: string;
      triggerOfferIds?: string;
      rewardOfferIds?: string;
      channelCodes?: string;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<PR01Response200> {
    return this.call(pR01, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      ids?: string;
      types?: string;
      states?: string;
      endingAfter?: string;
      startingBefore?: string;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastRequestDate?: string;
      locale?: string;
      triggerOfferIds?: string;
      rewardOfferIds?: string;
      channelCodes?: string;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PR01Response200Promotions, void, undefined> {
    return this.paginate(pR01, undefined, { ...params }, options);
  }

  /** Create a promotion (PR03). */
  create(body?: PR03Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<void> {
    return this.call(pR03, body, { ...params }, options);
  }

  /** Update a promotion (PR04). */
  update(
    promotionInternalId: string,
    body?: PR04Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(pR04, body, { promotionInternalId, ...params }, options);
  }
}
