// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  ErrorSchema,
  ShopListing,
  ShopListingWithAssociations,
  ShopListings,
  ShopListingsWithAssociations,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../runtime/index.js';

const createDraftListing: Operation = {
  id: 'createDraftListing',
  method: 'POST',
  path: '/v3/application/shops/{shop_id}/listings',
  resource: 'listings',
  name: 'createDraft',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'quantity', name: 'quantity', location: 'urlencoded' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'description', name: 'description', location: 'urlencoded' },
    { wire: 'price', name: 'price', location: 'urlencoded' },
    { wire: 'who_made', name: 'whoMade', location: 'urlencoded' },
    { wire: 'when_made', name: 'whenMade', location: 'urlencoded' },
    { wire: 'taxonomy_id', name: 'taxonomyId', location: 'urlencoded' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'urlencoded' },
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'urlencoded' },
    { wire: 'materials', name: 'materials', location: 'urlencoded' },
    { wire: 'shop_section_id', name: 'shopSectionId', location: 'urlencoded' },
    { wire: 'processing_min', name: 'processingMin', location: 'urlencoded' },
    { wire: 'processing_max', name: 'processingMax', location: 'urlencoded' },
    { wire: 'readiness_state_id', name: 'readinessStateId', location: 'urlencoded' },
    { wire: 'tags', name: 'tags', location: 'urlencoded' },
    { wire: 'styles', name: 'styles', location: 'urlencoded' },
    { wire: 'item_weight', name: 'itemWeight', location: 'urlencoded' },
    { wire: 'item_length', name: 'itemLength', location: 'urlencoded' },
    { wire: 'item_width', name: 'itemWidth', location: 'urlencoded' },
    { wire: 'item_height', name: 'itemHeight', location: 'urlencoded' },
    { wire: 'item_weight_unit', name: 'itemWeightUnit', location: 'urlencoded' },
    { wire: 'item_dimensions_unit', name: 'itemDimensionsUnit', location: 'urlencoded' },
    { wire: 'production_partner_ids', name: 'productionPartnerIds', location: 'urlencoded' },
    { wire: 'image_ids', name: 'imageIds', location: 'urlencoded' },
    { wire: 'ecgt_garan_brand', name: 'ecgtGaranBrand', location: 'urlencoded' },
    { wire: 'ecgt_garan_years', name: 'ecgtGaranYears', location: 'urlencoded' },
    { wire: 'ecgt_garan_model', name: 'ecgtGaranModel', location: 'urlencoded' },
    { wire: 'ecgt_garan_guarantee_details', name: 'ecgtGaranGuaranteeDetails', location: 'urlencoded' },
    {
      wire: 'ecgt_other_commercial_guarantee_details',
      name: 'ecgtOtherCommercialGuaranteeDetails',
      location: 'urlencoded',
    },
    { wire: 'ecgt_after_sales_service_info', name: 'ecgtAfterSalesServiceInfo', location: 'urlencoded' },
    { wire: 'ecgt_software_update_details', name: 'ecgtSoftwareUpdateDetails', location: 'urlencoded' },
    { wire: 'gpsr_manufacturer_type', name: 'gpsrManufacturerType', location: 'urlencoded' },
    { wire: 'gpsr_manufacturer_id', name: 'gpsrManufacturerId', location: 'urlencoded' },
    { wire: 'gpsr_responsible_person_type', name: 'gpsrResponsiblePersonType', location: 'urlencoded' },
    { wire: 'gpsr_responsible_person_id', name: 'gpsrResponsiblePersonId', location: 'urlencoded' },
    { wire: 'gpsr_serial_number', name: 'gpsrSerialNumber', location: 'urlencoded' },
    { wire: 'gpsr_safety_warnings', name: 'gpsrSafetyWarnings', location: 'urlencoded' },
    { wire: 'is_supply', name: 'isSupply', location: 'urlencoded' },
    { wire: 'is_customizable', name: 'isCustomizable', location: 'urlencoded' },
    { wire: 'should_auto_renew', name: 'shouldAutoRenew', location: 'urlencoded' },
    { wire: 'is_taxable', name: 'isTaxable', location: 'urlencoded' },
    { wire: 'type', name: 'type', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

const deleteListing: Operation = {
  id: 'deleteListing',
  method: 'DELETE',
  path: '/v3/application/listings/{listing_id}',
  resource: 'listings',
  name: 'delete',
  params: [{ wire: 'listing_id', name: 'listingId', location: 'path' }],
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_d'] },
    ],
  ],
};

const findAllActiveListingsByShop: Operation = {
  id: 'findAllActiveListingsByShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/active',
  resource: 'listings',
  name: 'listActiveByShop',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'sort_on', name: 'sortOn', location: 'query' },
    { wire: 'sort_order', name: 'sortOrder', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'keywords', name: 'keywords', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterActiveByShop',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const findAllListingsActive: Operation = {
  id: 'findAllListingsActive',
  method: 'GET',
  path: '/v3/application/listings/active',
  resource: 'listings',
  name: 'listActive',
  params: [
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'keywords', name: 'keywords', location: 'query' },
    { wire: 'sort_on', name: 'sortOn', location: 'query' },
    { wire: 'sort_order', name: 'sortOrder', location: 'query' },
    { wire: 'min_price', name: 'minPrice', location: 'query' },
    { wire: 'max_price', name: 'maxPrice', location: 'query' },
    { wire: 'taxonomy_id', name: 'taxonomyId', location: 'query' },
    { wire: 'shop_location', name: 'shopLocation', location: 'query' },
    { wire: 'is_safe', name: 'isSafe', location: 'query' },
    { wire: 'currency', name: 'currency', location: 'query' },
    { wire: 'buyer_country', name: 'buyerCountry', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterActive',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getFeaturedListingsByShop: Operation = {
  id: 'getFeaturedListingsByShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings/featured',
  resource: 'listings',
  name: 'listFeatured',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterFeatured',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListing: Operation = {
  id: 'getListing',
  method: 'GET',
  path: '/v3/application/listings/{listing_id}',
  resource: 'listings',
  name: 'get',
  params: [
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'includes', name: 'includes', location: 'query' },
    { wire: 'language', name: 'language', location: 'query' },
    { wire: 'allow_suggested_title', name: 'allowSuggestedTitle', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingsByListingIds: Operation = {
  id: 'getListingsByListingIds',
  method: 'GET',
  path: '/v3/application/listings/batch',
  resource: 'listings',
  name: 'listByIds',
  params: [
    { wire: 'listing_ids', name: 'listingIds', location: 'query' },
    { wire: 'includes', name: 'includes', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
    { wire: 'currency', name: 'currency', location: 'query' },
    { wire: 'buyer_country', name: 'buyerCountry', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingsByShop: Operation = {
  id: 'getListingsByShop',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/listings',
  resource: 'listings',
  name: 'listByShop',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'state', name: 'state', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort_on', name: 'sortOn', location: 'query' },
    { wire: 'sort_order', name: 'sortOrder', location: 'query' },
    { wire: 'includes', name: 'includes', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterByShop',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getListingsByShopReceipt: Operation = {
  id: 'getListingsByShopReceipt',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/receipts/{receipt_id}/listings',
  resource: 'listings',
  name: 'listByReceipt',
  params: [
    { wire: 'receipt_id', name: 'receiptId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterByReceipt',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['transactions_r'] },
    ],
  ],
};

const getListingsByShopReturnPolicy: Operation = {
  id: 'getListingsByShopReturnPolicy',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/policies/return/{return_policy_id}/listings',
  resource: 'listings',
  name: 'listByReturnPolicy',
  params: [
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'path' },
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_r'] },
    ],
  ],
};

const getListingsByShopSectionId: Operation = {
  id: 'getListingsByShopSectionId',
  method: 'GET',
  path: '/v3/application/shops/{shop_id}/shop-sections/listings',
  resource: 'listings',
  name: 'listBySections',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'shop_section_ids', name: 'shopSectionIds', location: 'query' },
    { wire: 'limit', name: 'limit', location: 'query' },
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'sort_on', name: 'sortOn', location: 'query' },
    { wire: 'sort_order', name: 'sortOrder', location: 'query' },
    { wire: 'legacy', name: 'legacy', location: 'query' },
  ],
  returnsJson: true,
  iterator: 'iterBySections',
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'api_key', scopes: [] }]],
};

const getListingsShippingByListingIds: Operation = {
  id: 'getListingsShippingByListingIds',
  method: 'GET',
  path: '/v3/application/listings/batch/shipping',
  resource: 'listings',
  name: 'listShippingByIds',
  params: [{ wire: 'listing_ids', name: 'listingIds', location: 'query' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['shops_r'] },
    ],
  ],
};

const updateListing: Operation = {
  id: 'updateListing',
  method: 'PATCH',
  path: '/v3/application/shops/{shop_id}/listings/{listing_id}',
  resource: 'listings',
  name: 'update',
  params: [
    { wire: 'shop_id', name: 'shopId', location: 'path' },
    { wire: 'listing_id', name: 'listingId', location: 'path' },
    { wire: 'image_ids', name: 'imageIds', location: 'urlencoded' },
    { wire: 'title', name: 'title', location: 'urlencoded' },
    { wire: 'description', name: 'description', location: 'urlencoded' },
    { wire: 'materials', name: 'materials', location: 'urlencoded' },
    { wire: 'should_auto_renew', name: 'shouldAutoRenew', location: 'urlencoded' },
    { wire: 'shipping_profile_id', name: 'shippingProfileId', location: 'urlencoded' },
    { wire: 'return_policy_id', name: 'returnPolicyId', location: 'urlencoded' },
    { wire: 'shop_section_id', name: 'shopSectionId', location: 'urlencoded' },
    { wire: 'item_weight', name: 'itemWeight', location: 'urlencoded' },
    { wire: 'item_length', name: 'itemLength', location: 'urlencoded' },
    { wire: 'item_width', name: 'itemWidth', location: 'urlencoded' },
    { wire: 'item_height', name: 'itemHeight', location: 'urlencoded' },
    { wire: 'item_weight_unit', name: 'itemWeightUnit', location: 'urlencoded' },
    { wire: 'item_dimensions_unit', name: 'itemDimensionsUnit', location: 'urlencoded' },
    { wire: 'is_taxable', name: 'isTaxable', location: 'urlencoded' },
    { wire: 'taxonomy_id', name: 'taxonomyId', location: 'urlencoded' },
    { wire: 'tags', name: 'tags', location: 'urlencoded' },
    { wire: 'who_made', name: 'whoMade', location: 'urlencoded' },
    { wire: 'when_made', name: 'whenMade', location: 'urlencoded' },
    { wire: 'state', name: 'state', location: 'urlencoded' },
    { wire: 'is_supply', name: 'isSupply', location: 'urlencoded' },
    { wire: 'production_partner_ids', name: 'productionPartnerIds', location: 'urlencoded' },
    { wire: 'type', name: 'type', location: 'urlencoded' },
    { wire: 'ecgt_garan_brand', name: 'ecgtGaranBrand', location: 'urlencoded' },
    { wire: 'ecgt_garan_years', name: 'ecgtGaranYears', location: 'urlencoded' },
    { wire: 'ecgt_garan_model', name: 'ecgtGaranModel', location: 'urlencoded' },
    { wire: 'ecgt_garan_guarantee_details', name: 'ecgtGaranGuaranteeDetails', location: 'urlencoded' },
    {
      wire: 'ecgt_other_commercial_guarantee_details',
      name: 'ecgtOtherCommercialGuaranteeDetails',
      location: 'urlencoded',
    },
    { wire: 'ecgt_after_sales_service_info', name: 'ecgtAfterSalesServiceInfo', location: 'urlencoded' },
    { wire: 'ecgt_software_update_details', name: 'ecgtSoftwareUpdateDetails', location: 'urlencoded' },
    { wire: 'gpsr_manufacturer_type', name: 'gpsrManufacturerType', location: 'urlencoded' },
    { wire: 'gpsr_manufacturer_id', name: 'gpsrManufacturerId', location: 'urlencoded' },
    { wire: 'gpsr_responsible_person_type', name: 'gpsrResponsiblePersonType', location: 'urlencoded' },
    { wire: 'gpsr_responsible_person_id', name: 'gpsrResponsiblePersonId', location: 'urlencoded' },
    { wire: 'gpsr_serial_number', name: 'gpsrSerialNumber', location: 'urlencoded' },
    { wire: 'gpsr_safety_warnings', name: 'gpsrSafetyWarnings', location: 'urlencoded' },
  ],
  returnsJson: true,
  security: [
    [
      { scheme: 'api_key', scopes: [] },
      { scheme: 'oauth2', scopes: ['listings_w'] },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [
  createDraftListing,
  deleteListing,
  findAllActiveListingsByShop,
  findAllListingsActive,
  getFeaturedListingsByShop,
  getListing,
  getListingsByListingIds,
  getListingsByShop,
  getListingsByShopReceipt,
  getListingsByShopReturnPolicy,
  getListingsByShopSectionId,
  getListingsShippingByListingIds,
  updateListing,
];

export class ListingsApi extends Resource {
  /** Create a draft listing. */
  createDraft(
    shopId: number,
    params: {
      quantity: number;
      title: string;
      description: string;
      price: number;
      whoMade: string;
      whenMade: string;
      taxonomyId: number;
      shippingProfileId?: number;
      returnPolicyId?: number;
      materials?: Array<string>;
      shopSectionId?: number;
      processingMin?: number;
      processingMax?: number;
      readinessStateId?: number;
      tags?: Array<string>;
      styles?: Array<string>;
      itemWeight?: number;
      itemLength?: number;
      itemWidth?: number;
      itemHeight?: number;
      itemWeightUnit?: string;
      itemDimensionsUnit?: string;
      productionPartnerIds?: Array<number>;
      imageIds?: Array<number>;
      ecgtGaranBrand?: string;
      ecgtGaranYears?: number;
      ecgtGaranModel?: string;
      ecgtGaranGuaranteeDetails?: string;
      ecgtOtherCommercialGuaranteeDetails?: string;
      ecgtAfterSalesServiceInfo?: string;
      ecgtSoftwareUpdateDetails?: string;
      gpsrManufacturerType?: string;
      gpsrManufacturerId?: number;
      gpsrResponsiblePersonType?: string;
      gpsrResponsiblePersonId?: number;
      gpsrSerialNumber?: string;
      gpsrSafetyWarnings?: string;
      isSupply?: boolean;
      isCustomizable?: boolean;
      shouldAutoRenew?: boolean;
      isTaxable?: boolean;
      type?: string;
    },
    options?: RequestOptions,
  ): Promise<ShopListing> {
    return this.call(createDraftListing, undefined, { shopId, ...params }, options);
  }

  /** Delete a listing. */
  delete(listingId: number, options?: RequestOptions): Promise<void> {
    return this.call(deleteListing, undefined, { listingId }, options);
  }

  /** List one page of a shop's active listings. */
  listActiveByShop(
    shopId: number,
    params: {
      limit?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      offset?: number;
      keywords?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(findAllActiveListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActiveByShop(
    shopId: number,
    params: {
      limit?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      offset?: number;
      keywords?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListing, void, undefined> {
    return this.paginate(findAllActiveListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** Search one page of active listings across all shops. */
  listActive(
    params: {
      limit?: number;
      offset?: number;
      keywords?: string;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      minPrice?: number;
      maxPrice?: number;
      taxonomyId?: number;
      shopLocation?: string;
      isSafe?: boolean;
      currency?: string;
      buyerCountry?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(findAllListingsActive, undefined, { ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterActive(
    params: {
      limit?: number;
      offset?: number;
      keywords?: string;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      minPrice?: number;
      maxPrice?: number;
      taxonomyId?: number;
      shopLocation?: string;
      isSafe?: boolean;
      currency?: string;
      buyerCountry?: string;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListing, void, undefined> {
    return this.paginate(findAllListingsActive, undefined, { ...params }, options);
  }

  /** List one page of a shop's featured listings. */
  listFeatured(
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(getFeaturedListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterFeatured(
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListing, void, undefined> {
    return this.paginate(getFeaturedListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** Get one listing. */
  get(
    listingId: number,
    params: {
      includes?: Array<'Images' | 'Shop' | 'User' | 'Translations' | 'Videos' | 'Personalization' | 'BuyerPrice'>;
      language?: string;
      allowSuggestedTitle?: boolean;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopListingWithAssociations> {
    return this.call(getListing, undefined, { listingId, ...params }, options);
  }

  /** Get several listings by ID. */
  listByIds(
    params: {
      listingIds: Array<number>;
      includes?: Array<'Images' | 'Shop' | 'User' | 'Translations' | 'Videos' | 'Personalization' | 'BuyerPrice'>;
      legacy?: boolean;
      currency?: string;
      buyerCountry?: string;
    },
    options?: RequestOptions,
  ): Promise<ShopListingsWithAssociations> {
    return this.call(getListingsByListingIds, undefined, { ...params }, options);
  }

  /** List one page of a shop's listings in any state. */
  listByShop(
    shopId: number,
    params: {
      state?: 'active' | 'inactive' | 'sold_out' | 'draft' | 'removed' | 'expired';
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      includes?: Array<
        | 'Shipping'
        | 'Images'
        | 'Shop'
        | 'User'
        | 'Translations'
        | 'Inventory'
        | 'Videos'
        | 'Personalization'
        | 'BuyerPrice'
      >;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopListingsWithAssociations> {
    return this.call(getListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterByShop(
    shopId: number,
    params: {
      state?: 'active' | 'inactive' | 'sold_out' | 'draft' | 'removed' | 'expired';
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      includes?: Array<
        | 'Shipping'
        | 'Images'
        | 'Shop'
        | 'User'
        | 'Translations'
        | 'Inventory'
        | 'Videos'
        | 'Personalization'
        | 'BuyerPrice'
      >;
    } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListingWithAssociations, void, undefined> {
    return this.paginate(getListingsByShop, undefined, { shopId, ...params }, options);
  }

  /** List one page of the listings on a receipt. */
  listByReceipt(
    receiptId: number,
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(getListingsByShopReceipt, undefined, { receiptId, shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterByReceipt(
    receiptId: number,
    shopId: number,
    params: { limit?: number; offset?: number; legacy?: boolean } = {},
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListing, void, undefined> {
    return this.paginate(getListingsByShopReceipt, undefined, { receiptId, shopId, ...params }, options);
  }

  /** List the listings that use a return policy. */
  listByReturnPolicy(
    returnPolicyId: number,
    shopId: number,
    params: { legacy?: boolean } = {},
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(getListingsByShopReturnPolicy, undefined, { returnPolicyId, shopId, ...params }, options);
  }

  /** List one page of the listings in shop sections. */
  listBySections(
    shopId: number,
    params: {
      shopSectionIds: Array<number>;
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      legacy?: boolean;
    },
    options?: RequestOptions,
  ): Promise<ShopListings> {
    return this.call(getListingsByShopSectionId, undefined, { shopId, ...params }, options);
  }

  /** Iterate every item across all pages. */
  iterBySections(
    shopId: number,
    params: {
      shopSectionIds: Array<number>;
      limit?: number;
      offset?: number;
      sortOn?: 'created' | 'price' | 'updated' | 'score';
      sortOrder?: 'asc' | 'ascending' | 'desc' | 'descending' | 'up' | 'down';
      legacy?: boolean;
    },
    options?: RequestOptions,
  ): AsyncGenerator<models.ShopListing, void, undefined> {
    return this.paginate(getListingsByShopSectionId, undefined, { shopId, ...params }, options);
  }

  /** Get the shipping details of several listings by ID. */
  listShippingByIds(
    params: { listingIds: Array<number> },
    options?: RequestOptions,
  ): Promise<ShopListingsWithAssociations> {
    return this.call(getListingsShippingByListingIds, undefined, { ...params }, options);
  }

  /** Update a listing. */
  update(
    shopId: number,
    listingId: number,
    params: {
      imageIds?: Array<number>;
      title?: string;
      description?: string;
      materials?: Array<string>;
      shouldAutoRenew?: boolean;
      shippingProfileId?: number;
      returnPolicyId?: number;
      shopSectionId?: number;
      itemWeight?: number;
      itemLength?: number;
      itemWidth?: number;
      itemHeight?: number;
      itemWeightUnit?: string;
      itemDimensionsUnit?: string;
      isTaxable?: boolean;
      taxonomyId?: number;
      tags?: Array<string>;
      whoMade?: string;
      whenMade?: string;
      state?: string;
      isSupply?: boolean;
      productionPartnerIds?: Array<number>;
      type?: string;
      ecgtGaranBrand?: string;
      ecgtGaranYears?: number;
      ecgtGaranModel?: string;
      ecgtGaranGuaranteeDetails?: string;
      ecgtOtherCommercialGuaranteeDetails?: string;
      ecgtAfterSalesServiceInfo?: string;
      ecgtSoftwareUpdateDetails?: string;
      gpsrManufacturerType?: string;
      gpsrManufacturerId?: number;
      gpsrResponsiblePersonType?: string;
      gpsrResponsiblePersonId?: number;
      gpsrSerialNumber?: string;
      gpsrSafetyWarnings?: string;
    } = {},
    options?: RequestOptions,
  ): Promise<ShopListing> {
    return this.call(updateListing, undefined, { shopId, listingId, ...params }, options);
  }
}
