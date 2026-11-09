// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Amount {
  currency?: string;
  value?: string;
}

export interface CalculatedHandlingRuleType {
  combinedShippingRuleType?: string;
  eachAdditionalAmount?: Amount;
  eachAdditionalAmountOffShippingCost?: Amount;
  eachAdditionalPercentOffShippingCost?: number;
  orderHandlingAmount?: Amount;
}

export interface CalculatedShippingRuleType {
  combinedShippingRules?: Array<CombinedShippingRule>;
  combinedShippingRuleType?: string;
}

export interface CombinedPaymentPreferencesType {
  combinedPaymentOption?: string;
}

export interface CombinedShippingRule {
  combinedShippingRuleId?: string;
  combinedShippingRuleName?: string;
  eachAdditionalAmount?: Amount;
  eachAdditionalAmountOffShippingCost?: Amount;
  eachAdditionalPercentOffShippingCost?: number;
  mappedCombinedShippingRuleId?: string;
  weightOffTotalWeight?: MeasureType;
}

export interface CreateCalculatedShippingRulesRequest {
  calculatedHandlingRule?: CalculatedHandlingRuleType;
  calculatedShippingRule?: CalculatedShippingRuleType;
  combinedDuration?: string;
}

export interface CreateFlatShippingRulesRequest {
  combinedDuration?: string;
  flatShippingRule?: FlatShippingRuleType;
}

export interface CreatePromotionalShippingRuleRequest {
  combinedDuration?: string;
  promotionalShippingRule?: PromotionalShippingRuleType;
}

export interface DispatchCutoffTimePreferencesType {
  cutoffTime?: string;
}

export interface EndOfAuctionEmailPreferencesType {
  emailCustomized?: boolean;
  logoCustomized?: boolean;
  logoType?: string;
  logoUrl?: string;
  templateText?: string;
  textCustomized?: boolean;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FlatShippingRuleType {
  combinedShippingRules?: Array<CombinedShippingRule>;
  combinedShippingRuleType?: string;
}

export interface GetCombinedShippingRulesPublicApiResponse {
  calculatedHandlingRule?: CalculatedHandlingRuleType;
  calculatedShippingRule?: CalculatedShippingRuleType;
  combinedDuration?: string;
  flatShippingRule?: FlatShippingRuleType;
  promotionalShippingRule?: PromotionalShippingRuleType;
}

export interface GetItemsAwaitingPaymentPreferencesType {
  autoRelist?: boolean;
  delayBeforeCancellingCommitment?: number;
  excludedUsers?: Array<string>;
  optInStatus?: boolean;
}

export interface GetRateTable429Response {
  errors?: Array<Error>;
}

export interface GetUserPreferencesResponse {
  combinedPaymentPreferences?: CombinedPaymentPreferencesType;
  dispatchCutoffTimePreference?: DispatchCutoffTimePreferencesType;
  emailShipmentTrackingNumberPreference?: boolean;
  endOfAuctionEmailPreferences?: EndOfAuctionEmailPreferencesType;
  globalShippingProgramListingPreference?: boolean;
  itemsAwaitingPaymentPreferences?: GetItemsAwaitingPaymentPreferencesType;
  offerGlobalShippingProgramPreference?: boolean;
  outOfStockControlPreference?: boolean;
  overrideGspServiceWithIntlServicePreference?: boolean;
  pickupDropoffSellerPreference?: boolean;
  purchaseReminderEmailPreferences?: boolean;
  requiredShipPhoneNumberPreference?: boolean;
  sellerExcludeShipToLocationPreferences?: SellerExcludeShipToLocationPreferencesType;
  sellerProfilePreferences?: SellerProfilePreferencesType;
  shippingCarrierRatePreferences?: ShippingCarrierRatePreferencesType;
}

export interface MeasureType {
  unit?: string;
  value?: string;
}

export interface ModelError {
  category?: string;
  domain?: string;
  errorId?: number;
  inputRefIds?: Array<string>;
  longMessage?: string;
  message?: string;
  outputRefIds?: Array<string>;
  parameters?: Array<ErrorParameter>;
  subdomain?: string;
}

export interface PayoutInstrument {
  accountLastFourDigits?: string;
  instrumentId?: string;
  instrumentStatus?: string;
  instrumentType?: string;
  nickname?: string;
  payoutPercentage?: string;
}

export interface PayoutSettingsResponse {
  payoutInstruments?: Array<PayoutInstrument>;
}

export interface PromotionalShippingRuleType {
  combinedShippingRuleType?: string;
  itemCount?: number;
  orderAmount?: Amount;
  shippingCost?: Amount;
}

export interface Rate {
  additionalCost?: Amount;
  rateId?: string;
  shippingCategory?: string;
  shippingCost?: Amount;
  shippingRegionNames?: Array<string>;
  shippingServiceCode?: string;
}

export interface RateTableDetails {
  marketplaceId?: string;
  name?: string;
  rates?: Array<Rate>;
  rateTableBasis?: string;
  rateTableId?: string;
  shippingOptionType?: string;
}

export interface RateTableUpdate {
  rates?: Array<RateUpdate>;
}

export interface RateUpdate {
  additionalCost?: Amount;
  rateId?: string;
  shippingCost?: Amount;
}

export interface SellerExcludeShipToLocationPreferencesType {
  excludeShipToLocations?: Array<string>;
}

export interface SellerProfilePreferencesType {
  sellerProfileOptedIn?: boolean;
}

export interface ShippingCarrierRatePreferencesType {
  fedexRateOption?: string;
  upsRateOption?: string;
}

export interface UpdateCalculatedShippingRulesRequest {
  calculatedHandlingRule?: CalculatedHandlingRuleType;
  calculatedShippingRule?: CalculatedShippingRuleType;
  combinedDuration?: string;
}

export interface UpdateCombinedPaymentsRequest {
  combinedDuration?: string;
}

export interface UpdateFlatShippingRulesRequest {
  combinedDuration?: string;
  flatShippingRule?: FlatShippingRuleType;
}

export interface UpdatePayoutPercentage {
  instrumentId?: string;
  payoutPercentage?: string;
}

export interface UpdatePayoutPercentageRequest {
  payoutInstruments?: Array<UpdatePayoutPercentage>;
}

export interface UpdatePromotionalShippingRuleRequest {
  combinedDuration?: string;
  promotionalShippingRule?: PromotionalShippingRuleType;
}
