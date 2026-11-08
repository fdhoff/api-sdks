// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface BuyerTaxonomyNode {
  id?: number;
  level?: number;
  name?: string;
  parent_id?: number | null;
  children?: Array<BuyerTaxonomyNode>;
  full_path_taxonomy_ids?: Array<number>;
}

export interface BuyerTaxonomyNodeProperties {
  count?: number;
  results?: Array<BuyerTaxonomyNodeProperty>;
}

export interface BuyerTaxonomyNodeProperty {
  property_id?: number;
  name?: string;
  display_name?: string;
  scales?: Array<BuyerTaxonomyPropertyScale>;
  is_required?: boolean;
  supports_attributes?: boolean;
  supports_variations?: boolean;
  is_multivalued?: boolean;
  max_values_allowed?: number | null;
  possible_values?: Array<BuyerTaxonomyPropertyValue>;
  selected_values?: Array<BuyerTaxonomyPropertyValue>;
}

export interface BuyerTaxonomyNodes {
  count?: number;
  results?: Array<BuyerTaxonomyNode>;
}

export interface BuyerTaxonomyPropertyScale {
  scale_id?: number;
  display_name?: string;
  description?: string;
}

export interface BuyerTaxonomyPropertyValue {
  value_id?: number | null;
  name?: string;
  scale_id?: number | null;
  equal_to?: Array<number>;
}

export interface CreateReceiptShipmentRequest {
  tracking_code?: string;
  carrier_name?: string;
  send_bcc?: boolean;
  note_to_buyer?: string;
  mail_class?: string | null;
  weight?: number | null;
  weight_units?: string | null;
  length?: number | null;
  width?: number | null;
  height?: number | null;
  dimension_units?: string | null;
  shipping_label_cost?: number | null;
  shipping_label_currency?: string | null;
  revenue_eligibility?: string | null;
  ship_from_country?: string | null;
  ship_to_country?: string | null;
  incoterm?: string | null;
  customs_data?: Array<CreateReceiptShipmentRequestCustomsDataInner> | null;
  duty_amount?: number | null;
  duty_currency?: string | null;
  ship_date?: string | null;
}

export interface CreateReceiptShipmentRequestCustomsDataInner {
  country_of_origin: string | null;
  declared_value: number | null;
  HS_code: string | null;
}

export interface ErrorSchema {
  error: string;
}

export interface ListingBuyerPrice {
  base_price?: Money;
  shipping_cost?: Money | null;
  is_free_shipping?: boolean;
  original_price?: Money;
  discounted_price?: Money | null;
  discount_amount?: Money | null;
  discount_percentage?: number | null;
  has_discount?: boolean;
  discount_start_epoch?: number | null;
  discount_end_epoch?: number | null;
}

export interface ListingImage {
  listing_id?: number;
  listing_image_id?: number;
  hex_code?: string | null;
  red?: number | null;
  green?: number | null;
  blue?: number | null;
  hue?: number | null;
  saturation?: number | null;
  brightness?: number | null;
  is_black_and_white?: boolean | null;
  creation_tsz?: number;
  created_timestamp?: number;
  rank?: number;
  url_75x75?: string;
  url_170x135?: string;
  url_570xN?: string;
  url_fullxfull?: string;
  full_height?: number | null;
  full_width?: number | null;
  alt_text?: string | null;
}

export interface ListingImages {
  count?: number;
  results?: Array<ListingImage>;
}

export interface ListingInventory {
  products?: Array<ListingInventoryProduct>;
  price_on_property?: Array<number>;
  quantity_on_property?: Array<number>;
  sku_on_property?: Array<number>;
  readiness_state_on_property?: Array<number>;
}

export interface ListingInventoryProduct {
  product_id?: number;
  sku?: string;
  is_deleted?: boolean;
  offerings?: Array<ListingInventoryProductOffering>;
  property_values?: Array<ListingPropertyValue>;
}

export interface ListingInventoryProductOffering {
  offering_id?: number;
  quantity?: number;
  is_enabled?: boolean;
  is_deleted?: boolean;
  price?: Money;
  readiness_state_id?: number | null;
}

export interface ListingInventoryWithAssociations {
  products?: Array<ListingInventoryProduct>;
  price_on_property?: Array<number>;
  quantity_on_property?: Array<number>;
  sku_on_property?: Array<number>;
  readiness_state_on_property?: Array<number>;
  listing?: ShopListing;
}

export interface ListingPersonalization {
  personalization_questions?: Array<PersonalizationQuestion>;
}

export interface ListingPropertyValue {
  property_id?: number;
  property_name?: string | null;
  scale_id?: number | null;
  scale_name?: string | null;
  value_ids?: Array<number>;
  values?: Array<string>;
}

export interface ListingPropertyValues {
  count?: number;
  results?: Array<ListingPropertyValue>;
}

export interface ListingReview {
  shop_id?: number;
  listing_id?: number;
  rating?: number;
  review?: string | null;
  language?: string;
  image_url_fullxfull?: string | null;
  create_timestamp?: number;
  created_timestamp?: number;
  update_timestamp?: number;
  updated_timestamp?: number;
}

export interface ListingReviews {
  count?: number;
  results?: Array<ListingReview>;
}

export interface ListingTranslation {
  listing_id?: number;
  language?: string;
  title?: string | null;
  description?: string | null;
  tags?: Array<string>;
}

export interface ListingTranslations {
  de?: ListingTranslation | null;
  en_GB?: ListingTranslation | null;
  en_IN?: ListingTranslation | null;
  en_US?: ListingTranslation | null;
  es?: ListingTranslation | null;
  fr?: ListingTranslation | null;
  it?: ListingTranslation | null;
  ja?: ListingTranslation | null;
  nl?: ListingTranslation | null;
  pl?: ListingTranslation | null;
  pt?: ListingTranslation | null;
  ru?: ListingTranslation | null;
  sv?: ListingTranslation | null;
}

export interface ListingVariationImage {
  property_id?: number;
  value_id?: number;
  value?: string | null;
  image_id?: number;
}

export interface ListingVariationImages {
  count?: number;
  results?: Array<ListingVariationImage>;
}

export interface ListingVideo {
  video_id?: number;
  height?: number;
  width?: number;
  thumbnail_url?: string;
  video_url?: string;
  video_state?: ListingVideoVideoStateEnum;
}

export type ListingVideoVideoStateEnum = 'active' | 'inactive' | 'deleted' | 'flagged';

export interface ListingVideos {
  count?: number;
  results?: Array<ListingVideo>;
}

export interface Me {
  user_id?: number;
  shop_id?: number;
}

export interface Money {
  amount?: number;
  divisor?: number;
  currency_code?: string;
}

export interface Payment {
  payment_id?: number;
  buyer_user_id?: number;
  shop_id?: number;
  receipt_id?: number;
  amount_gross?: Money;
  amount_fees?: Money;
  amount_net?: Money;
  posted_gross?: Money | null;
  posted_fees?: Money | null;
  posted_net?: Money | null;
  adjusted_gross?: Money | null;
  adjusted_fees?: Money | null;
  adjusted_net?: Money | null;
  currency?: string;
  shop_currency?: string | null;
  buyer_currency?: string | null;
  shipping_user_id?: number | null;
  shipping_address_id?: number;
  billing_address_id?: number;
  status?: string;
  shipped_timestamp?: number | null;
  create_timestamp?: number;
  created_timestamp?: number;
  update_timestamp?: number;
  updated_timestamp?: number;
  payment_adjustments?: Array<PaymentAdjustment>;
}

export interface PaymentAccountLedgerEntries {
  count?: number;
  results?: Array<PaymentAccountLedgerEntry>;
}

export interface PaymentAccountLedgerEntry {
  entry_id?: number;
  ledger_id?: number;
  sequence_number?: number;
  amount?: number;
  currency?: string;
  description?: string;
  balance?: number;
  create_date?: number;
  created_timestamp?: number;
  ledger_type?: string;
  reference_type?: string;
  reference_id?: string | null;
  parent_entry_id?: number;
  payment_adjustments?: Array<PaymentAdjustment>;
}

export interface PaymentAdjustment {
  payment_adjustment_id?: number;
  payment_id?: number;
  status?: string;
  is_success?: boolean;
  user_id?: number;
  reason_code?: string;
  total_adjustment_amount?: number | null;
  shop_total_adjustment_amount?: number | null;
  buyer_total_adjustment_amount?: number | null;
  total_fee_adjustment_amount?: number | null;
  create_timestamp?: number;
  created_timestamp?: number;
  update_timestamp?: number;
  updated_timestamp?: number;
  payment_adjustment_items?: Array<PaymentAdjustmentItem>;
}

export interface PaymentAdjustmentItem {
  payment_adjustment_id?: number;
  payment_adjustment_item_id?: number;
  adjustment_type?: string | null;
  amount?: number;
  shop_amount?: number;
  transaction_id?: number | null;
  bill_payment_id?: number | null;
  created_timestamp?: number;
  updated_timestamp?: number;
}

export interface Payments {
  count?: number;
  results?: Array<Payment>;
}

export interface PersonalizationQuestion {
  question_id?: number | null;
  question_text?: string;
  instructions?: string | null;
  question_type?: string;
  required?: boolean;
  max_allowed_characters?: number | null;
  max_allowed_files?: number | null;
  add_on_price?: Money | null;
  options?: Array<PersonalizationQuestionOptionsInner> | null;
}

export interface PersonalizationQuestionOptionsInner {
  option_id: number | null;
  label: string;
}

export interface Pong {
  application_id?: number;
}

export interface SellerTaxonomyNode {
  id?: number;
  level?: number;
  name?: string;
  parent_id?: number | null;
  children?: Array<SellerTaxonomyNode>;
  full_path_taxonomy_ids?: Array<number>;
}

export interface SellerTaxonomyNodes {
  count?: number;
  results?: Array<SellerTaxonomyNode>;
}

export interface ShippingCarrier {
  shipping_carrier_id?: number;
  name?: string;
  domestic_classes?: Array<ShippingCarrierMailClass>;
  international_classes?: Array<ShippingCarrierMailClass>;
}

export interface ShippingCarrierMailClass {
  mail_class_key?: string;
  name?: string;
}

export interface ShippingCarriers {
  count?: number;
  results?: Array<ShippingCarrier>;
}

export interface Shop {
  shop_id?: number;
  user_id?: number;
  shop_name?: string;
  create_date?: number;
  created_timestamp?: number;
  title?: string | null;
  announcement?: string | null;
  currency_code?: string;
  is_vacation?: boolean;
  vacation_message?: string | null;
  sale_message?: string | null;
  digital_sale_message?: string | null;
  update_date?: number;
  updated_timestamp?: number;
  listing_active_count?: number;
  digital_listing_count?: number;
  login_name?: string;
  accepts_custom_requests?: boolean;
  policy_welcome?: string | null;
  policy_payment?: string | null;
  policy_shipping?: string | null;
  policy_refunds?: string | null;
  policy_additional?: string | null;
  policy_seller_info?: string | null;
  policy_update_date?: number;
  policy_has_private_receipt_info?: boolean;
  has_unstructured_policies?: boolean;
  policy_privacy?: string | null;
  vacation_autoreply?: string | null;
  url?: string;
  image_url_760x100?: string | null;
  num_favorers?: number;
  languages?: Array<string>;
  icon_url_fullxfull?: string | null;
  is_using_structured_policies?: boolean;
  has_onboarded_structured_policies?: boolean;
  include_dispute_form_link?: boolean;
  is_direct_checkout_onboarded?: boolean;
  is_etsy_payments_onboarded?: boolean;
  is_calculated_eligible?: boolean;
  is_opted_in_to_buyer_promise?: boolean;
  is_shop_us_based?: boolean;
  transaction_sold_count?: number;
  shipping_from_country_iso?: string | null;
  shop_location_country_iso?: string | null;
  review_count?: number | null;
  review_average?: number | null;
}

export interface ShopEconomicOperator {
  economic_operator_id?: number;
  shop_id?: number;
  operator_name?: string;
  email?: string;
  trademark_name?: string | null;
  first_line?: string | null;
  second_line?: string | null;
  city?: string | null;
  state?: string | null;
  zip?: string | null;
  country_iso?: string | null;
  phone?: string | null;
  phone_country_iso?: string | null;
  create_date?: number;
  update_date?: number;
}

export interface ShopEconomicOperators {
  count?: number;
  results?: Array<ShopEconomicOperator>;
}

export interface ShopHolidayPreference {
  shop_id?: number;
  holiday_id?: ShopHolidayPreferenceHolidayIdEnum;
  country_iso?: string;
  is_working?: boolean;
  holiday_name?: string;
}

export type ShopHolidayPreferenceHolidayIdEnum =
  | 1
  | 2
  | 3
  | 4
  | 5
  | 6
  | 7
  | 8
  | 9
  | 10
  | 11
  | 12
  | 13
  | 14
  | 15
  | 16
  | 17
  | 18
  | 19
  | 20
  | 21
  | 22
  | 23
  | 24
  | 25
  | 26
  | 27
  | 28
  | 29
  | 30
  | 31
  | 32
  | 33
  | 34
  | 35
  | 36
  | 37
  | 38
  | 39
  | 40
  | 41
  | 42
  | 43
  | 44
  | 45
  | 46
  | 47
  | 48
  | 49
  | 50
  | 51
  | 52
  | 53
  | 54
  | 55
  | 56
  | 57
  | 58
  | 59
  | 60
  | 61
  | 62
  | 63
  | 64
  | 65
  | 66
  | 67
  | 68
  | 69
  | 70
  | 71
  | 72
  | 73
  | 74
  | 75
  | 76
  | 77
  | 78
  | 79
  | 80
  | 81
  | 82
  | 83
  | 84
  | 85
  | 86
  | 87
  | 88
  | 89
  | 90
  | 91
  | 92
  | 93
  | 94
  | 95
  | 96
  | 97
  | 98
  | 99
  | 100
  | 101
  | 102
  | 103
  | 104
  | 105;

export interface ShopListing {
  listing_id?: number;
  user_id?: number;
  shop_id?: number;
  title?: string;
  description?: string;
  state?: ShopListingStateEnum;
  creation_timestamp?: number;
  created_timestamp?: number;
  ending_timestamp?: number;
  original_creation_timestamp?: number;
  last_modified_timestamp?: number;
  updated_timestamp?: number;
  state_timestamp?: number | null;
  quantity?: number;
  shop_section_id?: number | null;
  featured_rank?: number;
  url?: string;
  num_favorers?: number;
  non_taxable?: boolean;
  is_taxable?: boolean;
  is_customizable?: boolean;
  is_personalizable?: boolean;
  listing_type?: ShopListingListingTypeEnum;
  tags?: Array<string>;
  materials?: Array<string>;
  shipping_profile_id?: number | null;
  return_policy_id?: number | null;
  processing_min?: number | null;
  processing_max?: number | null;
  who_made?: ShopListingWhoMadeEnum | null;
  when_made?: ShopListingWhenMadeEnum | null;
  is_supply?: boolean | null;
  item_weight?: number | null;
  item_weight_unit?: ShopListingItemWeightUnitEnum | null;
  item_length?: number | null;
  item_width?: number | null;
  item_height?: number | null;
  item_dimensions_unit?: ShopListingItemDimensionsUnitEnum | null;
  is_private?: boolean;
  style?: Array<string>;
  file_data?: string | null;
  has_variations?: boolean;
  should_auto_renew?: boolean;
  language?: string | null;
  price?: Money;
  converted_price?: Money | null;
  taxonomy_id?: number | null;
  readiness_state_id?: number | null;
  suggested_title?: string | null;
  ecgt_garan_brand?: string | null;
  ecgt_garan_years?: number | null;
  ecgt_garan_model?: string | null;
  ecgt_garan_guarantee_details?: string | null;
  ecgt_other_commercial_guarantee_details?: string | null;
  ecgt_after_sales_service_info?: string | null;
  ecgt_software_update_details?: string | null;
  ecgt_commercial_guarantee_enabled?: boolean | null;
  gpsr_manufacturer_type?: ShopListingGpsrManufacturerTypeEnum | null;
  gpsr_manufacturer_id?: number | null;
  gpsr_responsible_person_type?: ShopListingGpsrResponsiblePersonTypeEnum | null;
  gpsr_responsible_person_id?: number | null;
  gpsr_serial_number?: string | null;
  gpsr_safety_warnings?: string | null;
}

export type ShopListingStateEnum = 'active' | 'inactive' | 'sold_out' | 'draft' | 'removed' | 'expired';

export type ShopListingListingTypeEnum = 'physical' | 'download' | 'both';

export type ShopListingWhoMadeEnum = 'i_did' | 'someone_else' | 'collective';

export type ShopListingWhenMadeEnum =
  | 'made_to_order'
  | '2020_2026'
  | '2010_2019'
  | '2007_2009'
  | 'before_2007'
  | '2000_2006'
  | '1990s'
  | '1980s'
  | '1970s'
  | '1960s'
  | '1950s'
  | '1940s'
  | '1930s'
  | '1920s'
  | '1910s'
  | '1900s'
  | '1800s'
  | '1700s'
  | 'before_1700';

export type ShopListingItemWeightUnitEnum = 'oz' | 'lb' | 'g' | 'kg';

export type ShopListingItemDimensionsUnitEnum = 'in' | 'ft' | 'mm' | 'cm' | 'm' | 'yd' | 'inches';

export type ShopListingGpsrManufacturerTypeEnum = 'seller' | 'economic_operator';

export type ShopListingGpsrResponsiblePersonTypeEnum = 'seller' | 'economic_operator';

export interface ShopListingFile {
  listing_file_id?: number;
  listing_id?: number;
  rank?: number;
  filename?: string;
  filesize?: string;
  size_bytes?: number;
  filetype?: string;
  create_timestamp?: number;
  created_timestamp?: number;
}

export interface ShopListingFiles {
  count?: number;
  results?: Array<ShopListingFile>;
}

export interface ShopListingWithAssociations {
  listing_id?: number;
  user_id?: number;
  shop_id?: number;
  title?: string;
  description?: string;
  state?: ShopListingWithAssociationsStateEnum;
  creation_timestamp?: number;
  created_timestamp?: number;
  ending_timestamp?: number;
  original_creation_timestamp?: number;
  last_modified_timestamp?: number;
  updated_timestamp?: number;
  state_timestamp?: number | null;
  quantity?: number;
  shop_section_id?: number | null;
  featured_rank?: number;
  url?: string;
  num_favorers?: number;
  non_taxable?: boolean;
  is_taxable?: boolean;
  is_customizable?: boolean;
  is_personalizable?: boolean;
  listing_type?: ShopListingWithAssociationsListingTypeEnum;
  tags?: Array<string>;
  materials?: Array<string>;
  shipping_profile_id?: number | null;
  return_policy_id?: number | null;
  processing_min?: number | null;
  processing_max?: number | null;
  who_made?: ShopListingWithAssociationsWhoMadeEnum | null;
  when_made?: ShopListingWithAssociationsWhenMadeEnum | null;
  is_supply?: boolean | null;
  item_weight?: number | null;
  item_weight_unit?: ShopListingWithAssociationsItemWeightUnitEnum | null;
  item_length?: number | null;
  item_width?: number | null;
  item_height?: number | null;
  item_dimensions_unit?: ShopListingWithAssociationsItemDimensionsUnitEnum | null;
  is_private?: boolean;
  style?: Array<string>;
  file_data?: string | null;
  has_variations?: boolean;
  should_auto_renew?: boolean;
  language?: string | null;
  price?: Money;
  converted_price?: Money | null;
  taxonomy_id?: number | null;
  readiness_state_id?: number | null;
  suggested_title?: string | null;
  ecgt_garan_brand?: string | null;
  ecgt_garan_years?: number | null;
  ecgt_garan_model?: string | null;
  ecgt_garan_guarantee_details?: string | null;
  ecgt_other_commercial_guarantee_details?: string | null;
  ecgt_after_sales_service_info?: string | null;
  ecgt_software_update_details?: string | null;
  ecgt_commercial_guarantee_enabled?: boolean | null;
  gpsr_manufacturer_type?: ShopListingWithAssociationsGpsrManufacturerTypeEnum | null;
  gpsr_manufacturer_id?: number | null;
  gpsr_responsible_person_type?: ShopListingWithAssociationsGpsrResponsiblePersonTypeEnum | null;
  gpsr_responsible_person_id?: number | null;
  gpsr_serial_number?: string | null;
  gpsr_safety_warnings?: string | null;
  shipping_profile?: ShopShippingProfile | null;
  user?: User | null;
  shop?: Shop | null;
  images?: Array<ListingImage>;
  videos?: Array<ListingVideo>;
  inventory?: ListingInventory | null;
  production_partners?: Array<ShopProductionPartner>;
  skus?: Array<string>;
  translations?: ListingTranslations | null;
  views?: number;
  personalization?: ListingPersonalization | null;
  buyer_price?: ListingBuyerPrice | null;
}

export type ShopListingWithAssociationsStateEnum = 'active' | 'inactive' | 'sold_out' | 'draft' | 'removed' | 'expired';

export type ShopListingWithAssociationsListingTypeEnum = 'physical' | 'download' | 'both';

export type ShopListingWithAssociationsWhoMadeEnum = 'i_did' | 'someone_else' | 'collective';

export type ShopListingWithAssociationsWhenMadeEnum =
  | 'made_to_order'
  | '2020_2026'
  | '2010_2019'
  | '2007_2009'
  | 'before_2007'
  | '2000_2006'
  | '1990s'
  | '1980s'
  | '1970s'
  | '1960s'
  | '1950s'
  | '1940s'
  | '1930s'
  | '1920s'
  | '1910s'
  | '1900s'
  | '1800s'
  | '1700s'
  | 'before_1700';

export type ShopListingWithAssociationsItemWeightUnitEnum = 'oz' | 'lb' | 'g' | 'kg';

export type ShopListingWithAssociationsItemDimensionsUnitEnum = 'in' | 'ft' | 'mm' | 'cm' | 'm' | 'yd' | 'inches';

export type ShopListingWithAssociationsGpsrManufacturerTypeEnum = 'seller' | 'economic_operator';

export type ShopListingWithAssociationsGpsrResponsiblePersonTypeEnum = 'seller' | 'economic_operator';

export interface ShopListings {
  count?: number;
  results?: Array<ShopListing>;
}

export interface ShopListingsWithAssociations {
  count?: number;
  results?: Array<ShopListingWithAssociations>;
}

export interface ShopProcessingProfile {
  shop_id?: number;
  readiness_state_id?: number;
  readiness_state?: ShopProcessingProfileReadinessStateEnum;
  min_processing_days?: number;
  max_processing_days?: number;
  processing_days_display_label?: string;
}

export type ShopProcessingProfileReadinessStateEnum = 'ready_to_ship' | 'made_to_order';

export interface ShopProcessingProfiles {
  count?: number;
  results?: Array<ShopProcessingProfile>;
}

export interface ShopProductionPartner {
  production_partner_id?: number;
  partner_name?: string;
  location?: string;
}

export interface ShopProductionPartners {
  count?: number;
  results?: Array<ShopProductionPartner>;
}

export interface ShopReceipt {
  receipt_id?: number;
  receipt_type?: number;
  seller_user_id?: number;
  seller_email?: string | null;
  buyer_user_id?: number;
  buyer_email?: string | null;
  name?: string;
  first_line?: string | null;
  second_line?: string | null;
  city?: string | null;
  state?: string | null;
  zip?: string | null;
  status?: ShopReceiptStatusEnum;
  formatted_address?: string | null;
  country_iso?: string | null;
  payment_method?: string;
  payment_email?: string | null;
  message_from_seller?: string | null;
  message_from_buyer?: string | null;
  message_from_payment?: string | null;
  is_paid?: boolean;
  is_shipped?: boolean;
  create_timestamp?: number;
  created_timestamp?: number;
  update_timestamp?: number;
  updated_timestamp?: number;
  is_gift?: boolean;
  gift_message?: string;
  gift_sender?: string;
  grandtotal?: Money;
  subtotal?: Money;
  total_price?: Money;
  total_shipping_cost?: Money;
  total_tax_cost?: Money;
  total_vat_cost?: Money;
  discount_amt?: Money;
  gift_wrap_price?: Money;
  shipments?: Array<ShopReceiptShipment>;
  transactions?: Array<ShopReceiptTransaction>;
  refunds?: Array<ShopRefund>;
}

export type ShopReceiptStatusEnum =
  'paid' | 'completed' | 'open' | 'payment processing' | 'canceled' | 'fully refunded' | 'partially refunded';

export interface ShopReceiptShipment {
  receipt_shipping_id?: number | null;
  shipment_notification_timestamp?: number;
  carrier_name?: string;
  tracking_code?: string;
}

export interface ShopReceiptTransaction {
  transaction_id?: number;
  title?: string | null;
  description?: string | null;
  seller_user_id?: number;
  buyer_user_id?: number;
  create_timestamp?: number;
  created_timestamp?: number;
  paid_timestamp?: number | null;
  shipped_timestamp?: number | null;
  quantity?: number;
  listing_image_id?: number | null;
  receipt_id?: number;
  is_digital?: boolean;
  file_data?: string;
  listing_id?: number | null;
  transaction_type?: string;
  product_id?: number | null;
  sku?: string | null;
  price?: Money;
  shipping_cost?: Money;
  variations?: Array<TransactionVariations>;
  product_data?: Array<ListingPropertyValue>;
  shipping_profile_id?: number | null;
  min_processing_days?: number | null;
  max_processing_days?: number | null;
  shipping_method?: string | null;
  shipping_upgrade?: string | null;
  expected_ship_date?: number | null;
  buyer_coupon?: number;
  shop_coupon?: number;
}

export interface ShopReceiptTransactions {
  count?: number;
  results?: Array<ShopReceiptTransaction>;
}

export interface ShopReceipts {
  count?: number;
  results?: Array<ShopReceipt>;
}

export interface ShopRefund {
  amount?: Money;
  created_timestamp?: number;
  reason?: string | null;
  note_from_issuer?: string | null;
  status?: string | null;
}

export interface ShopReturnPolicies {
  count?: number;
  results?: Array<ShopReturnPolicy>;
}

export interface ShopReturnPolicy {
  return_policy_id?: number;
  shop_id?: number;
  accepts_returns?: boolean;
  accepts_exchanges?: boolean;
  return_deadline?: number | null;
}

export interface ShopSection {
  shop_section_id?: number;
  title?: string;
  rank?: number;
  user_id?: number;
  active_listing_count?: number;
}

export interface ShopSections {
  count?: number;
  results?: Array<ShopSection>;
}

export interface ShopShippingProfile {
  shipping_profile_id?: number;
  title?: string | null;
  user_id?: number;
  origin_country_iso?: string;
  is_deleted?: boolean;
  shipping_profile_destinations?: Array<ShopShippingProfileDestination>;
  shipping_profile_upgrades?: Array<ShopShippingProfileUpgrade>;
  origin_postal_code?: string | null;
  profile_type?: ShopShippingProfileProfileTypeEnum;
  domestic_handling_fee?: number;
  international_handling_fee?: number;
}

export type ShopShippingProfileProfileTypeEnum = 'manual' | 'calculated';

export interface ShopShippingProfileDestination {
  shipping_profile_destination_id?: number;
  shipping_profile_id?: number;
  origin_country_iso?: string;
  destination_country_iso?: string;
  destination_region?: ShopShippingProfileDestinationDestinationRegionEnum;
  primary_cost?: Money;
  secondary_cost?: Money;
  shipping_carrier_id?: number | null;
  mail_class?: string | null;
  min_delivery_days?: number | null;
  max_delivery_days?: number | null;
}

export type ShopShippingProfileDestinationDestinationRegionEnum = 'eu' | 'non_eu' | 'none';

export interface ShopShippingProfileDestinations {
  count?: number;
  results?: Array<ShopShippingProfileDestination>;
}

export interface ShopShippingProfileUpgrade {
  shipping_profile_id?: number;
  upgrade_id?: number;
  upgrade_name?: string;
  type?: ShopShippingProfileUpgradeTypeEnum;
  rank?: number;
  language?: string;
  price?: Money;
  secondary_price?: Money;
  shipping_carrier_id?: number | null;
  mail_class?: string | null;
  min_delivery_days?: number | null;
  max_delivery_days?: number | null;
}

export type ShopShippingProfileUpgradeTypeEnum = 0 | 1;

export interface ShopShippingProfileUpgrades {
  count?: number;
  results?: Array<ShopShippingProfileUpgrade>;
}

export interface ShopShippingProfiles {
  count?: number;
  results?: Array<ShopShippingProfile>;
}

export interface Shops {
  count?: number;
  results?: Array<Shop>;
}

export interface TaxonomyNodeProperties {
  count?: number;
  results?: Array<TaxonomyNodeProperty>;
}

export interface TaxonomyNodeProperty {
  property_id?: number;
  name?: string;
  display_name?: string;
  scales?: Array<TaxonomyPropertyScale>;
  is_required?: boolean;
  supports_attributes?: boolean;
  supports_variations?: boolean;
  is_multivalued?: boolean;
  max_values_allowed?: number | null;
  possible_values?: Array<TaxonomyPropertyValue>;
  selected_values?: Array<TaxonomyPropertyValue>;
}

export interface TaxonomyPropertyScale {
  scale_id?: number;
  display_name?: string;
  description?: string;
}

export interface TaxonomyPropertyValue {
  value_id?: number | null;
  name?: string;
  scale_id?: number | null;
  equal_to?: Array<number>;
}

export interface TransactionReview {
  shop_id?: number;
  listing_id?: number;
  transaction_id?: number;
  buyer_user_id?: number | null;
  rating?: number;
  review?: string;
  language?: string;
  image_url_fullxfull?: string | null;
  create_timestamp?: number;
  created_timestamp?: number;
  update_timestamp?: number;
  updated_timestamp?: number;
}

export interface TransactionReviews {
  count?: number;
  results?: Array<TransactionReview>;
}

export interface TransactionVariations {
  property_id?: number;
  value_id?: number | null;
  formatted_name?: string;
  formatted_value?: string;
  question_id?: number | null;
  mime_type?: TransactionVariationsMimeTypeEnum | null;
}

export type TransactionVariationsMimeTypeEnum =
  'image/jpeg' | 'image/png' | 'image/gif' | 'image/svg+xml' | 'image/heif' | 'image/heic' | 'application/pdf';

export interface TypeDiscriminator {
  __type: string;
}

export interface UpdateListingInventoryRequest {
  products: Array<UpdateListingInventoryRequestProductsInner>;
  price_on_property?: Array<number>;
  quantity_on_property?: Array<number>;
  sku_on_property?: Array<number>;
  readiness_state_on_property?: Array<number> | null;
}

export interface UpdateListingInventoryRequestProductsInner {
  sku?: string | null;
  property_values?: Array<UpdateListingInventoryRequestProductsInnerPropertyValuesInner>;
  offerings: Array<UpdateListingInventoryRequestProductsInnerOfferingsInner>;
}

export interface UpdateListingInventoryRequestProductsInnerOfferingsInner {
  price: number;
  quantity: number;
  is_enabled: boolean;
  readiness_state_id: number | null;
}

export interface UpdateListingInventoryRequestProductsInnerPropertyValuesInner {
  property_id: number;
  value_ids: Array<number>;
  scale_id?: number | null;
  property_name?: string;
  values: Array<string>;
}

export interface UpdateListingPersonalizationRequest {
  personalization_questions: Array<UpdateListingPersonalizationRequestPersonalizationQuestionsInner>;
}

export interface UpdateListingPersonalizationRequestPersonalizationQuestionsInner {
  question_id?: number | null;
  question_text: string;
  instructions?: string | null;
  question_type: UpdateListingPersonalizationRequestPersonalizationQuestionsInnerQuestionTypeEnum;
  required: boolean;
  max_allowed_files?: number | null;
  max_allowed_characters?: number | null;
  options?: Array<UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner> | null;
  add_on_price?: number | null;
}

export type UpdateListingPersonalizationRequestPersonalizationQuestionsInnerQuestionTypeEnum =
  'text_input' | 'dropdown' | 'unlabeled_upload' | 'labeled_upload';

export interface UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner {
  option_id?: number | null;
  label: string;
}

export interface UpdateVariationImagesRequest {
  variation_images: Array<UpdateVariationImagesRequestVariationImagesInner>;
}

export interface UpdateVariationImagesRequestVariationImagesInner {
  property_id: number;
  value_id: number;
  image_id: number;
}

export interface User {
  user_id?: number;
  primary_email?: string | null;
  first_name?: string | null;
  last_name?: string | null;
  image_url_75x75?: string | null;
}

export interface UserAddress {
  user_address_id?: number;
  user_id?: number;
  name?: string;
  first_line?: string;
  second_line?: string | null;
  city?: string;
  state?: string | null;
  zip?: string | null;
  iso_country_code?: string | null;
  country_name?: string | null;
  is_default_shipping_address?: boolean;
}

export interface UserAddresses {
  count?: number;
  results?: Array<UserAddress>;
}
