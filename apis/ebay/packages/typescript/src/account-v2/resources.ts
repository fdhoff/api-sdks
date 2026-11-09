// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

import {
  CombinedShippingRulesApi,
  OPERATIONS as CombinedShippingRulesApiOperations,
} from './apis/CombinedShippingRulesApi.js';
import { PayoutSettingsApi, OPERATIONS as PayoutSettingsApiOperations } from './apis/PayoutSettingsApi.js';
import { RateTablesApi, OPERATIONS as RateTablesApiOperations } from './apis/RateTablesApi.js';
import { UserPreferencesApi, OPERATIONS as UserPreferencesApiOperations } from './apis/UserPreferencesApi.js';
import type { Operation, Transport } from '../runtime/index.js';

export const OPERATIONS: ReadonlyMap<string, Operation> = new Map(
  [
    ...CombinedShippingRulesApiOperations,
    ...PayoutSettingsApiOperations,
    ...RateTablesApiOperations,
    ...UserPreferencesApiOperations,
  ].map((operation) => [operation.id, operation]),
);

export class Resources {
  readonly combinedShippingRules: CombinedShippingRulesApi;
  readonly payoutSettings: PayoutSettingsApi;
  readonly rateTables: RateTablesApi;
  readonly userPreferences: UserPreferencesApi;

  constructor(transport: Transport) {
    this.combinedShippingRules = new CombinedShippingRulesApi(transport);
    this.payoutSettings = new PayoutSettingsApi(transport);
    this.rateTables = new RateTablesApi(transport);
    this.userPreferences = new UserPreferencesApi(transport);
  }
}
