// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { OrdersApi, OPERATIONS as OrdersApiOperations } from './apis/OrdersApi.js';
import { PaymentDisputesApi, OPERATIONS as PaymentDisputesApiOperations } from './apis/PaymentDisputesApi.js';
import {
  ShippingFulfillmentsApi,
  OPERATIONS as ShippingFulfillmentsApiOperations,
} from './apis/ShippingFulfillmentsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [...OrdersApiOperations, ...PaymentDisputesApiOperations, ...ShippingFulfillmentsApiOperations].map((operation) => [
    operation.id,
    operation,
  ]),
);

export class Resources {
  readonly orders: OrdersApi;
  readonly paymentDisputes: PaymentDisputesApi;
  readonly shippingFulfillments: ShippingFulfillmentsApi;

  constructor(transport: Transport) {
    this.orders = new OrdersApi(transport);
    this.paymentDisputes = new PaymentDisputesApi(transport);
    this.shippingFulfillments = new ShippingFulfillmentsApi(transport);
  }
}
