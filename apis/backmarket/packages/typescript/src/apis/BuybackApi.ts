// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  BuybackCompetitor,
  BuybackCounterOfferReasonsInner,
  BuybackListing,
  BuybackListingUpdate,
  BuybackMessage,
  BuybackMessagePage,
  BuybackMessagePayload,
  BuybackOrder,
  BuybackOrderPage,
  BuybackOrderState,
  BuybackOrderSuspensionPayload,
  BuybackPaginatedListingResponse,
  BuybackReason,
  ErrorResponseV3,
  Problem,
  ProblemValidation,
  ValidationErrorResponseV3,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation } from '../runtime/index.js';

const getWsBuybackV1Competitors: Operation = {
  id: 'get-ws-buyback-v1-competitors',
  method: 'GET',
  path: '/ws/buyback/v1/competitors/{listingId}',
  resource: 'buyback',
  name: 'listCompetitors',
  params: [{ wire: 'listingId', name: 'listingId', location: 'path' }],
};

const getWsBuybackV1Listing: Operation = {
  id: 'get-ws-buyback-v1-listing',
  method: 'GET',
  path: '/ws/buyback/v1/listings/{buybackListingId}',
  resource: 'buyback',
  name: 'getListing',
  params: [{ wire: 'buybackListingId', name: 'buybackListingId', location: 'path' }],
};

const getWsBuybackV1Listings: Operation = {
  id: 'get-ws-buyback-v1-listings',
  method: 'GET',
  path: '/ws/buyback/v1/listings',
  resource: 'buyback',
  name: 'listListings',
  params: [
    { wire: 'productId', name: 'productId', location: 'query' },
    { wire: 'cursor', name: 'cursor', location: 'query' },
    { wire: 'pageSize', name: 'pageSize', location: 'query' },
  ],
  iterator: 'iterListings',
};

const getWsBuybackV1Order: Operation = {
  id: 'get-ws-buyback-v1-order',
  method: 'GET',
  path: '/ws/buyback/v1/orders/{buybackOrderId}',
  resource: 'buyback',
  name: 'getOrder',
  params: [{ wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' }],
};

const getWsBuybackV1Orders: Operation = {
  id: 'get-ws-buyback-v1-orders',
  method: 'GET',
  path: '/ws/buyback/v1/orders',
  resource: 'buyback',
  name: 'listOrders',
  params: [
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'productId', name: 'productId', location: 'query' },
    { wire: 'creationDate', name: 'creationDate', location: 'query' },
    { wire: 'modificationDate', name: 'modificationDate', location: 'query' },
    { wire: 'shippingDate', name: 'shippingDate', location: 'query' },
    { wire: 'receivedDate', name: 'receivedDate', location: 'query' },
    { wire: 'suspendedDate', name: 'suspendedDate', location: 'query' },
    { wire: 'paymentDate', name: 'paymentDate', location: 'query' },
    { wire: 'page', name: 'page', location: 'query' },
  ],
  iterator: 'iterOrders',
};

const getWsBuybackV1OrdersMessages: Operation = {
  id: 'get-ws-buyback-v1-orders-messages',
  method: 'GET',
  path: '/ws/buyback/v1/orders/{buybackOrderId}/messages',
  resource: 'buyback',
  name: 'listMessages',
  params: [
    { wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' },
    { wire: 'page', name: 'page', location: 'query' },
  ],
  iterator: 'iterMessages',
};

const getWsBuybackV1OrdersPendingReply: Operation = {
  id: 'get-ws-buyback-v1-orders-pending-reply',
  method: 'GET',
  path: '/ws/buyback/v1/orders/pending-reply',
  resource: 'buyback',
  name: 'listPendingOrders',
  params: [{ wire: 'page', name: 'page', location: 'query' }],
  iterator: 'iterPendingOrders',
};

const getWsBuybackV1OrdersSuspendReasons: Operation = {
  id: 'get-ws-buyback-v1-orders-suspend-reasons',
  method: 'GET',
  path: '/ws/buyback/v1/orders/suspend-reasons',
  resource: 'buyback',
  name: 'listSuspendReasons',
  params: [],
};

const getWsCounterOfferReason: Operation = {
  id: 'get-ws-counter-offer-reason',
  method: 'GET',
  path: '/ws/buyback/v1/orders/{buybackOrderId}/counter-offers/reasons',
  resource: 'buyback',
  name: 'listCounterOfferReasons',
  params: [{ wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' }],
};

const postWsBuybackV1OrdersMessages: Operation = {
  id: 'post-ws-buyback-v1-orders-messages',
  method: 'POST',
  path: '/ws/buyback/v1/orders/{buybackOrderId}/messages',
  resource: 'buyback',
  name: 'sendMessage',
  params: [{ wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' }],
  hasBody: true,
};

const putWsBuybackV1Listing: Operation = {
  id: 'put-ws-buyback-v1-listing',
  method: 'PUT',
  path: '/ws/buyback/v1/listings/{buybackListingId}',
  resource: 'buyback',
  name: 'updateListing',
  params: [{ wire: 'buybackListingId', name: 'buybackListingId', location: 'path' }],
  hasBody: true,
};

const putWsBuybackV1OrdersSuspend: Operation = {
  id: 'put-ws-buyback-v1-orders-suspend',
  method: 'PUT',
  path: '/ws/buyback/v1/orders/{buybackOrderId}/suspend',
  resource: 'buyback',
  name: 'suspendOrder',
  params: [{ wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' }],
  hasBody: true,
};

const putWsBuybackV1OrdersValidate: Operation = {
  id: 'put-ws-buyback-v1-orders-validate',
  method: 'PUT',
  path: '/ws/buyback/v1/orders/{buybackOrderId}/validate',
  resource: 'buyback',
  name: 'validateOrder',
  params: [{ wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' }],
};

const putWsRefurbisherCounterOffer: Operation = {
  id: 'put-ws-refurbisher-counter-offer',
  method: 'PUT',
  path: '/ws/buyback/v2/orders/{buybackOrderId}/counter-offers',
  resource: 'buyback',
  name: 'counterOffer',
  params: [
    { wire: 'buybackOrderId', name: 'buybackOrderId', location: 'path' },
    { wire: 'price', name: 'price', location: 'form' },
    { wire: 'comment', name: 'comment', location: 'form' },
    { wire: 'reasons', name: 'reasons', location: 'form' },
    { wire: 'files', name: 'files', location: 'form' },
  ],
};

export const OPERATIONS: readonly Operation[] = [
  getWsBuybackV1Competitors,
  getWsBuybackV1Listing,
  getWsBuybackV1Listings,
  getWsBuybackV1Order,
  getWsBuybackV1Orders,
  getWsBuybackV1OrdersMessages,
  getWsBuybackV1OrdersPendingReply,
  getWsBuybackV1OrdersSuspendReasons,
  getWsCounterOfferReason,
  postWsBuybackV1OrdersMessages,
  putWsBuybackV1Listing,
  putWsBuybackV1OrdersSuspend,
  putWsBuybackV1OrdersValidate,
  putWsRefurbisherCounterOffer,
];

export class BuybackApi extends Resource {
  /** List competitors for a buyback listing. */
  listCompetitors(listingId: string): Promise<Array<BuybackCompetitor>> {
    return this.call(getWsBuybackV1Competitors, undefined, { listingId });
  }

  /** Get one buyback listing. */
  getListing(buybackListingId: string): Promise<BuybackListing> {
    return this.call(getWsBuybackV1Listing, undefined, { buybackListingId });
  }

  /** List one page of buyback listings. */
  listListings(
    params: { productId?: string; cursor?: string; pageSize?: number } = {},
  ): Promise<BuybackPaginatedListingResponse> {
    return this.call(getWsBuybackV1Listings, undefined, { ...params });
  }

  /** Iterate every item across all pages. */
  iterListings(
    params: { productId?: string; cursor?: string; pageSize?: number } = {},
  ): AsyncGenerator<models.BuybackListing, void, undefined> {
    return this.paginate(getWsBuybackV1Listings, undefined, { ...params });
  }

  /** Get one buyback order. */
  getOrder(buybackOrderId: string): Promise<BuybackOrder> {
    return this.call(getWsBuybackV1Order, undefined, { buybackOrderId });
  }

  /** List one page of buyback orders. */
  listOrders(
    params: {
      status?: BuybackOrderState;
      productId?: number;
      creationDate?: string;
      modificationDate?: string;
      shippingDate?: string;
      receivedDate?: string;
      suspendedDate?: string;
      paymentDate?: string;
      page?: number;
    } = {},
  ): Promise<BuybackOrderPage> {
    return this.call(getWsBuybackV1Orders, undefined, { ...params });
  }

  /** Iterate every item across all pages. */
  iterOrders(
    params: {
      status?: BuybackOrderState;
      productId?: number;
      creationDate?: string;
      modificationDate?: string;
      shippingDate?: string;
      receivedDate?: string;
      suspendedDate?: string;
      paymentDate?: string;
      page?: number;
    } = {},
  ): AsyncGenerator<models.BuybackOrder, void, undefined> {
    return this.paginate(getWsBuybackV1Orders, undefined, { ...params });
  }

  /** List one page of a buyback order&#39;s messages. */
  listMessages(buybackOrderId: string, params: { page?: number } = {}): Promise<BuybackMessagePage> {
    return this.call(getWsBuybackV1OrdersMessages, undefined, { buybackOrderId, ...params });
  }

  /** Iterate every item across all pages. */
  iterMessages(
    buybackOrderId: string,
    params: { page?: number } = {},
  ): AsyncGenerator<models.BuybackMessage, void, undefined> {
    return this.paginate(getWsBuybackV1OrdersMessages, undefined, { buybackOrderId, ...params });
  }

  /** List one page of buyback orders awaiting a reply. */
  listPendingOrders(params: { page?: number } = {}): Promise<BuybackOrderPage> {
    return this.call(getWsBuybackV1OrdersPendingReply, undefined, { ...params });
  }

  /** Iterate every item across all pages. */
  iterPendingOrders(params: { page?: number } = {}): AsyncGenerator<models.BuybackOrder, void, undefined> {
    return this.paginate(getWsBuybackV1OrdersPendingReply, undefined, { ...params });
  }

  /** List the reasons a buyback order can be suspended. */
  listSuspendReasons(): Promise<Array<BuybackReason>> {
    return this.call(getWsBuybackV1OrdersSuspendReasons, undefined, {});
  }

  /** List the counter-offer reasons for a buyback order. */
  listCounterOfferReasons(buybackOrderId: string): Promise<Array<BuybackCounterOfferReasonsInner>> {
    return this.call(getWsCounterOfferReason, undefined, { buybackOrderId });
  }

  /** Send a message on a buyback order. */
  sendMessage(buybackOrderId: string, body: BuybackMessagePayload): Promise<BuybackMessage> {
    return this.call(postWsBuybackV1OrdersMessages, body, { buybackOrderId });
  }

  /** Update one buyback listing. */
  updateListing(buybackListingId: string, body: BuybackListingUpdate): Promise<object> {
    return this.call(putWsBuybackV1Listing, body, { buybackListingId });
  }

  /** Suspend a buyback order. */
  suspendOrder(buybackOrderId: string, body: BuybackOrderSuspensionPayload): Promise<BuybackOrder> {
    return this.call(putWsBuybackV1OrdersSuspend, body, { buybackOrderId });
  }

  /** Validate a buyback order. */
  validateOrder(buybackOrderId: string): Promise<BuybackOrder> {
    return this.call(putWsBuybackV1OrdersValidate, undefined, { buybackOrderId });
  }

  /** Make a counter-offer on a buyback order. */
  counterOffer(
    buybackOrderId: string,
    params: { price: number; comment?: string; reasons: Array<string>; files: FileInput[] },
  ): Promise<void> {
    return this.call(putWsRefurbisherCounterOffer, undefined, { buybackOrderId, ...params });
  }
}
