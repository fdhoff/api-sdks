// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BaseResponse,
  BulkCreateAdsByInventoryReference429Response,
  ItemPromotion,
  ItemPromotionResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createItemPromotion: Operation = {
  id: 'createItemPromotion',
  method: 'POST',
  path: '/sell/marketing/v1/item_promotion',
  resource: 'itemPromotions',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteItemPromotion: Operation = {
  id: 'deleteItemPromotion',
  method: 'DELETE',
  path: '/sell/marketing/v1/item_promotion/{promotion_id}',
  resource: 'itemPromotions',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getItemPromotion: Operation = {
  id: 'getItemPromotion',
  method: 'GET',
  path: '/sell/marketing/v1/item_promotion/{promotion_id}',
  resource: 'itemPromotions',
  name: 'get',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.marketing.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.marketing',
        ],
      },
    ],
  ],
};

const updateItemPromotion: Operation = {
  id: 'updateItemPromotion',
  method: 'PUT',
  path: '/sell/marketing/v1/item_promotion/{promotion_id}',
  resource: 'itemPromotions',
  name: 'update',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createItemPromotion,
  deleteItemPromotion,
  getItemPromotion,
  updateItemPromotion,
];

export class ItemPromotionsApi extends Resource {
  /** Create a threshold promotion. */
  create(body?: ItemPromotion, options?: RequestOptions): Promise<BaseResponse> {
    return this.call(createItemPromotion, body, {}, options);
  }

  /** Delete a threshold promotion. */
  delete(promotionId: string, options?: RequestOptions): Promise<Error | undefined> {
    return this.call(deleteItemPromotion, undefined, { promotionId }, options);
  }

  /** Get one threshold promotion. */
  get(promotionId: string, options?: RequestOptions): Promise<ItemPromotionResponse> {
    return this.call(getItemPromotion, undefined, { promotionId }, options);
  }

  /** Replace a threshold promotion. */
  update(promotionId: string, body?: ItemPromotion, options?: RequestOptions): Promise<BaseResponse | undefined> {
    return this.call(updateItemPromotion, body, { promotionId }, options);
  }
}
