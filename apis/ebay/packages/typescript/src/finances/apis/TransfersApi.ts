// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type { GetOrderEarnings429Response, Transfer } from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getTransfer: Operation = {
  id: 'getTransfer',
  method: 'GET',
  path: '/sell/finances/v1/transfer/{transfer_Id}',
  resource: 'transfers',
  name: 'get',
  host: 'apiz',
  params: [
    { wire: 'transfer_Id', name: 'transferId', location: 'path' },
    { wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.finances'] }]],
};

export const OPERATIONS: readonly Operation[] = [getTransfer];

export class TransfersApi extends Resource {
  /** Get one transfer of funds the seller owes eBay. */
  get(transferId: string, params: { marketplaceId?: string } = {}, options?: RequestOptions): Promise<Transfer> {
    return this.call(getTransfer, undefined, { transferId, ...params }, options);
  }
}
