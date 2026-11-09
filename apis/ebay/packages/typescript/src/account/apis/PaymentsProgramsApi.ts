// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import type {
  GetCustomPolicies429Response,
  PaymentsProgramOnboardingResponse,
  PaymentsProgramResponse,
} from '../models/index.js';
import type * as models from '../models/index.js';
import { Resource, type FileInput, type Operation, type RequestOptions } from '../../runtime/index.js';

const getPaymentsProgram: Operation = {
  id: 'getPaymentsProgram',
  method: 'GET',
  path: '/sell/account/v1/payments_program/{marketplace_id}/{payments_program_type}',
  resource: 'paymentsPrograms',
  name: 'get',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'payments_program_type', name: 'paymentsProgramType', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.account',
          'https://api.ebay.com/oauth/api_scope/sell.account.readonly',
        ],
      },
    ],
  ],
};

const getPaymentsProgramOnboarding: Operation = {
  id: 'getPaymentsProgramOnboarding',
  method: 'GET',
  path: '/sell/account/v1/payments_program/{marketplace_id}/{payments_program_type}/onboarding',
  resource: 'paymentsPrograms',
  name: 'getOnboarding',
  host: 'api',
  params: [
    { wire: 'marketplace_id', name: 'marketplaceId', location: 'path' },
    { wire: 'payments_program_type', name: 'paymentsProgramType', location: 'path' },
  ],
  returnsJson: true,
  security: [
    [
      {
        scheme: 'api_auth',
        scopes: [
          'https://api.ebay.com/oauth/api_scope/sell.account',
          'https://api.ebay.com/oauth/api_scope/sell.account.readonly',
        ],
      },
    ],
  ],
};

export const OPERATIONS: readonly Operation[] = [getPaymentsProgram, getPaymentsProgramOnboarding];

export class PaymentsProgramsApi extends Resource {
  /** Get the seller's status in a payments program. */
  get(marketplaceId: string, paymentsProgramType: string, options?: RequestOptions): Promise<PaymentsProgramResponse> {
    return this.call(getPaymentsProgram, undefined, { marketplaceId, paymentsProgramType }, options);
  }

  /** Get the seller's onboarding progress in a payments program. */
  getOnboarding(
    marketplaceId: string,
    paymentsProgramType: string,
    options?: RequestOptions,
  ): Promise<PaymentsProgramOnboardingResponse> {
    return this.call(getPaymentsProgramOnboarding, undefined, { marketplaceId, paymentsProgramType }, options);
  }
}
