// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Amount {
  currency?: string;
  value?: string;
}

export interface AutomotivePartsCompatibilityPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  compatibilityBasedOn?: string;
  compatibleVehicleTypes?: Array<string>;
  maxNumberOfCompatibleVehicles?: number;
}

export interface AutomotivePartsCompatibilityPolicyResponse {
  automotivePartsCompatibilityPolicies?: Array<AutomotivePartsCompatibilityPolicy>;
  warnings?: Array<Error>;
}

export interface CategoryPolicy {
  autoPayEnabled?: boolean;
  b2bVatEnabled?: boolean;
  categoryId?: string;
  categoryTreeId?: string;
  eanSupport?: string;
  expired?: boolean;
  intangibleEnabled?: boolean;
  isbnSupport?: string;
  lsd?: boolean;
  minimumReservePrice?: number;
  orpa?: boolean;
  orra?: boolean;
  paymentMethods?: Array<string>;
  reduceReserveAllowed?: boolean;
  reservePriceAllowed?: boolean;
  upcSupport?: string;
  valueCategory?: boolean;
  virtual?: boolean;
}

export interface CategoryPolicyResponse {
  categoryPolicies?: Array<CategoryPolicy>;
  warnings?: Array<Error>;
}

export interface ClassifiedAdPolicy {
  adFormatEnabled?: string;
  categoryId?: string;
  categoryTreeId?: string;
  classifiedAdAutoAcceptEnabled?: boolean;
  classifiedAdAutoDeclineEnabled?: boolean;
  classifiedAdBestOfferEnabled?: string;
  classifiedAdCompanyNameEnabled?: boolean;
  classifiedAdContactByAddressEnabled?: boolean;
  classifiedAdContactByEmailEnabled?: boolean;
  classifiedAdContactByPhoneEnabled?: boolean;
  classifiedAdCounterOfferEnabled?: boolean;
  classifiedAdPaymentMethodEnabled?: string;
  classifiedAdPhoneCount?: number;
  classifiedAdShippingMethodEnabled?: boolean;
  classifiedAdStreetCount?: number;
  sellerContactDetailsEnabled?: boolean;
}

export interface ClassifiedAdPolicyResponse {
  classifiedAdPolicies?: Array<ClassifiedAdPolicy>;
  warnings?: Array<Error>;
}

export interface Compatibility {
  compatibilityDetails?: Array<CompatibilityDetails>;
}

export interface CompatibilityDetails {
  propertyName?: string;
  propertyValue?: string;
}

export interface Currency {
  code?: string;
  description?: string;
}

export interface DisabledProductFilter {
  excludeForEbayReviews?: boolean;
  excludeForEbaySelling?: boolean;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface ExtendedProducerResponsibility {
  enabledForVariations?: boolean;
  name?: string;
  usage?: string;
}

export interface ExtendedProducerResponsibilityPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  supportedAttributes?: Array<ExtendedProducerResponsibility>;
}

export interface ExtendedProducerResponsibilityPolicyResponse {
  extendedProducerResponsibilities?: Array<ExtendedProducerResponsibilityPolicy>;
  warnings?: Array<Error>;
}

export interface GetAutomotivePartsCompatibilityPolicies429Response {
  errors?: Array<Error>;
}

export interface GetCurrenciesResponse {
  defaultCurrency?: Currency;
  marketplaceId?: string;
}

export interface HazardStatement {
  statementId?: string;
  statementDescription?: string;
}

export interface HazardousMaterialDetailsResponse {
  signalWords?: Array<SignalWord>;
  statements?: Array<HazardStatement>;
  pictograms?: Array<Pictogram>;
}

export interface ItemCondition {
  conditionDescription?: string;
  conditionDescriptors?: Array<ItemConditionDescriptor>;
  conditionHelpText?: string;
  conditionId?: string;
  usage?: string;
}

export interface ItemConditionDescriptor {
  conditionDescriptorConstraint?: ItemConditionDescriptorConstraint;
  conditionDescriptorHelpText?: string;
  conditionDescriptorId?: string;
  conditionDescriptorName?: string;
  conditionDescriptorValues?: Array<ItemConditionDescriptorValue>;
}

export interface ItemConditionDescriptorConstraint {
  applicableToConditionDescriptorIds?: Array<string>;
  cardinality?: string;
  defaultConditionDescriptorValueId?: string;
  maxLength?: number;
  mode?: string;
  usage?: string;
}

export interface ItemConditionDescriptorValue {
  conditionDescriptorValueAdditionalHelpText?: Array<string>;
  conditionDescriptorValueConstraints?: Array<ItemConditionDescriptorValueConstraint>;
  conditionDescriptorValueHelpText?: string;
  conditionDescriptorValueId?: string;
  conditionDescriptorValueName?: string;
}

export interface ItemConditionDescriptorValueConstraint {
  applicableToConditionDescriptorId?: string;
  applicableToConditionDescriptorValueIds?: Array<string>;
}

export interface ItemConditionPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  itemConditionRequired?: boolean;
  itemConditions?: Array<ItemCondition>;
}

export interface ItemConditionPolicyResponse {
  itemConditionPolicies?: Array<ItemConditionPolicy>;
  warnings?: Array<Error>;
}

export interface ListingDuration {
  durationValues?: Array<string>;
  listingType?: string;
}

export interface ListingStructurePolicy {
  categoryId?: string;
  categoryTreeId?: string;
  variationsSupported?: boolean;
}

export interface ListingStructurePolicyResponse {
  listingStructurePolicies?: Array<ListingStructurePolicy>;
  warnings?: Array<Error>;
}

export interface ListingTypePoliciesResponse {
  listingTypePolicies?: Array<ListingTypePolicy>;
  warnings?: Array<Error>;
}

export interface ListingTypePolicy {
  categoryId?: string;
  categoryTreeId?: string;
  digitalGoodDeliveryEnabled?: boolean;
  listingDurations?: Array<ListingDuration>;
  pickupDropOffEnabled?: boolean;
}

export interface LocalListingDistance {
  distances?: Array<number>;
  distanceType?: string;
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

export interface MotorsListingPoliciesResponse {
  motorsListingPolicies?: Array<MotorsListingPolicy>;
  warnings?: Array<Error>;
}

export interface MotorsListingPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  depositSupported?: boolean;
  ebayMotorsProAdFormatEnabled?: string;
  ebayMotorsProAutoAcceptEnabled?: boolean;
  ebayMotorsProAutoDeclineEnabled?: boolean;
  ebayMotorsProBestOfferEnabled?: string;
  ebayMotorsProCompanyNameEnabled?: boolean;
  ebayMotorsProContactByAddressEnabled?: boolean;
  ebayMotorsProContactByEmailEnabled?: boolean;
  ebayMotorsProContactByPhoneEnabled?: boolean;
  ebayMotorsProCounterOfferEnabled?: boolean;
  ebayMotorsProPaymentMethodCheckOutEnabled?: string;
  ebayMotorsProPhoneCount?: number;
  ebayMotorsProSellerContactDetailsEnabled?: boolean;
  ebayMotorsProShippingMethodEnabled?: boolean;
  ebayMotorsProStreetCount?: number;
  epidSupported?: boolean;
  kTypeSupported?: boolean;
  localListingDistances?: Array<LocalListingDistance>;
  localMarketAdFormatEnabled?: string;
  localMarketAutoAcceptEnabled?: boolean;
  localMarketAutoDeclineEnabled?: boolean;
  localMarketBestOfferEnabled?: string;
  localMarketCompanyNameEnabled?: boolean;
  localMarketContactByAddressEnabled?: boolean;
  localMarketContactByEmailEnabled?: boolean;
  localMarketContactByPhoneEnabled?: boolean;
  localMarketCounterOfferEnabled?: boolean;
  localMarketNonSubscription?: boolean;
  localMarketPaymentMethodCheckOutEnabled?: string;
  localMarketPhoneCount?: number;
  localMarketPremiumSubscription?: boolean;
  localMarketRegularSubscription?: boolean;
  localMarketSellerContactDetailsEnabled?: boolean;
  localMarketShippingMethodEnabled?: boolean;
  localMarketSpecialitySubscription?: boolean;
  localMarketStreetCount?: number;
  maxGranularFitmentCount?: number;
  maxItemCompatibility?: number;
  minItemCompatibility?: number;
  nonSubscription?: string;
  premiumSubscription?: string;
  regularSubscription?: string;
  sellerProvidedTitleSupported?: boolean;
  specialitySubscription?: string;
  vinSupported?: boolean;
  vrmSupported?: boolean;
}

export interface MultiCompatibilityPropertyValuesRequest {
  categoryId?: string;
  propertyFilters?: Array<PropertyFilterInner>;
  propertyNames?: Array<string>;
}

export interface MultiCompatibilityPropertyValuesResponse {
  compatibilities?: Array<Compatibility>;
  metadataVersion?: string;
}

export interface NegotiatedPricePolicy {
  bestOfferAutoAcceptEnabled?: boolean;
  bestOfferAutoDeclineEnabled?: boolean;
  bestOfferCounterEnabled?: boolean;
  categoryId?: string;
  categoryTreeId?: string;
}

export interface NegotiatedPricePolicyResponse {
  negotiatedPricePolicies?: Array<NegotiatedPricePolicy>;
  warnings?: Array<Error>;
}

export interface PackageLimits {
  dimensionUnit?: string;
  maxGirth?: number;
  maxHeight?: number;
  maxLength?: number;
  maxWeight?: number;
  maxWidth?: number;
  minGirth?: number;
  minHeight?: number;
  minLength?: number;
  minWeight?: number;
  minWidth?: number;
  weightUnit?: string;
}

export interface Pagination {
  count?: number;
  limit?: number;
  offset?: number;
  total?: number;
}

export interface PaginationInput {
  limit?: number;
  offset?: number;
}

export interface Pictogram {
  pictogramId?: string;
  pictogramDescription?: string;
  pictogramUrl?: string;
}

export interface ProductIdentifier {
  ean?: string;
  epid?: string;
  isbn?: string;
  productId?: string;
  upc?: string;
}

export interface ProductRequest {
  applicationPropertyFilters?: Array<PropertyFilterInner>;
  dataset?: Array<string>;
  datasetPropertyName?: Array<string>;
  disabledProductFilter?: DisabledProductFilter;
  paginationInput?: PaginationInput;
  productIdentifier?: ProductIdentifier;
  sortOrders?: Array<SortOrderInner>;
}

export interface ProductResponse {
  compatibilityDetails?: Array<ProductResponseCompatibilityDetails>;
  pagination?: Pagination;
}

export interface ProductResponseCompatibilityDetails {
  noteDetails?: Array<PropertyFilterInner>;
  productDetails?: Array<PropertyValues>;
}

export interface ProductSafetyLabelPictogram {
  pictogramDescription?: string;
  pictogramId?: string;
  pictogramUrl?: string;
}

export interface ProductSafetyLabelStatement {
  statementDescription?: string;
  statementId?: string;
}

export interface ProductSafetyLabelsResponse {
  pictograms?: Array<ProductSafetyLabelPictogram>;
  statements?: Array<ProductSafetyLabelStatement>;
}

export interface PropertyFilterInner {
  propertyName?: string;
  propertyValue?: string;
  unitOfMeasurement?: string;
  url?: string;
}

export interface PropertyNamesRequest {
  categoryId?: string;
  dataset?: Array<string>;
}

export interface PropertyNamesResponse {
  categoryId?: string;
  properties?: Array<PropertyNamesResponseProperties>;
}

export interface PropertyNamesResponseProperties {
  dataset?: string;
  propertyNames?: Array<PropertyNamesResponsePropertyNames>;
}

export interface PropertyNamesResponsePropertyNameMetadata {
  displaySequence?: number;
}

export interface PropertyNamesResponsePropertyNames {
  propertyDisplayName?: string;
  propertyName?: string;
  propertyNameMetadata?: PropertyNamesResponsePropertyNameMetadata;
}

export interface PropertyValues {
  propertyName?: string;
  propertyValue?: string;
}

export interface PropertyValuesRequest {
  categoryId?: string;
  propertyFilters?: Array<PropertyFilterInner>;
  propertyName?: string;
  sortOrder?: string;
}

export interface PropertyValuesResponse {
  metadataVersion?: string;
  propertyName?: string;
  propertyValues?: Array<string>;
}

export interface RegulatoryAttribute {
  name?: string;
  usage?: string;
}

export interface RegulatoryPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  supportedAttributes?: Array<RegulatoryAttribute>;
}

export interface RegulatoryPolicyResponse {
  regulatoryPolicies?: Array<RegulatoryPolicy>;
  warnings?: Array<Error>;
}

export interface ReturnPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  domestic?: ReturnPolicyDetails;
  international?: ReturnPolicyDetails;
  required?: boolean;
}

export interface ReturnPolicyDetails {
  policyDescriptionEnabled?: boolean;
  refundMethods?: Array<string>;
  returnMethods?: Array<string>;
  returnPeriods?: Array<TimeDuration>;
  returnsAcceptanceEnabled?: boolean;
  returnShippingCostPayers?: Array<string>;
}

export interface ReturnPolicyResponse {
  returnPolicies?: Array<ReturnPolicy>;
  warnings?: Array<Error>;
}

export interface SalesTaxJurisdiction {
  salesTaxJurisdictionId?: string;
}

export interface SalesTaxJurisdictions {
  salesTaxJurisdictions?: Array<SalesTaxJurisdiction>;
}

export interface ShippingCarrier {
  description?: string;
  shippingCarrier?: string;
}

export interface ShippingCarrierResponse {
  shippingCarriers?: Array<ShippingCarrier>;
}

export interface ShippingExcludeLocation {
  description?: string;
  location?: string;
  region?: string;
}

export interface ShippingExcludeLocationResponse {
  excludeShippingLocations?: Array<ShippingExcludeLocation>;
}

export interface ShippingHandlingTime {
  description?: string;
  extendedHandling?: boolean;
  maxHandlingTime?: number;
}

export interface ShippingHandlingTimeResponse {
  handlingTimes?: Array<ShippingHandlingTime>;
}

export interface ShippingLocation {
  description?: string;
  shippingLocation?: string;
}

export interface ShippingLocationResponse {
  shippingLocations?: Array<ShippingLocation>;
}

export interface ShippingPoliciesResponse {
  shippingPolicies?: Array<ShippingPolicy>;
  warnings?: Array<Error>;
}

export interface ShippingPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  globalShippingEnabled?: boolean;
  group1MaxFlatShippingCost?: Amount;
  group2MaxFlatShippingCost?: Amount;
  group3MaxFlatShippingCost?: Amount;
  handlingTimeEnabled?: boolean;
  maxFlatShippingCost?: Amount;
  shippingTermsRequired?: boolean;
}

export interface ShippingService {
  description?: string;
  internationalService?: boolean;
  maxShippingTime?: number;
  minShippingTime?: number;
  packageLimits?: PackageLimits;
  shippingCarrier?: string;
  shippingCategory?: string;
  shippingCostTypes?: Array<string>;
  shippingService?: string;
  validForSellingFlow?: boolean;
}

export interface ShippingServiceResponse {
  shippingServices?: Array<ShippingService>;
}

export interface SignalWord {
  signalWordId?: string;
  signalWordDescription?: string;
}

export interface SiteVisibilityPoliciesResponse {
  siteVisibilityPolicies?: Array<SiteVisibilityPolicy>;
  warnings?: Array<Error>;
}

export interface SiteVisibilityPolicy {
  categoryId?: string;
  categoryTreeId?: string;
  crossBorderTradeAustraliaEnabled?: boolean;
  crossBorderTradeGBEnabled?: boolean;
  crossBorderTradeNorthAmericaEnabled?: boolean;
}

export interface SortOrderInner {
  sortOrder?: SortOrderProperties;
  sortPriority?: string;
}

export interface SortOrderProperties {
  order?: string;
  propertyName?: string;
}

export interface SpecificationRequest {
  categoryId?: string;
  compatibilityPropertyFilters?: Array<PropertyFilterInner>;
  dataset?: string;
  datasetPropertyName?: Array<string>;
  exactMatch?: boolean;
  paginationInput?: PaginationInput;
  sortOrders?: Array<SortOrderInner>;
  specifications?: Array<PropertyFilterInner>;
}

export interface SpecificationResponse {
  compatibilityDetails?: Array<Compatibility>;
  pagination?: Pagination;
}

export interface TimeDuration {
  unit?: string;
  value?: number;
}
