// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { ErrorSchema, PaymentAccountLedgerEntries, PaymentAccountLedgerEntry } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const getShopPaymentAccountLedgerEntries: Operation = {
  id: 'getShopPaymentAccountLedgerEntries',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/payment-account/ledger-entries',
  resource: 'ledgerEntries',
  name: 'list',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'min_created', name: 'minCreated', location: 'query' },
    { wire: 'max_created', name: 'maxCreated', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getShopPaymentAccountLedgerEntry: Operation = {
  id: 'getShopPaymentAccountLedgerEntry',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/payment-account/ledger-entries/{ledger_entry_id}',
  resource: 'ledgerEntries',
  name: 'get',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'ledger_entry_id', name: 'ledgerEntryId', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getShopPaymentAccountLedgerEntries, getShopPaymentAccountLedgerEntry];

export class LedgerEntriesApi extends Resource {
  /** List one page of a shop's payment account ledger entries. */
  list(
    shopId: number,
    params: { minCreated: number; maxCreated: number; limit?: number; offset?: number },
    options?: RequestOptions,
  ): Promise<PaymentAccountLedgerEntries> {
    return this.call(getShopPaymentAccountLedgerEntries, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    shopId: number,
    params: { minCreated: number; maxCreated: number; limit?: number; offset?: number },
    options?: RequestOptions,
  ): AsyncGenerator<models.PaymentAccountLedgerEntry, void, undefined> {
    return this.paginate(getShopPaymentAccountLedgerEntries, undefined, { shopId, ...params }, options);
  }

  /** Get one payment account ledger entry. */
  get(shopId: number, ledgerEntryId: number, options?: RequestOptions): Promise<PaymentAccountLedgerEntry> {
    return this.call(getShopPaymentAccountLedgerEntry, undefined, { shopId, ledgerEntryId }, options);
  }
}
