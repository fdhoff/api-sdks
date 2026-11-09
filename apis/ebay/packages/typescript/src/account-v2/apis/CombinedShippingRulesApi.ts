// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  CreateCalculatedShippingRulesRequest,
  CreateFlatShippingRulesRequest,
  CreatePromotionalShippingRuleRequest,
  GetCombinedShippingRulesPublicApiResponse,
  GetRateTable429Response,
  UpdateCalculatedShippingRulesRequest,
  UpdateCombinedPaymentsRequest,
  UpdateFlatShippingRulesRequest,
  UpdatePromotionalShippingRuleRequest,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const createCalculatedShippingRules: Operation = {
  id: 'createCalculatedShippingRules',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/create_calculated_shipping_rules',
  resource: 'combinedShippingRules',
  name: 'createCalculated',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const createFlatShippingRules: Operation = {
  id: 'createFlatShippingRules',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/create_flat_shipping_rules',
  resource: 'combinedShippingRules',
  name: 'createFlat',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const createPromotionalShippingRule: Operation = {
  id: 'createPromotionalShippingRule',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/create_promotional_shipping_rule',
  resource: 'combinedShippingRules',
  name: 'createPromotional',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const getCombinedShippingRules: Operation = {
  id: 'getCombinedShippingRules',
  method: 'GET',
  path: '/sell/account/v2/combined_shipping_rules',
  resource: 'combinedShippingRules',
  name: 'get',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  returnsJson: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account.readonly'] }]],
};

const updateCalculatedShippingRules: Operation = {
  id: 'updateCalculatedShippingRules',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/update_calculated_shipping_rules',
  resource: 'combinedShippingRules',
  name: 'updateCalculated',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const updateCombinedPayments: Operation = {
  id: 'updateCombinedPayments',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/update_combined_payments',
  resource: 'combinedShippingRules',
  name: 'updateCombinedPayments',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const updateFlatShippingRules: Operation = {
  id: 'updateFlatShippingRules',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/update_flat_shipping_rules',
  resource: 'combinedShippingRules',
  name: 'updateFlat',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

const updatePromotionalShippingRule: Operation = {
  id: 'updatePromotionalShippingRule',
  method: 'POST',
  path: '/sell/account/v2/combined_shipping_rules/update_promotional_shipping_rule',
  resource: 'combinedShippingRules',
  name: 'updatePromotional',
  host: 'api',
  params: [{ wire: 'X-EBAY-C-MARKETPLACE-ID', name: 'marketplaceId', location: 'header' }],
  hasBody: true,
  security: [[{ scheme: 'api_auth', scopes: ['https://api.ebay.com/oauth/api_scope/sell.account'] }]],
};

export const OPERATIONS: readonly Operation[] = [
  createCalculatedShippingRules,
  createFlatShippingRules,
  createPromotionalShippingRule,
  getCombinedShippingRules,
  updateCalculatedShippingRules,
  updateCombinedPayments,
  updateFlatShippingRules,
  updatePromotionalShippingRule,
];

export class CombinedShippingRulesApi extends Resource {
  /** Create calculated combined shipping rules. */
  createCalculated(
    body?: CreateCalculatedShippingRulesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createCalculatedShippingRules, body, { ...params }, options);
  }

  /** Create flat-rate combined shipping rules. */
  createFlat(
    body?: CreateFlatShippingRulesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createFlatShippingRules, body, { ...params }, options);
  }

  /** Create a promotional shipping rule. */
  createPromotional(
    body?: CreatePromotionalShippingRuleRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(createPromotionalShippingRule, body, { ...params }, options);
  }

  /** Get the seller's combined shipping rules. */
  get(
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<GetCombinedShippingRulesPublicApiResponse> {
    return this.call(getCombinedShippingRules, undefined, { ...params }, options);
  }

  /** Update calculated combined shipping rules. */
  updateCalculated(
    body?: UpdateCalculatedShippingRulesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateCalculatedShippingRules, body, { ...params }, options);
  }

  /** Set whether buyers can pay for several items at once. */
  updateCombinedPayments(
    body?: UpdateCombinedPaymentsRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateCombinedPayments, body, { ...params }, options);
  }

  /** Update flat-rate combined shipping rules. */
  updateFlat(
    body?: UpdateFlatShippingRulesRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updateFlatShippingRules, body, { ...params }, options);
  }

  /** Update a promotional shipping rule. */
  updatePromotional(
    body?: UpdatePromotionalShippingRuleRequest,
    params: { marketplaceId?: string } = {},
    options?: RequestOptions,
  ): Promise<void> {
    return this.call(updatePromotionalShippingRule, body, { ...params }, options);
  }
}
