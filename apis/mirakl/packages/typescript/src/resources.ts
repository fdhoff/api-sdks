// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { AccountingApi, OPERATIONS as AccountingApiOperations } from './apis/AccountingApi.js';
import { MessagesApi, OPERATIONS as MessagesApiOperations } from './apis/MessagesApi.js';
import { OffersApi, OPERATIONS as OffersApiOperations } from './apis/OffersApi.js';
import { OrdersApi, OPERATIONS as OrdersApiOperations } from './apis/OrdersApi.js';
import { PicklistsApi, OPERATIONS as PicklistsApiOperations } from './apis/PicklistsApi.js';
import { PlatformApi, OPERATIONS as PlatformApiOperations } from './apis/PlatformApi.js';
import { ProductsApi, OPERATIONS as ProductsApiOperations } from './apis/ProductsApi.js';
import { PromotionsApi, OPERATIONS as PromotionsApiOperations } from './apis/PromotionsApi.js';
import { ReturnsApi, OPERATIONS as ReturnsApiOperations } from './apis/ReturnsApi.js';
import { ShipmentsApi, OPERATIONS as ShipmentsApiOperations } from './apis/ShipmentsApi.js';
import { ShopApi, OPERATIONS as ShopApiOperations } from './apis/ShopApi.js';
import { UsersApi, OPERATIONS as UsersApiOperations } from './apis/UsersApi.js';
import type { Operation, Transport } from './runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...AccountingApiOperations,
    ...MessagesApiOperations,
    ...OffersApiOperations,
    ...OrdersApiOperations,
    ...PicklistsApiOperations,
    ...PlatformApiOperations,
    ...ProductsApiOperations,
    ...PromotionsApiOperations,
    ...ReturnsApiOperations,
    ...ShipmentsApiOperations,
    ...ShopApiOperations,
    ...UsersApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly accounting: AccountingApi;
  readonly messages: MessagesApi;
  readonly offers: OffersApi;
  readonly orders: OrdersApi;
  readonly picklists: PicklistsApi;
  readonly platform: PlatformApi;
  readonly products: ProductsApi;
  readonly promotions: PromotionsApi;
  readonly returns: ReturnsApi;
  readonly shipments: ShipmentsApi;
  readonly shop: ShopApi;
  readonly users: UsersApi;

  constructor(transport: Transport) {
    this.accounting = new AccountingApi(transport);
    this.messages = new MessagesApi(transport);
    this.offers = new OffersApi(transport);
    this.orders = new OrdersApi(transport);
    this.picklists = new PicklistsApi(transport);
    this.platform = new PlatformApi(transport);
    this.products = new ProductsApi(transport);
    this.promotions = new PromotionsApi(transport);
    this.returns = new ReturnsApi(transport);
    this.shipments = new ShipmentsApi(transport);
    this.shop = new ShopApi(transport);
    this.users = new UsersApi(transport);
  }
}
