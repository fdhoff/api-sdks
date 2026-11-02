// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { BackboxApi, OPERATIONS as BackboxApiOperations } from './apis/BackboxApi.js';
import { BuybackApi, OPERATIONS as BuybackApiOperations } from './apis/BuybackApi.js';
import { CareApi, OPERATIONS as CareApiOperations } from './apis/CareApi.js';
import { CategoriesApi, OPERATIONS as CategoriesApiOperations } from './apis/CategoriesApi.js';
import { ListingsApi, OPERATIONS as ListingsApiOperations } from './apis/ListingsApi.js';
import { OrdersApi, OPERATIONS as OrdersApiOperations } from './apis/OrdersApi.js';
import { ShippingApi, OPERATIONS as ShippingApiOperations } from './apis/ShippingApi.js';
import { TasksApi, OPERATIONS as TasksApiOperations } from './apis/TasksApi.js';
import type { Operation, Transport } from './runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...BackboxApiOperations,
    ...BuybackApiOperations,
    ...CareApiOperations,
    ...CategoriesApiOperations,
    ...ListingsApiOperations,
    ...OrdersApiOperations,
    ...ShippingApiOperations,
    ...TasksApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly backbox: BackboxApi;
  readonly buyback: BuybackApi;
  readonly care: CareApi;
  readonly categories: CategoriesApi;
  readonly listings: ListingsApi;
  readonly orders: OrdersApi;
  readonly shipping: ShippingApi;
  readonly tasks: TasksApi;

  constructor(transport: Transport) {
    this.backbox = new BackboxApi(transport);
    this.buyback = new BuybackApi(transport);
    this.care = new CareApi(transport);
    this.categories = new CategoriesApi(transport);
    this.listings = new ListingsApi(transport);
    this.orders = new OrdersApi(transport);
    this.shipping = new ShippingApi(transport);
    this.tasks = new TasksApi(transport);
  }
}
