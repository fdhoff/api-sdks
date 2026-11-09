// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import { BillingActivitiesApi, OPERATIONS as BillingActivitiesApiOperations } from './apis/BillingActivitiesApi.js';
import { OrderEarningsApi, OPERATIONS as OrderEarningsApiOperations } from './apis/OrderEarningsApi.js';
import { PayoutsApi, OPERATIONS as PayoutsApiOperations } from './apis/PayoutsApi.js';
import { SellerFundsApi, OPERATIONS as SellerFundsApiOperations } from './apis/SellerFundsApi.js';
import { TransactionsApi, OPERATIONS as TransactionsApiOperations } from './apis/TransactionsApi.js';
import { TransfersApi, OPERATIONS as TransfersApiOperations } from './apis/TransfersApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...BillingActivitiesApiOperations,
    ...OrderEarningsApiOperations,
    ...PayoutsApiOperations,
    ...SellerFundsApiOperations,
    ...TransactionsApiOperations,
    ...TransfersApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly billingActivities: BillingActivitiesApi;
  readonly orderEarnings: OrderEarningsApi;
  readonly payouts: PayoutsApi;
  readonly sellerFunds: SellerFundsApi;
  readonly transactions: TransactionsApi;
  readonly transfers: TransfersApi;

  constructor(transport: Transport) {
    this.billingActivities = new BillingActivitiesApi(transport);
    this.orderEarnings = new OrderEarningsApi(transport);
    this.payouts = new PayoutsApi(transport);
    this.sellerFunds = new SellerFundsApi(transport);
    this.transactions = new TransactionsApi(transport);
    this.transfers = new TransfersApi(transport);
  }
}
