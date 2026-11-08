// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, Payments } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getPaymentAccountLedgerEntryPayments: Operation = {
  id: 'getPaymentAccountLedgerEntryPayments',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/payment-account/ledger-entries/payments',
  resource: 'payments',
  name: 'listByLedgerEntries',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'ledger_entry_ids', name: 'ledgerEntryIds', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getPayments: Operation = {
  id: 'getPayments',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/payments',
  resource: 'payments',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'payment_ids', name: 'paymentIds', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getShopPaymentByReceiptId: Operation = {
  id: 'getShopPaymentByReceiptId',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}/payments',
  resource: 'payments',
  name: 'listByReceipt',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'receipt_id', name: 'receiptId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  getPaymentAccountLedgerEntryPayments,
  getPayments,
  getShopPaymentByReceiptId,
];

export class PaymentsApi extends Resource {
  /** Get the payments behind several ledger entries. */
  listByLedgerEntries(
    shopId: number,
    params: { ledgerEntryIds: Array<number> },
    options?: RequestOptions,
  ): Promise<Payments> {
    return this.call(getPaymentAccountLedgerEntryPayments, undefined, { shopId, ...params }, options);
  }

  /** Get several payments by ID. */
  list(shopId: number, params: { paymentIds: Array<number> }, options?: RequestOptions): Promise<Payments> {
    return this.call(getPayments, undefined, { shopId, ...params }, options);
  }

  /** List the payments for a receipt. */
  listByReceipt(shopId: number, receiptId: number, options?: RequestOptions): Promise<Payments> {
    return this.call(getShopPaymentByReceiptId, undefined, { shopId, receiptId }, options);
  }
}
