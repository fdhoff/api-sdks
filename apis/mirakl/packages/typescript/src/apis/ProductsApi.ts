// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  H11Response200,
  P31Response200,
  P41RequestMultipartFormDataConversionOptions,
  P41Response201,
  P42Response200,
  P51Response200,
  PM11Response200,
  PM11Response200TextCsvExtFileStructure,
  VL11Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const h11: Operation = {
  id: 'H11',
  method: 'GET',
  path: '/api/hierarchies',
  resource: 'products',
  name: 'listCategories',
  params: [
    { wire: 'hierarchy', name: 'hierarchy', location: 'query' },
    { wire: 'max_level', name: 'maxLevel', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_CONFIGURATION_READ'] }]],
};

const p31: Operation = {
  id: 'P31',
  method: 'GET',
  path: '/api/products',
  resource: 'products',
  name: 'list',
  params: [
    { wire: 'product_references', name: 'productReferences', location: 'query' },
    { wire: 'products', name: 'products', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_READ'] }]],
};

const p41: Operation = {
  id: 'P41',
  method: 'POST',
  path: '/api/products/imports',
  resource: 'products',
  name: 'import',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'conversion_options', name: 'conversionOptions', location: 'form' },
    { wire: 'conversion_type', name: 'conversionType', location: 'form' },
    { wire: 'file', name: 'file', location: 'form' },
    { wire: 'operator_format', name: 'operatorFormat', location: 'form' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p42: Operation = {
  id: 'P42',
  method: 'GET',
  path: '/api/products/imports/{import}',
  resource: 'products',
  name: 'getImport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'import_status', done: ['COMPLETE'], failed: ['TRANSFORMATION_FAILED', 'CANCELLED', 'FAILED'] },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p44: Operation = {
  id: 'P44',
  method: 'GET',
  path: '/api/products/imports/{import}/error_report',
  resource: 'products',
  name: 'downloadErrorReport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p45: Operation = {
  id: 'P45',
  method: 'GET',
  path: '/api/products/imports/{import}/new_product_report',
  resource: 'products',
  name: 'downloadNewProductReport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p46: Operation = {
  id: 'P46',
  method: 'GET',
  path: '/api/products/imports/{import}/transformed_file',
  resource: 'products',
  name: 'downloadTransformedFile',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'text/csv',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p47: Operation = {
  id: 'P47',
  method: 'GET',
  path: '/api/products/imports/{import}/transformation_error_report',
  resource: 'products',
  name: 'downloadTransformationErrorReport',
  params: [
    { wire: 'import', name: 'importId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const p51: Operation = {
  id: 'P51',
  method: 'GET',
  path: '/api/products/imports',
  resource: 'products',
  name: 'listImports',
  params: [
    { wire: 'last_request_date', name: 'lastRequestDate', location: 'query' },
    { wire: 'status', name: 'status', location: 'query' },
    { wire: 'has_transformed_file', name: 'hasTransformedFile', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterImports',
  paging: { style: 'offset', items: 'product_import_trackings', total: 'total_count', offset: 'offset' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_WRITE'] }]],
};

const pM11: Operation = {
  id: 'PM11',
  method: 'GET',
  path: '/api/products/attributes',
  resource: 'products',
  name: 'listAttributes',
  params: [
    { wire: 'hierarchy', name: 'hierarchy', location: 'query' },
    { wire: 'max_level', name: 'maxLevel', location: 'query' },
    { wire: 'all_operator_attributes', name: 'allOperatorAttributes', location: 'query' },
    { wire: 'with_roles', name: 'withRoles', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_CONFIGURATION_READ'] }]],
};

const vL11: Operation = {
  id: 'VL11',
  method: 'GET',
  path: '/api/values_lists',
  resource: 'products',
  name: 'listValueLists',
  params: [
    { wire: 'code', name: 'code', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_PRODUCT_CONFIGURATION_READ'] }]],
};

export const OPERATIONS: readonly Operation[] = [h11, p31, p41, p42, p44, p45, p46, p47, p51, pM11, vL11];

export class ProductsApi extends Resource {
  /** List catalog categories and their parents and children (H11). */
  listCategories(
    params: { hierarchy?: string; maxLevel?: number; shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<H11Response200> {
    return this.call(h11, undefined, { ...params }, options);
  }

  /** Get products by their references (P31). */
  list(
    params: { productReferences: string; products?: string; shopId?: number },
    options?: RequestOptions,
  ): Promise<P31Response200> {
    return this.call(p31, undefined, { ...params }, options);
  }

  /** Import a product file into the operator's catalog (P41). */
  import(
    params: {
      shopId?: number;
      conversionOptions?: P41RequestMultipartFormDataConversionOptions;
      conversionType?: string;
      file: FileInput;
      operatorFormat?: boolean;
    },
    options?: RequestOptions,
  ): Promise<P41Response201> {
    return this.call(p41, undefined, { ...params }, options);
  }

  /** Get the status of a product import (P42). */
  getImport(importId: number, params: { shopId?: number } = {}, options?: RequestOptions): Promise<P42Response200> {
    return this.call(p42, undefined, { importId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `import` started ends, and return its last status, done or
   * failed. Pass the `import_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForImport(importId: number, options?: import('../runtime/index.js').WaitOptions): Promise<P42Response200> {
    return this.pollJob(p42, { importId }, options);
  }

  /** Download the report of a product import's rejected products (P44). */
  downloadErrorReport(
    importId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(p44, undefined, { importId, ...params }, options);
  }

  /** Download the report of a product import's added products (P45). */
  downloadNewProductReport(
    importId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(p45, undefined, { importId, ...params }, options);
  }

  /** Download a product import's file in the operator's format (P46). */
  downloadTransformedFile(
    importId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(p46, undefined, { importId, ...params }, options);
  }

  /** Download a product import's transformation error report (P47). */
  downloadTransformationErrorReport(
    importId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(p47, undefined, { importId, ...params }, options);
  }

  /** List one page of product imports (P51). */
  listImports(
    params: {
      lastRequestDate?: string;
      status?: string;
      hasTransformedFile?: boolean;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<P51Response200> {
    return this.call(p51, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterImports(
    params: {
      lastRequestDate?: string;
      status?: string;
      hasTransformedFile?: boolean;
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.P51Response200ProductImportTrackings, void, undefined> {
    return this.paginate(p51, undefined, { ...params }, options);
  }

  /** Get the product attribute configuration (PM11). */
  listAttributes(
    params: {
      hierarchy?: string;
      maxLevel?: number;
      allOperatorAttributes?: boolean;
      withRoles?: boolean;
      shopId?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<PM11Response200> {
    return this.call(pM11, undefined, { ...params }, options);
  }

  /** Get the operator's value lists (VL11). */
  listValueLists(params: { code?: string; shopId?: number } = {}, options?: RequestOptions): Promise<VL11Response200> {
    return this.call(vL11, undefined, { ...params }, options);
  }
}
