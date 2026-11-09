// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateOffersRequest,
  FindEligibleItems429Response,
  PagedEligibleItemCollection,
  SendOfferToInterestedBuyersCollectionResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const findEligibleItems: Operation = {
  id: 'findEligibleItems',
  method: 'GET',
  path: '/sell/negotiation/v1/find_eligible_items',
  resource: 'offers',
  name: 'findEligibleItems',
  host: 'api',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  iterator: 'iterEligibleItems',
  paging: {
    style: 'next_link',
    items: 'eligibleItems',
    link: 'next',
    params: ['offset', 'limit', 'continuation_token'],
  },
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
          'https://api.ebay.com/oauth/api_scope/sell.inventory',
        ],
      },
    ],
  ],
};

const sendOfferToInterestedBuyers: Operation = {
  id: 'sendOfferToInterestedBuyers',
  method: 'POST',
  path: '/sell/negotiation/v1/send_offer_to_interested_buyers',
  resource: 'offers',
  name: 'sendToInterestedBuyers',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.inventory'] }]],
};

export const OPERATIONS: readonly Operation[] = [findEligibleItems, sendOfferToInterestedBuyers];

export class OffersApi extends Resource {
  /** List one page of the seller's listings with interested buyers. */
  findEligibleItems(
    params: { limit?: string; offset?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<PagedEligibleItemCollection | undefined> {
    return this.call(findEligibleItems, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterEligibleItems(
    params: { limit?: string; offset?: string; marketplaceId?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.EligibleItem, void, undefined> {
    return this.paginate(findEligibleItems, undefined, { ...params }, options);
  }

  /** Send a discount offer to the buyers interested in a listing. */
  sendToInterestedBuyers(
    body?: CreateOffersRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<SendOfferToInterestedBuyersCollectionResponse> {
    return this.call(sendOfferToInterestedBuyers, body, { ...params }, options);
  }
}
