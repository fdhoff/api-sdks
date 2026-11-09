// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  AutomotivePartsCompatibilityPolicyResponse,
  CategoryPolicyResponse,
  ClassifiedAdPolicyResponse,
  ExtendedProducerResponsibilityPolicyResponse,
  GetAutomotivePartsCompatibilityPolicies429Response,
  GetCurrenciesResponse,
  HazardousMaterialDetailsResponse,
  ItemConditionPolicyResponse,
  ListingStructurePolicyResponse,
  ListingTypePoliciesResponse,
  MotorsListingPoliciesResponse,
  NegotiatedPricePolicyResponse,
  ProductSafetyLabelsResponse,
  RegulatoryPolicyResponse,
  ReturnPolicyResponse,
  ShippingPoliciesResponse,
  SiteVisibilityPoliciesResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getAutomotivePartsCompatibilityPolicies: Operation = {
  id: 'getAutomotivePartsCompatibilityPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies',
  resource: 'marketplaces',
  name: 'getAutomotivePartsCompatibilityPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCategoryPolicies: Operation = {
  id: 'getCategoryPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_category_policies',
  resource: 'marketplaces',
  name: 'getCategoryPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getClassifiedAdPolicies: Operation = {
  id: 'getClassifiedAdPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_classified_ad_policies',
  resource: 'marketplaces',
  name: 'getClassifiedAdPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getCurrencies: Operation = {
  id: 'getCurrencies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_currencies',
  resource: 'marketplaces',
  name: 'getCurrencies',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getExtendedProducerResponsibilityPolicies: Operation = {
  id: 'getExtendedProducerResponsibilityPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies',
  resource: 'marketplaces',
  name: 'getExtendedProducerResponsibilityPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getHazardousMaterialsLabels: Operation = {
  id: 'getHazardousMaterialsLabels',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_hazardous_materials_labels',
  resource: 'marketplaces',
  name: 'getHazardousMaterialsLabels',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getItemConditionPolicies: Operation = {
  id: 'getItemConditionPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies',
  resource: 'marketplaces',
  name: 'getItemConditionPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: ['https://api.ebay.com/oauth/api_scope', 'https://api.ebay.com/oauth/api_scope/sell.inventory'],
      },
    ],
  ],
};

const getListingStructurePolicies: Operation = {
  id: 'getListingStructurePolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_structure_policies',
  resource: 'marketplaces',
  name: 'getListingStructurePolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getListingTypePolicies: Operation = {
  id: 'getListingTypePolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_type_policies',
  resource: 'marketplaces',
  name: 'getListingTypePolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getMotorsListingPolicies: Operation = {
  id: 'getMotorsListingPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_motors_listing_policies',
  resource: 'marketplaces',
  name: 'getMotorsListingPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getNegotiatedPricePolicies: Operation = {
  id: 'getNegotiatedPricePolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_negotiated_price_policies',
  resource: 'marketplaces',
  name: 'getNegotiatedPricePolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getProductSafetyLabels: Operation = {
  id: 'getProductSafetyLabels',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_product_safety_labels',
  resource: 'marketplaces',
  name: 'getProductSafetyLabels',
  host: 'api',
  params: [{ wire: 'marketplace_id', name: 'marketplaceId', location: 'path' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getRegulatoryPolicies: Operation = {
  id: 'getRegulatoryPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_regulatory_policies',
  resource: 'marketplaces',
  name: 'getRegulatoryPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getReturnPolicies: Operation = {
  id: 'getReturnPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_return_policies',
  resource: 'marketplaces',
  name: 'getReturnPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getShippingPolicies: Operation = {
  id: 'getShippingPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_shipping_policies',
  resource: 'marketplaces',
  name: 'getShippingPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

const getSiteVisibilityPolicies: Operation = {
  id: 'getSiteVisibilityPolicies',
  method: 'GET',
  path: '/sell/metadata/v1/marketplace/{marketplace_id}/get_site_visibility_policies',
  resource: 'marketplaces',
  name: 'getSiteVisibilityPolicies',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'filter', name: 'filter', location: 'query' },
  ],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  getAutomotivePartsCompatibilityPolicies,
  getCategoryPolicies,
  getClassifiedAdPolicies,
  getCurrencies,
  getExtendedProducerResponsibilityPolicies,
  getHazardousMaterialsLabels,
  getItemConditionPolicies,
  getListingStructurePolicies,
  getListingTypePolicies,
  getMotorsListingPolicies,
  getNegotiatedPricePolicies,
  getProductSafetyLabels,
  getRegulatoryPolicies,
  getReturnPolicies,
  getShippingPolicies,
  getSiteVisibilityPolicies,
];

export class MarketplacesApi extends Resource {
  /** List the categories of a marketplace that support parts compatibility. */
  getAutomotivePartsCompatibilityPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<AutomotivePartsCompatibilityPolicyResponse | undefined> {
    return this.call(getAutomotivePartsCompatibilityPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the listing policies of a marketplace's categories. */
  getCategoryPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<CategoryPolicyResponse | undefined> {
    return this.call(getCategoryPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the classified ad policies of a marketplace's categories. */
  getClassifiedAdPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ClassifiedAdPolicyResponse | undefined> {
    return this.call(getClassifiedAdPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** Get the default currency of a marketplace. */
  getCurrencies(marketplaceId: string, options?: RequestOptions): Promise<GetCurrenciesResponse | undefined> {
    return this.call(getCurrencies, undefined, { marketplaceId }, options);
  }

  /** List the extended producer responsibility policies of a marketplace's categories. */
  getExtendedProducerResponsibilityPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ExtendedProducerResponsibilityPolicyResponse | undefined> {
    return this.call(getExtendedProducerResponsibilityPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the hazardous materials labels a marketplace accepts. */
  getHazardousMaterialsLabels(
    marketplaceId: string,
    options?: RequestOptions,
  ): Promise<HazardousMaterialDetailsResponse | undefined> {
    return this.call(getHazardousMaterialsLabels, undefined, { marketplaceId }, options);
  }

  /** List the item conditions a marketplace's categories accept. */
  getItemConditionPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ItemConditionPolicyResponse | undefined> {
    return this.call(getItemConditionPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List which of a marketplace's categories accept multi-variation listings. */
  getListingStructurePolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ListingStructurePolicyResponse | undefined> {
    return this.call(getListingStructurePolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the listing formats and durations of a marketplace's categories. */
  getListingTypePolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ListingTypePoliciesResponse | undefined> {
    return this.call(getListingTypePolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the motors listing policies of a marketplace's categories. */
  getMotorsListingPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<MotorsListingPoliciesResponse | undefined> {
    return this.call(getMotorsListingPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the Best Offer policies of a marketplace's categories. */
  getNegotiatedPricePolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<NegotiatedPricePolicyResponse | undefined> {
    return this.call(getNegotiatedPricePolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the product safety labels a marketplace accepts. */
  getProductSafetyLabels(
    marketplaceId: string,
    options?: RequestOptions,
  ): Promise<ProductSafetyLabelsResponse | undefined> {
    return this.call(getProductSafetyLabels, undefined, { marketplaceId }, options);
  }

  /** List the regulatory policies of a marketplace's categories. */
  getRegulatoryPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<RegulatoryPolicyResponse | undefined> {
    return this.call(getRegulatoryPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the return policies of a marketplace's categories. */
  getReturnPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ReturnPolicyResponse | undefined> {
    return this.call(getReturnPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List the shipping policies of a marketplace's categories. */
  getShippingPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<ShippingPoliciesResponse | undefined> {
    return this.call(getShippingPolicies, undefined, { marketplaceId, ...params }, options);
  }

  /** List which of a marketplace's categories show on other marketplaces. */
  getSiteVisibilityPolicies(
    marketplaceId: string,
    params: { filter?: string } = {},
    options?: RequestOptions,
  ): Promise<SiteVisibilityPoliciesResponse | undefined> {
    return this.call(getSiteVisibilityPolicies, undefined, { marketplaceId, ...params }, options);
  }
}
