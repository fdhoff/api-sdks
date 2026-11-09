// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface AcceptPaymentDisputeRequest {
  returnAddress?: ReturnAddress;
  revision?: number;
}

export interface AddEvidencePaymentDisputeRequest {
  evidenceType?: string;
  files?: Array<FileEvidence>;
  lineItems?: Array<OrderLineItems>;
}

export interface AddEvidencePaymentDisputeResponse {
  evidenceId?: string;
}

export interface Address {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  countryCode?: string;
  county?: string;
  postalCode?: string;
  stateOrProvince?: string;
}

export interface Amount {
  convertedFromCurrency?: string;
  convertedFromValue?: string;
  currency?: string;
  value?: string;
}

export interface AppliedPromotion {
  description?: string;
  discountAmount?: Amount;
  promotionId?: string;
}

export interface AppointmentDetails {
  appointmentEndTime?: string;
  appointmentStartTime?: string;
  appointmentStatus?: string;
  appointmentType?: string;
  appointmentWindow?: string;
  serviceProviderAppointmentDate?: string;
}

export interface Buyer {
  buyerRegistrationAddress?: ExtendedContact;
  taxAddress?: TaxAddress;
  taxIdentifier?: TaxIdentifier;
  username?: string;
}

export interface CancelRequest {
  cancelCompletedDate?: string;
  cancelInitiator?: string;
  cancelReason?: string;
  cancelRequestedDate?: string;
  cancelRequestId?: string;
  cancelRequestState?: string;
}

export interface CancelStatus {
  cancelledDate?: string;
  cancelRequests?: Array<CancelRequest>;
  cancelState?: string;
}

export interface Charge {
  amount?: Amount;
  chargeType?: string;
}

export interface ContestPaymentDisputeRequest {
  note?: string;
  returnAddress?: ReturnAddress;
  revision?: number;
}

export interface DeliveryCost {
  discountAmount?: Amount;
  handlingCost?: Amount;
  importCharges?: Amount;
  shippingCost?: Amount;
  shippingIntermediationFee?: Amount;
}

export interface DisputeAmount {
  convertedFromCurrency?: string;
  convertedFromValue?: string;
  currency?: string;
  exchangeRate?: string;
  value?: string;
}

export interface DisputeEvidence {
  evidenceId?: string;
  evidenceType?: string;
  files?: Array<FileInfo>;
  lineItems?: Array<OrderLineItems>;
  providedDate?: string;
  requestDate?: string;
  respondByDate?: string;
  shipmentTracking?: Array<TrackingInfo>;
}

export interface DisputeSummaryResponse {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  paymentDisputeSummaries?: Array<PaymentDisputeSummary>;
  prev?: string;
  total?: number;
}

export interface EbayCollectAndRemitTax {
  amount?: Amount;
  ebayReference?: EbayTaxReference;
  taxType?: string;
  collectionMethod?: string;
}

export interface EbayCollectedCharges {
  ebayShipping?: Amount;
  charges?: Array<Charge>;
}

export interface EbayFulfillmentProgram {
  fulfilledBy?: string;
}

export interface EbayInternationalShipping {
  returnsManagedBy?: string;
}

export interface EbayShipping {
  shippingLabelProvidedBy?: string;
}

export interface EbayTaxReference {
  name?: string;
  value?: string;
}

export interface EbayVaultProgram {
  fulfillmentType?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface EvidenceRequest {
  evidenceId?: string;
  evidenceType?: string;
  lineItems?: Array<OrderLineItems>;
  requestDate?: string;
  respondByDate?: string;
}

export interface ExtendedContact {
  companyName?: string;
  contactAddress?: Address;
  email?: string;
  fullName?: string;
  primaryPhone?: PhoneNumber;
}

export interface FileEvidence {
  fileId?: string;
}

export interface FileInfo {
  fileId?: string;
  fileType?: string;
  name?: string;
  uploadedDate?: string;
}

export interface FulfillmentStartInstruction {
  appointment?: AppointmentDetails;
  ebaySupportedFulfillment?: boolean;
  finalDestinationAddress?: Address;
  fulfillmentInstructionsType?: string;
  maxEstimatedDeliveryDate?: string;
  minEstimatedDeliveryDate?: string;
  pickupStep?: PickupStep;
  shippingStep?: ShippingStep;
}

export interface GetOrder429Response {
  errors?: Array<Error>;
}

export interface GiftDetails {
  message?: string;
  recipientEmail?: string;
  senderName?: string;
}

export interface InfoFromBuyer {
  contentOnHold?: boolean;
  note?: string;
  returnShipmentTracking?: Array<TrackingInfo>;
}

export interface IssueRefundRequest {
  reasonForRefund?: string;
  comment?: string;
  refundItems?: Array<RefundItem>;
  orderLevelRefundAmount?: SimpleAmount;
}

export interface ItemLocation {
  countryCode?: string;
  location?: string;
  postalCode?: string;
}

export interface LegacyReference {
  legacyItemId?: string;
  legacyTransactionId?: string;
}

export interface LineItem {
  appliedPromotions?: Array<AppliedPromotion>;
  compatibilityProperties?: Array<Property>;
  deliveryCost?: DeliveryCost;
  discountedLineItemCost?: Amount;
  ebayCollectAndRemitTaxes?: Array<EbayCollectAndRemitTax>;
  ebayCollectedCharges?: EbayCollectedCharges;
  giftDetails?: GiftDetails;
  itemLocation?: ItemLocation;
  legacyItemId?: string;
  legacyVariationId?: string;
  lineItemCost?: Amount;
  lineItemFulfillmentInstructions?: LineItemFulfillmentInstructions;
  lineItemFulfillmentStatus?: string;
  lineItemId?: string;
  linkedOrderLineItems?: Array<LinkedOrderLineItem>;
  listingMarketplaceId?: string;
  properties?: LineItemProperties;
  purchaseMarketplaceId?: string;
  quantity?: number;
  refunds?: Array<LineItemRefund>;
  sku?: string;
  soldFormat?: string;
  taxes?: Array<Tax>;
  title?: string;
  total?: Amount;
  variationAspects?: Array<NameValuePair>;
}

export interface LineItemFulfillmentInstructions {
  guaranteedDelivery?: boolean;
  maxEstimatedDeliveryDate?: string;
  minEstimatedDeliveryDate?: string;
  shipByDate?: string;
}

export interface LineItemProperties {
  buyerProtection?: boolean;
  fromBestOffer?: boolean;
  soldViaAdCampaign?: boolean;
}

export interface LineItemReference {
  lineItemId?: string;
  quantity?: number;
}

export interface LineItemRefund {
  amount?: Amount;
  refundDate?: string;
  refundId?: string;
  refundReferenceId?: string;
}

export interface LinkedOrderLineItem {
  lineItemAspects?: Array<NameValuePair>;
  lineItemId?: string;
  maxEstimatedDeliveryDate?: string;
  minEstimatedDeliveryDate?: string;
  orderId?: string;
  sellerId?: string;
  shipments?: Array<TrackingInfo>;
  title?: string;
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

export interface MonetaryTransaction {
  date?: string;
  type?: string;
  reason?: string;
  amount?: DisputeAmount;
}

export interface NameValuePair {
  name?: string;
  value?: string;
}

export interface Order {
  buyer?: Buyer;
  buyerCheckoutNotes?: string;
  cancelStatus?: CancelStatus;
  creationDate?: string;
  ebayCollectAndRemitTax?: boolean;
  fulfillmentHrefs?: Array<string>;
  fulfillmentStartInstructions?: Array<FulfillmentStartInstruction>;
  lastModifiedDate?: string;
  lineItems?: Array<LineItem>;
  orderFulfillmentStatus?: string;
  orderId?: string;
  orderPaymentStatus?: string;
  paymentSummary?: PaymentSummary;
  pricingSummary?: PricingSummary;
  program?: Program;
  salesRecordReference?: string;
  sellerId?: string;
  totalFeeBasisAmount?: Amount;
  totalMarketplaceFee?: Amount;
}

export interface OrderLineItems {
  itemId?: string;
  lineItemId?: string;
}

export interface OrderRefund {
  amount?: Amount;
  refundDate?: string;
  refundId?: string;
  refundReferenceId?: string;
  refundStatus?: string;
}

export interface OrderSearchPagedCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  orders?: Array<Order>;
  prev?: string;
  total?: number;
  warnings?: Array<Error>;
}

export interface Payment {
  amount?: Amount;
  paymentDate?: string;
  paymentHolds?: Array<PaymentHold>;
  paymentMethod?: string;
  paymentReferenceId?: string;
  paymentStatus?: string;
}

export interface PaymentDispute {
  amount?: SimpleAmount;
  availableChoices?: Array<string>;
  buyerProvided?: InfoFromBuyer;
  buyerUsername?: string;
  closedDate?: string;
  evidence?: Array<DisputeEvidence>;
  evidenceRequests?: Array<EvidenceRequest>;
  lineItems?: Array<OrderLineItems>;
  monetaryTransactions?: Array<MonetaryTransaction>;
  note?: string;
  openDate?: string;
  orderId?: string;
  paymentDisputeId?: string;
  paymentDisputeStatus?: string;
  reason?: string;
  resolution?: PaymentDisputeOutcomeDetail;
  respondByDate?: string;
  returnAddress?: ReturnAddress;
  revision?: number;
  sellerResponse?: string;
}

export interface PaymentDisputeActivity {
  activityDate?: string;
  activityType?: string;
  actor?: string;
}

export interface PaymentDisputeActivityHistory {
  activity?: Array<PaymentDisputeActivity>;
}

export interface PaymentDisputeOutcomeDetail {
  fees?: SimpleAmount;
  protectedAmount?: SimpleAmount;
  protectionStatus?: string;
  reasonForClosure?: string;
  recoupAmount?: SimpleAmount;
  totalFeeCredit?: SimpleAmount;
}

export interface PaymentDisputeSummary {
  amount?: SimpleAmount;
  buyerUsername?: string;
  closedDate?: string;
  openDate?: string;
  orderId?: string;
  paymentDisputeId?: string;
  paymentDisputeStatus?: string;
  reason?: string;
  respondByDate?: string;
}

export interface PaymentHold {
  expectedReleaseDate?: string;
  holdAmount?: Amount;
  holdReason?: string;
  holdState?: string;
  releaseDate?: string;
  sellerActionsToRelease?: Array<SellerActionsToRelease>;
}

export interface PaymentSummary {
  payments?: Array<Payment>;
  refunds?: Array<OrderRefund>;
  totalDueSeller?: Amount;
}

export interface Phone {
  countryCode?: string;
  number?: string;
}

export interface PhoneNumber {
  phoneNumber?: string;
}

export interface PickupStep {
  merchantLocationKey?: string;
}

export interface PostSaleAuthenticationProgram {
  outcomeReason?: string;
  status?: string;
}

export interface PricingSummary {
  adjustment?: Amount;
  deliveryCost?: Amount;
  deliveryDiscount?: Amount;
  fee?: Amount;
  priceDiscount?: Amount;
  priceSubtotal?: Amount;
  tax?: Amount;
  total?: Amount;
}

export interface Program {
  authenticityVerification?: PostSaleAuthenticationProgram;
  ebayShipping?: EbayShipping;
  ebayVault?: EbayVaultProgram;
  ebayInternationalShipping?: EbayInternationalShipping;
  fulfillmentProgram?: EbayFulfillmentProgram;
}

export interface Property {
  propertyDisplayName?: string;
  propertyName?: string;
  propertyValue?: string;
}

export interface Refund {
  refundId?: string;
  refundStatus?: string;
}

export interface RefundItem {
  refundAmount?: SimpleAmount;
  lineItemId?: string;
  legacyReference?: LegacyReference;
}

export interface ReturnAddress {
  addressLine1?: string;
  addressLine2?: string;
  city?: string;
  country?: string;
  county?: string;
  fullName?: string;
  postalCode?: string;
  primaryPhone?: Phone;
  stateOrProvince?: string;
}

export interface SellerActionsToRelease {
  sellerActionToRelease?: string;
}

export interface ShippingFulfillment {
  fulfillmentId?: string;
  lineItems?: Array<LineItemReference>;
  shipmentTrackingNumber?: string;
  shippedDate?: string;
  shippingCarrierCode?: string;
}

export interface ShippingFulfillmentDetails {
  lineItems?: Array<LineItemReference>;
  shippedDate?: string;
  shippingCarrierCode?: string;
  trackingNumber?: string;
}

export interface ShippingFulfillmentPagedCollection {
  fulfillments?: Array<ShippingFulfillment>;
  total?: number;
  warnings?: Array<Error>;
}

export interface ShippingStep {
  shippingCarrierCode?: string;
  shippingServiceCode?: string;
  shipTo?: ExtendedContact;
  shipToReferenceId?: string;
}

export interface SimpleAmount {
  currency?: string;
  value?: string;
}

export interface Tax {
  amount?: Amount;
  taxType?: string;
}

export interface TaxAddress {
  city?: string;
  countryCode?: string;
  postalCode?: string;
  stateOrProvince?: string;
}

export interface TaxIdentifier {
  taxpayerId?: string;
  taxIdentifierType?: string;
  issuingCountry?: string;
}

export interface TrackingInfo {
  shipmentTrackingNumber?: string;
  shippingCarrierCode?: string;
}

export interface UpdateEvidencePaymentDisputeRequest {
  evidenceId?: string;
  evidenceType?: string;
  files?: Array<FileEvidence>;
  lineItems?: Array<OrderLineItems>;
}
