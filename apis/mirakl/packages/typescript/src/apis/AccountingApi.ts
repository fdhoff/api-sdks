// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  DR11Response200,
  DR12Response200,
  DR74RequestMultipartFormDataDocumentsInput,
  DR74Response200,
  DR75Request,
  DR75Response200,
  IV01Response200,
  SBC11Response200,
  TL02Response200,
  TL03Request,
  TL03Response200,
  TL04Response200,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const dR11: Operation = {
  id: 'DR11',
  method: 'GET',
  path: '/api/document-request/requests',
  resource: 'accounting',
  name: 'listDocumentRequests',
  params: [
    { wire: 'id', name: 'id', location: 'query' },
    { wire: 'document_number', name: 'documentNumber', location: 'query' },
    { wire: 'date_created_from', name: 'dateCreatedFrom', location: 'query' },
    { wire: 'date_created_to', name: 'dateCreatedTo', location: 'query' },
    { wire: 'last_updated_from', name: 'lastUpdatedFrom', location: 'query' },
    { wire: 'last_updated_to', name: 'lastUpdatedTo', location: 'query' },
    { wire: 'issue_date_from', name: 'issueDateFrom', location: 'query' },
    { wire: 'issue_date_to', name: 'issueDateTo', location: 'query' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'issuer_type', name: 'issuerType', location: 'query' },
    { wire: 'entity_id', name: 'entityId', location: 'query' },
    { wire: 'entity_type', name: 'entityType', location: 'query' },
    { wire: 'shop_billing_cycle_id', name: 'shopBillingCycleId', location: 'query' },
    { wire: 'shop_billing_cycle_from', name: 'shopBillingCycleFrom', location: 'query' },
    { wire: 'shop_billing_cycle_to', name: 'shopBillingCycleTo', location: 'query' },
    { wire: 'payment_state', name: 'paymentState', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDocumentRequests',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_REQUEST_READ',
          'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ',
        ],
      },
    ],
  ],
};

const dR12: Operation = {
  id: 'DR12',
  method: 'GET',
  path: '/api/document-request/{document_request_id}/lines',
  resource: 'accounting',
  name: 'listDocumentRequestLines',
  params: [
    { wire: 'document_request_id', name: 'documentRequestId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterDocumentRequestLines',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_REQUEST_READ',
          'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ',
        ],
      },
    ],
  ],
};

const dR73: Operation = {
  id: 'DR73',
  method: 'GET',
  path: '/api/document-request/documents/download',
  resource: 'accounting',
  name: 'downloadDocuments',
  params: [
    { wire: 'document_request_id', name: 'documentRequestId', location: 'query' },
    { wire: 'document_id', name: 'documentId', location: 'query' },
    { wire: 'document_format', name: 'documentFormat', location: 'query' },
    { wire: 'entity_id', name: 'entityId', location: 'query' },
    { wire: 'entity_type', name: 'entityType', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_READ',
          'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ',
        ],
      },
    ],
  ],
};

const dR74: Operation = {
  id: 'DR74',
  method: 'POST',
  path: '/api/document-request/documents/upload',
  resource: 'accounting',
  name: 'uploadDocuments',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'documents_input', name: 'documentsInput', location: 'form' },
    { wire: 'files', name: 'files', location: 'form' },
  ],
  returnsJson: true,
  security: [
    [{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_WRITE'] }],
  ],
};

const dR75: Operation = {
  id: 'DR75',
  method: 'POST',
  path: '/api/document-request/documents/confirm-issuance',
  resource: 'accounting',
  name: 'confirmIssuance',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [
    [{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_CUSTOMER_ACCOUNTING_DOCUMENT_WRITE'] }],
  ],
};

const iV01: Operation = {
  id: 'IV01',
  method: 'GET',
  path: '/api/invoices',
  resource: 'accounting',
  name: 'listInvoices',
  params: [
    { wire: 'currency', name: 'currency', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'invoice_id', name: 'invoiceId', location: 'query' },
    { wire: 'issuing_user_types', name: 'issuingUserTypes', location: 'query' },
    { wire: 'pay_out_psp_codes', name: 'payOutPspCodes', location: 'query' },
    { wire: 'payment_status', name: 'paymentStatus', location: 'query' },
    { wire: 'seller_billing_cycle_id', name: 'sellerBillingCycleId', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'type', name: 'type', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'max', name: 'max', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
    { wire: 'order', name: 'order', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterInvoices',
  paging: { style: 'offset', items: 'invoices', total: 'total_count', offset: 'offset' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ',
          'ROLE_PARTNER_OWN_ACCOUNTING_DOCUMENT_READ',
        ],
      },
    ],
  ],
};

const iV02: Operation = {
  id: 'IV02',
  method: 'GET',
  path: '/api/invoices/{accounting_document_id}',
  resource: 'accounting',
  name: 'downloadInvoice',
  params: [
    { wire: 'accounting_document_id', name: 'accountingDocumentId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsBinary: true,
  accept: 'application/octet-stream',
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: [
          'ROLE_SHOP_ADMIN',
          'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ',
          'ROLE_PARTNER_OWN_ACCOUNTING_DOCUMENT_READ',
        ],
      },
    ],
  ],
};

const sBC11: Operation = {
  id: 'SBC11',
  method: 'GET',
  path: '/api/seller-billing-cycles',
  resource: 'accounting',
  name: 'listBillingCycles',
  params: [
    { wire: 'currency', name: 'currency', location: 'query' },
    { wire: 'end_date', name: 'endDate', location: 'query' },
    { wire: 'id', name: 'id', location: 'query' },
    { wire: 'pay_out_psp_code', name: 'payOutPspCode', location: 'query' },
    { wire: 'pay_out_state', name: 'payOutState', location: 'query' },
    { wire: 'start_date', name: 'startDate', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterBillingCycles',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [
    [
      {
        scheme: 'Shop-API-Key',
        scopes: ['ROLE_SHOP_ADMIN', 'ROLE_PARTNER_SELLER_BILLING_CYCLE_READ', 'ROLE_PARTNER_ACCOUNTING_DOCUMENT_READ'],
      },
    ],
  ],
};

const tL02: Operation = {
  id: 'TL02',
  method: 'GET',
  path: '/api/sellerpayment/transactions_logs',
  resource: 'accounting',
  name: 'listTransactions',
  params: [
    { wire: 'seller_billing_cycle_id', name: 'sellerBillingCycleId', location: 'query' },
    { wire: 'date_created_from', name: 'dateCreatedFrom', location: 'query' },
    { wire: 'date_created_to', name: 'dateCreatedTo', location: 'query' },
    { wire: 'transaction_date_from', name: 'transactionDateFrom', location: 'query' },
    { wire: 'transaction_date_to', name: 'transactionDateTo', location: 'query' },
    { wire: 'last_updated_from', name: 'lastUpdatedFrom', location: 'query' },
    { wire: 'payment_state', name: 'paymentState', location: 'query' },
    { wire: 'transaction_type', name: 'transactionType', location: 'query' },
    { wire: 'accounting_document_number', name: 'accountingDocumentNumber', location: 'query' },
    { wire: 'order_id', name: 'orderId', location: 'query' },
    { wire: 'order_line_id', name: 'orderLineId', location: 'query' },
    { wire: 'order_reference_for_customer', name: 'orderReferenceForCustomer', location: 'query' },
    { wire: 'order_reference_for_seller', name: 'orderReferenceForSeller', location: 'query' },
    { wire: 'accounting_document_id', name: 'accountingDocumentId', location: 'query' },
    { wire: 'shop_model', name: 'shopModel', location: 'query' },
    { wire: 'pay_out_psp_codes', name: 'payOutPspCodes', location: 'query' },
    { wire: 'other_reference', name: 'otherReference', location: 'query' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'page_token', name: 'pageToken', location: 'query' },
    { wire: 'sort', name: 'sort', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterTransactions',
  paging: { style: 'cursor', items: 'data', next: 'next_page_token', param: 'page_token' },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ACCOUNTANCY', 'ROLE_PARTNER_TRANSACTION_LOG_READ'] }]],
};

const tL03: Operation = {
  id: 'TL03',
  method: 'POST',
  path: '/api/sellerpayment/transactions_logs/async',
  resource: 'accounting',
  name: 'exportTransactions',
  params: [{ wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true }],
  hasBody: true,
  returnsJson: true,
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ACCOUNTANCY', 'ROLE_PARTNER_TRANSACTION_LOG_READ'] }]],
};

const tL04: Operation = {
  id: 'TL04',
  method: 'GET',
  path: '/api/sellerpayment/transactions_logs/async/status/{tracking_id}',
  resource: 'accounting',
  name: 'getTransactionExport',
  params: [
    { wire: 'tracking_id', name: 'trackingId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'query', defaulted: true },
  ],
  returnsJson: true,
  job: { state: 'status', done: ['COMPLETED'], failed: ['FAILED', 'CANCELED'] },
  security: [[{ scheme: 'Shop-API-Key', scopes: ['ROLE_SHOP_ACCOUNTANCY', 'ROLE_PARTNER_TRANSACTION_LOG_READ'] }]],
};

export const OPERATIONS: readonly Operation[] = [dR11, dR12, dR73, dR74, dR75, iV01, iV02, sBC11, tL02, tL03, tL04];

export class AccountingApi extends Resource {
  /** List one page of accounting document requests (DR11). */
  listDocumentRequests(
    params: {
      id?: string;
      documentNumber?: string;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      issueDateFrom?: string;
      issueDateTo?: string;
      state?: Array<'STAGING' | 'TO_PROCESS' | 'ISSUED' | 'CANCELED'>;
      type?: Array<'INVOICE' | 'CREDIT_NOTE'>;
      issuerType?: Array<'OPERATOR' | 'SHOP'>;
      entityId?: Array<string>;
      entityType?: Array<
        | 'PRODUCT_LOGISTIC_ORDER'
        | 'SHOP_BILLING_CYCLE_PURCHASE_ORDER'
        | 'LOGISTIC_PURCHASE_ORDER'
        | 'FEES'
        | 'ONE_OFF_FEES'
      >;
      shopBillingCycleId?: string;
      shopBillingCycleFrom?: string;
      shopBillingCycleTo?: string;
      paymentState?: 'PAID' | 'PENDING';
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<DR11Response200> {
    return this.call(dR11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterDocumentRequests(
    params: {
      id?: string;
      documentNumber?: string;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      lastUpdatedFrom?: string;
      lastUpdatedTo?: string;
      issueDateFrom?: string;
      issueDateTo?: string;
      state?: Array<'STAGING' | 'TO_PROCESS' | 'ISSUED' | 'CANCELED'>;
      type?: Array<'INVOICE' | 'CREDIT_NOTE'>;
      issuerType?: Array<'OPERATOR' | 'SHOP'>;
      entityId?: Array<string>;
      entityType?: Array<
        | 'PRODUCT_LOGISTIC_ORDER'
        | 'SHOP_BILLING_CYCLE_PURCHASE_ORDER'
        | 'LOGISTIC_PURCHASE_ORDER'
        | 'FEES'
        | 'ONE_OFF_FEES'
      >;
      shopBillingCycleId?: string;
      shopBillingCycleFrom?: string;
      shopBillingCycleTo?: string;
      paymentState?: 'PAID' | 'PENDING';
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.DR11Response200Data, void, undefined> {
    return this.paginate(dR11, undefined, { ...params }, options);
  }

  /** List one page of a document request's lines (DR12). */
  listDocumentRequestLines(
    documentRequestId: string,
    params: { shopId?: number; limit?: number; pageToken?: string; sort?: string } = {},
    options?: RequestOptions,
  ): Promise<DR12Response200> {
    return this.call(dR12, undefined, { documentRequestId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterDocumentRequestLines(
    documentRequestId: string,
    params: { shopId?: number; limit?: number; pageToken?: string; sort?: string } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.DR12Response200Data, void, undefined> {
    return this.paginate(dR12, undefined, { documentRequestId, ...params }, options);
  }

  /** Download accounting documents (DR73). */
  downloadDocuments(
    params: {
      documentRequestId?: Array<string>;
      documentId?: Array<string>;
      documentFormat?: Array<'PDF' | 'cXML'>;
      entityId?: Array<string>;
      entityType?: Array<
        | 'PRODUCT_LOGISTIC_ORDER'
        | 'SHOP_BILLING_CYCLE_PURCHASE_ORDER'
        | 'LOGISTIC_PURCHASE_ORDER'
        | 'FEES'
        | 'ONE_OFF_FEES'
      >;
      shopId?: number;
    } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(dR73, undefined, { ...params }, options);
  }

  /** Upload accounting documents (DR74). */
  uploadDocuments(
    params: { shopId?: number; documentsInput: DR74RequestMultipartFormDataDocumentsInput; files: FileInput[] },
    options?: RequestOptions,
  ): Promise<DR74Response200> {
    return this.call(dR74, undefined, { ...params }, options);
  }

  /** Confirm that accounting documents were issued (DR75). */
  confirmIssuance(
    body?: DR75Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<DR75Response200> {
    return this.call(dR75, body, { ...params }, options);
  }

  /** List one page of accounting documents (IV01). */
  listInvoices(
    params: {
      currency?:
        | 'AED'
        | 'ARS'
        | 'AUD'
        | 'BAM'
        | 'BGN'
        | 'BHD'
        | 'BRL'
        | 'CAD'
        | 'CHF'
        | 'CLP'
        | 'CNY'
        | 'COP'
        | 'CZK'
        | 'DKK'
        | 'EGP'
        | 'EUR'
        | 'GBP'
        | 'GEL'
        | 'GTQ'
        | 'HKD'
        | 'HRK'
        | 'HUF'
        | 'IDR'
        | 'ILS'
        | 'INR'
        | 'IQD'
        | 'JOD'
        | 'JPY'
        | 'KES'
        | 'KRW'
        | 'KWD'
        | 'LKR'
        | 'MAD'
        | 'MGA'
        | 'MXN'
        | 'MYR'
        | 'NGN'
        | 'NOK'
        | 'NZD'
        | 'OMR'
        | 'PEN'
        | 'PHP'
        | 'PKR'
        | 'PLN'
        | 'QAR'
        | 'RON'
        | 'RSD'
        | 'RUB'
        | 'SAR'
        | 'SEK'
        | 'SGD'
        | 'TND'
        | 'TRY'
        | 'THB'
        | 'TWD'
        | 'UAH'
        | 'USD'
        | 'UYU'
        | 'UZS'
        | 'VND'
        | 'ZAR';
      endDate?: string;
      invoiceId?: Array<number>;
      issuingUserTypes?: Array<'OPERATOR' | 'BATCH' | 'PARTNER'>;
      payOutPspCodes?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      paymentStatus?: 'PENDING' | 'PAID' | 'FAILED';
      sellerBillingCycleId?: Array<string>;
      startDate?: string;
      type?: 'ALL' | 'AUTO_INVOICE' | 'MANUAL_INVOICE' | 'MANUAL_CREDIT';
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): Promise<IV01Response200> {
    return this.call(iV01, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterInvoices(
    params: {
      currency?:
        | 'AED'
        | 'ARS'
        | 'AUD'
        | 'BAM'
        | 'BGN'
        | 'BHD'
        | 'BRL'
        | 'CAD'
        | 'CHF'
        | 'CLP'
        | 'CNY'
        | 'COP'
        | 'CZK'
        | 'DKK'
        | 'EGP'
        | 'EUR'
        | 'GBP'
        | 'GEL'
        | 'GTQ'
        | 'HKD'
        | 'HRK'
        | 'HUF'
        | 'IDR'
        | 'ILS'
        | 'INR'
        | 'IQD'
        | 'JOD'
        | 'JPY'
        | 'KES'
        | 'KRW'
        | 'KWD'
        | 'LKR'
        | 'MAD'
        | 'MGA'
        | 'MXN'
        | 'MYR'
        | 'NGN'
        | 'NOK'
        | 'NZD'
        | 'OMR'
        | 'PEN'
        | 'PHP'
        | 'PKR'
        | 'PLN'
        | 'QAR'
        | 'RON'
        | 'RSD'
        | 'RUB'
        | 'SAR'
        | 'SEK'
        | 'SGD'
        | 'TND'
        | 'TRY'
        | 'THB'
        | 'TWD'
        | 'UAH'
        | 'USD'
        | 'UYU'
        | 'UZS'
        | 'VND'
        | 'ZAR';
      endDate?: string;
      invoiceId?: Array<number>;
      issuingUserTypes?: Array<'OPERATOR' | 'BATCH' | 'PARTNER'>;
      payOutPspCodes?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      paymentStatus?: 'PENDING' | 'PAID' | 'FAILED';
      sellerBillingCycleId?: Array<string>;
      startDate?: string;
      type?: 'ALL' | 'AUTO_INVOICE' | 'MANUAL_INVOICE' | 'MANUAL_CREDIT';
      shopId?: number;
      max?: number;
      offset?: number;
      sort?: string;
      order?: 'asc' | 'desc';
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.IV01Response200Invoices, void, undefined> {
    return this.paginate(iV01, undefined, { ...params }, options);
  }

  /** Download an accounting document (IV02). */
  downloadInvoice(
    accountingDocumentId: number,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<import('../runtime/index.js').Download> {
    return this.call(iV02, undefined, { accountingDocumentId, ...params }, options);
  }

  /** List one page of seller billing cycles (SBC11). */
  listBillingCycles(
    params: {
      currency?: Array<
        | 'AED'
        | 'ARS'
        | 'AUD'
        | 'BAM'
        | 'BGN'
        | 'BHD'
        | 'BRL'
        | 'CAD'
        | 'CHF'
        | 'CLP'
        | 'CNY'
        | 'COP'
        | 'CZK'
        | 'DKK'
        | 'EGP'
        | 'EUR'
        | 'GBP'
        | 'GEL'
        | 'GTQ'
        | 'HKD'
        | 'HRK'
        | 'HUF'
        | 'IDR'
        | 'ILS'
        | 'INR'
        | 'IQD'
        | 'JOD'
        | 'JPY'
        | 'KES'
        | 'KRW'
        | 'KWD'
        | 'LKR'
        | 'MAD'
        | 'MGA'
        | 'MXN'
        | 'MYR'
        | 'NGN'
        | 'NOK'
        | 'NZD'
        | 'OMR'
        | 'PEN'
        | 'PHP'
        | 'PKR'
        | 'PLN'
        | 'QAR'
        | 'RON'
        | 'RSD'
        | 'RUB'
        | 'SAR'
        | 'SEK'
        | 'SGD'
        | 'TND'
        | 'TRY'
        | 'THB'
        | 'TWD'
        | 'UAH'
        | 'USD'
        | 'UYU'
        | 'UZS'
        | 'VND'
        | 'ZAR'
      >;
      endDate?: string;
      id?: Array<string>;
      payOutPspCode?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      payOutState?: Array<'TO_PAY' | 'PAID' | 'FAILED'>;
      startDate?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<SBC11Response200> {
    return this.call(sBC11, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterBillingCycles(
    params: {
      currency?: Array<
        | 'AED'
        | 'ARS'
        | 'AUD'
        | 'BAM'
        | 'BGN'
        | 'BHD'
        | 'BRL'
        | 'CAD'
        | 'CHF'
        | 'CLP'
        | 'CNY'
        | 'COP'
        | 'CZK'
        | 'DKK'
        | 'EGP'
        | 'EUR'
        | 'GBP'
        | 'GEL'
        | 'GTQ'
        | 'HKD'
        | 'HRK'
        | 'HUF'
        | 'IDR'
        | 'ILS'
        | 'INR'
        | 'IQD'
        | 'JOD'
        | 'JPY'
        | 'KES'
        | 'KRW'
        | 'KWD'
        | 'LKR'
        | 'MAD'
        | 'MGA'
        | 'MXN'
        | 'MYR'
        | 'NGN'
        | 'NOK'
        | 'NZD'
        | 'OMR'
        | 'PEN'
        | 'PHP'
        | 'PKR'
        | 'PLN'
        | 'QAR'
        | 'RON'
        | 'RSD'
        | 'RUB'
        | 'SAR'
        | 'SEK'
        | 'SGD'
        | 'TND'
        | 'TRY'
        | 'THB'
        | 'TWD'
        | 'UAH'
        | 'USD'
        | 'UYU'
        | 'UZS'
        | 'VND'
        | 'ZAR'
      >;
      endDate?: string;
      id?: Array<string>;
      payOutPspCode?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      payOutState?: Array<'TO_PAY' | 'PAID' | 'FAILED'>;
      startDate?: string;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.SBC11Response200Data, void, undefined> {
    return this.paginate(sBC11, undefined, { ...params }, options);
  }

  /** List one page of transaction lines (TL02). */
  listTransactions(
    params: {
      sellerBillingCycleId?: Array<string>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      transactionDateFrom?: string;
      transactionDateTo?: string;
      lastUpdatedFrom?: string;
      paymentState?: Array<'PENDING' | 'PAYABLE' | 'PAID' | 'NOT_APPLICABLE' | 'RESERVE'>;
      transactionType?: Array<
        | 'MANUAL_CREDIT'
        | 'MANUAL_CREDIT_VAT'
        | 'MANUAL_INVOICE'
        | 'MANUAL_INVOICE_VAT'
        | 'INVOICEABLE_ONE_OFF_DEBIT'
        | 'INVOICEABLE_ONE_OFF_DEBIT_TAX'
        | 'INVOICEABLE_ONE_OFF_CREDIT'
        | 'INVOICEABLE_ONE_OFF_CREDIT_TAX'
        | 'INVOICEABLE_MIRAKL_ADS_DEBIT'
        | 'INVOICEABLE_MIRAKL_ADS_DEBIT_TAX'
        | 'INVOICEABLE_MIRAKL_ADS_CREDIT'
        | 'INVOICEABLE_MIRAKL_ADS_CREDIT_TAX'
        | 'ORDER_AMOUNT'
        | 'ORDER_AMOUNT_TAX'
        | 'ORDER_SHIPPING_AMOUNT'
        | 'ORDER_SHIPPING_AMOUNT_TAX'
        | 'COMMISSION_FEE'
        | 'COMMISSION_VAT'
        | 'REFUND_ORDER_AMOUNT'
        | 'REFUND_ORDER_AMOUNT_TAX'
        | 'REFUND_ORDER_SHIPPING_AMOUNT'
        | 'REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'REFUND_COMMISSION_FEE'
        | 'REFUND_COMMISSION_VAT'
        | 'SUBSCRIPTION_FEE'
        | 'SUBSCRIPTION_VAT'
        | 'OPERATOR_REMITTED_ORDER_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_REFUND_ORDER_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_PAID_ORDER_SHIPPING_AMOUNT'
        | 'OPERATOR_PAID_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_PAID_REFUND_ORDER_SHIPPING_AMOUNT'
        | 'OPERATOR_PAID_REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'PAYMENT'
        | 'PURCHASE_COMMISSION_FEE'
        | 'PURCHASE_SHIPPING_COMMISSION_FEE'
        | 'PURCHASE_ORDER_AMOUNT_TAX'
        | 'PURCHASE_ORDER_SHIPPING_AMOUNT_TAX'
        | 'REFUND_PURCHASE_COMMISSION_FEE'
        | 'REFUND_PURCHASE_SHIPPING_COMMISSION_FEE'
        | 'REFUND_PURCHASE_ORDER_AMOUNT_TAX'
        | 'REFUND_PURCHASE_ORDER_SHIPPING_AMOUNT_TAX'
        | 'ORDER_FEE_AMOUNT'
        | 'OPERATOR_REMITTED_ORDER_FEE_AMOUNT'
        | 'REFUND_ORDER_FEE_AMOUNT'
        | 'OPERATOR_REMITTED_REFUND_ORDER_FEE_AMOUNT'
        | 'PURCHASE_FEE_COMMISSION_FEE'
        | 'REFUND_PURCHASE_FEE_COMMISSION_FEE'
        | 'RESERVE_FUNDING'
        | 'RESERVE_SETTLEMENT'
        | 'SELLER_FEE_ON_ORDER'
        | 'SELLER_FEE_ON_ORDER_TAX'
        | 'SELLER_PENALTY_FEE'
        | 'SELLER_PENALTY_FEE_TAX'
      >;
      accountingDocumentNumber?: string;
      orderId?: Array<string>;
      orderLineId?: Array<string>;
      orderReferenceForCustomer?: Array<string>;
      orderReferenceForSeller?: Array<string>;
      accountingDocumentId?: string;
      shopModel?: Array<'MARKETPLACE' | 'DROPSHIP' | 'ONE_CREDITOR'>;
      payOutPspCodes?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      otherReference?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<TL02Response200> {
    return this.call(tL02, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterTransactions(
    params: {
      sellerBillingCycleId?: Array<string>;
      dateCreatedFrom?: string;
      dateCreatedTo?: string;
      transactionDateFrom?: string;
      transactionDateTo?: string;
      lastUpdatedFrom?: string;
      paymentState?: Array<'PENDING' | 'PAYABLE' | 'PAID' | 'NOT_APPLICABLE' | 'RESERVE'>;
      transactionType?: Array<
        | 'MANUAL_CREDIT'
        | 'MANUAL_CREDIT_VAT'
        | 'MANUAL_INVOICE'
        | 'MANUAL_INVOICE_VAT'
        | 'INVOICEABLE_ONE_OFF_DEBIT'
        | 'INVOICEABLE_ONE_OFF_DEBIT_TAX'
        | 'INVOICEABLE_ONE_OFF_CREDIT'
        | 'INVOICEABLE_ONE_OFF_CREDIT_TAX'
        | 'INVOICEABLE_MIRAKL_ADS_DEBIT'
        | 'INVOICEABLE_MIRAKL_ADS_DEBIT_TAX'
        | 'INVOICEABLE_MIRAKL_ADS_CREDIT'
        | 'INVOICEABLE_MIRAKL_ADS_CREDIT_TAX'
        | 'ORDER_AMOUNT'
        | 'ORDER_AMOUNT_TAX'
        | 'ORDER_SHIPPING_AMOUNT'
        | 'ORDER_SHIPPING_AMOUNT_TAX'
        | 'COMMISSION_FEE'
        | 'COMMISSION_VAT'
        | 'REFUND_ORDER_AMOUNT'
        | 'REFUND_ORDER_AMOUNT_TAX'
        | 'REFUND_ORDER_SHIPPING_AMOUNT'
        | 'REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'REFUND_COMMISSION_FEE'
        | 'REFUND_COMMISSION_VAT'
        | 'SUBSCRIPTION_FEE'
        | 'SUBSCRIPTION_VAT'
        | 'OPERATOR_REMITTED_ORDER_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_REFUND_ORDER_AMOUNT_TAX'
        | 'OPERATOR_REMITTED_REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_PAID_ORDER_SHIPPING_AMOUNT'
        | 'OPERATOR_PAID_ORDER_SHIPPING_AMOUNT_TAX'
        | 'OPERATOR_PAID_REFUND_ORDER_SHIPPING_AMOUNT'
        | 'OPERATOR_PAID_REFUND_ORDER_SHIPPING_AMOUNT_TAX'
        | 'PAYMENT'
        | 'PURCHASE_COMMISSION_FEE'
        | 'PURCHASE_SHIPPING_COMMISSION_FEE'
        | 'PURCHASE_ORDER_AMOUNT_TAX'
        | 'PURCHASE_ORDER_SHIPPING_AMOUNT_TAX'
        | 'REFUND_PURCHASE_COMMISSION_FEE'
        | 'REFUND_PURCHASE_SHIPPING_COMMISSION_FEE'
        | 'REFUND_PURCHASE_ORDER_AMOUNT_TAX'
        | 'REFUND_PURCHASE_ORDER_SHIPPING_AMOUNT_TAX'
        | 'ORDER_FEE_AMOUNT'
        | 'OPERATOR_REMITTED_ORDER_FEE_AMOUNT'
        | 'REFUND_ORDER_FEE_AMOUNT'
        | 'OPERATOR_REMITTED_REFUND_ORDER_FEE_AMOUNT'
        | 'PURCHASE_FEE_COMMISSION_FEE'
        | 'REFUND_PURCHASE_FEE_COMMISSION_FEE'
        | 'RESERVE_FUNDING'
        | 'RESERVE_SETTLEMENT'
        | 'SELLER_FEE_ON_ORDER'
        | 'SELLER_FEE_ON_ORDER_TAX'
        | 'SELLER_PENALTY_FEE'
        | 'SELLER_PENALTY_FEE_TAX'
      >;
      accountingDocumentNumber?: string;
      orderId?: Array<string>;
      orderLineId?: Array<string>;
      orderReferenceForCustomer?: Array<string>;
      orderReferenceForSeller?: Array<string>;
      accountingDocumentId?: string;
      shopModel?: Array<'MARKETPLACE' | 'DROPSHIP' | 'ONE_CREDITOR'>;
      payOutPspCodes?: Array<'NOT_SPECIFIED' | 'MANGOPAY' | 'MIRAKL_PAYOUT' | 'OPERATOR'>;
      otherReference?: Array<string>;
      shopId?: number;
      limit?: number;
      pageToken?: string;
      sort?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.TL02Response200Data, void, undefined> {
    return this.paginate(tL02, undefined, { ...params }, options);
  }

  /** Start an export of transaction lines as JSON files (TL03). */
  exportTransactions(
    body?: TL03Request,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<TL03Response200> {
    return this.call(tL03, body, { ...params }, options);
  }

  /** Get the status of a transaction line export (TL04). */
  getTransactionExport(
    trackingId: string,
    params: { shopId?: number } = {},
    options?: RequestOptions,
  ): Promise<TL04Response200> {
    return this.call(tL04, undefined, { trackingId, ...params }, options);
  }

  /** Poll every `intervalMs` until the job that `exportTransactions` started ends, and return its last status, done or
   * failed. Pass the `tracking_id` it returned. Throws `JobTimeoutError` once `timeoutMs` pass, and stops when `signal`
   * aborts. */
  waitForTransactionExport(
    trackingId: string,
    options?: import('../runtime/index.js').WaitOptions,
  ): Promise<TL04Response200> {
    return this.pollJob(tL04, { trackingId }, options);
  }
}
