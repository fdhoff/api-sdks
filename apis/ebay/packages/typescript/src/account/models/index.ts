// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Amount {
  currency?: string;
  value?: string;
}

export interface BulkSalesTaxInput {
  salesTaxInputList?: Array<SalesTaxInput>;
}

export interface CategoryType {
  _default?: boolean;
  name?: string;
}

export interface CompactCustomPolicyResponse {
  customPolicyId?: string;
  label?: string;
  name?: string;
  policyType?: string;
}

export interface CustomPolicy {
  customPolicyId?: string;
  description?: string;
  label?: string;
  name?: string;
  policyType?: string;
}

export interface CustomPolicyCreateRequest {
  description?: string;
  label?: string;
  name?: string;
  policyType?: string;
}

export interface CustomPolicyRequest {
  description?: string;
  label?: string;
  name?: string;
}

export interface CustomPolicyResponse {
  customPolicies?: Array<CompactCustomPolicyResponse>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface Deposit {
  amount?: Amount;
  dueIn?: TimeDuration;
  paymentMethods?: Array<PaymentMethod>;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FulfillmentPolicy {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  freightShipping?: boolean;
  fulfillmentPolicyId?: string;
  globalShipping?: boolean;
  handlingTime?: TimeDuration;
  localPickup?: boolean;
  marketplaceId?: string;
  name?: string;
  pickupDropOff?: boolean;
  shippingOptions?: Array<ShippingOption>;
  shipToLocations?: RegionSet;
}

export interface FulfillmentPolicyRequest {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  freightShipping?: boolean;
  globalShipping?: boolean;
  handlingTime?: TimeDuration;
  localPickup?: boolean;
  marketplaceId?: string;
  name?: string;
  pickupDropOff?: boolean;
  shippingOptions?: Array<ShippingOption>;
  shipToLocations?: RegionSet;
}

export interface FulfillmentPolicyResponse {
  fulfillmentPolicies?: Array<FulfillmentPolicy>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface GetCustomPolicies429Response {
  errors?: Array<Error>;
}

export interface InternationalReturnOverrideType {
  returnMethod?: string;
  returnPeriod?: TimeDuration;
  returnsAccepted?: boolean;
  returnShippingCostPayer?: string;
}

export interface KycCheck {
  dataRequired?: string;
  dueDate?: string;
  remedyUrl?: string;
  alert?: string;
  detailMessage?: string;
}

export interface KycResponse {
  kycChecks?: Array<KycCheck>;
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

export interface PaymentMethod {
  brands?: Array<string>;
  paymentMethodType?: string;
  recipientAccountReference?: RecipientAccountReference;
}

export interface PaymentPolicy {
  categoryTypes?: Array<CategoryType>;
  deposit?: Deposit;
  description?: string;
  fullPaymentDueIn?: TimeDuration;
  immediatePay?: boolean;
  marketplaceId?: string;
  name?: string;
  paymentInstructions?: string;
  paymentMethods?: Array<PaymentMethod>;
  paymentPolicyId?: string;
}

export interface PaymentPolicyRequest {
  categoryTypes?: Array<CategoryType>;
  deposit?: Deposit;
  description?: string;
  fullPaymentDueIn?: TimeDuration;
  immediatePay?: boolean;
  marketplaceId?: string;
  name?: string;
  paymentInstructions?: string;
  paymentMethods?: Array<PaymentMethod>;
}

export interface PaymentPolicyResponse {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  paymentPolicies?: Array<PaymentPolicy>;
  prev?: string;
  total?: number;
}

export interface PaymentsProgramOnboardingResponse {
  onboardingStatus?: string;
  steps?: Array<PaymentsProgramOnboardingSteps>;
}

export interface PaymentsProgramOnboardingSteps {
  name?: string;
  status?: string;
  webUrl?: string;
}

export interface PaymentsProgramResponse {
  marketplaceId?: string;
  paymentsProgramType?: string;
  status?: string;
  wasPreviouslyOptedIn?: boolean;
}

export interface Program {
  programType?: string;
}

export interface Programs {
  programs?: Array<Program>;
}

export interface RateTable {
  countryCode?: string;
  locality?: string;
  name?: string;
  rateTableId?: string;
}

export interface RateTableResponse {
  rateTables?: Array<RateTable>;
}

export interface RecipientAccountReference {
  referenceId?: string;
  referenceType?: string;
}

export interface Region {
  regionName?: string;
  regionType?: string;
}

export interface RegionSet {
  regionExcluded?: Array<Region>;
  regionIncluded?: Array<Region>;
}

export interface ReturnPolicy {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  extendedHolidayReturnsOffered?: boolean;
  internationalOverride?: InternationalReturnOverrideType;
  marketplaceId?: string;
  name?: string;
  refundMethod?: string;
  restockingFeePercentage?: string;
  returnInstructions?: string;
  returnMethod?: string;
  returnPeriod?: TimeDuration;
  returnPolicyId?: string;
  returnsAccepted?: boolean;
  returnShippingCostPayer?: string;
}

export interface ReturnPolicyRequest {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  extendedHolidayReturnsOffered?: boolean;
  internationalOverride?: InternationalReturnOverrideType;
  marketplaceId?: string;
  name?: string;
  refundMethod?: string;
  restockingFeePercentage?: string;
  returnInstructions?: string;
  returnMethod?: string;
  returnPeriod?: TimeDuration;
  returnsAccepted?: boolean;
  returnShippingCostPayer?: string;
}

export interface ReturnPolicyResponse {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  returnPolicies?: Array<ReturnPolicy>;
  total?: number;
}

export interface SalesTax {
  countryCode?: string;
  salesTaxJurisdictionId?: string;
  salesTaxPercentage?: string;
  shippingAndHandlingTaxed?: boolean;
}

export interface SalesTaxBase {
  salesTaxPercentage?: string;
  shippingAndHandlingTaxed?: boolean;
}

export interface SalesTaxInput {
  countryCode?: string;
  salesTaxJurisdictionId?: string;
  salesTaxPercentage?: string;
  shippingAndHandlingTaxed?: boolean;
}

export interface SalesTaxes {
  salesTaxes?: Array<SalesTax>;
}

export interface SellerEligibilityMultiProgramResponse {
  advertisingEligibility?: Array<SellerEligibilityResponse>;
}

export interface SellerEligibilityResponse {
  programType?: string;
  reason?: string;
  status?: string;
}

export interface SellingLimit {
  amount?: Amount;
  quantity?: number;
}

export interface SellingPrivileges {
  sellerRegistrationCompleted?: boolean;
  sellingLimit?: SellingLimit;
}

export interface SetFulfillmentPolicyResponse {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  freightShipping?: boolean;
  fulfillmentPolicyId?: string;
  globalShipping?: boolean;
  handlingTime?: TimeDuration;
  localPickup?: boolean;
  marketplaceId?: string;
  name?: string;
  pickupDropOff?: boolean;
  shippingOptions?: Array<ShippingOption>;
  shipToLocations?: RegionSet;
  warnings?: Array<Error>;
}

export interface SetPaymentPolicyResponse {
  categoryTypes?: Array<CategoryType>;
  deposit?: Deposit;
  description?: string;
  fullPaymentDueIn?: TimeDuration;
  immediatePay?: boolean;
  marketplaceId?: string;
  name?: string;
  paymentInstructions?: string;
  paymentMethods?: Array<PaymentMethod>;
  paymentPolicyId?: string;
  warnings?: Array<Error>;
}

export interface SetReturnPolicyResponse {
  categoryTypes?: Array<CategoryType>;
  description?: string;
  extendedHolidayReturnsOffered?: boolean;
  internationalOverride?: InternationalReturnOverrideType;
  marketplaceId?: string;
  name?: string;
  refundMethod?: string;
  restockingFeePercentage?: string;
  returnInstructions?: string;
  returnMethod?: string;
  returnPeriod?: TimeDuration;
  returnPolicyId?: string;
  returnsAccepted?: boolean;
  returnShippingCostPayer?: string;
  warnings?: Array<Error>;
}

export interface ShippingOption {
  costType?: string;
  insuranceFee?: Amount;
  insuranceOffered?: boolean;
  optionType?: string;
  packageHandlingCost?: Amount;
  rateTableId?: string;
  shippingDiscountProfileId?: string;
  shippingPromotionOffered?: boolean;
  shippingServices?: Array<ShippingService>;
}

export interface ShippingService {
  additionalShippingCost?: Amount;
  buyerResponsibleForPickup?: boolean;
  buyerResponsibleForShipping?: boolean;
  freeShipping?: boolean;
  shippingCarrierCode?: string;
  shippingCost?: Amount;
  shippingServiceCode?: string;
  shipToLocations?: RegionSet;
  sortOrder?: number;
  surcharge?: Amount;
}

export interface Subscription {
  marketplaceId?: string;
  subscriptionId?: string;
  subscriptionLevel?: string;
  subscriptionType?: string;
  term?: TimeDuration;
}

export interface SubscriptionResponse {
  href?: string;
  limit?: number;
  next?: string;
  subscriptions?: Array<Subscription>;
  total?: number;
}

export interface TimeDuration {
  unit?: string;
  value?: number;
}

export interface UpdatedSalesTaxEntry {
  countryCode?: string;
  jurisdictionId?: string;
  statusCode?: number;
}

export interface UpdatedSalesTaxResponse {
  updatedSalesTaxEntries?: Array<UpdatedSalesTaxEntry>;
}
