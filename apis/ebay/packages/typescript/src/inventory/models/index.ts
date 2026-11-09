// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Address {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  country?: string;
  county?: string;
  postalCode?: string;
  stateOrProvince?: string;
}

export interface Amount {
  currency?: string;
  value?: string;
}

export interface Availability {
  pickupAtLocationAvailability?: Array<PickupAtLocationAvailability>;
  shipToLocationAvailability?: ShipToLocationAvailability;
}

export interface AvailabilityDistribution {
  fulfillmentTime?: TimeDuration;
  merchantLocationKey?: string;
  quantity?: number;
}

export interface AvailabilityWithAll {
  pickupAtLocationAvailability?: Array<PickupAtLocationAvailability>;
  shipToLocationAvailability?: ShipToLocationAvailabilityWithAll;
}

export interface BaseResponse {
  warnings?: Array<Error>;
}

export interface BestOffer {
  autoAcceptPrice?: Amount;
  autoDeclinePrice?: Amount;
  bestOfferEnabled?: boolean;
}

export interface BulkCreateOrReplaceInventoryItem429Response {
  errors?: Array<Error>;
}

export interface BulkEbayOfferDetailsWithKeys {
  requests?: Array<EbayOfferDetailsWithKeys>;
}

export interface BulkGetInventoryItem {
  requests?: Array<GetInventoryItem>;
}

export interface BulkGetInventoryItemResponse {
  responses?: Array<GetInventoryItemResponse>;
}

export interface BulkInventoryItem {
  requests?: Array<InventoryItemWithSkuLocale>;
}

export interface BulkInventoryItemResponse {
  responses?: Array<InventoryItemResponse>;
}

export interface BulkMigrateListing {
  requests?: Array<MigrateListing>;
}

export interface BulkMigrateListingResponse {
  responses?: Array<MigrateListingResponse>;
}

export interface BulkOffer {
  requests?: Array<OfferKeyWithId>;
}

export interface BulkOfferResponse {
  responses?: Array<OfferSkuResponse>;
}

export interface BulkPriceQuantity {
  requests?: Array<PriceQuantity>;
}

export interface BulkPriceQuantityResponse {
  responses?: Array<PriceQuantityResponse>;
}

export interface BulkPublishResponse {
  responses?: Array<OfferResponseWithListingId>;
}

export interface Charity {
  charityId?: string;
  donationPercentage?: string;
}

export interface Compatibility {
  compatibleProducts?: Array<CompatibleProduct>;
  sku?: string;
}

export interface CompatibleProduct {
  compatibilityProperties?: Array<NameValueList>;
  notes?: string;
  productFamilyProperties?: ProductFamilyProperties;
  productIdentifier?: ProductIdentifier;
}

export interface ConditionDescriptor {
  additionalInfo?: string;
  name?: string;
  values?: Array<string>;
}

export interface CountryPolicy {
  country?: string;
  policyIds?: Array<string>;
}

export interface Dimension {
  height?: number;
  length?: number;
  unit?: string;
  width?: number;
}

export interface Document {
  documentId?: string;
}

export interface EbayOfferDetailsWithAll {
  availableQuantity?: number;
  categoryId?: string;
  charity?: Charity;
  extendedProducerResponsibility?: ExtendedProducerResponsibility;
  format?: string;
  hideBuyerDetails?: boolean;
  includeCatalogProductDetails?: boolean;
  listing?: ListingDetails;
  listingDescription?: string;
  listingDuration?: string;
  listingPolicies?: ListingPolicies;
  listingStartDate?: string;
  lotSize?: number;
  marketplaceId?: string;
  merchantLocationKey?: string;
  offerId?: string;
  pricingSummary?: PricingSummary;
  quantityLimitPerBuyer?: number;
  regulatory?: Regulatory;
  secondaryCategoryId?: string;
  sku?: string;
  status?: string;
  storeCategoryNames?: Array<string>;
  tax?: Tax;
}

export interface EbayOfferDetailsWithId {
  availableQuantity?: number;
  categoryId?: string;
  charity?: Charity;
  extendedProducerResponsibility?: ExtendedProducerResponsibility;
  hideBuyerDetails?: boolean;
  includeCatalogProductDetails?: boolean;
  listingDescription?: string;
  listingDuration?: string;
  listingPolicies?: ListingPolicies;
  listingStartDate?: string;
  lotSize?: number;
  merchantLocationKey?: string;
  pricingSummary?: PricingSummary;
  quantityLimitPerBuyer?: number;
  regulatory?: Regulatory;
  secondaryCategoryId?: string;
  storeCategoryNames?: Array<string>;
  tax?: Tax;
}

export interface EbayOfferDetailsWithKeys {
  availableQuantity?: number;
  categoryId?: string;
  charity?: Charity;
  extendedProducerResponsibility?: ExtendedProducerResponsibility;
  format?: string;
  hideBuyerDetails?: boolean;
  includeCatalogProductDetails?: boolean;
  listingDescription?: string;
  listingDuration?: string;
  listingPolicies?: ListingPolicies;
  listingStartDate?: string;
  lotSize?: number;
  marketplaceId?: string;
  merchantLocationKey?: string;
  pricingSummary?: PricingSummary;
  quantityLimitPerBuyer?: number;
  regulatory?: Regulatory;
  secondaryCategoryId?: string;
  sku?: string;
  storeCategoryNames?: Array<string>;
  tax?: Tax;
}

export interface EnergyEfficiencyLabel {
  imageDescription?: string;
  imageURL?: string;
  productInformationSheet?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface ExtendedProducerResponsibility {
  ecoParticipationFee?: Amount;
  producerProductId?: string;
  productDocumentationId?: string;
  productPackageId?: string;
  shipmentPackageId?: string;
}

export interface Fee {
  amount?: Amount;
  feeType?: string;
  promotionalDiscount?: Amount;
}

export interface FeeSummary {
  fees?: Array<Fee>;
  marketplaceId?: string;
  warnings?: Array<Error>;
}

export interface FeesSummaryResponse {
  feeSummaries?: Array<FeeSummary>;
}

export interface FormatAllocation {
  auction?: number;
  fixedPrice?: number;
}

export interface FulfillmentCenterSpecifications {
  sameDayShippingCutOffTimes?: SameDayShippingCutOffTimes;
}

export interface GeoCoordinates {
  latitude?: number;
  longitude?: number;
}

export interface GetInventoryItem {
  sku?: string;
}

export interface GetInventoryItemResponse {
  errors?: Array<Error>;
  inventoryItem?: InventoryItemWithSkuLocaleGroupKeys;
  sku?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface Hazmat {
  component?: string;
  pictograms?: Array<string>;
  signalWord?: string;
  statements?: Array<string>;
}

export interface Interval {
  close?: string;
  open?: string;
}

export interface InventoryItem {
  availability?: Availability;
  condition?: string;
  conditionDescription?: string;
  conditionDescriptors?: Array<ConditionDescriptor>;
  packageWeightAndSize?: PackageWeightAndSize;
  product?: Product;
}

export interface InventoryItemGroup {
  aspects?: string;
  description?: string;
  imageUrls?: Array<string>;
  inventoryItemGroupKey?: string;
  subtitle?: string;
  title?: string;
  variantSKUs?: Array<string>;
  variesBy?: VariesBy;
  videoIds?: Array<string>;
}

export interface InventoryItemListing {
  offerId?: string;
  sku?: string;
}

export interface InventoryItemResponse {
  errors?: Array<Error>;
  locale?: string;
  sku?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface InventoryItemWithSkuLocale {
  availability?: Availability;
  condition?: string;
  conditionDescription?: string;
  conditionDescriptors?: Array<ConditionDescriptor>;
  locale?: string;
  packageWeightAndSize?: PackageWeightAndSize;
  product?: Product;
  sku?: string;
}

export interface InventoryItemWithSkuLocaleGroupKeys {
  availability?: AvailabilityWithAll;
  condition?: string;
  conditionDescription?: string;
  conditionDescriptors?: Array<ConditionDescriptor>;
  inventoryItemGroupKeys?: Array<string>;
  locale?: string;
  packageWeightAndSize?: PackageWeightAndSize;
  product?: Product;
  sku?: string;
}

export interface InventoryItemWithSkuLocaleGroupid {
  availability?: AvailabilityWithAll;
  condition?: string;
  conditionDescription?: string;
  conditionDescriptors?: Array<ConditionDescriptor>;
  groupIds?: Array<string>;
  inventoryItemGroupKeys?: Array<string>;
  locale?: string;
  packageWeightAndSize?: PackageWeightAndSize;
  product?: Product;
  sku?: string;
}

export interface InventoryItems {
  href?: string;
  inventoryItems?: Array<InventoryItemWithSkuLocaleGroupid>;
  limit?: number;
  next?: string;
  prev?: string;
  size?: number;
  total?: number;
}

export interface InventoryLocation {
  location?: LocationDetails;
  locationAdditionalInformation?: string;
  locationInstructions?: string;
  locationTypes?: Array<string>;
  locationWebUrl?: string;
  name?: string;
  operatingHours?: Array<OperatingHours>;
  phone?: string;
  specialHours?: Array<SpecialHours>;
  timeZoneId?: string;
  fulfillmentCenterSpecifications?: FulfillmentCenterSpecifications;
}

export interface InventoryLocationFull {
  location?: LocationDetails;
  locationAdditionalInformation?: string;
  locationInstructions?: string;
  locationTypes?: Array<string>;
  locationWebUrl?: string;
  merchantLocationStatus?: string;
  name?: string;
  operatingHours?: Array<OperatingHours>;
  phone?: string;
  specialHours?: Array<SpecialHours>;
  timeZoneId?: string;
  fulfillmentCenterSpecifications?: FulfillmentCenterSpecifications;
}

export interface InventoryLocationResponse {
  location?: Location;
  locationAdditionalInformation?: string;
  locationInstructions?: string;
  locationTypes?: Array<string>;
  locationWebUrl?: string;
  merchantLocationKey?: string;
  merchantLocationStatus?: string;
  name?: string;
  operatingHours?: Array<OperatingHours>;
  phone?: string;
  specialHours?: Array<SpecialHours>;
  timeZoneId?: string;
  fulfillmentCenterSpecifications?: FulfillmentCenterSpecifications;
}

export interface ListingDetails {
  listingId?: string;
  listingOnHold?: boolean;
  listingStatus?: string;
  soldQuantity?: number;
}

export interface ListingPolicies {
  bestOfferTerms?: BestOffer;
  eBayPlusIfEligible?: boolean;
  fulfillmentPolicyId?: string;
  paymentPolicyId?: string;
  productCompliancePolicyIds?: Array<string>;
  regionalProductCompliancePolicies?: RegionalProductCompliancePolicies;
  regionalTakeBackPolicies?: RegionalTakeBackPolicies;
  returnPolicyId?: string;
  shippingCostOverrides?: Array<ShippingCostOverride>;
  takeBackPolicyId?: string;
}

export interface Location {
  address?: Address;
  geoCoordinates?: GeoCoordinates;
  locationId?: string;
}

export interface LocationAvailabilityDetails {
  merchantLocationKey?: string;
}

export interface LocationDetails {
  address?: Address;
  geoCoordinates?: GeoCoordinates;
}

export interface LocationMapping {
  locations?: Array<LocationAvailabilityDetails>;
}

export interface LocationResponse {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
  locations?: Array<InventoryLocationResponse>;
}

export interface Manufacturer {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  companyName?: string;
  contactUrl?: string;
  country?: string;
  email?: string;
  phone?: string;
  postalCode?: string;
  stateOrProvince?: string;
}

export interface MigrateListing {
  listingId?: string;
}

export interface MigrateListingResponse {
  errors?: Array<Error>;
  inventoryItemGroupKey?: string;
  inventoryItems?: Array<InventoryItemListing>;
  listingId?: string;
  marketplaceId?: string;
  statusCode?: number;
  warnings?: Array<Error>;
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

export interface NameValueList {
  name?: string;
  value?: string;
}

export interface OfferKeyWithId {
  offerId?: string;
}

export interface OfferKeysWithId {
  offers?: Array<OfferKeyWithId>;
}

export interface OfferPriceQuantity {
  availableQuantity?: number;
  offerId?: string;
  price?: Amount;
}

export interface OfferResponse {
  offerId?: string;
  warnings?: Array<Error>;
}

export interface OfferResponseWithListingId {
  errors?: Array<Error>;
  listingId?: string;
  offerId?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface OfferSkuResponse {
  errors?: Array<Error>;
  format?: string;
  marketplaceId?: string;
  offerId?: string;
  sku?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface Offers {
  href?: string;
  limit?: number;
  next?: string;
  offers?: Array<EbayOfferDetailsWithAll>;
  prev?: string;
  size?: number;
  total?: number;
}

export interface OperatingHours {
  dayOfWeekEnum?: string;
  intervals?: Array<Interval>;
}

export interface Overrides {
  cutOffTime?: string;
  endDate?: string;
  startDate?: string;
}

export interface PackageWeightAndSize {
  dimensions?: Dimension;
  packageType?: string;
  shippingIrregular?: boolean;
  weight?: Weight;
}

export interface PickupAtLocationAvailability {
  availabilityType?: string;
  fulfillmentTime?: TimeDuration;
  merchantLocationKey?: string;
  quantity?: number;
}

export interface PriceQuantity {
  offers?: Array<OfferPriceQuantity>;
  shipToLocationAvailability?: ShipToLocationAvailability;
  sku?: string;
}

export interface PriceQuantityResponse {
  errors?: Array<Error>;
  offerId?: string;
  sku?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface PricingSummary {
  auctionReservePrice?: Amount;
  auctionStartPrice?: Amount;
  minimumAdvertisedPrice?: Amount;
  originallySoldForRetailPriceOn?: string;
  originalRetailPrice?: Amount;
  price?: Amount;
  pricingVisibility?: string;
}

export interface Product {
  aspects?: string;
  brand?: string;
  description?: string;
  ean?: Array<string>;
  epid?: string;
  imageUrls?: Array<string>;
  isbn?: Array<string>;
  mpn?: string;
  subtitle?: string;
  title?: string;
  upc?: Array<string>;
  videoIds?: Array<string>;
}

export interface ProductFamilyProperties {
  engine?: string;
  make?: string;
  model?: string;
  trim?: string;
  year?: string;
}

export interface ProductIdentifier {
  epid?: string;
  gtin?: string;
  ktype?: string;
}

export interface ProductSafety {
  component?: string;
  pictograms?: Array<string>;
  statements?: Array<string>;
}

export interface PublishByInventoryItemGroupRequest {
  inventoryItemGroupKey?: string;
  marketplaceId?: string;
}

export interface PublishResponse {
  listingId?: string;
  warnings?: Array<Error>;
}

export interface RegionalProductCompliancePolicies {
  countryPolicies?: Array<CountryPolicy>;
}

export interface RegionalTakeBackPolicies {
  countryPolicies?: Array<CountryPolicy>;
}

export interface Regulatory {
  documents?: Array<Document>;
  energyEfficiencyLabel?: EnergyEfficiencyLabel;
  hazmat?: Hazmat;
  manufacturer?: Manufacturer;
  productSafety?: ProductSafety;
  repairScore?: number;
  responsiblePersons?: Array<ResponsiblePerson>;
}

export interface ResponsiblePerson {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  companyName?: string;
  contactUrl?: string;
  country?: string;
  email?: string;
  phone?: string;
  postalCode?: string;
  stateOrProvince?: string;
  types?: Array<string>;
}

export interface SameDayShippingCutOffTimes {
  overrides?: Array<Overrides>;
  weeklySchedule?: Array<WeeklySchedule>;
}

export interface ShipToLocationAvailability {
  availabilityDistributions?: Array<AvailabilityDistribution>;
  quantity?: number;
}

export interface ShipToLocationAvailabilityWithAll {
  allocationByFormat?: FormatAllocation;
  availabilityDistributions?: Array<AvailabilityDistribution>;
  quantity?: number;
}

export interface ShippingCostOverride {
  additionalShippingCost?: Amount;
  priority?: number;
  shippingCost?: Amount;
  shippingServiceType?: string;
  surcharge?: Amount;
}

export interface SpecialHours {
  date?: string;
  intervals?: Array<Interval>;
}

export interface Specification {
  name?: string;
  values?: Array<string>;
}

export interface Tax {
  applyTax?: boolean;
  thirdPartyTaxCategory?: string;
  vatPercentage?: number;
}

export interface TimeDuration {
  unit?: string;
  value?: number;
}

export interface VariesBy {
  aspectsImageVariesBy?: Array<string>;
  specifications?: Array<Specification>;
}

export interface Version {
  instance?: Version;
  version?: string;
}

export interface WeeklySchedule {
  cutOffTime?: string;
  dayOfWeekEnum?: Array<string>;
}

export interface Weight {
  unit?: string;
  value?: number;
}

export interface WithdrawByInventoryItemGroupRequest {
  inventoryItemGroupKey?: string;
  marketplaceId?: string;
}

export interface WithdrawResponse {
  listingId?: string;
  warnings?: Array<Error>;
}
