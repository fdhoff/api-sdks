// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  AdvertisingEligibilityApi,
  OPERATIONS as AdvertisingEligibilityApiOperations,
} from './apis/AdvertisingEligibilityApi.js';
import { CustomPoliciesApi, OPERATIONS as CustomPoliciesApiOperations } from './apis/CustomPoliciesApi.js';
import {
  FulfillmentPoliciesApi,
  OPERATIONS as FulfillmentPoliciesApiOperations,
} from './apis/FulfillmentPoliciesApi.js';
import { KycApi, OPERATIONS as KycApiOperations } from './apis/KycApi.js';
import { PaymentPoliciesApi, OPERATIONS as PaymentPoliciesApiOperations } from './apis/PaymentPoliciesApi.js';
import { PaymentsProgramsApi, OPERATIONS as PaymentsProgramsApiOperations } from './apis/PaymentsProgramsApi.js';
import { PrivilegesApi, OPERATIONS as PrivilegesApiOperations } from './apis/PrivilegesApi.js';
import { ProgramsApi, OPERATIONS as ProgramsApiOperations } from './apis/ProgramsApi.js';
import { RateTablesApi, OPERATIONS as RateTablesApiOperations } from './apis/RateTablesApi.js';
import { ReturnPoliciesApi, OPERATIONS as ReturnPoliciesApiOperations } from './apis/ReturnPoliciesApi.js';
import { SalesTaxesApi, OPERATIONS as SalesTaxesApiOperations } from './apis/SalesTaxesApi.js';
import { SubscriptionsApi, OPERATIONS as SubscriptionsApiOperations } from './apis/SubscriptionsApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...AdvertisingEligibilityApiOperations,
    ...CustomPoliciesApiOperations,
    ...FulfillmentPoliciesApiOperations,
    ...KycApiOperations,
    ...PaymentPoliciesApiOperations,
    ...PaymentsProgramsApiOperations,
    ...PrivilegesApiOperations,
    ...ProgramsApiOperations,
    ...RateTablesApiOperations,
    ...ReturnPoliciesApiOperations,
    ...SalesTaxesApiOperations,
    ...SubscriptionsApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly advertisingEligibility: AdvertisingEligibilityApi;
  readonly customPolicies: CustomPoliciesApi;
  readonly fulfillmentPolicies: FulfillmentPoliciesApi;
  readonly kyc: KycApi;
  readonly paymentPolicies: PaymentPoliciesApi;
  readonly paymentsPrograms: PaymentsProgramsApi;
  readonly privileges: PrivilegesApi;
  readonly programs: ProgramsApi;
  readonly rateTables: RateTablesApi;
  readonly returnPolicies: ReturnPoliciesApi;
  readonly salesTaxes: SalesTaxesApi;
  readonly subscriptions: SubscriptionsApi;

  constructor(transport: Transport) {
    this.advertisingEligibility = new AdvertisingEligibilityApi(transport);
    this.customPolicies = new CustomPoliciesApi(transport);
    this.fulfillmentPolicies = new FulfillmentPoliciesApi(transport);
    this.kyc = new KycApi(transport);
    this.paymentPolicies = new PaymentPoliciesApi(transport);
    this.paymentsPrograms = new PaymentsProgramsApi(transport);
    this.privileges = new PrivilegesApi(transport);
    this.programs = new ProgramsApi(transport);
    this.rateTables = new RateTablesApi(transport);
    this.returnPolicies = new ReturnPoliciesApi(transport);
    this.salesTaxes = new SalesTaxesApi(transport);
    this.subscriptions = new SubscriptionsApi(transport);
  }
}
