// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Address {
  id?: number;
  country?: string;
  city?: string;
  postalCode?: string;
  firstName?: string;
  lastName?: string;
  company?: string;
  phoneNumber?: string;
  state?: string;
  street?: string;
  street2?: string;
}

export type AestheticGradeValue = 'PREMIUM' | 'EXCELLENT' | 'VERY_GOOD' | 'GOOD' | 'FAIR' | 'STALLONE';

export interface Attachment {
  msg?: number;
  group?: number;
  sender?: number;
  attachment?: string;
}

export interface Backbox {
  product: number;
  sku: string;
  price: number;
  quantity: number;
  buybox: boolean;
  price_for_buybox: number;
  currency: string;
  condition: ProductCondition;
  same_merchant_winner: boolean;
}

export interface BackboxPage {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<Backbox>;
}

export type BuybackAestheticGradeCode =
  | 'FUNCTIONAL_FLAWLESS'
  | 'FUNCTIONAL_GOOD'
  | 'FUNCTIONAL_USED'
  | 'FUNCTIONAL_CRACKED'
  | 'NOT_FUNCTIONAL_USED'
  | 'NOT_FUNCTIONAL_CRACKED';

export interface BuybackBasePaginated {
  count: number;
  next: string | null;
  previous: string | null;
}

export interface BuybackCompetitor {
  listing_id: string;
  product_id: string;
  market: MarketCode;
  price?: MonetaryAmount;
  price_to_win: MonetaryAmount;
  is_winning: boolean;
  winner_price: MonetaryAmount | null;
}

export type BuybackCounterOfferReasonCategory = 'functional' | 'esthetics' | 'other';

export interface BuybackCounterOfferReasonsInner {
  id: BuybackCounterOfferReasonCategory;
  label: string;
  reasons: Array<BuybackCounterOfferReasonsInnerReasonsInner>;
}

export interface BuybackCounterOfferReasonsInnerReasonsInner {
  id?: string;
  label?: string;
}

export type BuybackKycDocuments =
  | 'PASSPORT'
  | 'ID'
  | 'ID_CARD_FRONT'
  | 'ID_CARD_BACK'
  | 'BANK_STATEMENT'
  | 'DRIVING_LICENCE_FRONT'
  | 'DRIVING_LICENCE_BACK';

export interface BuybackListing {
  id: string;
  productId: string;
  prices: { [key: string]: MonetaryAmount };
  aestheticGradeCode: BuybackAestheticGradeCode;
  sku: string | null;
  markets: Array<string>;
}

export type BuybackListingGrade = 'DIAMOND' | 'PLATINUM' | 'GOLD' | 'SILVER' | 'BRONZE' | 'STALLONE';

export interface BuybackListingUpdate {
  prices?: { [key: string]: MonetaryAmount };
}

export interface BuybackMessage {
  body?: string;
  date: string;
  attachments?: Array<string>;
  author: BuybackMessageAuthor;
}

export type BuybackMessageAuthor = 'Merchant' | 'Client' | 'BackMarket' | 'Unknown';

export interface BuybackMessagePage {
  count: number;
  next: string | null;
  previous: string | null;
  results?: Set<BuybackMessage>;
}

export interface BuybackMessagePayload {
  message: string;
  files: Set<BuybackMessagePayloadFilesInner>;
}

export interface BuybackMessagePayloadFilesInner {
  name: string;
  content: string;
}

export interface BuybackOrder {
  orderPublicId: string;
  creationDate: string;
  modificationDate: string;
  shippingDate: string;
  suspensionDate?: string;
  receivalDate?: string;
  paymentDate?: string;
  counterProposalDate?: string;
  status: BuybackOrderState;
  market: string;
  transferCertificateLink: string;
  listing: BuybackOrderListing;
  customer: BuybackOrderCustomer;
  returnAddress: BuybackOrderReturnAddress;
  originalPrice: BuybackOrderOriginalPrice;
  counterOfferPrice?: BuybackOrderOriginalPrice;
  trackingNumber?: string;
  shipper?: string;
  suspendReasons?: Array<BuybackReason>;
  counterOfferReasons?: Array<BuybackReason>;
}

export interface BuybackOrderCustomer {
  firstName?: string;
  lastName?: string;
  phone?: string;
  dateOfBirth?: string;
  documents?: Array<BuybackOrderCustomerDocumentsInner>;
}

export interface BuybackOrderCustomerDocumentsInner {
  type: BuybackKycDocuments;
  url: string;
}

export interface BuybackOrderListing {
  sku?: string;
  productId: number;
  title: string;
  grade: BuybackListingGrade;
}

export interface BuybackOrderOriginalPrice {
  value: number;
  currency: string;
}

export interface BuybackOrderPage {
  count: number;
  next: string | null;
  previous: string | null;
  results?: Set<BuybackOrder>;
}

export interface BuybackOrderReturnAddress {
  address1?: string;
  address2?: string;
  city?: string;
  zipcode?: string;
  country: string;
}

export type BuybackOrderState =
  | 'NEW'
  | 'PENDING'
  | 'TO_SEND'
  | 'SENT'
  | 'RECEIVED'
  | 'COUNTER_PROPOSAL'
  | 'VALIDATED'
  | 'PAID'
  | 'MONEY_TRANSFERED'
  | 'SUSPENDED';

export interface BuybackOrderSuspensionPayload {
  reasons: Array<string>;
}

export interface BuybackPaginatedListingResponse {
  next: string | null;
  results: Array<BuybackListing>;
}

export interface BuybackReason {
  message: string;
  identifier: string;
  category?: string;
}

export interface CareAddress {
  company?: string;
  first_name?: string;
  last_name?: string;
  street?: string;
  street2?: string;
  postal_code?: string;
  country?: string;
  city?: string;
  phone?: string;
  email?: string;
  customer_id_number?: string;
}

export interface CareClient {
  id?: number;
  username?: string;
  first_name?: string;
  last_name?: string;
  email?: string;
}

export interface CareFolder {
  id?: number;
  client?: number;
  merchant?: number;
  orderline?: number;
  date_creation?: string;
  date_modification?: string;
  date_last_message?: string;
  date_closed?: string;
  state?: number;
  lines?: Array<number>;
  country_code?: string;
  backcare?: boolean;
}

export interface CareOrder {
  order_id?: number;
  shipping_address?: CareAddress;
  billing_address?: CareAddress;
  tracking_number?: string;
  tracking_url?: string;
  shipper?: number;
  shipper_display?: string;
  date_creation?: string;
  date_modification?: string;
  date_shipping?: string;
  date_payment?: string;
  state?: CareOrderStateEnum;
  price?: string;
  shipping_price?: string;
  currency?: string;
  country_code?: string;
}

export type CareOrderStateEnum = 0 | 1 | 3 | 8 | 9;

export interface CareOrderline {
  id?: number;
  order?: CareOrder;
  snapshot?: Snapshot;
  quantity?: number;
  price?: string;
  state?: number;
  trust_pack_plus?: boolean;
}

export interface Category3 {
  category_name?: string;
  parent?: Category3;
}

export interface CategoryTree {
  category_id: number;
  category_name: string;
  marketplace_category_id: number;
  is_leaf: boolean;
  attributes: Array<CategoryTreeAttributesInner>;
  childrens: Array<CategoryTree>;
}

export interface CategoryTreeAttributesInner {
  field: string;
  field_name: string;
  type: CategoryTreeAttributesInnerTypeEnum;
  allowed_values: string;
  required: boolean;
}

export type CategoryTreeAttributesInnerTypeEnum = 0 | 1 | 2 | 3;

export interface Claim {
  id?: number;
  tiles?: Array<Tile>;
  issues?: Array<Issue>;
  rate?: number;
  score?: number;
  state?: number;
  withdraw?: boolean;
  gras_savoye?: boolean;
  warnings?: Array<any>;
  resolution_choice?: ClaimResolutionChoiceEnum;
  declared_warranty_state?: ClaimDeclaredWarrantyStateEnum;
  return_labels?: Array<ReturnLabel>;
}

export type ClaimResolutionChoiceEnum = 'REMOTE_ASSISTANCE' | 'REPAIR' | 'REPLACE' | 'REPAIR_REPLACE' | 'REFUND';

export type ClaimDeclaredWarrantyStateEnum = 'IN_WARRANTY' | 'WATER_OR_DROPPED' | 'THIRD_PARTY_REPAIR';

export interface Competitor {
  is_winning: boolean;
  listing_id: string;
  min_price: MonetaryAmount | null;
  price: MonetaryAmount;
  price_to_win: MonetaryAmount;
  product_id: string;
  winner_price: MonetaryAmount | null;
  market: MarketCode;
}

export type CountryCode =
  | 'fr-fr'
  | 'fr-be'
  | 'es-es'
  | 'de-de'
  | 'de-at'
  | 'it-it'
  | 'ja-jp'
  | 'en-au'
  | 'en-gb'
  | 'en-us'
  | 'nl-nl'
  | 'pt-pt'
  | 'en-ie'
  | 'el-gr'
  | 'sk-sk'
  | 'sv-se';

export interface Delivery {
  order: number;
  shipmentId: number;
  carrierId: number;
  orderlines: Array<number>;
  referenceNumber: string;
  trackingNumber: string;
  trackingUrl: string;
  carrierName: string;
  hubScanned: boolean;
  invoicedCurrency: string;
  invoicedPrice: number;
  datePickup: string;
  dateCreation: string;
  dateDelivery: string;
  labelUrl: string;
  type: string;
  pickupInfo: PickupInfo;
}

export interface DeliveryPage {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<Delivery>;
}

export interface ErrorResponseV1 {
  error: Error;
  requestId?: string;
}

export interface ErrorResponseV2 {
  errors: Array<Error>;
  requestId?: string;
}

export interface ErrorResponseV3 {
  error: Error;
  status: number;
  title: string | null;
  type: string | null;
  requestId?: string;
}

export interface GetCareFolderDetailsResponse {
  backcare?: boolean;
  client?: CareClient;
  country_code?: string;
  date_closed?: string;
  date_creation?: string;
  date_last_message?: string;
  date_modification?: string;
  id?: number;
  lines?: Array<Claim>;
  merchant?: Seller;
  messages?: Array<Message>;
  orderline?: CareOrderline;
  state?: GetCareFolderDetailsResponseStateEnum;
}

export type GetCareFolderDetailsResponseStateEnum = 0 | 9;

export interface GetCareFolderListResponse {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results?: Array<CareFolder>;
}

export type IntegerOrString = number | string;

export interface Issue {
  customerIssue?: string;
  tag?: string;
}

export interface LightAttachment {
  id?: number;
  attachment?: string;
  date_creation?: string;
}

export interface ListingDetail {
  backmarket_id: number;
  comment: string | null;
  currency: string;
  id: string;
  listing_id: number;
  max_price: string;
  min_price: string | null;
  price: string;
  product_id: string;
  publication_state: ListingDetailPublicationStateEnum;
  quantity: number;
  shippings: Array<ListingPublicShippingsInner>;
  sku: string;
  state: ListingStateValue;
  grade: AestheticGradeValue;
  title: string;
  warranty_delay: number;
  new_battery?: boolean;
  outlet?: boolean;
  statuscode: number;
}

export type ListingDetailPublicationStateEnum = 0 | 1 | 2 | 3 | 4;

export interface ListingPage {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<ListingPublic>;
}

export type ListingPrice = number | string;

export interface ListingPublic {
  backmarket_id: number;
  comment: string | null;
  currency: string;
  id: string;
  listing_id: number;
  max_price: string;
  min_price: string | null;
  price: string;
  product_id: string;
  publication_state: ListingPublicPublicationStateEnum;
  quantity: number;
  shippings: Array<ListingPublicShippingsInner>;
  sku: string;
  state: ListingStateValue;
  grade: AestheticGradeValue;
  title: string;
  warranty_delay: number;
  new_battery?: boolean;
  outlet?: boolean;
}

export type ListingPublicPublicationStateEnum = 0 | 1 | 2 | 3 | 4;

export interface ListingPublicShippingsInner {
  country_code: string;
  shipper: string;
  shipper_display: string;
  shipping_delay: number;
  shipping_price: string;
}

export type ListingShippingPrice = number | string;

export type ListingStateValue = 9 | 0 | 1 | 2 | 3 | 4;

export interface ListingUpdate {
  price?: ListingPrice;
  currency?: string;
  comment?: string | null;
  warranty_delay?: IntegerOrString;
  quantity?: IntegerOrString;
  shipper_1?: Shipper | null;
  shipper_display_1?: string | null;
  shipping_delay_1?: number | null;
  shipping_price_1?: ListingShippingPrice | null;
  shipper_2?: Shipper | null;
  shipper_display_2?: string | null;
  shipping_delay_2?: number | null;
  shipping_price_2?: ListingShippingPrice | null;
  shipper_3?: Shipper | null;
  shipper_display_3?: string | null;
  shipping_delay_3?: number | null;
  shipping_price_3?: ListingShippingPrice | null;
  min_price?: ListingShippingPrice | null;
}

export interface ListingsBatch {
  bodymessage: number;
  statuscode: number;
}

export interface ListingsCatalog {
  catalog: string;
  quotechar: string;
  delimiter: string;
  encoding: string;
}

export type MarketCode =
  'FR' | 'BE' | 'DE' | 'IT' | 'ES' | 'GB' | 'AT' | 'NL' | 'US' | 'FI' | 'PT' | 'IE' | 'GR' | 'SK' | 'SE' | 'JP';

export interface Message {
  id?: number;
  message?: string;
  date_creation?: string;
  attachments?: Array<LightAttachment>;
  initiator?: string;
  kind?: string;
  is_informative?: boolean;
}

export interface ModelError {
  code: string;
  data?: object;
  docLink?: string;
  message: string;
  target?: string;
}

export interface MonetaryAmount {
  amount: string;
  currency: string;
}

export interface Order {
  order_id?: number;
  delivery_mode?: OrderDeliveryModeEnum;
  shipping_address?: Address;
  billing_address?: Address;
  delivery_note?: string;
  expected_dispatch_date?: string;
  tracking_number?: string;
  tracking_url?: string;
  shipper_display?: string;
  is_backship?: boolean;
  date_creation?: string;
  date_modification?: string;
  date_shipping?: string;
  date_payment?: string;
  state?: OrderState;
  orderlines?: Array<OrderLine>;
  price?: string;
  shipping_price?: string;
  currency?: string;
  country_code?: CountryCode;
  paypal_reference?: string | null;
  installment_payment?: boolean;
  payment_method?: string;
  sales_taxes?: string;
}

export type OrderDeliveryModeEnum = 'HOME_DELIVERY' | 'COLLECTION_POINT';

export interface OrderIdValidationError {
  error: OrderIdValidationErrorError;
  data: OrderIdValidationErrorData;
}

export interface OrderIdValidationErrorData {
  fields: object;
}

export interface OrderIdValidationErrorError {
  code: string;
  message: string;
}

export interface OrderLine {
  id?: number;
  date_creation?: string;
  state?: OrderLineState;
  price?: string;
  shipping_price?: string;
  shipping_delay?: number;
  currency?: string;
  return_reason?: ReturnReason;
  return_message?: string;
  listing?: string;
  listing_id?: number;
  orderline_fee?: string;
  product?: string;
  quantity?: number;
  brand?: string;
  product_id?: number;
  backcare?: boolean;
  backcare_price?: number;
  sales_taxes?: string;
  imei?: string;
  serial_number?: string;
  condition?: ProductCondition;
}

export type OrderLineState = 0 | 9 | 8 | 1 | 2 | 3 | 4 | 5 | 6 | 7;

export interface OrderLineUpdate {
  imei?: string;
  serial_number?: string;
}

export interface OrderPage {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results?: Array<Order>;
}

export type OrderState = 0 | 10 | 1 | 3 | 8 | 9;

export interface PickupInfo {
  confirmationNumber: string;
  datePickupActual: string;
  datePickupRangeStart: string;
  datePickupRangeEnd: string;
  datePickupRequested: string;
  isCanceled: boolean;
  pickupId: number;
}

export interface PostItemTransferCreateRequest {
  shipperName: string;
  trackingNumber: string;
  action?: PostItemTransferCreateRequestActionEnum;
}

export type PostItemTransferCreateRequestActionEnum = 'REPAIR' | 'REPLACE' | 'NOTHING';

export interface PostMessageResponse {
  attachment?: Attachment;
  attachments?: Array<Attachment>;
  date_creation?: string;
  group?: number;
  id?: number;
  message?: string;
  sender?: number;
}

export interface PostNoteRequest {
  note?: string | null;
}

export interface PostNoteResponse {
  note?: string | null;
}

export interface PostRefundCreateRequest {
  amount?: number;
  orderline_pk?: number;
  refund_type?: PostRefundCreateRequestRefundTypeEnum;
}

export type PostRefundCreateRequestRefundTypeEnum = 4 | 5 | 6;

export interface Problem {
  type: string;
  title: string;
  status: number;
  detail?: string;
  instance?: string;
}

export interface ProblemValidation {
  type: string;
  title: string;
  status: number;
  detail?: string;
  instance?: string;
  errors?: Array<ProblemValidationErrorMember>;
}

export interface ProblemValidationErrorMember {
  type: string;
  title: string;
  detail?: string;
  target: string;
  context?: object;
}

export interface Product {
  product_id?: number;
  category_3?: Category3;
}

export type ProductCondition = 9 | 10 | 11 | 12;

export interface ReturnLabel {
  date_creation?: string;
  state?: ReturnLabelStateEnum;
  label?: string;
  initiator?: ReturnLabelInitiatorEnum;
  kind?: ReturnLabelKindEnum;
}

export type ReturnLabelStateEnum = 'USED' | 'ALIVE' | 'EXPIRED';

export type ReturnLabelInitiatorEnum = 'Merchant' | 'BackMarket';

export type ReturnLabelKindEnum = 'UNSET' | 'CUSTOMER_TO_MERCHANT' | 'MERCHANT_TO_CUSTOMER';

export interface ReturnPage {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<ReturnShipment>;
}

export type ReturnReason = 0 | 1 | 11 | 12 | 13 | 21 | 22 | 23 | 24 | 25;

export interface ReturnShipment {
  orderId: number;
  orderlineId: number;
  shipmentId: number;
  carrierId: number;
  carrierName: string;
  dateCreation: string;
  referenceNumber: string;
  trackingNumber: string;
  trackingUrl: string;
  hubScanned: boolean;
  datePickup: string;
  dateDelivery: string;
  label: string;
  invoicedPrice: number;
  invoicedCurrency: string;
  type: string;
}

export interface Seller {
  id?: number;
  username?: string;
  first_name?: string;
  last_name?: string;
}

export type Shipper =
  | 'Allied Express'
  | 'Aramex Australia'
  | 'Australia Post'
  | 'Australia Post Express'
  | 'Austrian Post'
  | 'BPost'
  | 'BRT'
  | 'Chronopost'
  | 'Chronopost Express'
  | 'ColisPrivé'
  | 'Colissimo'
  | 'Correos'
  | 'Correos Express'
  | 'Couriers Please'
  | 'CTT'
  | 'Cubyn'
  | 'Cubyn Express'
  | 'DB Schenker'
  | 'Deutsche Post'
  | 'DHL'
  | 'DHL DE'
  | 'DHL Express'
  | 'DHL  EXPRESS'
  | 'DHL NL'
  | 'DHL Parcel Spain'
  | 'DHL SP'
  | 'DPD'
  | 'DPD Benelux'
  | 'DPD DE'
  | 'DPD FR'
  | 'DPD International'
  | 'DPD UK'
  | 'DPD UK Express'
  | 'DTDC Australia'
  | 'FedEx'
  | 'FedEx - 2Days'
  | 'FedEx Express'
  | 'FedEx International'
  | 'FedEx - Overnight'
  | 'Geodis'
  | 'Girard Agediss - Livraison dans la pièce de votre choix sur RDV'
  | 'GLS'
  | 'GLS - DE'
  | 'GLS - FR'
  | 'GLS International'
  | 'GLS - IT'
  | 'GLS-SPAIN'
  | 'GLS Spain Express'
  | 'Hermes - DE'
  | 'Hermes - UK'
  | 'Japan Post'
  | 'Livraison au pied du camion'
  | 'Livraison dans la pièce de votre choix'
  | 'Logoix'
  | 'MRW'
  | 'Murfy transporteur'
  | 'NACEX'
  | 'ParcelForce Express'
  | 'Parcelforce (Worldwide)'
  | 'Parcelpoint Pty Ltd'
  | 'Poste Italiane'
  | 'Post NL'
  | 'Private Transporter'
  | 'Royal Mail'
  | 'Royal Mail Express'
  | 'Sagawa'
  | 'Seino'
  | 'Sendle'
  | 'Seur'
  | 'Socolissimo'
  | 'Star Track Express'
  | 'TIPSA'
  | 'TIPSA Express'
  | 'TNT'
  | 'TNT Australia'
  | 'TNT Express'
  | 'Tourline'
  | 'UPS'
  | 'UPS 2 days'
  | 'UPS 2nd Day Air'
  | 'UPS Express'
  | 'UPS express save'
  | 'UPS Ground'
  | 'UPS next day'
  | 'UPS Overnight'
  | 'UPS standard'
  | 'USPS'
  | 'USPS Express'
  | 'USPS - First Class'
  | 'USPS - Priority Mail'
  | 'USPS - Priority Mail Express'
  | 'VIR'
  | 'Yamato'
  | 'Zeleris'
  | 'Other';

export interface Snapshot {
  id?: number;
  product?: Product;
  listing?: number;
  sku?: string;
  snowden?: boolean;
  image?: string;
}

export interface Task {
  task_id: number;
  action_status: TaskActionStatusEnum;
  last_action_error: string | null;
  result: any | null;
  statuscode: number;
}

export type TaskActionStatusEnum = 0 | 2 | 3 | 7 | 8 | 9;

export interface Tile {
  id?: number;
  name?: string;
}

export interface UpdateOrder {
  order_id: number;
  new_state: OrderLineState;
  sku?: string;
  imei?: string;
  serial_number?: string;
  tracking_number?: string;
  tracking_url?: string;
  vat_type?: VatType;
  date_shipping?: string;
  shipper?: string;
  return_reason?: ReturnReason;
  return_message?: string;
}

export interface UpdateWsSpecificListing200ResponseShippingsInner {
  shipping_price: string;
  shipping_delay: number;
  shipper: string;
  shipper_display: string;
  country_code: string;
}

export interface UpdatedListing {
  id: string;
  listing_id: number;
  product_id?: string;
  backmarket_id: number;
  title: string;
  shippings: Array<UpdateWsSpecificListing200ResponseShippingsInner>;
  state: ListingStateValue;
  grade: AestheticGradeValue;
  quantity: number;
  currency: string;
  sku: string;
  publication_state: UpdatedListingPublicationStateEnum;
  warranty_delay: number;
  price: string;
  comment: string | null;
  max_price: string;
  shippings_response?: Array<string>;
  statuscode: number;
  min_price: string | null;
}

export type UpdatedListingPublicationStateEnum = 0 | 1 | 2 | 3 | 4;

export interface UpdatedOrderLine {
  imei?: string;
  serial_number?: string;
}

export interface ValidationErrorResponseV3 {
  error: Error;
  status: number;
  title: string | null;
  type: string | null;
  requestId?: string;
  errors?: Array<ValidationErrorResponseV3AllOfErrors>;
}

export interface ValidationErrorResponseV3AllOfErrors {
  type: string;
  title: string;
  detail?: string;
  target: string;
  context?: object;
}

export type VatType = 'REGULAR' | 'MARGINAL';
