// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  OF01Response201,
  OF02Response200,
  OF04Response200,
  OF21Response200,
  OF22Response200,
  OF24Request,
  OF24Response201,
  OF52Request,
  OF52Response200,
  OF53Response200,
  P11Response200,
  PRI01Response201,
  PRI02Response200,
  STO01Response201,
  STO02Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const oF01: Operation = {
  id: 'OF01',
  method: 'POST',
  path: '/api/offers/imports',
  resource: 'offers',
  name: 'import',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'file', name: 'file', location: 'form' },
    { wire: 'import_mode', name: 'importMode', location: 'form' },
    { wire: 'operator_format', name: 'operatorFormat', location: 'form' },
    { wire: 'with_products', name: 'withProducts', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_WRITE'] }]],
};

const oF02: Operation = {
  id: 'OF02',
  method: 'GET',
  path: '/api/offers/imports/{import}',
  resource: 'offers',
  name: 'getImport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'status', done: ['COMPLETE'], failed: ['FAILED'] },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_WRITE', 'ROLE_PARTNER_OFFER_TRACKING_READ'],
      },
    ],
  ],
};

const oF03: Operation = {
  id: 'OF03',
  method: 'GET',
  path: '/api/offers/imports/{import}/error_report',
  resource: 'offers',
  name: 'downloadImportErrorReport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_WRITE', 'ROLE_PARTNER_OFFER_TRACKING_READ'],
      },
    ],
  ],
};

const oF04: Operation = {
  id: 'OF04',
  method: 'GET',
  path: '/api/offers/imports',
  resource: 'offers',
  name: 'listImports',
  params: [
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'mode', name: 'mode', location: 'query' },
    { wire: 'origins', name: 'origins', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterImports',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_WRITE', 'ROLE_PARTNER_OFFER_TRACKING_READ'],
      },
    ],
  ],
};

const oF21: Operation = {
  id: 'OF21',
  method: 'GET',
  path: '/api/offers',
  resource: 'offers',
  name: 'list',
  params: [
    { wire: 'offer_state_codes', name: 'offerStateCodes', location: 'query' },
    { wire: 'sku', name: 'sku', location: 'query' },
    { wire: 'product_id', name: 'productId', location: 'query' },
    { wire: 'favorite', name: 'favorite', location: 'query' },
    { wire: 'pricing_channel_code', name: 'pricingChannelCode', location: 'query' },
    { wire: 'pricing_customer_organization_id', name: 'pricingCustomerOrganizationId', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iter',
  paging: { style: 'offset', items: 'offers', total: 'total_count', offset: 'offset' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_READ'] }]],
};

const oF22: Operation = {
  id: 'OF22',
  method: 'GET',
  path: '/api/offers/{offer}',
  resource: 'offers',
  name: 'get',
  params: [
    { wire: 'offer', name: 'offer', location: 'path' },
    { wire: 'pricing_channel_code', name: 'pricingChannelCode', location: 'query' },
    { wire: 'pricing_customer_organization_id', name: 'pricingCustomerOrganizationId', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_READ'] }]],
};

const oF24: Operation = {
  id: 'OF24',
  method: 'POST',
  path: '/api/offers',
  resource: 'offers',
  name: 'update',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_WRITE'] }]],
};

const oF52: Operation = {
  id: 'OF52',
  method: 'POST',
  path: '/api/offers/export/async',
  resource: 'offers',
  name: 'export',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_OFFER_READ', 'ROLE_SHOP_ADMIN'] }]],
};

const oF53: Operation = {
  id: 'OF53',
  method: 'GET',
  path: '/api/offers/export/async/status/{tracking_id}',
  resource: 'offers',
  name: 'getExport',
  params: [
    { wire: 'tracking_id', name: 'trackingId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'status', done: ['COMPLETED'], failed: ['FAILED'] },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_PARTNER_OFFER_READ', 'ROLE_SHOP_ADMIN'] }]],
};

const p11: Operation = {
  id: 'P11',
  method: 'GET',
  path: '/api/products/offers',
  resource: 'offers',
  name: 'listForProducts',
  params: [
    { wire: 'product_ids', name: 'productIds', location: 'query' },
    { wire: 'product_references', name: 'productReferences', location: 'query' },
    { wire: 'offer_state_codes', name: 'offerStateCodes', location: 'query' },
    { wire: 'all_offers', name: 'allOffers', location: 'query' },
    { wire: 'channel_codes', name: 'channelCodes', location: 'query' },
    { wire: 'all_channels', name: 'allChannels', location: 'query' },
    { wire: 'pricing_channel_code', name: 'pricingChannelCode', location: 'query' },
    { wire: 'pricing_customer_organization_id', name: 'pricingCustomerOrganizationId', location: 'query' },
    { wire: 'shipping_zones', name: 'shippingZones', location: 'query' },
    { wire: 'all_shipping_zones', name: 'allShippingZones', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterForProducts',
  paging: { style: 'offset', items: 'products', total: 'total_count', offset: 'offset' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_READ'] }]],
};

const pRI01: Operation = {
  id: 'PRI01',
  method: 'POST',
  path: '/api/offers/pricing/imports',
  resource: 'offers',
  name: 'importPrices',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_PRICING_WRITE'] }]],
};

const pRI02: Operation = {
  id: 'PRI02',
  method: 'GET',
  path: '/api/offers/pricing/imports',
  resource: 'offers',
  name: 'listPriceImports',
  params: [
    { wire: 'import_id', name: 'importId', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'origins', name: 'origins', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterPriceImports',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_PRICING_READ'] }]],
};

const pRI03: Operation = {
  id: 'PRI03',
  method: 'GET',
  path: '/api/offers/pricing/imports/{import_id}/error_report',
  resource: 'offers',
  name: 'downloadPriceImportErrorReport',
  params: [
    { wire: 'import_id', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'text/csv',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_PRICING_READ'] }]],
};

const sTO01: Operation = {
  id: 'STO01',
  method: 'POST',
  path: '/api/offers/stock/imports',
  resource: 'offers',
  name: 'importStock',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'file', name: 'file', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_STOCK_WRITE'] }]],
};

const sTO02: Operation = {
  id: 'STO02',
  method: 'GET',
  path: '/api/offers/stock/imports/{import_id}/status',
  resource: 'offers',
  name: 'getStockImport',
  params: [
    { wire: 'import_id', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'status', done: ['COMPLETE'], failed: ['FAILED'] },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_STOCK_WRITE'] }]],
};

const sTO03: Operation = {
  id: 'STO03',
  method: 'GET',
  path: '/api/offers/stock/imports/{import_id}/error_report',
  resource: 'offers',
  name: 'downloadStockImportErrorReport',
  params: [
    { wire: 'import_id', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'text/csv',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_OFFER_STOCK_WRITE'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  oF01,
  oF02,
  oF03,
  oF04,
  oF21,
  oF22,
  oF24,
  oF52,
  oF53,
  p11,
  pRI01,
  pRI02,
  pRI03,
  sTO01,
  sTO02,
  sTO03,
];

export class OffersApi extends Resource {
  /** Import a file that creates, updates or deletes offers (OF01). */
  import(
    params: { shopId?: number; file: FileInput; importMode: string; operatorFormat?: boolean; withProducts?: boolean },
    options?: RequestOptions,
  ): Promise<OF01Response201> {
    return this.call(oF01, undefined, { ...params }, options);
  }

  /** Get the status and statistics of an offer import (OF02). */
  getImport(importId: number, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OF02Response200> {
    return this.call(oF02, undefined, { importId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `import` started ends, and return its last status, done or
   * failed. Pass the `import_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForImport(importId: number, options?: import('../runtime/index.js').WaitOptions): Promise<OF02Response200> {
    return this.pollJob(oF02, { importId }, options);
  }

  /** Download an offer import's error report (OF03). */
  downloadImportErrorReport(
    importId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(oF03, undefined, { importId, ...params }, options);
  }

  /** List one page of offer imports (OF04). */
  listImports(
    params: {
      startDate?: string;
      endDate?: string;
      status?: 'WAITING_SYNCHRONIZATION_PRODUCT' | 'WAITING' | 'RUNNING' | 'COMPLETE' | 'FAILED';
      mode?: 'NORMAL' | 'REPLACE';
      origins?: Array<'API' | 'FTP' | 'SFTP' | 'HTTP' | 'HTTPS' | 'FRONT' | 'PENDING_OFFERS'>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<OF04Response200> {
    return this.call(oF04, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterImports(
    params: {
      startDate?: string;
      endDate?: string;
      status?: 'WAITING_SYNCHRONIZATION_PRODUCT' | 'WAITING' | 'RUNNING' | 'COMPLETE' | 'FAILED';
      mode?: 'NORMAL' | 'REPLACE';
      origins?: Array<'API' | 'FTP' | 'SFTP' | 'HTTP' | 'HTTPS' | 'FRONT' | 'PENDING_OFFERS'>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OF04Response200Data, void, undefined> {
    return this.paginate(oF04, undefined, { ...params }, options);
  }

  /** List one page of your shop's offers (OF21). */
  list(
    params: {
      offerStateCodes?: string;
      sku?: string;
      productId?: string;
      favorite?: boolean;
      pricingChannelCode?: string;
      pricingCustomerOrganizationId?: string;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<OF21Response200> {
    return this.call(oF21, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iter(
    params: {
      offerStateCodes?: string;
      sku?: string;
      productId?: string;
      favorite?: boolean;
      pricingChannelCode?: string;
      pricingCustomerOrganizationId?: string;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.OF21Response200Offers, void, undefined> {
    return this.paginate(oF21, undefined, { ...params }, options);
  }

  /** Get one offer (OF22). */
  get(
    offer: number,
    params: { pricingChannelCode?: string; pricingCustomerOrganizationId?: string; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<OF22Response200> {
    return this.call(oF22, undefined, { offer, ...params }, options);
  }

  /** Create, update or delete offers (OF24). */
  update(body?: OF24Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OF24Response201> {
    return this.call(oF24, body, { ...params }, options);
  }

  /** Start an export of offers as CSV or JSON files (OF52). */
  export(body?: OF52Request, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OF52Response200> {
    return this.call(oF52, body, { ...params }, options);
  }

  /** Get the status of an offer export (OF53). */
  getExport(trackingId: string, params: { shopId?: number } = {}, options?: RequestOptions): Promise<OF53Response200> {
    return this.call(oF53, undefined, { trackingId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `export` started ends, and return its last status, done or
   * failed. Pass the `tracking_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForExport(trackingId: string, options?: import('../runtime/index.js').WaitOptions): Promise<OF53Response200> {
    return this.pollJob(oF53, { trackingId }, options);
  }

  /** List one page of the offers on each given product (P11). */
  listForProducts(
    params: {
      productIds?: string;
      productReferences?: string;
      offerStateCodes?: string;
      allOffers?: boolean;
      channelCodes?: string;
      allChannels?: boolean;
      pricingChannelCode?: string;
      pricingCustomerOrganizationId?: string;
      shippingZones?: string;
      allShippingZones?: boolean;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<P11Response200> {
    return this.call(p11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterForProducts(
    params: {
      productIds?: string;
      productReferences?: string;
      offerStateCodes?: string;
      allOffers?: boolean;
      channelCodes?: string;
      allChannels?: boolean;
      pricingChannelCode?: string;
      pricingCustomerOrganizationId?: string;
      shippingZones?: string;
      allShippingZones?: boolean;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.P11Response200Products, void, undefined> {
    return this.paginate(p11, undefined, { ...params }, options);
  }

  /** Import a price file (PRI01). */
  importPrices(params: { shopId?: number; file: FileInput }, options?: RequestOptions): Promise<PRI01Response201> {
    return this.call(pRI01, undefined, { ...params }, options);
  }

  /** List one page of price imports (PRI02). */
  listPriceImports(
    params: {
      importId?: Array<string>;
      startDate?: string;
      endDate?: string;
      status?: 'WAITING' | 'RUNNING' | 'COMPLETE' | 'FAILED';
      origins?: Array<'API' | 'FTP' | 'SFTP' | 'HTTP' | 'HTTPS' | 'FRONT' | 'PENDING_OFFERS'>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<PRI02Response200> {
    return this.call(pRI02, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterPriceImports(
    params: {
      importId?: Array<string>;
      startDate?: string;
      endDate?: string;
      status?: 'WAITING' | 'RUNNING' | 'COMPLETE' | 'FAILED';
      origins?: Array<'API' | 'FTP' | 'SFTP' | 'HTTP' | 'HTTPS' | 'FRONT' | 'PENDING_OFFERS'>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.PRI02Response200Data, void, undefined> {
    return this.paginate(pRI02, undefined, { ...params }, options);
  }

  /** Download a price import's error report as CSV (PRI03). */
  downloadPriceImportErrorReport(
    importId: string,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(pRI03, undefined, { importId, ...params }, options);
  }

  /** Import a stock file (STO01). */
  importStock(params: { shopId?: number; file: FileInput }, options?: RequestOptions): Promise<STO01Response201> {
    return this.call(sTO01, undefined, { ...params }, options);
  }

  /** Get the status and statistics of a stock import (STO02). */
  getStockImport(
    importId: string,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<STO02Response200> {
    return this.call(sTO02, undefined, { importId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `importStock` started ends, and return its last status, done or
   * failed. Pass the `import_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForStockImport(importId: string, options?: import('../runtime/index.js').WaitOptions): Promise<STO02Response200> {
    return this.pollJob(sTO02, { importId }, options);
  }

  /** Download a stock import's error report as CSV (STO03). */
  downloadStockImportErrorReport(
    importId: string,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(sTO03, undefined, { importId, ...params }, options);
  }
}
