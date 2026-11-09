// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { BulkCreateAdsByInventoryReference429Response, ItemPriceMarkdown } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createItemPriceMarkdownPromotion: Operation = {
  id: 'createItemPriceMarkdownPromotion',
  method: 'POST',
  path: '/sell/marketing/v1/item_price_markdown',
  resource: 'itemPriceMarkdowns',
  name: 'create',
  host: 'api',
  params: [],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const deleteItemPriceMarkdownPromotion: Operation = {
  id: 'deleteItemPriceMarkdownPromotion',
  method: 'DELETE',
  path: '/sell/marketing/v1/item_price_markdown/{promotion_id}',
  resource: 'itemPriceMarkdowns',
  name: 'delete',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const getItemPriceMarkdownPromotion: Operation = {
  id: 'getItemPriceMarkdownPromotion',
  method: 'GET',
  path: '/sell/marketing/v1/item_price_markdown/{promotion_id}',
  resource: 'itemPriceMarkdowns',
  name: 'get',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

const updateItemPriceMarkdownPromotion: Operation = {
  id: 'updateItemPriceMarkdownPromotion',
  method: 'PUT',
  path: '/sell/marketing/v1/item_price_markdown/{promotion_id}',
  resource: 'itemPriceMarkdowns',
  name: 'update',
  host: 'api',
  params: [{ wire: 'promotion_id', name: 'promotionId', location: 'path' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.marketing'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createItemPriceMarkdownPromotion,
  deleteItemPriceMarkdownPromotion,
  getItemPriceMarkdownPromotion,
  updateItemPriceMarkdownPromotion,
];

export class ItemPriceMarkdownsApi extends Resource {
  /** Create a markdown sale. */
  create(body?: ItemPriceMarkdown, options?: RequestOptions): Promise<object> {
    return this.call(createItemPriceMarkdownPromotion, body, {}, options);
  }

  /** Delete a markdown sale. */
  delete(promotionId: string, options?: RequestOptions): Promise<void> {
    return this.call(deleteItemPriceMarkdownPromotion, undefined, { promotionId }, options);
  }

  /** Get one markdown sale. */
  get(promotionId: string, options?: RequestOptions): Promise<ItemPriceMarkdown> {
    return this.call(getItemPriceMarkdownPromotion, undefined, { promotionId }, options);
  }

  /** Replace a markdown sale. */
  update(promotionId: string, body?: ItemPriceMarkdown, options?: RequestOptions): Promise<object | undefined> {
    return this.call(updateItemPriceMarkdownPromotion, body, { promotionId }, options);
  }
}
