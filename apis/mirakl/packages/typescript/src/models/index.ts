// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface A01Response200 {
  applicable_taxes?: Array<A01Response200ApplicableTaxes>;
  approval_delay?: number;
  approval_rate?: number;
  banner?: string;
  billing_info: A01Response200BillingInfo;
  channels: Array<string>;
  closed_from?: string;
  closed_to?: string;
  contact_informations: A01Response200ContactInformations;
  currency_iso_code: string;
  date_created: string;
  default_billing_information: A01Response200DefaultBillingInformation;
  description?: string;
  domains: Array<string>;
  dropship?: A01Response200Dropship;
  evaluations_count: number;
  free_shipping: boolean;
  grade?: number;
  is_professional: boolean;
  kyc?: A01Response200Kyc;
  last_updated_date: string;
  logo?: string;
  model?: string;
  offers_count: number;
  order_messages_response_delay?: number;
  orders_count: number;
  payment_details: A01Response200PaymentDetails;
  payment_info?: A01Response200PaymentInfo;
  payment_method_mandatory: boolean;
  premium: boolean;
  pro_details: A01Response200ProDetails;
  producer_identifiers?: Array<A01Response200ProducerIdentifiers>;
  recycling_policy?: string;
  return_policy?: string;
  shipping: A01Response200Shipping;
  shipping_country?: string;
  shipping_types: Array<string>;
  shipping_zones: Array<string>;
  shippings?: Array<A01Response200Shippings>;
  shop_additional_fields: Array<A01Response200ShopAdditionalFields>;
  shop_id: number;
  shop_name: string;
  shop_state: string;
  specific_billing_informations?: Array<A01Response200SpecificBillingInformations>;
  suspension_type?: string;
}

export interface A01Response200ApplicableTaxes {
  code: string;
  fee_types?: Array<string>;
  label: string;
}

export interface A01Response200BillingInfo {
  bank_city?: string;
  bank_name?: string;
  bank_street?: string;
  bic?: string;
  iban?: string;
  owner?: string;
  zip_code?: string;
}

export interface A01Response200ContactInformations {
  city: string;
  civility?: string;
  country: string;
  email: string;
  fax?: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1: string;
  street2?: string;
  web_site?: string;
  zip_code?: string;
}

export interface A01Response200DefaultBillingInformation {
  corporate_information?: A01Response200DefaultBillingInformationCorporateInformation;
  default_language: string;
  fiscal_information?: A01Response200DefaultBillingInformationFiscalInformation;
  fiscal_representative?: A01Response200DefaultBillingInformationFiscalRepresentative;
  id: string;
  personal_information?: A01Response200DefaultBillingInformationPersonalInformation;
  registration_address: A01Response200DefaultBillingInformationRegistrationAddress;
}

export interface A01Response200DefaultBillingInformationCorporateInformation {
  company_registration_name?: string;
  company_registration_number?: string;
  complementary_information?: A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation;
  electronic_address?: string;
  phone_number?: string;
}

export interface A01Response200DefaultBillingInformationCorporateInformationComplementaryInformation {
  business_activity_code?: string;
  company_registration_city?: string;
  company_registration_province?: string;
  company_shareholders?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  share_capital?: number;
  share_capital_currency?: string;
  sole_trader?: boolean;
}

export interface A01Response200DefaultBillingInformationFiscalInformation {
  local_tax_number?: string;
  tax_identification_country?: string;
  tax_identification_number?: string;
}

export interface A01Response200DefaultBillingInformationFiscalRepresentative {
  city: string;
  civility: string;
  company_registration_name: string;
  company_registration_number: string;
  country_iso_code: string;
  first_name: string;
  last_name: string;
  local_tax_number?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A01Response200DefaultBillingInformationPersonalInformation {
  birth_city?: string;
  birth_country?: string;
  birth_date?: string;
  civility?: string;
  first_name?: string;
  last_name?: string;
}

export interface A01Response200DefaultBillingInformationRegistrationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A01Response200Dropship {
  retail_pricing_edition_enabled: boolean;
}

export interface A01Response200Kyc {
  reason?: string;
  status: string;
}

export interface A01Response200PaymentDetails {
  paid_balance: number;
  payable_balance: number;
  pending_balance: number;
  reserve_balance?: number;
  reserve_target?: number;
  sub_balances?: Array<A01Response200PaymentDetailsSubBalances>;
}

export interface A01Response200PaymentDetailsSubBalances {
  paid: number;
  pay_out_psp_code: string;
  payable: number;
  pending: number;
}

export interface A01Response200PaymentInfo {
  at_type?: string;
  owner: string;
}

export interface A01Response200PaymentInfoAba extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  routing_number: string;
}

export interface A01Response200PaymentInfoAubsb extends A01Response200PaymentInfo {
  auban: string;
  aubsb: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A01Response200PaymentInfoBrazilian extends A01Response200PaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  pix_key?: string;
}

export interface A01Response200PaymentInfoCanadian extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  institution_number: string;
  swift_code?: string;
  transit_number: string;
}

export interface A01Response200PaymentInfoColombian extends A01Response200PaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A01Response200PaymentInfoGuatemalan extends A01Response200PaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A01Response200PaymentInfoHk extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code: string;
}

export interface A01Response200PaymentInfoIban extends A01Response200PaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic: string;
  iban: string;
}

export interface A01Response200PaymentInfoIndian extends A01Response200PaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  indian_financial_system_code: string;
  swift_code?: string;
}

export interface A01Response200PaymentInfoIsraeli extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A01Response200PaymentInfoJapanese extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  branch_name: string;
  swift_code?: string;
}

export interface A01Response200PaymentInfoMexican extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  clabe: string;
}

export interface A01Response200PaymentInfoNuban extends A01Response200PaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nuban: string;
}

export interface A01Response200PaymentInfoNzbsb extends A01Response200PaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nzban: string;
  nzbsb: string;
}

export interface A01Response200PaymentInfoPayout extends A01Response200PaymentInfo {
  bank_account_number?: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
  payout_format: string;
  sort_code?: string;
}

export interface A01Response200PaymentInfoPhilippines extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A01Response200PaymentInfoSerbian extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_branch_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
}

export interface A01Response200PaymentInfoSg {
  bank_account_number: string;
  bank_city?: string;
  bank_key?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  owner: string;
  swift_code: string;
}

export interface A01Response200PaymentInfoTaiwanese extends A01Response200PaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A01Response200PaymentInfoThai extends A01Response200PaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A01Response200PaymentInfoUk extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_sort_code: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code?: string;
}

export interface A01Response200PaymentInfoUruguayan extends A01Response200PaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A01Response200PaymentInfoVietnamese extends A01Response200PaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A01Response200ProDetails {
  VAT_number?: string;
  corporate_name?: string;
  identification_number?: string;
  tax_identification_number?: string;
}

export interface A01Response200ProducerIdentifiers {
  epr_category_code: string;
  producer_id: string;
}

export interface A01Response200Shipping {
  lead_time_to_ship?: number;
}

export interface A01Response200Shippings {
  additional_fields?: Array<A01Response200ShippingsAdditionalFields>;
  shipping_free_amount?: number;
  shipping_type_code: string;
  shipping_type_label: string;
  shipping_type_standard_code?: string;
  shipping_zone_code: string;
  shipping_zone_label: string;
}

export interface A01Response200ShippingsAdditionalFields {
  code: string;
  type?: string;
}

export interface A01Response200ShippingsAdditionalFieldsBoolean extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsDate extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsLink extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsList extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsMultipleValuesList extends A01Response200ShippingsAdditionalFields {
  value: Array<string>;
}

export interface A01Response200ShippingsAdditionalFieldsNumeric extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsRegex extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsString extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShippingsAdditionalFieldsTextarea extends A01Response200ShippingsAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFields {
  code: string;
  type?: string;
}

export interface A01Response200ShopAdditionalFieldsBoolean extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsDate extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsLink extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsList extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsMultipleValuesList extends A01Response200ShopAdditionalFields {
  value: Array<string>;
}

export interface A01Response200ShopAdditionalFieldsNumeric extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsRegex extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsString extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200ShopAdditionalFieldsTextarea extends A01Response200ShopAdditionalFields {
  value: string;
}

export interface A01Response200SpecificBillingInformations {
  corporate_information?: A01Response200SpecificBillingInformationsCorporateInformation;
  fiscal_information?: A01Response200SpecificBillingInformationsFiscalInformation;
  fiscal_representative?: A01Response200SpecificBillingInformationsFiscalRepresentative;
  id: string;
  personal_information?: A01Response200SpecificBillingInformationsPersonalInformation;
  registration_address: A01Response200SpecificBillingInformationsRegistrationAddress;
}

export interface A01Response200SpecificBillingInformationsCorporateInformation {
  company_registration_name?: string;
  company_registration_number?: string;
  complementary_information?: A01Response200SpecificBillingInformationsCorporateInformationComplementaryInformation;
  electronic_address?: string;
  phone_number?: string;
}

export interface A01Response200SpecificBillingInformationsCorporateInformationComplementaryInformation {
  business_activity_code?: string;
  company_registration_city?: string;
  company_registration_province?: string;
  company_shareholders?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  share_capital?: number;
  share_capital_currency?: string;
  sole_trader?: boolean;
}

export interface A01Response200SpecificBillingInformationsFiscalInformation {
  local_tax_number?: string;
  tax_identification_country?: string;
  tax_identification_number?: string;
}

export interface A01Response200SpecificBillingInformationsFiscalRepresentative {
  city: string;
  civility: string;
  company_registration_name: string;
  company_registration_number: string;
  country_iso_code: string;
  first_name: string;
  last_name: string;
  local_tax_number?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A01Response200SpecificBillingInformationsPersonalInformation {
  birth_city?: string;
  birth_country?: string;
  birth_date?: string;
  civility?: string;
  first_name?: string;
  last_name?: string;
}

export interface A01Response200SpecificBillingInformationsRegistrationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A02Request {
  address?: A02RequestAddress;
  channels?: Array<string>;
  closed_from?: string;
  closed_to?: string;
  description?: string;
  email?: string;
  fax?: string;
  is_professional?: boolean;
  payment_info?: A02RequestPaymentInfo;
  pro_details?: A02RequestProDetails;
  producer_identifiers?: Array<A02RequestProducerIdentifiers>;
  recycling_policy?: string;
  return_policy?: string;
  shipping_country?: string;
  shop_additional_fields?: Array<A02RequestShopAdditionalFields>;
  shop_name?: string;
  web_site?: string;
}

export interface A02RequestAddress {
  city?: string;
  civility?: string;
  country?: string;
  firstname?: string;
  lastname?: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface A02RequestPaymentInfo {
  at_type?: string;
  owner: string;
}

export interface A02RequestPaymentInfoAba extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  routing_number: string;
}

export interface A02RequestPaymentInfoAubsb extends A02RequestPaymentInfo {
  auban: string;
  aubsb: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02RequestPaymentInfoBrazilian extends A02RequestPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  pix_key?: string;
}

export interface A02RequestPaymentInfoCanadian extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  institution_number: string;
  swift_code?: string;
  transit_number: string;
}

export interface A02RequestPaymentInfoColombian extends A02RequestPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02RequestPaymentInfoGuatemalan extends A02RequestPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02RequestPaymentInfoHk extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code: string;
}

export interface A02RequestPaymentInfoIban extends A02RequestPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic: string;
  iban: string;
}

export interface A02RequestPaymentInfoIndian extends A02RequestPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  indian_financial_system_code: string;
  swift_code?: string;
}

export interface A02RequestPaymentInfoIsraeli extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A02RequestPaymentInfoJapanese extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  branch_name: string;
  swift_code?: string;
}

export interface A02RequestPaymentInfoMexican extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  clabe: string;
}

export interface A02RequestPaymentInfoNuban extends A02RequestPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nuban: string;
}

export interface A02RequestPaymentInfoNzbsb extends A02RequestPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nzban: string;
  nzbsb: string;
}

export interface A02RequestPaymentInfoPayout extends A02RequestPaymentInfo {
  bank_account_number?: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
  payout_format: string;
  sort_code?: string;
}

export interface A02RequestPaymentInfoPhilippines extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02RequestPaymentInfoSerbian extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_branch_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
}

export interface A02RequestPaymentInfoSg {
  bank_account_number: string;
  bank_city?: string;
  bank_key?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  owner: string;
  swift_code: string;
}

export interface A02RequestPaymentInfoTaiwanese extends A02RequestPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A02RequestPaymentInfoThai extends A02RequestPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02RequestPaymentInfoUk extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_sort_code: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code?: string;
}

export interface A02RequestPaymentInfoUruguayan extends A02RequestPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A02RequestPaymentInfoVietnamese extends A02RequestPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A02RequestProDetails {
  corporate_name?: string;
  identification_number?: string;
  tax_identification_number?: string;
}

export interface A02RequestProducerIdentifiers {
  epr_category_code: string;
  producer_id: string;
}

export interface A02RequestShopAdditionalFields {
  code: string;
  type?: string;
}

export interface A02RequestShopAdditionalFieldsBoolean extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsDate extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsLink extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsList extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsMultipleValuesList extends A02RequestShopAdditionalFields {
  value: Array<string>;
}

export interface A02RequestShopAdditionalFieldsNumeric extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsRegex extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsString extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02RequestShopAdditionalFieldsTextarea extends A02RequestShopAdditionalFields {
  value: string;
}

export interface A02Response200 {
  errors?: Array<A02Response200Errors>;
  updated?: A02Response200Updated;
}

export interface A02Response200Errors {
  code: string;
  field: string;
  message: string;
}

export interface A02Response200Updated {
  address?: A02Response200UpdatedAddress;
  channels?: Array<string>;
  closed_from?: string;
  closed_to?: string;
  default_billing_information?: A02Response200UpdatedDefaultBillingInformation;
  description?: string;
  email?: string;
  fax?: string;
  is_professional?: boolean;
  model?: string;
  payment_info?: A02Response200UpdatedPaymentInfo;
  payment_method_mandatory?: boolean;
  pro_details?: A02Response200UpdatedProDetails;
  producer_identifiers?: Array<A02Response200UpdatedProducerIdentifiers>;
  recycling_policy?: string;
  return_policy?: string;
  shipping?: A02Response200UpdatedShipping;
  shipping_country?: string;
  shop_additional_fields?: Array<A02Response200UpdatedShopAdditionalFields>;
  shop_name?: string;
  specific_billing_informations?: Array<A02Response200UpdatedSpecificBillingInformations>;
  web_site?: string;
}

export interface A02Response200UpdatedAddress {
  city?: string;
  civility?: string;
  country?: string;
  firstname?: string;
  lastname?: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface A02Response200UpdatedDefaultBillingInformation {
  corporate_information?: A02Response200UpdatedDefaultBillingInformationCorporateInformation;
  default_language: string;
  fiscal_information?: A02Response200UpdatedDefaultBillingInformationFiscalInformation;
  fiscal_representative?: A02Response200UpdatedDefaultBillingInformationFiscalRepresentative;
  id: string;
  personal_information?: A02Response200UpdatedDefaultBillingInformationPersonalInformation;
  registration_address: A02Response200UpdatedDefaultBillingInformationRegistrationAddress;
}

export interface A02Response200UpdatedDefaultBillingInformationCorporateInformation {
  company_registration_name?: string;
  company_registration_number?: string;
  complementary_information?: A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation;
  electronic_address?: string;
  phone_number?: string;
}

export interface A02Response200UpdatedDefaultBillingInformationCorporateInformationComplementaryInformation {
  business_activity_code?: string;
  company_registration_city?: string;
  company_registration_province?: string;
  company_shareholders?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  share_capital?: number;
  share_capital_currency?: string;
  sole_trader?: boolean;
}

export interface A02Response200UpdatedDefaultBillingInformationFiscalInformation {
  local_tax_number?: string;
  tax_identification_country?: string;
  tax_identification_number?: string;
}

export interface A02Response200UpdatedDefaultBillingInformationFiscalRepresentative {
  city: string;
  civility: string;
  company_registration_name: string;
  company_registration_number: string;
  country_iso_code: string;
  first_name: string;
  last_name: string;
  local_tax_number?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A02Response200UpdatedDefaultBillingInformationPersonalInformation {
  birth_city?: string;
  birth_country?: string;
  birth_date?: string;
  civility?: string;
  first_name?: string;
  last_name?: string;
}

export interface A02Response200UpdatedDefaultBillingInformationRegistrationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A02Response200UpdatedPaymentInfo {
  at_type?: string;
  owner: string;
}

export interface A02Response200UpdatedPaymentInfoAba extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  routing_number: string;
}

export interface A02Response200UpdatedPaymentInfoAubsb extends A02Response200UpdatedPaymentInfo {
  auban: string;
  aubsb: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02Response200UpdatedPaymentInfoBrazilian extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  pix_key?: string;
}

export interface A02Response200UpdatedPaymentInfoCanadian extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  institution_number: string;
  swift_code?: string;
  transit_number: string;
}

export interface A02Response200UpdatedPaymentInfoColombian extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02Response200UpdatedPaymentInfoGuatemalan extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02Response200UpdatedPaymentInfoHk extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code: string;
}

export interface A02Response200UpdatedPaymentInfoIban extends A02Response200UpdatedPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic: string;
  iban: string;
}

export interface A02Response200UpdatedPaymentInfoIndian extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  indian_financial_system_code: string;
  swift_code?: string;
}

export interface A02Response200UpdatedPaymentInfoIsraeli extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A02Response200UpdatedPaymentInfoJapanese extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
  branch_name: string;
  swift_code?: string;
}

export interface A02Response200UpdatedPaymentInfoMexican extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  clabe: string;
}

export interface A02Response200UpdatedPaymentInfoNuban extends A02Response200UpdatedPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nuban: string;
}

export interface A02Response200UpdatedPaymentInfoNzbsb extends A02Response200UpdatedPaymentInfo {
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  nzban: string;
  nzbsb: string;
}

export interface A02Response200UpdatedPaymentInfoPayout extends A02Response200UpdatedPaymentInfo {
  bank_account_number?: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
  payout_format: string;
  sort_code?: string;
}

export interface A02Response200UpdatedPaymentInfoPhilippines extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02Response200UpdatedPaymentInfoSerbian extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_branch_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  bic?: string;
  iban?: string;
}

export interface A02Response200UpdatedPaymentInfoSg {
  bank_account_number: string;
  bank_city?: string;
  bank_key?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  owner: string;
  swift_code: string;
}

export interface A02Response200UpdatedPaymentInfoTaiwanese extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_code: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A02Response200UpdatedPaymentInfoThai extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
}

export interface A02Response200UpdatedPaymentInfoUk extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_sort_code: string;
  bank_street?: string;
  bank_zip?: string;
  swift_code?: string;
}

export interface A02Response200UpdatedPaymentInfoUruguayan extends A02Response200UpdatedPaymentInfo {
  account_number: string;
  bank_account_type: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_code: string;
}

export interface A02Response200UpdatedPaymentInfoVietnamese extends A02Response200UpdatedPaymentInfo {
  bank_account_number: string;
  bank_city?: string;
  bank_name: string;
  bank_street?: string;
  bank_zip?: string;
  branch_name?: string;
}

export interface A02Response200UpdatedProDetails {
  corporate_name?: string;
  identification_number?: string;
  tax_identification_number?: string;
}

export interface A02Response200UpdatedProducerIdentifiers {
  epr_category_code: string;
  producer_id: string;
}

export interface A02Response200UpdatedShipping {
  lead_time_to_ship?: number;
}

export interface A02Response200UpdatedShopAdditionalFields {
  code: string;
  type?: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsBoolean extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsDate extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsLink extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsList extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsMultipleValuesList extends A02Response200UpdatedShopAdditionalFields {
  value: Array<string>;
}

export interface A02Response200UpdatedShopAdditionalFieldsNumeric extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsRegex extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsString extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedShopAdditionalFieldsTextarea extends A02Response200UpdatedShopAdditionalFields {
  value: string;
}

export interface A02Response200UpdatedSpecificBillingInformations {
  corporate_information?: A02Response200UpdatedSpecificBillingInformationsCorporateInformation;
  fiscal_information?: A02Response200UpdatedSpecificBillingInformationsFiscalInformation;
  fiscal_representative?: A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative;
  id: string;
  personal_information?: A02Response200UpdatedSpecificBillingInformationsPersonalInformation;
  registration_address: A02Response200UpdatedSpecificBillingInformationsRegistrationAddress;
}

export interface A02Response200UpdatedSpecificBillingInformationsCorporateInformation {
  company_registration_name?: string;
  company_registration_number?: string;
  complementary_information?: A02Response200UpdatedSpecificBillingInformationsCorporateInformationComplementaryInformation;
  electronic_address?: string;
  phone_number?: string;
}

export interface A02Response200UpdatedSpecificBillingInformationsCorporateInformationComplementaryInformation {
  business_activity_code?: string;
  company_registration_city?: string;
  company_registration_province?: string;
  company_shareholders?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  share_capital?: number;
  share_capital_currency?: string;
  sole_trader?: boolean;
}

export interface A02Response200UpdatedSpecificBillingInformationsFiscalInformation {
  local_tax_number?: string;
  tax_identification_country?: string;
  tax_identification_number?: string;
}

export interface A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative {
  city: string;
  civility: string;
  company_registration_name: string;
  company_registration_number: string;
  country_iso_code: string;
  first_name: string;
  last_name: string;
  local_tax_number?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A02Response200UpdatedSpecificBillingInformationsPersonalInformation {
  birth_city?: string;
  birth_country?: string;
  birth_date?: string;
  civility?: string;
  first_name?: string;
  last_name?: string;
}

export interface A02Response200UpdatedSpecificBillingInformationsRegistrationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface A21Response200 {
  approval_delay?: Array<A21Response200ApprovalDelay>;
  approval_rate?: Array<A21Response200ApprovalRate>;
  auto_refused_rate?: Array<A21Response200AutoRefusedRate>;
  average_cart?: Array<A21Response200AverageCart>;
  average_cart_with_shipping?: Array<A21Response200AverageCartWithShipping>;
  cancelation_rate?: Array<A21Response200CancelationRate>;
  channel?: string;
  consecutive_refused_orders_count?: Array<A21Response200ConsecutiveRefusedOrdersCount>;
  evaluations_count?: Array<A21Response200EvaluationsCount>;
  grade?: Array<A21Response200Grade>;
  incident_rate?: Array<A21Response200IncidentRate>;
  last_updated_date?: string;
  late_shipment_rate?: Array<A21Response200LateShipmentRate>;
  offers_count?: Array<A21Response200OffersCount>;
  order_messages_response_delay?: Array<A21Response200OrderMessagesResponseDelay>;
  orders_count?: Array<A21Response200OrdersCount>;
  refund_rate?: Array<A21Response200RefundRate>;
  return_rate?: Array<A21Response200ReturnRate>;
  shipping_delay?: Array<A21Response200ShippingDelay>;
  shop_id?: number;
  total_revenue?: Array<A21Response200TotalRevenue>;
  valid_tracking_rate?: Array<A21Response200ValidTrackingRate>;
}

export interface A21Response200ApprovalDelay {
  period?: string;
  value?: number;
}

export interface A21Response200ApprovalRate {
  period?: string;
  value?: number;
}

export interface A21Response200AutoRefusedRate {
  period?: string;
  value?: number;
}

export interface A21Response200AverageCart {
  period?: string;
  value?: number;
}

export interface A21Response200AverageCartWithShipping {
  period?: string;
  value?: number;
}

export interface A21Response200CancelationRate {
  period?: string;
  value?: number;
}

export interface A21Response200ConsecutiveRefusedOrdersCount {
  period?: string;
  value?: number;
}

export interface A21Response200EvaluationsCount {
  period?: string;
  value?: number;
}

export interface A21Response200Grade {
  period?: string;
  value?: number;
}

export interface A21Response200IncidentRate {
  period?: string;
  value?: number;
}

export interface A21Response200LateShipmentRate {
  period?: string;
  value?: number;
}

export interface A21Response200OffersCount {
  period?: string;
  value?: number;
}

export interface A21Response200OrderMessagesResponseDelay {
  period?: string;
  value?: number;
}

export interface A21Response200OrdersCount {
  period?: string;
  value?: number;
}

export interface A21Response200RefundRate {
  period?: string;
  value?: number;
}

export interface A21Response200ReturnRate {
  period?: string;
  value?: number;
}

export interface A21Response200ShippingDelay {
  period?: string;
  value?: number;
}

export interface A21Response200TotalRevenue {
  period?: string;
  value?: number;
}

export interface A21Response200ValidTrackingRate {
  period?: string;
  value?: number;
}

export interface AF01Response200 {
  additional_fields: Array<AF01Response200AdditionalFields>;
  total_count: number;
}

export interface AF01Response200AdditionalFields {
  accepted_values?: Array<string>;
  code: string;
  default_value?: string;
  description?: string;
  editable: boolean;
  entity?: string;
  label: string;
  personal_data?: boolean;
  regex?: string;
  required: boolean;
  type: string;
}

export interface CH11Response200 {
  channels?: Array<CH11Response200Channels>;
}

export interface CH11Response200Channels {
  code: string;
  description: string;
  label: string;
}

export interface CUR01Response200 {
  currencies: Array<CUR01Response200Currencies>;
}

export interface CUR01Response200Currencies {
  code: string;
  label: string;
  platform_default?: boolean;
}

export interface DO01Response200 {
  documents: Array<DO01Response200Documents>;
}

export interface DO01Response200Documents {
  code: string;
  description: string;
  entity: string;
  label: string;
  mime_types?: Array<string>;
}

export interface DR11Response200 {
  data: Array<DR11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface DR11Response200Data {
  currency_iso_code: string;
  date_created: string;
  document_details: Array<DR11Response200DataDocumentDetails>;
  document_number?: string;
  document_upload_date?: string;
  due_date: string;
  entities?: DR11Response200DataEntities;
  entity_date_created?: string;
  entity_id: string;
  entity_type: string;
  id: string;
  initial_documents?: Array<DR11Response200DataInitialDocuments>;
  initial_payment_state: string;
  issue_date: string;
  issuer: DR11Response200DataIssuer;
  last_updated: string;
  payment?: DR11Response200DataPayment;
  payment_destination?: DR11Response200DataPaymentDestination;
  payment_terms?: DR11Response200DataPaymentTerms;
  recipient?: DR11Response200DataRecipient;
  state: string;
  taxes?: Array<DR11Response200DataTaxes>;
  total_amount_excluding_taxes: number;
  total_amount_including_taxes: number;
  total_tax_amount: number;
  type: string;
}

export interface DR11Response200DataDocumentDetails {
  format: string;
}

export interface DR11Response200DataEntities {
  delivery_bill_information?: Array<DR11Response200DataEntitiesDeliveryBillInformation>;
  order_additional_fields?: Array<DR11Response200DataEntitiesOrderAdditionalFields>;
  ship_to_iso_country_code?: string;
  shipping_information?: DR11Response200DataEntitiesShippingInformation;
  shop_billing_cycle?: DR11Response200DataEntitiesShopBillingCycle;
}

export interface DR11Response200DataEntitiesDeliveryBillInformation {
  delivery_bill_date?: string;
  delivery_bill_id?: string;
}

export interface DR11Response200DataEntitiesOrderAdditionalFields {
  code?: string;
  type?: string;
  value?: string;
}

export interface DR11Response200DataEntitiesShippingInformation {
  ship_to_address?: DR11Response200DataEntitiesShippingInformationShipToAddress;
}

export interface DR11Response200DataEntitiesShippingInformationShipToAddress {
  city?: string;
  civility?: string;
  company?: string;
  company2?: string;
  country_iso_code?: string;
  firstname?: string;
  lastname?: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface DR11Response200DataEntitiesShopBillingCycle {
  date_from?: string;
  date_to?: string;
  id?: string;
}

export interface DR11Response200DataInitialDocuments {
  id: string;
  issue_date: string;
  number?: string;
  type: string;
}

export interface DR11Response200DataIssuer {
  id?: string;
  locale?: string;
  organization: DR11Response200DataIssuerOrganization;
  type: string;
}

export interface DR11Response200DataIssuerOrganization {
  address?: DR11Response200DataIssuerOrganizationAddress;
  business_activity_code?: string;
  company_shareholders?: string;
  electronic_address?: string;
  fiscal_representative?: DR11Response200DataIssuerOrganizationFiscalRepresentative;
  identification_number?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  local_tax_number?: string;
  local_tax_number_country?: string;
  name: string;
  personal_information?: DR11Response200DataIssuerOrganizationPersonalInformation;
  phone_number?: string;
  share_capital?: number;
  share_capital_currency?: string;
  sole_trader?: boolean;
  tax_identification_number?: string;
  tax_number_country?: string;
  trade_company_registration_location?: string;
}

export interface DR11Response200DataIssuerOrganizationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface DR11Response200DataIssuerOrganizationFiscalRepresentative {
  city: string;
  civility: string;
  company_registration_name: string;
  company_registration_number: string;
  country_iso_code: string;
  first_name: string;
  last_name: string;
  local_tax_number?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface DR11Response200DataIssuerOrganizationPersonalInformation {
  civility?: string;
  first_name?: string;
  last_name?: string;
}

export interface DR11Response200DataPayment {
  reference?: string;
  state?: string;
  transaction_date?: string;
}

export interface DR11Response200DataPaymentDestination {
  at_type: string;
  payment_reference?: string;
}

export interface DR11Response200DataPaymentDestinationIban extends DR11Response200DataPaymentDestination {
  iban: string;
}

export interface DR11Response200DataPaymentTerms {
  days?: number;
  type?: string;
}

export interface DR11Response200DataRecipient {
  billing_address: DR11Response200DataRecipientBillingAddress;
  id: string;
  locale?: string;
  organization?: DR11Response200DataRecipientOrganization;
  shipping_address?: DR11Response200DataRecipientShippingAddress;
  type?: string;
}

export interface DR11Response200DataRecipientBillingAddress {
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code?: string;
  firstname?: string;
  lastname: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface DR11Response200DataRecipientOrganization {
  address?: DR11Response200DataRecipientOrganizationAddress;
  business_activity_code?: string;
  company_shareholders?: string;
  electronic_address?: string;
  identification_number?: string;
  is_in_liquidation?: boolean;
  legal_form?: string;
  local_tax_number?: string;
  local_tax_number_country?: string;
  name: string;
  organization_id?: string;
  phone_number?: string;
  share_capital?: number;
  share_capital_currency?: string;
  tax_identification_number?: string;
  tax_number_country?: string;
  trade_company_registration_location?: string;
}

export interface DR11Response200DataRecipientOrganizationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface DR11Response200DataRecipientShippingAddress {
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code?: string;
  firstname?: string;
  lastname: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface DR11Response200DataTaxes {
  code: string;
  rate?: number;
  total_amount: number;
}

export interface DR12Response200 {
  data: Array<DR12Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface DR12Response200Data {
  delivery_bill_information?: Array<DR12Response200DataDeliveryBillInformation>;
  eco_contributions?: Array<DR12Response200DataEcoContributions>;
  entity_id: string;
  entity_type: string;
  fees_excluding_taxes?: Array<DR12Response200DataFeesExcludingTaxes>;
  id: string;
  order?: DR12Response200DataOrder;
  order_line?: DR12Response200DataOrderLine;
  origin_unit_price_excluding_taxes?: number;
  origin_unit_price_including_taxes?: number;
  price_excluding_taxes: number;
  product?: DR12Response200DataProduct;
  quantity: number;
  shipments?: Array<DR12Response200DataShipments>;
  shipping_from?: DR12Response200DataShippingFrom;
  shipping_price_excluding_taxes?: number;
  shipping_taxes?: Array<DR12Response200DataShippingTaxes>;
  shipping_to?: DR12Response200DataShippingTo;
  shop: DR12Response200DataShop;
  tax_legal_notice?: string;
  taxes: Array<DR12Response200DataTaxes>;
  total_price_including_taxes: number;
  unit_price_excluding_taxes: number;
}

export interface DR12Response200DataDeliveryBillInformation {
  delivery_bill_date?: string;
  delivery_bill_id?: string;
}

export interface DR12Response200DataEcoContributions {
  epr_category_code?: string;
  producer_id?: string;
  producer_id_owner?: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface DR12Response200DataFeesCreditCommissionRefund extends DR12Response200Data {
  period: DR12Response200DataFeesCreditCommissionRefundPeriod;
}

export interface DR12Response200DataFeesCreditCommissionRefundPeriod {
  date_from: string;
  date_to: string;
}

export interface DR12Response200DataFeesCreditOneOff extends DR12Response200Data {
  description: string;
  operation_date?: string;
  references: Array<DR12Response200DataFeesCreditOneOffReferences>;
}

export interface DR12Response200DataFeesCreditOneOffReferences {
  type: string;
  value: string;
}

export interface DR12Response200DataFeesDebitCommission extends DR12Response200Data {
  period: DR12Response200DataFeesDebitCommissionPeriod;
}

export interface DR12Response200DataFeesDebitCommissionPeriod {
  date_from: string;
  date_to: string;
}

export interface DR12Response200DataFeesDebitOneOff extends DR12Response200Data {
  description: string;
  operation_date?: string;
  references: Array<DR12Response200DataFeesDebitOneOffReferences>;
}

export interface DR12Response200DataFeesDebitOneOffReferences {
  type: string;
  value: string;
}

export interface DR12Response200DataFeesDebitSellerFeeOnOrder extends DR12Response200Data {
  period: DR12Response200DataFeesDebitSellerFeeOnOrderPeriod;
}

export interface DR12Response200DataFeesDebitSellerFeeOnOrderPeriod {
  date_from: string;
  date_to: string;
}

export interface DR12Response200DataFeesDebitSellerPenaltyFee extends DR12Response200Data {
  period: DR12Response200DataFeesDebitSellerPenaltyFeePeriod;
}

export interface DR12Response200DataFeesDebitSellerPenaltyFeePeriod {
  date_from: string;
  date_to: string;
}

export interface DR12Response200DataFeesDebitSubscription extends DR12Response200Data {
  period: DR12Response200DataFeesDebitSubscriptionPeriod;
}

export interface DR12Response200DataFeesDebitSubscriptionPeriod {
  date_from: string;
  date_to: string;
}

export interface DR12Response200DataFeesExcludingTaxes {
  amount: number;
  code: string;
  label: string;
}

export interface DR12Response200DataOrder {
  additional_fields?: Array<DR12Response200DataOrderAdditionalFields>;
  commercial_id?: string;
  date_created?: string;
  id: string;
  reference_for_customer?: string;
  reference_for_seller?: string;
  transaction_info?: DR12Response200DataOrderTransactionInfo;
}

export interface DR12Response200DataOrderAdditionalFields {
  code?: string;
  type?: string;
  value?: string;
}

export interface DR12Response200DataOrderLine {
  additional_fields?: Array<DR12Response200DataOrderLineAdditionalFields>;
  id: string;
}

export interface DR12Response200DataOrderLineAdditionalFields {
  code?: string;
  type?: string;
  value?: string;
}

export interface DR12Response200DataOrderTransactionInfo {
  date: string;
  number: string;
}

export interface DR12Response200DataProduct {
  references: Array<DR12Response200DataProductReferences>;
  sku?: string;
  title: string;
}

export interface DR12Response200DataProductCreditCancel extends DR12Response200Data {}

export interface DR12Response200DataProductCreditCancelAdjustment extends DR12Response200Data {}

export interface DR12Response200DataProductCreditCancelCommercialGesture extends DR12Response200Data {}

export interface DR12Response200DataProductCreditRefund extends DR12Response200Data {}

export interface DR12Response200DataProductCreditRefundAdjustment extends DR12Response200Data {}

export interface DR12Response200DataProductCreditRefundCommercialGesture extends DR12Response200Data {}

export interface DR12Response200DataProductDebit extends DR12Response200Data {
  promotions: Array<DR12Response200DataProductDebitPromotions>;
}

export interface DR12Response200DataProductDebitPromotions {
  deduced_amount: number;
  id: string;
  type: string;
}

export interface DR12Response200DataProductReferences {
  reference: string;
  type: string;
}

export interface DR12Response200DataPurchaseOrderCredit extends DR12Response200Data {}

export interface DR12Response200DataPurchaseOrderDebit extends DR12Response200Data {
  promotions: Array<DR12Response200DataPurchaseOrderDebitPromotions>;
}

export interface DR12Response200DataPurchaseOrderDebitPromotions {
  deduced_amount: number;
  id: string;
  type: string;
}

export interface DR12Response200DataShipments {
  carrier_name?: string;
  carrier_scac_code?: string;
  delivery_bill_date?: string;
  delivery_bill_id?: string;
  id?: string;
  shipped_date?: string;
  tracking_number?: string;
}

export interface DR12Response200DataShippingFrom {
  address?: DR12Response200DataShippingFromAddress;
}

export interface DR12Response200DataShippingFromAddress {
  city?: string;
  country_iso_code: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface DR12Response200DataShippingTaxes {
  amount: number;
  code: string;
  rate?: number;
}

export interface DR12Response200DataShippingTo {
  address?: DR12Response200DataShippingToAddress;
}

export interface DR12Response200DataShippingToAddress {
  city?: string;
  civility?: string;
  company?: string;
  company2?: string;
  country_iso_code?: string;
  firstname?: string;
  lastname?: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface DR12Response200DataShop {
  id: number;
}

export interface DR12Response200DataTaxes {
  amount: number;
  code: string;
  rate?: number;
}

export interface DR74RequestMultipartFormDataDocumentsInput {
  requests: Array<DR74RequestMultipartFormDataDocumentsInputRequests>;
}

export interface DR74RequestMultipartFormDataDocumentsInputRequests {
  document_number: string;
  due_date?: string;
  files: Array<DR74RequestMultipartFormDataDocumentsInputRequestsFiles>;
  issue_date?: string;
  request_id: string;
  total_amount_excluding_taxes?: number;
  total_tax_amount?: number;
}

export interface DR74RequestMultipartFormDataDocumentsInputRequestsFiles {
  format: string;
  name: string;
}

export interface DR74Response200 {
  requests: Array<DR74Response200Requests>;
}

export interface DR74Response200Requests {
  errors?: Array<DR74Response200RequestsErrors>;
  input: DR74Response200RequestsInput;
}

export interface DR74Response200RequestsErrors {
  code: string;
  field: string;
  message: string;
}

export interface DR74Response200RequestsInput {
  document_number: string;
  due_date?: string;
  files: Array<DR74Response200RequestsInputFiles>;
  issue_date?: string;
  request_id: string;
  total_amount_excluding_taxes?: number;
  total_tax_amount?: number;
}

export interface DR74Response200RequestsInputFiles {
  format: string;
  name: string;
}

export interface DR75Request {
  requests: Array<DR75RequestRequests>;
}

export interface DR75RequestRequests {
  document_number: string;
  due_date?: string;
  issue_date?: string;
  request_id: string;
  total_amount_excluding_taxes?: number;
  total_tax_amount?: number;
}

export interface DR75Response200 {
  requests: Array<DR75Response200Requests>;
}

export interface DR75Response200Requests {
  errors?: Array<DR75Response200RequestsErrors>;
  input: DR75Response200RequestsInput;
}

export interface DR75Response200RequestsErrors {
  code: string;
  field: string;
  message: string;
}

export interface DR75Response200RequestsInput {
  document_number: string;
  due_date?: string;
  issue_date?: string;
  request_id: string;
  total_amount_excluding_taxes?: number;
  total_tax_amount?: number;
}

export interface H11Response200 {
  hierarchies: Array<H11Response200Hierarchies>;
}

export interface H11Response200Hierarchies {
  code: string;
  label?: string;
  label_translations: Array<H11Response200HierarchiesLabelTranslations>;
  level: number;
  parent_code: string;
}

export interface H11Response200HierarchiesLabelTranslations {
  locale?: string;
  value?: string;
}

export interface IV01Response200 {
  invoices?: Array<IV01Response200Invoices>;
  total_count?: number;
}

export interface IV01Response200Invoices {
  currency_iso_code?: string;
  date_created?: string;
  details?: Array<IV01Response200InvoicesDetails>;
  due_date?: string;
  id?: string;
  invoice_id?: number;
  issue_date?: string;
  issuing_user?: IV01Response200InvoicesIssuingUser;
  pay_out_psp_code?: string;
  payment?: IV01Response200InvoicesPayment;
  shop_address?: IV01Response200InvoicesShopAddress;
  shop_corporate_name?: string;
  shop_id?: number;
  shop_model?: string;
  shop_name?: string;
  shop_operator_internal_id?: string;
  shop_tax_number?: string;
  state?: string;
  total_amount_excl_taxes?: number;
  total_amount_incl_taxes?: number;
  total_charged_amount?: number;
  total_taxes?: Array<IV01Response200InvoicesTotalTaxes>;
  type?: string;
}

export interface IV01Response200InvoicesAutoInvoice extends IV01Response200Invoices {
  end_time?: string;
  payment_info?: IV01Response200InvoicesAutoInvoicePaymentInfo;
  seller_billing_cycle_id?: string;
  start_time?: string;
  summary?: IV01Response200InvoicesAutoInvoiceSummary;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfo {
  at_type?: string;
  bank_city?: string;
  bank_name?: string;
  bank_street?: string;
  bank_zip?: string;
  owner?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoAba extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bic?: string;
  routing_number?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoAubsb extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  auban?: string;
  aubsb?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoBrazilian extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  bank_account_type?: string;
  bank_code?: string;
  branch_code?: string;
  pix_key?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoCanadian extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  institution_number?: string;
  swift_code?: string;
  transit_number?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoColombian extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  bank_account_type?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoGuatemalan extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  bank_account_type?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoHk extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  swift_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoIban extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bic?: string;
  iban?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoIndian extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  indian_financial_system_code?: string;
  swift_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoIsraeli extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bank_code?: string;
  branch_name?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoJapanese extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bank_account_type?: string;
  bank_code?: string;
  branch_code?: string;
  branch_name?: string;
  swift_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoMexican extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  clabe?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoNuban extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  nuban?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoNzbsb extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  nzban?: string;
  nzbsb?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoPayout extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bic?: string;
  iban?: string;
  payout_format?: string;
  sort_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoPhilippines extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoSerbian extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bank_branch_number?: string;
  bic?: string;
  iban?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoSg extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  bank_key?: string;
  swift_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoTaiwanese extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  bank_code?: string;
  branch_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoThai extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoUk extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  sort_code?: string;
  swift_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoUruguayan extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  account_number?: string;
  bank_account_type?: string;
  branch_code?: string;
}

export interface IV01Response200InvoicesAutoInvoicePaymentInfoVietnamese extends IV01Response200InvoicesAutoInvoicePaymentInfo {
  bank_account_number?: string;
  branch_name?: string;
}

export interface IV01Response200InvoicesAutoInvoiceSummary {
  amount_transferred?: number;
  amount_transferred_to_operator?: number;
  reserve_funding?: number;
  reserve_settlement?: number;
  total_commissions_excl_tax?: number;
  total_commissions_incl_tax?: number;
  total_fee_excl_tax?: number;
  total_fee_incl_tax?: number;
  total_fee_operator_remitted_excl_tax?: number;
  total_fee_operator_remitted_incl_tax?: number;
  total_mirakl_ads_credit_excl_tax?: number;
  total_mirakl_ads_credit_incl_tax?: number;
  total_mirakl_ads_debit_excl_tax?: number;
  total_mirakl_ads_debit_incl_tax?: number;
  total_non_payable_orders_excl_tax?: number;
  total_non_payable_orders_incl_tax?: number;
  total_operator_paid_shipping_charges_excl_tax?: number;
  total_operator_paid_shipping_charges_incl_tax?: number;
  total_operator_remitted_taxes?: number;
  total_other_credits_excl_tax?: number;
  total_other_credits_incl_tax?: number;
  total_other_invoices_excl_tax?: number;
  total_other_invoices_incl_tax?: number;
  total_payable_orders_excl_tax?: number;
  total_payable_orders_incl_tax?: number;
  total_purchase_taxes?: number;
  total_refund_commissions_excl_tax?: number;
  total_refund_commissions_incl_tax?: number;
  total_refund_fee_excl_tax?: number;
  total_refund_fee_incl_tax?: number;
  total_refund_fee_operator_remitted_excl_tax?: number;
  total_refund_fee_operator_remitted_incl_tax?: number;
  total_refund_non_payable_orders_excl_tax?: number;
  total_refund_non_payable_orders_incl_tax?: number;
  total_refund_operator_paid_shipping_charges_excl_tax?: number;
  total_refund_operator_paid_shipping_charges_incl_tax?: number;
  total_refund_operator_remitted_taxes?: number;
  total_refund_orders_excl_tax?: number;
  total_refund_orders_incl_tax?: number;
  total_refund_payable_orders_excl_tax?: number;
  total_refund_payable_orders_incl_tax?: number;
  total_refund_purchase_taxes?: number;
  total_seller_fees_on_orders_excl_tax?: number;
  total_seller_fees_on_orders_incl_tax?: number;
  total_seller_penalty_fees_excl_tax?: number;
  total_seller_penalty_fees_incl_tax?: number;
  total_subscription_excl_tax?: number;
  total_subscription_incl_tax?: number;
}

export interface IV01Response200InvoicesDetails {
  amount_excl_taxes?: number;
  description?: string;
  operation_date?: string;
  order_id?: string;
  quantity?: number;
  taxes?: Array<IV01Response200InvoicesDetailsTaxes>;
}

export interface IV01Response200InvoicesDetailsTaxes {
  amount?: number;
  code?: string;
}

export interface IV01Response200InvoicesIssuingUser {
  information?: string;
  type?: string;
}

export interface IV01Response200InvoicesManualCredit extends IV01Response200Invoices {
  emission_date?: string;
  seller_billing_cycle_id?: string;
}

export interface IV01Response200InvoicesManualInvoice extends IV01Response200Invoices {
  emission_date?: string;
  seller_billing_cycle_id?: string;
}

export interface IV01Response200InvoicesPayment {
  failure_reason?: string;
  reference?: string;
  state?: string;
  transaction_date?: string;
}

export interface IV01Response200InvoicesShopAddress {
  city?: string;
  civility?: string;
  company?: string;
  complementary?: string;
  country?: string;
  firstname?: string;
  lastname?: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street1?: string;
  street2?: string;
  zip_code?: string;
}

export interface IV01Response200InvoicesTotalTaxes {
  amount?: number;
  code?: string;
}

export interface L01Response200 {
  locales: Array<L01Response200Locales>;
}

export interface L01Response200Locales {
  code: string;
  label: string;
  platform_default?: boolean;
}

export interface M01Response200 {
  messages: Array<M01Response200Messages>;
  total_count: number;
}

export interface M01Response200Messages {
  archived?: boolean;
  body: string;
  commercial_id: string;
  date_created: string;
  documents?: Array<M01Response200MessagesDocuments>;
  from_id: string;
  from_name: string;
  from_type: string;
  id: number;
  offer_id?: number;
  order_id?: string;
  read?: boolean;
  subject: string;
  to_customer_archived: boolean;
  to_customer_id: string;
  to_customer_name: string;
  to_operator: boolean;
  to_operator_archived: boolean;
  to_shop_archived: boolean;
  to_shop_id: number;
  to_shop_name: string;
  visible?: boolean;
}

export interface M01Response200MessagesDocuments {
  date_uploaded?: string;
  file_name: string;
  file_size?: number;
  id: number;
  type: string;
}

export interface M10Response200 {
  authorized_participants: Array<M10Response200AuthorizedParticipants>;
  current_participants: Array<M10Response200CurrentParticipants>;
  customer_organization?: M10Response200CustomerOrganization;
  date_created: string;
  date_updated: string;
  entities?: Array<M10Response200Entities>;
  id: string;
  messages: Array<M10Response200Messages>;
  metadata: M10Response200Metadata;
  no_store_reply_needed?: Array<M10Response200NoStoreReplyNeeded>;
  topic: M10Response200Topic;
}

export interface M10Response200AuthorizedParticipants {
  display_name: string;
  id?: string;
  type: string;
}

export interface M10Response200CurrentParticipants {
  display_name: string;
  id?: string;
  type: string;
}

export interface M10Response200CustomerOrganization {
  display_name: string;
  id: string;
}

export interface M10Response200Entities {
  id: string;
  label: string;
  type: string;
}

export interface M10Response200Messages {
  attachments?: Array<M10Response200MessagesAttachments>;
  body: string;
  date_created: string;
  from: M10Response200MessagesFrom;
  id: string;
  to: Array<M10Response200MessagesTo>;
}

export interface M10Response200MessagesAttachments {
  id: string;
  name: string;
  size: number;
}

export interface M10Response200MessagesFrom {
  display_name: string;
  organization_details?: M10Response200MessagesFromOrganizationDetails;
  type: string;
}

export interface M10Response200MessagesFromOrganizationDetails {
  display_name: string;
  id?: string;
  type: string;
}

export interface M10Response200MessagesTo {
  display_name: string;
  id?: string;
  type: string;
}

export interface M10Response200Metadata {
  last_message_date: string;
  last_sender: M10Response200MetadataLastSender;
  shop_reply_needed_since: string;
  total_count: number;
}

export interface M10Response200MetadataLastSender {
  display_name: string;
  organization_details?: M10Response200MetadataLastSenderOrganizationDetails;
  type: string;
}

export interface M10Response200MetadataLastSenderOrganizationDetails {
  display_name: string;
  id?: string;
  type: string;
}

export interface M10Response200NoStoreReplyNeeded {
  date: string;
  user_type: string;
}

export interface M10Response200Topic {
  type: string;
  value: string;
}

export interface M11Response200 {
  data: Array<M11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface M11Response200Data {
  authorized_participants: Array<M11Response200DataAuthorizedParticipants>;
  current_participants: Array<M11Response200DataCurrentParticipants>;
  customer_organization?: M11Response200DataCustomerOrganization;
  date_created: string;
  date_updated: string;
  entities?: Array<M11Response200DataEntities>;
  id: string;
  messages?: Array<M11Response200DataMessages>;
  metadata: M11Response200DataMetadata;
  no_store_reply_needed?: Array<M11Response200DataNoStoreReplyNeeded>;
  topic: M11Response200DataTopic;
}

export interface M11Response200DataAuthorizedParticipants {
  display_name: string;
  id?: string;
  type: string;
}

export interface M11Response200DataCurrentParticipants {
  display_name: string;
  id?: string;
  type: string;
}

export interface M11Response200DataCustomerOrganization {
  display_name: string;
  id: string;
}

export interface M11Response200DataEntities {
  id: string;
  label: string;
  type: string;
}

export interface M11Response200DataMessages {
  attachments?: Array<M11Response200DataMessagesAttachments>;
  body: string;
  date_created: string;
  from: M11Response200DataMessagesFrom;
  id: string;
  to: Array<M11Response200DataMessagesTo>;
}

export interface M11Response200DataMessagesAttachments {
  id: string;
  name: string;
  size: number;
}

export interface M11Response200DataMessagesFrom {
  display_name: string;
  organization_details?: M11Response200DataMessagesFromOrganizationDetails;
  type: string;
}

export interface M11Response200DataMessagesFromOrganizationDetails {
  display_name: string;
  id?: string;
  type: string;
}

export interface M11Response200DataMessagesTo {
  display_name: string;
  id?: string;
  type: string;
}

export interface M11Response200DataMetadata {
  last_message_date: string;
  last_sender: M11Response200DataMetadataLastSender;
  shop_reply_needed_since: string;
  total_count: number;
}

export interface M11Response200DataMetadataLastSender {
  display_name: string;
  organization_details?: M11Response200DataMetadataLastSenderOrganizationDetails;
  type: string;
}

export interface M11Response200DataMetadataLastSenderOrganizationDetails {
  display_name: string;
  id?: string;
  type: string;
}

export interface M11Response200DataNoStoreReplyNeeded {
  date: string;
  user_type: string;
}

export interface M11Response200DataTopic {
  type: string;
  value: string;
}

export interface M12RequestMultipartFormDataMessageInput {
  body: string;
  to: Array<M12RequestMultipartFormDataMessageInputTo>;
  topic?: M12RequestMultipartFormDataMessageInputTopic;
}

export interface M12RequestMultipartFormDataMessageInputTo {
  id?: string;
  type: string;
}

export interface M12RequestMultipartFormDataMessageInputTopic {
  type?: string;
  value?: string;
}

export interface M12RequestMultipartFormDataMessageInputTopicFreeText extends M12RequestMultipartFormDataMessageInputTopic {
  value: string;
}

export interface M12RequestMultipartFormDataMessageInputTopicReasonCode extends M12RequestMultipartFormDataMessageInputTopic {
  value: string;
}

export interface M12Response201 {
  message_id?: string;
  thread_id?: string;
}

export interface M14RequestMultipartFormDataThreadInput {
  body: string;
  entity: M14RequestMultipartFormDataThreadInputEntity;
  topic: M14RequestMultipartFormDataThreadInputTopic;
}

export interface M14RequestMultipartFormDataThreadInputEntity {
  type: string;
}

export interface M14RequestMultipartFormDataThreadInputTopic {
  type?: string;
  value?: string;
}

export interface M14RequestMultipartFormDataThreadInputTopicFreeText extends M14RequestMultipartFormDataThreadInputTopic {
  value: string;
}

export interface M14RequestMultipartFormDataThreadInputTopicReasonCode extends M14RequestMultipartFormDataThreadInputTopic {
  value: string;
}

export interface M14Response201 {
  message_id?: string;
  thread_id?: string;
}

export interface OF01Response201 {
  import_id: number;
  product_import_id?: number;
}

export interface OF02Response200 {
  date_created: string;
  has_error_report: boolean;
  import_id: number;
  lines_in_error: number;
  lines_in_pending: number;
  lines_in_success: number;
  lines_read: number;
  mode: string;
  offer_deleted: number;
  offer_inserted: number;
  offer_updated: number;
  reason_status: string;
  status: string;
  type: string;
}

export interface OF04Response200 {
  data: Array<OF04Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface OF04Response200Data {
  date_created: string;
  has_error_report: boolean;
  import_id: number;
  lines_in_error: number;
  lines_in_pending: number;
  lines_in_success: number;
  lines_read: number;
  mode: string;
  offer_deleted: number;
  offer_inserted: number;
  offer_updated: number;
  origin: string;
  reason_status?: string;
  shop_id: number;
  status: string;
}

export interface OF21Response200 {
  offers: Array<OF21Response200Offers>;
  total_count: number;
}

export interface OF21Response200Offers {
  active: boolean;
  all_prices: Array<OF21Response200OffersAllPrices>;
  allow_quote_requests?: boolean;
  applicable_pricing?: OF21Response200OffersApplicablePricing;
  available_end_date?: string;
  available_start_date?: string;
  category_code: string;
  category_label: string;
  channels: Array<string>;
  currency_iso_code: string;
  description: string;
  discount?: OF21Response200OffersDiscount;
  eco_contributions?: Array<OF21Response200OffersEcoContributions>;
  favorite_rank?: number;
  fulfillment: OF21Response200OffersFulfillment;
  inactivity_reasons?: Array<string>;
  internal_description?: string;
  leadtime_to_ship: number;
  logistic_class: OF21Response200OffersLogisticClass;
  max_order_quantity: number;
  min_order_quantity: number;
  min_quantity_alert: number;
  min_shipping_price: number;
  min_shipping_price_additional: number;
  min_shipping_type: string;
  min_shipping_zone: string;
  msrp?: number;
  offer_additional_fields?: Array<OF21Response200OffersOfferAdditionalFields>;
  offer_id: number;
  package_quantity: number;
  price?: number;
  price_additional_info?: string;
  product_brand?: string;
  product_description?: string;
  product_references: Array<OF21Response200OffersProductReferences>;
  product_sku: string;
  product_tax_code?: string;
  product_title: string;
  quantity: number;
  retail_prices?: Array<OF21Response200OffersRetailPrices>;
  shipping_deadline: string;
  shop_sku: string;
  state_code: string;
  total_price?: number;
  warehouses?: Array<OF21Response200OffersWarehouses>;
}

export interface OF21Response200OffersAllPrices {
  channel_code?: string;
  context?: OF21Response200OffersAllPricesContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<OF21Response200OffersAllPricesVolumePrices>;
}

export interface OF21Response200OffersAllPricesContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface OF21Response200OffersAllPricesVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface OF21Response200OffersApplicablePricing {
  channel_code?: string;
  context?: OF21Response200OffersApplicablePricingContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<OF21Response200OffersApplicablePricingVolumePrices>;
}

export interface OF21Response200OffersApplicablePricingContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface OF21Response200OffersApplicablePricingVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface OF21Response200OffersDiscount {
  discount_price?: number;
  end_date?: string;
  origin_price?: number;
  ranges?: Array<OF21Response200OffersDiscountRanges>;
  start_date?: string;
}

export interface OF21Response200OffersDiscountRanges {
  price: number;
  quantity_threshold: number;
}

export interface OF21Response200OffersEcoContributions {
  eco_contribution_amount?: number;
  epr_category_code: string;
  producer_id?: string;
}

export interface OF21Response200OffersFulfillment {
  center: OF21Response200OffersFulfillmentCenter;
}

export interface OF21Response200OffersFulfillmentCenter {
  code: string;
}

export interface OF21Response200OffersLogisticClass {
  code: string;
  label: string;
}

export interface OF21Response200OffersOfferAdditionalFields {
  code: string;
  type?: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsBoolean extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsDate extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsLink extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsList extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsMultipleValuesList extends OF21Response200OffersOfferAdditionalFields {
  value: Array<string>;
}

export interface OF21Response200OffersOfferAdditionalFieldsNumeric extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsRegex extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsString extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersOfferAdditionalFieldsTextarea extends OF21Response200OffersOfferAdditionalFields {
  value: string;
}

export interface OF21Response200OffersProductReferences {
  reference: string;
  reference_type: string;
}

export interface OF21Response200OffersRetailPrices {
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
}

export interface OF21Response200OffersWarehouses {
  code: string;
  quantity: number;
}

export interface OF22Response200 {
  active: boolean;
  all_prices: Array<OF22Response200AllPrices>;
  allow_quote_requests?: boolean;
  applicable_pricing?: OF22Response200ApplicablePricing;
  available_end_date?: string;
  available_start_date?: string;
  category_code: string;
  category_label: string;
  channels: Array<string>;
  currency_iso_code: string;
  description: string;
  discount?: OF22Response200Discount;
  eco_contributions?: Array<OF22Response200EcoContributions>;
  favorite_rank?: number;
  fulfillment: OF22Response200Fulfillment;
  inactivity_reasons?: Array<string>;
  internal_description?: string;
  leadtime_to_ship: number;
  logistic_class: OF22Response200LogisticClass;
  max_order_quantity: number;
  min_order_quantity: number;
  min_quantity_alert: number;
  min_shipping_price: number;
  min_shipping_price_additional: number;
  min_shipping_type: string;
  min_shipping_zone: string;
  msrp?: number;
  offer_additional_fields?: Array<OF22Response200OfferAdditionalFields>;
  offer_id: number;
  package_quantity: number;
  price?: number;
  price_additional_info?: string;
  product_brand?: string;
  product_description?: string;
  product_references: Array<OF22Response200ProductReferences>;
  product_sku: string;
  product_tax_code?: string;
  product_title: string;
  quantity: number;
  retail_prices?: Array<OF22Response200RetailPrices>;
  shipping_deadline: string;
  shop_sku: string;
  state_code: string;
  total_price?: number;
  warehouses?: Array<OF22Response200Warehouses>;
}

export interface OF22Response200AllPrices {
  channel_code?: string;
  context?: OF22Response200AllPricesContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<OF22Response200AllPricesVolumePrices>;
}

export interface OF22Response200AllPricesContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface OF22Response200AllPricesVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface OF22Response200ApplicablePricing {
  channel_code?: string;
  context?: OF22Response200ApplicablePricingContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<OF22Response200ApplicablePricingVolumePrices>;
}

export interface OF22Response200ApplicablePricingContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface OF22Response200ApplicablePricingVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface OF22Response200Discount {
  discount_price?: number;
  end_date?: string;
  origin_price?: number;
  ranges?: Array<OF22Response200DiscountRanges>;
  start_date?: string;
}

export interface OF22Response200DiscountRanges {
  price: number;
  quantity_threshold: number;
}

export interface OF22Response200EcoContributions {
  eco_contribution_amount?: number;
  epr_category_code: string;
  producer_id?: string;
}

export interface OF22Response200Fulfillment {
  center: OF22Response200FulfillmentCenter;
}

export interface OF22Response200FulfillmentCenter {
  code: string;
}

export interface OF22Response200LogisticClass {
  code: string;
  label: string;
}

export interface OF22Response200OfferAdditionalFields {
  code: string;
  type?: string;
}

export interface OF22Response200OfferAdditionalFieldsBoolean extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsDate extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsLink extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsList extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsMultipleValuesList extends OF22Response200OfferAdditionalFields {
  value: Array<string>;
}

export interface OF22Response200OfferAdditionalFieldsNumeric extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsRegex extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsString extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200OfferAdditionalFieldsTextarea extends OF22Response200OfferAdditionalFields {
  value: string;
}

export interface OF22Response200ProductReferences {
  reference: string;
  reference_type: string;
}

export interface OF22Response200RetailPrices {
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
}

export interface OF22Response200Warehouses {
  code: string;
  quantity: number;
}

export interface OF24Request {
  offers: Array<OF24RequestOffers>;
}

export interface OF24RequestOffers {
  all_prices?: Array<OF24RequestOffersAllPrices>;
  allow_quote_requests?: boolean;
  available_ended?: string;
  available_started?: string;
  description?: string;
  discount?: OF24RequestOffersDiscount;
  eco_contributions?: Array<OF24RequestOffersEcoContributions>;
  internal_description?: string;
  leadtime_to_ship?: number;
  logistic_class?: string;
  max_order_quantity?: number;
  min_order_quantity?: number;
  min_quantity_alert?: number;
  msrp?: number;
  offer_additional_fields?: Array<OF24RequestOffersOfferAdditionalFields>;
  package_quantity?: number;
  price: number;
  price_additional_info?: string;
  pricing_unit?: string;
  product_id: string;
  product_id_type: string;
  product_tax_code?: string;
  quantity?: number;
  retail_prices?: Array<OF24RequestOffersRetailPrices>;
  shop_sku: string;
  state_code: string;
  update_delete: string;
}

export interface OF24RequestOffersAllPrices {
  channel_code?: string;
  discount_end_date?: string;
  discount_start_date?: string;
  unit_discount_price?: number;
  unit_origin_price?: number;
  volume_prices?: Array<OF24RequestOffersAllPricesVolumePrices>;
}

export interface OF24RequestOffersAllPricesVolumePrices {
  quantity_threshold: number;
  unit_discount_price?: number;
  unit_origin_price: number;
}

export interface OF24RequestOffersDiscount {
  end_date?: string;
  price?: number;
  ranges?: Array<OF24RequestOffersDiscountRanges>;
  start_date?: string;
}

export interface OF24RequestOffersDiscountRanges {
  price: number;
  quantity_threshold: number;
}

export interface OF24RequestOffersEcoContributions {
  eco_contribution_amount?: number;
  epr_category_code: string;
  producer_id?: string;
}

export interface OF24RequestOffersOfferAdditionalFields {
  code: string;
  type?: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsBoolean extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsDate extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsLink extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsList extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsMultipleValuesList extends OF24RequestOffersOfferAdditionalFields {
  value: Array<string>;
}

export interface OF24RequestOffersOfferAdditionalFieldsNumeric extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsRegex extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsString extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersOfferAdditionalFieldsTextarea extends OF24RequestOffersOfferAdditionalFields {
  value: string;
}

export interface OF24RequestOffersRetailPrices {
  discount_end_date?: string;
  discount_start_date?: string;
  unit_discount_price?: number;
  unit_origin_price?: number;
}

export interface OF24Response201 {
  import_id: number;
}

export interface OF26Response200 {
  offer_id: number;
  quantity: number;
}

export interface OF51Response200TextCsvExtFileStructure {
  active?: boolean;
  allow_quote_requests?: boolean;
  available_end_date?: string;
  available_start_date?: string;
  channels?: string;
  currency_iso_code?: string;
  date_created?: string;
  deleted?: boolean;
  delivery_time_earliest_days_zoneCODEmethodCODE?: string;
  delivery_time_latest_days_zoneCODEmethodCODE?: string;
  description?: string;
  discount_end_date?: string;
  discount_end_date_channelchannelCode?: string;
  discount_price?: number;
  discount_price_channelchannelCode?: number;
  discount_ranges?: string;
  discount_ranges_channelchannelCode?: string;
  discount_retail_price?: number;
  discount_retail_price_end_date?: string;
  discount_retail_price_start_date?: string;
  discount_start_date?: string;
  discount_start_date_channelchannelCode?: string;
  eco_contribution_amount_EPR_category_code?: number;
  favorite_rank?: number;
  fulfillment_center_code?: string;
  last_updated?: string;
  leadtime_to_ship?: number;
  logistic_class?: string;
  max_order_quantity?: number;
  measurement_units?: string;
  min_order_quantity?: number;
  min_shipping_price?: number;
  min_shipping_price_additional?: number;
  min_shipping_type?: string;
  min_shipping_zone?: string;
  msrp?: number;
  offer_id?: number;
  ongoing_discount_campaigns?: string;
  origin_price?: number;
  origin_price_channelchannelCode?: number;
  origin_retail_price?: number;
  package_quantity?: number;
  premium?: boolean;
  price?: number;
  price_additional_info?: string;
  price_ranges?: string;
  price_ranges_channelchannelCode?: string;
  price_channelchannelCode?: number;
  producer_id_EPR_category_code?: string;
  product_sku?: string;
  product_tax_code?: string;
  professional?: boolean;
  quantity?: number;
  retail_price?: number;
  shipping_price_type_zoneCODEmethodCODE?: string;
  shipping_price_zoneCODEmethodCODE?: number;
  shop_id?: number;
  shop_name?: string;
  shop_sku?: string;
  state_code?: string;
  total_price?: number;
}

export interface OF52Request {
  channel_codes?: Array<string>;
  export_type?: string;
  include_fields?: Array<string>;
  include_inactive_offers?: boolean;
  items_per_chunk?: number;
  last_request_date?: string;
  megabytes_per_chunk?: number;
  ongoing_discount_campaign_identifiers?: Array<string>;
  rename_fields?: { [key: string]: string };
  shipping_zones?: Array<string>;
}

export interface OF52Response200 {
  tracking_id?: string;
}

export interface OF53Response200 {
  error?: OF53Response200Error;
  last_updated?: string;
  status?: string;
  urls?: Array<string>;
}

export interface OF53Response200Error {
  code?: string;
  detail?: string;
}

export interface OF54Response200ExtFileStructure {
  active?: boolean;
  allow_quote_requests?: boolean;
  available_end_date?: string;
  available_start_date?: string;
  channels?: Array<string>;
  currency_iso_code?: string;
  date_created?: string;
  deleted?: boolean;
  description?: string;
  eco_contributions?: Array<OF54Response200ExtFileStructureEcoContributions>;
  favorite_rank?: number;
  fulfillment?: OF54Response200ExtFileStructureFulfillment;
  is_professional?: boolean;
  last_updated?: string;
  leadtime_to_ship?: number;
  logistic_class?: OF54Response200ExtFileStructureLogisticClass;
  max_order_quantity?: number;
  measurement?: OF54Response200ExtFileStructureMeasurement;
  min_order_quantity?: number;
  min_shipping_price?: number;
  min_shipping_price_additional?: number;
  min_shipping_type?: string;
  min_shipping_zone?: string;
  msrp?: number;
  offer_additional_fields?: Array<OF54Response200ExtFileStructureOfferAdditionalFields>;
  offer_id?: number;
  ongoing_discount_campaigns?: Array<OF54Response200ExtFileStructureOngoingDiscountCampaigns>;
  package_quantity?: number;
  premium?: boolean;
  price_additional_info?: string;
  prices?: Array<OF54Response200ExtFileStructurePrices>;
  product_sku?: string;
  product_tax_code?: string;
  quantity?: number;
  retail_prices?: Array<OF54Response200ExtFileStructureRetailPrices>;
  shipping_types?: Array<OF54Response200ExtFileStructureShippingTypes>;
  shop_id?: number;
  shop_name?: string;
  shop_sku?: string;
  state_code?: string;
  warehouses?: Array<OF54Response200ExtFileStructureWarehouses>;
}

export interface OF54Response200ExtFileStructureEcoContributions {
  eco_contribution_amount?: number;
  epr_category_code: string;
  producer_id?: string;
}

export interface OF54Response200ExtFileStructureFulfillment {
  center?: OF54Response200ExtFileStructureFulfillmentCenter;
}

export interface OF54Response200ExtFileStructureFulfillmentCenter {
  code?: string;
}

export interface OF54Response200ExtFileStructureLogisticClass {
  code?: string;
}

export interface OF54Response200ExtFileStructureMeasurement {
  total_measurement_of_product?: number;
  unit?: string;
}

export interface OF54Response200ExtFileStructureOfferAdditionalFields {
  code?: string;
  type?: string;
  value?: string;
}

export interface OF54Response200ExtFileStructureOngoingDiscountCampaigns {
  identifier?: string;
}

export interface OF54Response200ExtFileStructurePrices {
  context?: OF54Response200ExtFileStructurePricesContext;
  discount_end_date?: string;
  discount_price?: number;
  discount_start_date?: string;
  origin_price?: number;
  volume_prices?: Array<OF54Response200ExtFileStructurePricesVolumePrices>;
}

export interface OF54Response200ExtFileStructurePricesContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface OF54Response200ExtFileStructurePricesVolumePrices {
  quantity_threshold?: number;
  unit_discount_price?: number;
  unit_origin_price?: number;
}

export interface OF54Response200ExtFileStructureRetailPrices {
  discount_end_date?: string;
  discount_price?: number;
  discount_start_date?: string;
  origin_price?: number;
}

export interface OF54Response200ExtFileStructureShippingTypes {
  code?: string;
  delivery_time?: OF54Response200ExtFileStructureShippingTypesDeliveryTime;
  shipping_price_additional_unit?: number;
  shipping_price_type?: string;
  shipping_price_unit?: number;
  shipping_zone_code?: string;
}

export interface OF54Response200ExtFileStructureShippingTypesDeliveryTime {
  earliest_days?: number;
  latest_days?: number;
}

export interface OF54Response200ExtFileStructureWarehouses {
  code?: string;
  quantity?: number;
}

export interface OF54Response200TextCsvExtFileStructure {
  active?: boolean;
  allow_quote_requests?: boolean;
  available_end_date?: string;
  available_start_date?: string;
  channels?: string;
  currency_iso_code?: string;
  date_created?: string;
  deleted?: boolean;
  delivery_time_earliest_days_zoneCODEmethodCODE?: string;
  delivery_time_latest_days_zoneCODEmethodCODE?: string;
  description?: string;
  discount_end_date?: string;
  discount_end_date_channelchannelCode?: string;
  discount_price?: number;
  discount_price_channelchannelCode?: number;
  discount_ranges?: string;
  discount_ranges_channelchannelCode?: string;
  discount_retail_price?: number;
  discount_retail_price_end_date?: string;
  discount_retail_price_start_date?: string;
  discount_start_date?: string;
  discount_start_date_channelchannelCode?: string;
  eco_contribution_amount_EPR_category_code?: number;
  favorite_rank?: number;
  fulfillment_center_code?: string;
  last_updated?: string;
  leadtime_to_ship?: number;
  logistic_class?: string;
  max_order_quantity?: number;
  measurement_units?: string;
  min_order_quantity?: number;
  min_shipping_price?: number;
  min_shipping_price_additional?: number;
  min_shipping_type?: string;
  min_shipping_zone?: string;
  msrp?: number;
  offer_id?: number;
  ongoing_discount_campaigns?: string;
  origin_price?: number;
  origin_price_channelchannelCode?: number;
  origin_retail_price?: number;
  package_quantity?: number;
  premium?: boolean;
  price?: number;
  price_additional_info?: string;
  price_ranges?: string;
  price_ranges_channelchannelCode?: string;
  price_channelchannelCode?: number;
  producer_id_EPR_category_code?: string;
  product_sku?: string;
  product_tax_code?: string;
  professional?: boolean;
  quantity?: number;
  retail_price?: number;
  shipping_price_additional_zoneCODEmethodCODE?: number;
  shipping_price_type_zoneCODEmethodCODE?: string;
  shipping_price_zoneCODEmethodCODE?: number;
  shop_id?: number;
  shop_name?: string;
  shop_sku?: string;
  state_code?: string;
  total_price?: number;
}

export interface OF61Response200 {
  offer_states: Array<OF61Response200OfferStates>;
  total_count: number;
}

export interface OF61Response200OfferStates {
  code: string;
  label: string;
}

export interface OR04Request {
  orders: Array<OR04RequestOrders>;
}

export interface OR04RequestOrders {
  order_id: string;
  order_lines?: Array<OR04RequestOrdersOrderLines>;
  references?: OR04RequestOrdersReferences;
}

export interface OR04RequestOrdersOrderLines {
  eco_contributions?: Array<OR04RequestOrdersOrderLinesEcoContributions>;
  order_line_id: string;
}

export interface OR04RequestOrdersOrderLinesEcoContributions {
  epr_category_code: string;
  producer_id: string;
  unit_amount?: number;
}

export interface OR04RequestOrdersReferences {
  order_reference_for_seller?: string;
}

export interface OR04Response200 {
  updated_orders?: Array<OR04Response200UpdatedOrders>;
}

export interface OR04Response200UpdatedOrders {
  errors?: Array<OR04Response200UpdatedOrdersErrors>;
  order_id?: string;
  updated?: OR04Response200UpdatedOrdersUpdated;
}

export interface OR04Response200UpdatedOrdersErrors {
  code: string;
  field: string;
  message: string;
}

export interface OR04Response200UpdatedOrdersUpdated {
  order_lines?: Array<OR04Response200UpdatedOrdersUpdatedOrderLines>;
  references?: OR04Response200UpdatedOrdersUpdatedReferences;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLines {
  cancelations?: Array<OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations>;
  eco_contributions?: Array<OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions>;
  order_line_id?: string;
  refunds?: Array<OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds>;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations {
  cancelation_id?: string;
  eco_contributions?: Array<OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions>;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions {
  epr_category_code?: string;
  producer_id?: string;
  producer_id_owner?: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLinesEcoContributions {
  epr_category_code?: string;
  producer_id?: string;
  producer_id_owner?: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLinesRefunds {
  eco_contributions?: Array<OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions>;
  refund_id?: string;
}

export interface OR04Response200UpdatedOrdersUpdatedOrderLinesRefundsEcoContributions {
  epr_category_code?: string;
  producer_id?: string;
  producer_id_owner?: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR04Response200UpdatedOrdersUpdatedReferences {
  order_reference_for_seller?: string;
}

export interface OR07Request {
  order_lines: Array<OR07RequestOrderLines>;
}

export interface OR07RequestOrderLines {
  id: string;
  shipping_from: OR07RequestOrderLinesShippingFrom;
}

export interface OR07RequestOrderLinesShippingFrom {
  address?: OR07RequestOrderLinesShippingFromAddress;
  warehouse?: OR07RequestOrderLinesShippingFromWarehouse;
}

export interface OR07RequestOrderLinesShippingFromAddress {
  city?: string;
  country_iso_code: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR07RequestOrderLinesShippingFromWarehouse {
  code?: string;
}

export interface OR07Response200 {
  order_lines?: Array<OR07Response200OrderLines>;
}

export interface OR07Response200OrderLines {
  errors?: Array<OR07Response200OrderLinesErrors>;
  id: string;
  updated?: OR07Response200OrderLinesUpdated;
}

export interface OR07Response200OrderLinesErrors {
  code: string;
  field: string;
  message: string;
}

export interface OR07Response200OrderLinesUpdated {
  address?: OR07Response200OrderLinesUpdatedAddress;
  warehouse?: OR07Response200OrderLinesUpdatedWarehouse;
}

export interface OR07Response200OrderLinesUpdatedAddress {
  city?: string;
  country_iso_code: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR07Response200OrderLinesUpdatedWarehouse {
  code?: string;
}

export interface OR11Response200 {
  orders: Array<OR11Response200Orders>;
  total_count: number;
}

export interface OR11Response200Orders {
  acceptance_decision_date?: string;
  can_cancel: boolean;
  can_shop_ship: boolean;
  channel?: OR11Response200OrdersChannel;
  commercial_id: string;
  created_date: string;
  currency_iso_code: string;
  customer: OR11Response200OrdersCustomer;
  customer_debited_date?: string;
  customer_directly_pays_seller?: boolean;
  customer_notification_email?: string;
  delivery_date?: OR11Response200OrdersDeliveryDate;
  discount_campaigns?: Array<OR11Response200OrdersDiscountCampaigns>;
  fulfillment: OR11Response200OrdersFulfillment;
  fully_refunded: boolean;
  has_customer_message: boolean;
  has_incident: boolean;
  has_invoice: boolean;
  invoice_details?: OR11Response200OrdersInvoiceDetails;
  last_updated_date: string;
  leadtime_to_ship: number;
  order_additional_fields?: Array<OR11Response200OrdersOrderAdditionalFields>;
  order_id: string;
  order_lines: Array<OR11Response200OrdersOrderLines>;
  order_refunds?: Array<OR11Response200OrdersOrderRefunds>;
  order_state: string;
  order_state_reason_code?: string;
  order_state_reason_label?: string;
  order_tax_mode: string;
  order_taxes?: Array<OR11Response200OrdersOrderTaxes>;
  paymentType: string;
  payment_duration?: number;
  payment_type?: string;
  payment_workflow?: string;
  price: number;
  promotions?: OR11Response200OrdersPromotions;
  quote_id?: string;
  references?: OR11Response200OrdersReferences;
  shipping_carrier_code?: string;
  shipping_carrier_standard_code?: string;
  shipping_company?: string;
  shipping_deadline?: string;
  shipping_price: number;
  shipping_pudo_id?: string;
  shipping_tracking?: string;
  shipping_tracking_url?: string;
  shipping_type_code: string;
  shipping_type_label: string;
  shipping_type_standard_code?: string;
  shipping_zone_code: string;
  shipping_zone_label: string;
  total_commission: number;
  total_price: number;
  transaction_date?: string;
  transaction_number?: string;
}

export interface OR11Response200OrdersChannel {
  code: string;
  label: string;
}

export interface OR11Response200OrdersCustomer {
  accounting_contact?: OR11Response200OrdersCustomerAccountingContact;
  billing_address: OR11Response200OrdersCustomerBillingAddress;
  civility?: string;
  customer_id: string;
  delivery_contact?: OR11Response200OrdersCustomerDeliveryContact;
  firstname: string;
  lastname: string;
  locale?: string;
  organization?: OR11Response200OrdersCustomerOrganization;
  shipping_address: OR11Response200OrdersCustomerShippingAddress;
}

export interface OR11Response200OrdersCustomerAccountingContact {
  civility?: string;
  customer_id: string;
  firstname: string;
  lastname: string;
  locale?: string;
}

export interface OR11Response200OrdersCustomerBillingAddress {
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR11Response200OrdersCustomerDeliveryContact {
  civility?: string;
  customer_id: string;
  firstname: string;
  lastname: string;
  locale?: string;
}

export interface OR11Response200OrdersCustomerOrganization {
  address?: OR11Response200OrdersCustomerOrganizationAddress;
  electronic_address?: string;
  identification_number?: string;
  name?: string;
  organization_id: string;
  phone_number?: string;
  tax_identification_number?: string;
}

export interface OR11Response200OrdersCustomerOrganizationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code: string;
}

export interface OR11Response200OrdersCustomerShippingAddress {
  additional_info?: string;
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR11Response200OrdersDeliveryDate {
  earliest: string;
  latest: string;
}

export interface OR11Response200OrdersDiscountCampaigns {
  identifier: string;
}

export interface OR11Response200OrdersFulfillment {
  center: OR11Response200OrdersFulfillmentCenter;
}

export interface OR11Response200OrdersFulfillmentCenter {
  code: string;
}

export interface OR11Response200OrdersInvoiceDetails {
  document_details?: Array<OR11Response200OrdersInvoiceDetailsDocumentDetails>;
  payment_terms?: OR11Response200OrdersInvoiceDetailsPaymentTerms;
}

export interface OR11Response200OrdersInvoiceDetailsDocumentDetails {
  format?: string;
}

export interface OR11Response200OrdersInvoiceDetailsPaymentTerms {
  days: number;
  type: string;
}

export interface OR11Response200OrdersOrderAdditionalFields {
  code: string;
  type?: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsBoolean extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsDate extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsLink extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsList extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsMultipleValuesList extends OR11Response200OrdersOrderAdditionalFields {
  value: Array<string>;
}

export interface OR11Response200OrdersOrderAdditionalFieldsNumeric extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsRegex extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsString extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderAdditionalFieldsTextarea extends OR11Response200OrdersOrderAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLines {
  can_refund: boolean;
  cancelations: Array<OR11Response200OrdersOrderLinesCancelations>;
  category_code: string;
  category_label: string;
  commission_fee: number;
  commission_rate_vat: number;
  commission_taxes?: Array<OR11Response200OrdersOrderLinesCommissionTaxes>;
  commission_vat: number;
  created_date: string;
  debited_date?: string;
  description: string;
  discount_campaign?: OR11Response200OrdersOrderLinesDiscountCampaign;
  eco_contributions?: Array<OR11Response200OrdersOrderLinesEcoContributions>;
  fees?: Array<OR11Response200OrdersOrderLinesFees>;
  last_updated_date: string;
  measurement?: OR11Response200OrdersOrderLinesMeasurement;
  offer_id: number;
  offer_sku: string;
  offer_state_code: string;
  order_line_additional_fields: Array<OR11Response200OrdersOrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
  order_line_index: number;
  order_line_state: string;
  order_line_state_reason_code?: string;
  order_line_state_reason_label?: string;
  origin_unit_price?: number;
  price: number;
  price_additional_info?: string;
  price_amount_breakdown?: OR11Response200OrdersOrderLinesPriceAmountBreakdown;
  price_unit: number;
  product_medias: Array<OR11Response200OrdersOrderLinesProductMedias>;
  product_shop_sku?: string;
  product_sku: string;
  product_title: string;
  promotions?: Array<OR11Response200OrdersOrderLinesPromotions>;
  purchase_information?: OR11Response200OrdersOrderLinesPurchaseInformation;
  quantity: number;
  received_date?: string;
  refunds: Array<OR11Response200OrdersOrderLinesRefunds>;
  shipped_date?: string;
  shipping_from?: OR11Response200OrdersOrderLinesShippingFrom;
  shipping_price: number;
  shipping_price_additional_unit?: number;
  shipping_price_amount_breakdown?: OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown;
  shipping_price_unit?: number;
  shipping_taxes?: Array<OR11Response200OrdersOrderLinesShippingTaxes>;
  tax_legal_notice?: string;
  taxes?: Array<OR11Response200OrdersOrderLinesTaxes>;
  total_commission: number;
  total_price: number;
}

export interface OR11Response200OrdersOrderLinesCancelations {
  amount?: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesCancelationsAmountBreakdown;
  commission_amount: number;
  commission_taxes: Array<OR11Response200OrdersOrderLinesCancelationsCommissionTaxes>;
  commission_total_amount: number;
  created_date: string;
  eco_contributions?: Array<OR11Response200OrdersOrderLinesCancelationsEcoContributions>;
  fees?: Array<OR11Response200OrdersOrderLinesCancelationsFees>;
  id: string;
  purchase_information?: OR11Response200OrdersOrderLinesCancelationsPurchaseInformation;
  quantity?: number;
  reason_code?: string;
  shipping_amount?: number;
  shipping_amount_breakdown?: OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown;
  shipping_taxes?: Array<OR11Response200OrdersOrderLinesCancelationsShippingTaxes>;
  taxes?: Array<OR11Response200OrdersOrderLinesCancelationsTaxes>;
}

export interface OR11Response200OrdersOrderLinesCancelationsAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesCancelationsAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesCancelationsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesCancelationsCommissionTaxes {
  amount: number;
  code: string;
}

export interface OR11Response200OrdersOrderLinesCancelationsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsFees {
  amount: number;
  code: string;
}

export interface OR11Response200OrdersOrderLinesCancelationsPurchaseInformation {
  purchase_commission_on_fees?: OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesCancelationsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR11Response200OrdersOrderLinesCancelationsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesCancelationsShippingTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesCancelationsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR11Response200OrdersOrderLinesCancelationsTaxesPurchaseTax;
  rate?: number;
}

export interface OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesCancelationsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesCancelationsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderLinesCommissionTaxes {
  amount: number;
  code: string;
  rate: number;
}

export interface OR11Response200OrdersOrderLinesDiscountCampaign {
  identifier: string;
}

export interface OR11Response200OrdersOrderLinesEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR11Response200OrdersOrderLinesFees {
  amount: number;
  code: string;
}

export interface OR11Response200OrdersOrderLinesMeasurement {
  actual_measurement?: number;
  measurement_unit?: string;
  ordered_measurement?: number;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsBoolean extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsDate extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsLink extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsList extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsNumeric extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsRegex extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsString extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsTextarea extends OR11Response200OrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR11Response200OrdersOrderLinesPriceAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesPriceAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesPriceAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesProductMedias {
  media_url: string;
  mime_type: string;
  type: string;
}

export interface OR11Response200OrdersOrderLinesPromotions {
  apportioned: boolean;
  campaign?: OR11Response200OrdersOrderLinesPromotionsCampaign;
  _configuration: OR11Response200OrdersOrderLinesPromotionsConfiguration;
  deduced_amount: number;
  id: string;
  offered_quantity?: number;
  promo_code?: string;
}

export interface OR11Response200OrdersOrderLinesPromotionsCampaign {
  identifier: string;
}

export interface OR11Response200OrdersOrderLinesPromotionsConfiguration {
  amount_off?: number;
  free_items_quantity?: number;
  internal_description: string;
  percentage_off?: number;
  reduced_unit_price?: number;
  type: string;
}

export interface OR11Response200OrdersOrderLinesPurchaseInformation {
  purchase_commission_on_fees?: OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
  purchase_unit_price: number;
}

export interface OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesRefunds {
  amount?: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesRefundsAmountBreakdown;
  commission_amount: number;
  commission_tax_amount: number;
  commission_taxes: Array<OR11Response200OrdersOrderLinesRefundsCommissionTaxes>;
  commission_total_amount: number;
  created_date: string;
  eco_contributions?: Array<OR11Response200OrdersOrderLinesRefundsEcoContributions>;
  fees?: Array<OR11Response200OrdersOrderLinesRefundsFees>;
  id: string;
  order_refund_id: string;
  purchase_information?: OR11Response200OrdersOrderLinesRefundsPurchaseInformation;
  quantity: number;
  reason_code: string;
  refund_state: string;
  shipping_amount?: number;
  shipping_amount_breakdown?: OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown;
  shipping_taxes?: Array<OR11Response200OrdersOrderLinesRefundsShippingTaxes>;
  state: string;
  tax_legal_notice?: string;
  taxes?: Array<OR11Response200OrdersOrderLinesRefundsTaxes>;
  transaction_date?: string;
  transaction_number?: string;
}

export interface OR11Response200OrdersOrderLinesRefundsAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesRefundsAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesRefundsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesRefundsCommissionTaxes {
  amount: number;
  code: string;
}

export interface OR11Response200OrdersOrderLinesRefundsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR11Response200OrdersOrderLinesRefundsFees {
  amount: number;
  code: string;
}

export interface OR11Response200OrdersOrderLinesRefundsPurchaseInformation {
  purchase_commission_on_fees?: OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR11Response200OrdersOrderLinesRefundsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesRefundsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderLinesRefundsTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesRefundsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR11Response200OrdersOrderLinesRefundsTaxesPurchaseTax;
  rate?: number;
}

export interface OR11Response200OrdersOrderLinesRefundsTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesRefundsTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesRefundsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesRefundsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderLinesShippingFrom {
  address?: OR11Response200OrdersOrderLinesShippingFromAddress;
  warehouse?: OR11Response200OrdersOrderLinesShippingFromWarehouse;
}

export interface OR11Response200OrdersOrderLinesShippingFromAddress {
  city?: string;
  country_iso_code: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR11Response200OrdersOrderLinesShippingFromWarehouse {
  code?: string;
}

export interface OR11Response200OrdersOrderLinesShippingPriceAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesShippingPriceAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesShippingPriceAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesShippingTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR11Response200OrdersOrderLinesShippingTaxesPurchaseTax;
  rate?: number;
  tax_calculation_rule: string;
}

export interface OR11Response200OrdersOrderLinesShippingTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesShippingTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderLinesTaxes {
  amount: number;
  amount_breakdown?: OR11Response200OrdersOrderLinesTaxesAmountBreakdown;
  code: string;
  origin_unit_amount?: number;
  purchase_tax?: OR11Response200OrdersOrderLinesTaxesPurchaseTax;
  rate?: number;
  tax_calculation_rule: string;
}

export interface OR11Response200OrdersOrderLinesTaxesAmountBreakdown {
  parts: Array<OR11Response200OrdersOrderLinesTaxesAmountBreakdownParts>;
}

export interface OR11Response200OrdersOrderLinesTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR11Response200OrdersOrderLinesTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR11Response200OrdersOrderRefunds {
  order_refund_id: string;
  taxes?: Array<OR11Response200OrdersOrderRefundsTaxes>;
}

export interface OR11Response200OrdersOrderRefundsTaxes {
  code: string;
  rate?: number;
  total_amount: number;
}

export interface OR11Response200OrdersOrderTaxes {
  code: string;
  rate?: number;
  total_amount: number;
}

export interface OR11Response200OrdersPromotions {
  applied_promotions: Array<OR11Response200OrdersPromotionsAppliedPromotions>;
  total_deduced_amount: number;
}

export interface OR11Response200OrdersPromotionsAppliedPromotions {
  apportioned: boolean;
  campaign?: OR11Response200OrdersPromotionsAppliedPromotionsCampaign;
  _configuration: OR11Response200OrdersPromotionsAppliedPromotionsConfiguration;
  deduced_amount: number;
  id: string;
  offered_quantity?: number;
  promo_code?: string;
}

export interface OR11Response200OrdersPromotionsAppliedPromotionsCampaign {
  identifier: string;
}

export interface OR11Response200OrdersPromotionsAppliedPromotionsConfiguration {
  amount_off?: number;
  free_items_quantity?: number;
  internal_description: string;
  percentage_off?: number;
  reduced_unit_price?: number;
  type: string;
}

export interface OR11Response200OrdersReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface OR12Response200 {
  acceptance_decision_date: string;
  commercial_id: string;
  created_date: string;
  customer?: OR12Response200Customer;
  has_customer_message: boolean;
  has_incident: boolean;
  has_invoice: boolean;
  last_updated_date: string;
  order_id: string;
  order_lines: Array<OR12Response200OrderLines>;
  order_state: string;
  order_state_reason_code: string;
  order_state_reason_label: string;
  paymentType: string;
  payment_type: string;
  price: number;
  shipping_company?: string;
  shipping_price: number;
  shipping_tracking?: string;
  shipping_tracking_url?: string;
  shipping_type_code: string;
  shipping_type_label: string;
  shipping_zone_code: string;
  shipping_zone_label: string;
  total_commission: number;
  total_price: number;
}

export interface OR12Response200Customer {
  billing_address: OR12Response200CustomerBillingAddress;
  civility?: string;
  customer_id: string;
  firstname: string;
  lastname: string;
  shipping_address: OR12Response200CustomerShippingAddress;
}

export interface OR12Response200CustomerBillingAddress {
  city: string;
  civility?: string;
  company?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR12Response200CustomerShippingAddress {
  additional_info?: string;
  city: string;
  civility?: string;
  company?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR12Response200OrderLines {
  can_refund: boolean;
  category_code: string;
  category_label: string;
  commission_fee: number;
  commission_rate_vat: number;
  commission_vat: number;
  created_date: string;
  debited_date: string;
  description: string;
  last_updated_date: string;
  offer_id: number;
  offer_sku: string;
  offer_state_code: string;
  order_line_additional_fields: Array<OR12Response200OrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
  order_line_index: number;
  order_line_state: string;
  order_line_state_reason_code: string;
  order_line_state_reason_label: string;
  price: number;
  price_additional_info?: string;
  price_unit: number;
  product_sku: string;
  product_title: string;
  quantity: number;
  received_date: string;
  shipped_date: string;
  shipping_price: number;
  shipping_price_additional_unit: number;
  shipping_price_unit: number;
  total_commission: number;
  total_price: number;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsBoolean extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsDate extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsLink extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsList extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsNumeric extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsRegex extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsString extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR12Response200OrderLinesOrderLineAdditionalFieldsTextarea extends OR12Response200OrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR13Request {
  channel_codes?: Array<string>;
  end_date?: string;
  end_update_date?: string;
  fulfillment_center_codes?: string;
  items_per_chunk?: number;
  megabytes_per_chunk?: number;
  only_null_channel?: boolean;
  order_state_codes?: Array<string>;
  order_tax_mode?: string;
  start_date?: string;
  start_update_date?: string;
}

export interface OR13Response200 {
  tracking_id: string;
}

export interface OR14Response200 {
  last_updated: string;
  status: string;
  urls?: Array<string>;
}

export interface OR15Response200ExtFileStructure {
  orders: Array<OR15Response200ExtFileStructureOrders>;
}

export interface OR15Response200ExtFileStructureOrders {
  acceptance_decision_date?: string;
  can_cancel: boolean;
  can_shop_ship: boolean;
  channel?: OR15Response200ExtFileStructureOrdersChannel;
  commercial_id: string;
  created_date: string;
  currency_iso_code: string;
  customer: OR15Response200ExtFileStructureOrdersCustomer;
  customer_debited_date?: string;
  customer_directly_pays_seller?: boolean;
  customer_notification_email?: string;
  delivery_date?: OR15Response200ExtFileStructureOrdersDeliveryDate;
  discount_campaigns?: Array<OR15Response200ExtFileStructureOrdersDiscountCampaigns>;
  fulfillment: OR15Response200ExtFileStructureOrdersFulfillment;
  fully_refunded: boolean;
  has_customer_message: boolean;
  has_incident: boolean;
  has_invoice: boolean;
  invoice_details?: OR15Response200ExtFileStructureOrdersInvoiceDetails;
  last_updated_date: string;
  leadtime_to_ship: number;
  order_additional_fields?: Array<OR15Response200ExtFileStructureOrdersOrderAdditionalFields>;
  order_id: string;
  order_lines: Array<OR15Response200ExtFileStructureOrdersOrderLines>;
  order_refunds?: Array<OR15Response200ExtFileStructureOrdersOrderRefunds>;
  order_state: string;
  order_state_reason_code?: string;
  order_state_reason_label?: string;
  order_tax_mode: string;
  order_taxes?: Array<OR15Response200ExtFileStructureOrdersOrderTaxes>;
  paymentType: string;
  payment_duration?: number;
  payment_type?: string;
  payment_workflow?: string;
  price: number;
  promotions?: OR15Response200ExtFileStructureOrdersPromotions;
  quote_id?: string;
  references?: OR15Response200ExtFileStructureOrdersReferences;
  shipping_carrier_code?: string;
  shipping_carrier_standard_code?: string;
  shipping_company?: string;
  shipping_deadline?: string;
  shipping_price: number;
  shipping_pudo_id?: string;
  shipping_tracking?: string;
  shipping_tracking_url?: string;
  shipping_type_code: string;
  shipping_type_label: string;
  shipping_type_standard_code?: string;
  shipping_zone_code: string;
  shipping_zone_label: string;
  total_commission: number;
  total_price: number;
  transaction_date?: string;
  transaction_number?: string;
}

export interface OR15Response200ExtFileStructureOrdersChannel {
  code: string;
  label: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomer {
  accounting_contact?: OR15Response200ExtFileStructureOrdersCustomerAccountingContact;
  billing_address: OR15Response200ExtFileStructureOrdersCustomerBillingAddress;
  civility?: string;
  customer_id: string;
  delivery_contact?: OR15Response200ExtFileStructureOrdersCustomerDeliveryContact;
  firstname: string;
  lastname: string;
  locale?: string;
  organization?: OR15Response200ExtFileStructureOrdersCustomerOrganization;
  shipping_address: OR15Response200ExtFileStructureOrdersCustomerShippingAddress;
}

export interface OR15Response200ExtFileStructureOrdersCustomerAccountingContact {
  civility?: string;
  customer_id: string;
  firstname: string;
  lastname: string;
  locale?: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomerBillingAddress {
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomerDeliveryContact {
  civility?: string;
  customer_id: string;
  firstname: string;
  lastname: string;
  locale?: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomerOrganization {
  address?: OR15Response200ExtFileStructureOrdersCustomerOrganizationAddress;
  electronic_address?: string;
  identification_number?: string;
  name?: string;
  organization_id: string;
  phone_number?: string;
  tax_identification_number?: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomerOrganizationAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code: string;
}

export interface OR15Response200ExtFileStructureOrdersCustomerShippingAddress {
  additional_info?: string;
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR15Response200ExtFileStructureOrdersDeliveryDate {
  earliest: string;
  latest: string;
}

export interface OR15Response200ExtFileStructureOrdersDiscountCampaigns {
  identifier: string;
}

export interface OR15Response200ExtFileStructureOrdersFulfillment {
  center: OR15Response200ExtFileStructureOrdersFulfillmentCenter;
}

export interface OR15Response200ExtFileStructureOrdersFulfillmentCenter {
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersInvoiceDetails {
  document_details?: Array<OR15Response200ExtFileStructureOrdersInvoiceDetailsDocumentDetails>;
  payment_terms?: OR15Response200ExtFileStructureOrdersInvoiceDetailsPaymentTerms;
}

export interface OR15Response200ExtFileStructureOrdersInvoiceDetailsDocumentDetails {
  format?: string;
}

export interface OR15Response200ExtFileStructureOrdersInvoiceDetailsPaymentTerms {
  days: number;
  type: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  code: string;
  type?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsBoolean extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsDate extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsLink extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsList extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsMultipleValuesList extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: Array<string>;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsNumeric extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsRegex extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsString extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderAdditionalFieldsTextarea extends OR15Response200ExtFileStructureOrdersOrderAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLines {
  can_refund: boolean;
  cancelations: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelations>;
  category_code: string;
  category_label: string;
  commission_fee: number;
  commission_rate_vat: number;
  commission_taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesCommissionTaxes>;
  commission_vat: number;
  created_date: string;
  debited_date?: string;
  description: string;
  discount_campaign?: OR15Response200ExtFileStructureOrdersOrderLinesDiscountCampaign;
  eco_contributions?: Array<OR15Response200ExtFileStructureOrdersOrderLinesEcoContributions>;
  fees?: Array<OR15Response200ExtFileStructureOrdersOrderLinesFees>;
  last_updated_date: string;
  measurement?: OR15Response200ExtFileStructureOrdersOrderLinesMeasurement;
  offer_id: number;
  offer_sku: string;
  offer_state_code: string;
  order_line_additional_fields: Array<OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
  order_line_index: number;
  order_line_state: string;
  order_line_state_reason_code?: string;
  order_line_state_reason_label?: string;
  origin_unit_price?: number;
  price: number;
  price_additional_info?: string;
  price_amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdown;
  price_unit: number;
  product_medias: Array<OR15Response200ExtFileStructureOrdersOrderLinesProductMedias>;
  product_shop_sku?: string;
  product_sku: string;
  product_title: string;
  promotions?: Array<OR15Response200ExtFileStructureOrdersOrderLinesPromotions>;
  purchase_information?: OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformation;
  quantity: number;
  received_date?: string;
  refunds: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefunds>;
  shipped_date?: string;
  shipping_from?: OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom;
  shipping_price: number;
  shipping_price_additional_unit?: number;
  shipping_price_amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown;
  shipping_price_unit?: number;
  shipping_taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes>;
  tax_legal_notice?: string;
  taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesTaxes>;
  total_commission: number;
  total_price: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelations {
  amount?: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdown;
  commission_amount: number;
  commission_taxes: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsCommissionTaxes>;
  commission_total_amount: number;
  created_date: string;
  eco_contributions?: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsEcoContributions>;
  fees?: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsFees>;
  id: string;
  purchase_information?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformation;
  quantity?: number;
  reason_code?: string;
  shipping_amount?: number;
  shipping_amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdown;
  shipping_taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxes>;
  taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxes>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsCommissionTaxes {
  amount: number;
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsFees {
  amount: number;
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformation {
  purchase_commission_on_fees?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesPurchaseTax;
  rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCancelationsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesCommissionTaxes {
  amount: number;
  code: string;
  rate: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesDiscountCampaign {
  identifier: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesFees {
  amount: number;
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesMeasurement {
  actual_measurement?: number;
  measurement_unit?: string;
  ordered_measurement?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsBoolean extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsDate extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsLink extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsList extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsNumeric extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsRegex extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsString extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsTextarea extends OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPriceAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesProductMedias {
  media_url: string;
  mime_type: string;
  type: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPromotions {
  apportioned: boolean;
  campaign?: OR15Response200ExtFileStructureOrdersOrderLinesPromotionsCampaign;
  _configuration: OR15Response200ExtFileStructureOrdersOrderLinesPromotionsConfiguration;
  deduced_amount: number;
  id: string;
  offered_quantity?: number;
  promo_code?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPromotionsCampaign {
  identifier: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPromotionsConfiguration {
  amount_off?: number;
  free_items_quantity?: number;
  internal_description: string;
  percentage_off?: number;
  reduced_unit_price?: number;
  type: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformation {
  purchase_commission_on_fees?: OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
  purchase_unit_price: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefunds {
  amount?: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdown;
  commission_amount: number;
  commission_tax_amount: number;
  commission_taxes: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsCommissionTaxes>;
  commission_total_amount: number;
  created_date: string;
  eco_contributions?: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions>;
  fees?: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsFees>;
  id: string;
  order_refund_id: string;
  purchase_information?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation;
  quantity: number;
  reason_code: string;
  refund_state: string;
  shipping_amount?: number;
  shipping_amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdown;
  shipping_taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxes>;
  state: string;
  tax_legal_notice?: string;
  taxes?: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxes>;
  transaction_date?: string;
  transaction_number?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsCommissionTaxes {
  amount: number;
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsFees {
  amount: number;
  code: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation {
  purchase_commission_on_fees?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesPurchaseTax;
  rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom {
  address?: OR15Response200ExtFileStructureOrdersOrderLinesShippingFromAddress;
  warehouse?: OR15Response200ExtFileStructureOrdersOrderLinesShippingFromWarehouse;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingFromAddress {
  city?: string;
  country_iso_code: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingFromWarehouse {
  code?: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesPurchaseTax;
  rate?: number;
  tax_calculation_rule: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesTaxes {
  amount: number;
  amount_breakdown?: OR15Response200ExtFileStructureOrdersOrderLinesTaxesAmountBreakdown;
  code: string;
  origin_unit_amount?: number;
  purchase_tax?: OR15Response200ExtFileStructureOrdersOrderLinesTaxesPurchaseTax;
  rate?: number;
  tax_calculation_rule: string;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesTaxesAmountBreakdown {
  parts: Array<OR15Response200ExtFileStructureOrdersOrderLinesTaxesAmountBreakdownParts>;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR15Response200ExtFileStructureOrdersOrderLinesTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderRefunds {
  order_refund_id: string;
  taxes?: Array<OR15Response200ExtFileStructureOrdersOrderRefundsTaxes>;
}

export interface OR15Response200ExtFileStructureOrdersOrderRefundsTaxes {
  code: string;
  rate?: number;
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersOrderTaxes {
  code: string;
  rate?: number;
  total_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersPromotions {
  applied_promotions: Array<OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotions>;
  total_deduced_amount: number;
}

export interface OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotions {
  apportioned: boolean;
  campaign?: OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsCampaign;
  _configuration: OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsConfiguration;
  deduced_amount: number;
  id: string;
  offered_quantity?: number;
  promo_code?: string;
}

export interface OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsCampaign {
  identifier: string;
}

export interface OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsConfiguration {
  amount_off?: number;
  free_items_quantity?: number;
  internal_description: string;
  percentage_off?: number;
  reduced_unit_price?: number;
  type: string;
}

export interface OR15Response200ExtFileStructureOrdersReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface OR21Request {
  order_lines: Array<OR21RequestOrderLines>;
}

export interface OR21RequestOrderLines {
  accepted: boolean;
  id: string;
}

export interface OR23Request {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  carrier_url?: string;
  tracking_number?: string;
}

export interface OR26Request {
  order_lines: Array<OR26RequestOrderLines>;
}

export interface OR26RequestOrderLines {
  id: string;
  reason_code: string;
}

export interface OR28Request {
  order_tax_mode?: string;
  refunds: Array<OR28RequestRefunds>;
}

export interface OR28RequestRefunds {
  amount: number;
  currency_iso_code?: string;
  excluded_from_shipment?: boolean;
  fees?: Array<OR28RequestRefundsFees>;
  order_line_id: string;
  quantity?: number;
  reason_code: string;
  shipping_amount: number;
  shipping_taxes?: Array<OR28RequestRefundsShippingTaxes>;
  taxes?: Array<OR28RequestRefundsTaxes>;
}

export interface OR28RequestRefundsFees {
  amount?: number;
  code?: string;
}

export interface OR28RequestRefundsShippingTaxes {
  amount?: number;
  code?: string;
}

export interface OR28RequestRefundsTaxes {
  amount?: number;
  code?: string;
}

export interface OR28Response200 {
  order_tax_mode: string;
  refunds: Array<OR28Response200Refunds>;
}

export interface OR28Response200Refunds {
  amount: number;
  amount_breakdown?: OR28Response200RefundsAmountBreakdown;
  currency_iso_code?: string;
  eco_contributions?: Array<OR28Response200RefundsEcoContributions>;
  excluded_from_shipment?: boolean;
  fees?: Array<OR28Response200RefundsFees>;
  order_line_id: string;
  order_refund_id: string;
  purchase_information?: OR28Response200RefundsPurchaseInformation;
  quantity: number;
  reason_code: string;
  refund_id: string;
  shipping_amount: number;
  shipping_amount_breakdown?: OR28Response200RefundsShippingAmountBreakdown;
  shipping_taxes?: Array<OR28Response200RefundsShippingTaxes>;
  taxes?: Array<OR28Response200RefundsTaxes>;
}

export interface OR28Response200RefundsAmountBreakdown {
  parts: Array<OR28Response200RefundsAmountBreakdownParts>;
}

export interface OR28Response200RefundsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR28Response200RefundsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR28Response200RefundsFees {
  amount?: number;
  code?: string;
}

export interface OR28Response200RefundsPurchaseInformation {
  purchase_commission_on_fees?: OR28Response200RefundsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR28Response200RefundsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR28Response200RefundsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR28Response200RefundsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR28Response200RefundsShippingAmountBreakdown {
  parts: Array<OR28Response200RefundsShippingAmountBreakdownParts>;
}

export interface OR28Response200RefundsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR28Response200RefundsShippingTaxes {
  amount: number;
  amount_breakdown?: OR28Response200RefundsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR28Response200RefundsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR28Response200RefundsShippingTaxesAmountBreakdown {
  parts: Array<OR28Response200RefundsShippingTaxesAmountBreakdownParts>;
}

export interface OR28Response200RefundsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR28Response200RefundsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR28Response200RefundsTaxes {
  amount: number;
  amount_breakdown?: OR28Response200RefundsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR28Response200RefundsTaxesPurchaseTax;
  rate?: number;
}

export interface OR28Response200RefundsTaxesAmountBreakdown {
  parts: Array<OR28Response200RefundsTaxesAmountBreakdownParts>;
}

export interface OR28Response200RefundsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR28Response200RefundsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR30Request {
  cancelations: Array<OR30RequestCancelations>;
  order_tax_mode?: string;
}

export interface OR30RequestCancelations {
  amount: number;
  currency_iso_code?: string;
  fees?: Array<OR30RequestCancelationsFees>;
  order_line_id: string;
  quantity: number;
  reason_code: string;
  shipping_amount: number;
  shipping_taxes?: Array<OR30RequestCancelationsShippingTaxes>;
  taxes?: Array<OR30RequestCancelationsTaxes>;
}

export interface OR30RequestCancelationsFees {
  amount?: number;
  code?: string;
}

export interface OR30RequestCancelationsShippingTaxes {
  amount?: number;
  code?: string;
}

export interface OR30RequestCancelationsTaxes {
  amount?: number;
  code?: string;
}

export interface OR30Response200 {
  cancelations: Array<OR30Response200Cancelations>;
  order_tax_mode: string;
}

export interface OR30Response200Cancelations {
  amount: number;
  amount_breakdown?: OR30Response200CancelationsAmountBreakdown;
  cancelation_id: string;
  currency_iso_code?: string;
  eco_contributions?: Array<OR30Response200CancelationsEcoContributions>;
  fees?: Array<OR30Response200CancelationsFees>;
  order_line_id: string;
  purchase_information?: OR30Response200CancelationsPurchaseInformation;
  quantity?: number;
  reason_code: string;
  shipping_amount: number;
  shipping_amount_breakdown?: OR30Response200CancelationsShippingAmountBreakdown;
  shipping_taxes?: Array<OR30Response200CancelationsShippingTaxes>;
  taxes?: Array<OR30Response200CancelationsTaxes>;
}

export interface OR30Response200CancelationsAmountBreakdown {
  parts: Array<OR30Response200CancelationsAmountBreakdownParts>;
}

export interface OR30Response200CancelationsAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR30Response200CancelationsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR30Response200CancelationsFees {
  amount?: number;
  code?: string;
}

export interface OR30Response200CancelationsPurchaseInformation {
  purchase_commission_on_fees?: OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees;
  purchase_commission_on_price: number;
  purchase_commission_on_shipping: number;
  purchase_fee_amount?: OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount;
  purchase_price: number;
  purchase_shipping_price: number;
}

export interface OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees {
  total_amount: number;
}

export interface OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount {
  total_amount: number;
}

export interface OR30Response200CancelationsShippingAmountBreakdown {
  parts: Array<OR30Response200CancelationsShippingAmountBreakdownParts>;
}

export interface OR30Response200CancelationsShippingAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR30Response200CancelationsShippingTaxes {
  amount: number;
  amount_breakdown?: OR30Response200CancelationsShippingTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR30Response200CancelationsShippingTaxesPurchaseTax;
  rate?: number;
}

export interface OR30Response200CancelationsShippingTaxesAmountBreakdown {
  parts: Array<OR30Response200CancelationsShippingTaxesAmountBreakdownParts>;
}

export interface OR30Response200CancelationsShippingTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR30Response200CancelationsShippingTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR30Response200CancelationsTaxes {
  amount: number;
  amount_breakdown?: OR30Response200CancelationsTaxesAmountBreakdown;
  code: string;
  purchase_tax?: OR30Response200CancelationsTaxesPurchaseTax;
  rate?: number;
}

export interface OR30Response200CancelationsTaxesAmountBreakdown {
  parts: Array<OR30Response200CancelationsTaxesAmountBreakdownParts>;
}

export interface OR30Response200CancelationsTaxesAmountBreakdownParts {
  amount: number;
  commissionable?: boolean;
  debitable_from_customer?: boolean;
  payable_to_shop?: boolean;
}

export interface OR30Response200CancelationsTaxesPurchaseTax {
  purchase_amount: number;
  purchase_rate?: number;
}

export interface OR31Request {
  order_additional_fields?: Array<OR31RequestOrderAdditionalFields>;
  order_lines?: Array<OR31RequestOrderLines>;
}

export interface OR31RequestOrderAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31RequestOrderAdditionalFieldsBoolean extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsDate extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsLink extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsList extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsMultipleValuesList extends OR31RequestOrderAdditionalFields {
  value: Array<string>;
}

export interface OR31RequestOrderAdditionalFieldsNumeric extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsRegex extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsString extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderAdditionalFieldsTextarea extends OR31RequestOrderAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLines {
  order_line_additional_fields?: Array<OR31RequestOrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsBoolean extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsDate extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsLink extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsList extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsNumeric extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsRegex extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsString extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31RequestOrderLinesOrderLineAdditionalFieldsTextarea extends OR31RequestOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200 {
  order_update_errors?: OR31Response200OrderUpdateErrors;
  order_update_result?: OR31Response200OrderUpdateResult;
}

export interface OR31Response200OrderUpdateErrors {
  errors: Array<OR31Response200OrderUpdateErrorsErrors>;
  input?: OR31Response200OrderUpdateErrorsInput;
}

export interface OR31Response200OrderUpdateErrorsErrors {
  code: string;
  field: string;
  message: string;
}

export interface OR31Response200OrderUpdateErrorsInput {
  order_additional_fields?: Array<OR31Response200OrderUpdateErrorsInputOrderAdditionalFields>;
  order_lines?: Array<OR31Response200OrderUpdateErrorsInputOrderLines>;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsBoolean extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsDate extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsLink extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsList extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsMultipleValuesList extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: Array<string>;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsNumeric extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsRegex extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsString extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderAdditionalFieldsTextarea extends OR31Response200OrderUpdateErrorsInputOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLines {
  order_line_additional_fields?: Array<OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsBoolean extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsDate extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsLink extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsList extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsNumeric extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsRegex extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsString extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsTextarea extends OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResult {
  order_additional_fields?: Array<OR31Response200OrderUpdateResultOrderAdditionalFields>;
  order_lines?: Array<OR31Response200OrderUpdateResultOrderLines>;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsBoolean extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsDate extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsLink extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsList extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsMultipleValuesList extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: Array<string>;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsNumeric extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsRegex extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsString extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderAdditionalFieldsTextarea extends OR31Response200OrderUpdateResultOrderAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLines {
  order_line_additional_fields?: Array<OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields>;
  order_line_id: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  code: string;
  type?: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsBoolean extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsDate extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsLink extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsList extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsMultipleValuesList extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: Array<string>;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsNumeric extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsRegex extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsString extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFieldsTextarea extends OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields {
  value: string;
}

export interface OR32Request {
  order_lines: Array<OR32RequestOrderLines>;
}

export interface OR32RequestOrderLines {
  actual_measurement: number;
  order_line_id: string;
}

export interface OR32Response200 {
  order_lines_adjusted?: Array<OR32Response200OrderLinesAdjusted>;
}

export interface OR32Response200OrderLinesAdjusted {
  cancelations?: Array<OR32Response200OrderLinesAdjustedCancelations>;
  errors?: Array<OR32Response200OrderLinesAdjustedErrors>;
  measurement?: OR32Response200OrderLinesAdjustedMeasurement;
  order_line_id?: string;
  refunds?: Array<OR32Response200OrderLinesAdjustedRefunds>;
}

export interface OR32Response200OrderLinesAdjustedCancelations {
  amount?: number;
  currency_iso_code?: string;
  eco_contributions?: Array<OR32Response200OrderLinesAdjustedCancelationsEcoContributions>;
  quantity?: number;
  reason_code?: string;
  shipping_amount?: number;
  shipping_taxes?: Array<OR32Response200OrderLinesAdjustedCancelationsShippingTaxes>;
  taxes?: Array<OR32Response200OrderLinesAdjustedCancelationsTaxes>;
}

export interface OR32Response200OrderLinesAdjustedCancelationsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR32Response200OrderLinesAdjustedCancelationsShippingTaxes {
  amount?: number;
  code?: string;
}

export interface OR32Response200OrderLinesAdjustedCancelationsTaxes {
  amount?: number;
  code?: string;
}

export interface OR32Response200OrderLinesAdjustedErrors {
  code: string;
  field: string;
  message: string;
}

export interface OR32Response200OrderLinesAdjustedMeasurement {
  actual_measurement?: number;
  measurement_unit?: string;
  ordered_measurement?: number;
}

export interface OR32Response200OrderLinesAdjustedRefunds {
  amount?: number;
  currency_iso_code?: string;
  eco_contributions?: Array<OR32Response200OrderLinesAdjustedRefundsEcoContributions>;
  quantity?: number;
  reason_code?: string;
  shipping_amount?: number;
  shipping_taxes?: Array<OR32Response200OrderLinesAdjustedRefundsShippingTaxes>;
  taxes?: Array<OR32Response200OrderLinesAdjustedRefundsTaxes>;
}

export interface OR32Response200OrderLinesAdjustedRefundsEcoContributions {
  epr_category_code: string;
  producer_id: string;
  producer_id_owner: string;
  total_amount?: number;
  unit_amount?: number;
}

export interface OR32Response200OrderLinesAdjustedRefundsShippingTaxes {
  amount?: number;
  code?: string;
}

export interface OR32Response200OrderLinesAdjustedRefundsTaxes {
  amount?: number;
  code?: string;
}

export interface OR33Request {
  order_lines: Array<OR33RequestOrderLines>;
}

export interface OR33RequestOrderLines {
  id: string;
  reason_code: string;
}

export interface OR41Response200 {
  messages: Array<OR41Response200Messages>;
  total_count: number;
}

export interface OR41Response200Messages {
  archived?: boolean;
  body: string;
  commercial_id: string;
  date_created: string;
  documents?: Array<OR41Response200MessagesDocuments>;
  from_id: string;
  from_name: string;
  from_type: string;
  id: number;
  offer_id?: number;
  order_id?: string;
  read?: boolean;
  subject: string;
  to_customer_archived: boolean;
  to_customer_id: string;
  to_customer_name: string;
  to_operator: boolean;
  to_operator_archived: boolean;
  to_shop_archived: boolean;
  to_shop_id: number;
  to_shop_name: string;
  visible?: boolean;
}

export interface OR41Response200MessagesDocuments {
  date_uploaded?: string;
  file_name: string;
  file_size?: number;
  id: number;
  type: string;
}

export interface OR42Request {
  body: string;
  document_ids?: Array<number>;
  subject: string;
  to_customer: boolean;
  to_operator: boolean;
  to_shop: boolean;
}

export interface OR42Response201 {
  id: number;
}

export interface OR43RequestMultipartFormDataThreadInput {
  body: string;
  to: Array<string>;
  topic: OR43RequestMultipartFormDataThreadInputTopic;
}

export interface OR43RequestMultipartFormDataThreadInputTopic {
  type: string;
  value: string;
}

export interface OR43RequestMultipartFormDataThreadInputTopicFreeText {
  type: string;
  value: string;
}

export interface OR43RequestMultipartFormDataThreadInputTopicReasonCode {
  type: string;
  value: string;
}

export interface OR43Response201 {
  message_id: string;
  thread_id: string;
}

export interface OR51Response200 {
  assessments: Array<OR51Response200Assessments>;
  comment?: string;
  customer_id: string;
  date: string;
  firstname: string;
  grade: number;
  last_updated_date: string;
  lastname: string;
  reply?: OR51Response200Reply;
  visible: boolean;
}

export interface OR51Response200Assessments {
  code: string;
  label: string;
  response: string;
}

export interface OR51Response200Reply {
  comment: string;
  date: string;
  type: string;
}

export interface OR64Request {
  reason_code: string;
}

export interface OR72Response200 {
  order_documents: Array<OR72Response200OrderDocuments>;
  total_count?: number;
}

export interface OR72Response200OrderDocuments {
  date_uploaded?: string;
  file_name: string;
  file_size?: number;
  id: number;
  order_id: string;
  type: string;
}

export interface OR74RequestMultipartFormDataOrderDocuments {
  order_documents: Array<OR74RequestMultipartFormDataOrderDocumentsOrderDocuments>;
}

export interface OR74RequestMultipartFormDataOrderDocumentsOrderDocuments {
  entity?: OR74RequestMultipartFormDataOrderDocumentsOrderDocumentsEntity;
  file_name: string;
  type_code: string;
}

export interface OR74RequestMultipartFormDataOrderDocumentsOrderDocumentsEntity {
  id: string;
  type: string;
}

export interface OR74Response200 {
  errors_count?: number;
  order_documents: Array<OR74Response200OrderDocuments>;
}

export interface OR74Response200OrderDocuments {
  errors: Array<OR74Response200OrderDocumentsErrors>;
  input?: OR74Response200OrderDocumentsInput;
}

export interface OR74Response200OrderDocumentsErrors {
  code: string;
  field: string;
  message: string;
}

export interface OR74Response200OrderDocumentsInput {
  file_name?: string;
  type_code?: string;
}

export interface OR75Response200 {
  taxes: Array<OR75Response200Taxes>;
}

export interface OR75Response200Taxes {
  code: string;
  label: string;
  tax_calculation_rule: string;
}

export interface P11Response200 {
  products?: Array<P11Response200Products>;
}

export interface P11Response200Products {
  category_code: string;
  category_label: string;
  measurement?: P11Response200ProductsMeasurement;
  offers?: Array<P11Response200ProductsOffers>;
  product_brand?: string;
  product_description?: string;
  product_media?: P11Response200ProductsProductMedia;
  product_references: Array<P11Response200ProductsProductReferences>;
  product_sku: string;
  product_title: string;
  total_count: number;
}

export interface P11Response200ProductsMeasurement {
  total_measurement_of_product?: number;
  unit: string;
}

export interface P11Response200ProductsOffers {
  active: boolean;
  all_prices: Array<P11Response200ProductsOffersAllPrices>;
  allow_quote_requests?: boolean;
  applicable_pricing?: P11Response200ProductsOffersApplicablePricing;
  available_end_date?: string;
  available_start_date?: string;
  channels: Array<string>;
  currency_iso_code: string;
  description: string;
  discount?: P11Response200ProductsOffersDiscount;
  eco_contributions?: Array<P11Response200ProductsOffersEcoContributions>;
  favorite_rank?: number;
  inactivity_reasons?: Array<string>;
  is_professional: boolean;
  leadtime_to_ship: number;
  logistic_class: P11Response200ProductsOffersLogisticClass;
  min_quantity_alert: number;
  min_shipping_price: number;
  min_shipping_price_additional: number;
  min_shipping_type: string;
  min_shipping_zone: string;
  msrp?: number;
  nb_evaluation: number;
  offer_additional_fields?: Array<P11Response200ProductsOffersOfferAdditionalFields>;
  offer_id: number;
  premium: boolean;
  price?: number;
  price_additional_info?: string;
  quantity: number;
  retail_prices?: Array<P11Response200ProductsOffersRetailPrices>;
  shipping_deadline: string;
  shipping_types?: Array<P11Response200ProductsOffersShippingTypes>;
  shop_grade: number;
  shop_id: number;
  shop_name: string;
  state_code: string;
  total_price?: number;
}

export interface P11Response200ProductsOffersAllPrices {
  channel_code?: string;
  context?: P11Response200ProductsOffersAllPricesContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<P11Response200ProductsOffersAllPricesVolumePrices>;
}

export interface P11Response200ProductsOffersAllPricesContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface P11Response200ProductsOffersAllPricesVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface P11Response200ProductsOffersApplicablePricing {
  channel_code?: string;
  context?: P11Response200ProductsOffersApplicablePricingContext;
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
  volume_prices: Array<P11Response200ProductsOffersApplicablePricingVolumePrices>;
}

export interface P11Response200ProductsOffersApplicablePricingContext {
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  start_date?: string;
}

export interface P11Response200ProductsOffersApplicablePricingVolumePrices {
  price: number;
  quantity_threshold: number;
  unit_discount_price: number;
  unit_origin_price: number;
}

export interface P11Response200ProductsOffersDiscount {
  discount_price?: number;
  end_date?: string;
  origin_price?: number;
  ranges?: Array<P11Response200ProductsOffersDiscountRanges>;
  start_date?: string;
}

export interface P11Response200ProductsOffersDiscountRanges {
  price: number;
  quantity_threshold: number;
}

export interface P11Response200ProductsOffersEcoContributions {
  eco_contribution_amount?: number;
  epr_category_code: string;
  producer_id?: string;
}

export interface P11Response200ProductsOffersLogisticClass {
  code: string;
  label: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFields {
  code: string;
  type?: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsBoolean extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsDate extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsLink extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsList extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsMultipleValuesList extends P11Response200ProductsOffersOfferAdditionalFields {
  value: Array<string>;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsNumeric extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsRegex extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsString extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersOfferAdditionalFieldsTextarea extends P11Response200ProductsOffersOfferAdditionalFields {
  value: string;
}

export interface P11Response200ProductsOffersRetailPrices {
  discount_end_date?: string;
  discount_start_date?: string;
  price: number;
  unit_discount_price?: number;
  unit_origin_price: number;
}

export interface P11Response200ProductsOffersShippingTypes {
  code: string;
  cut_off_next_date?: string;
  cut_off_time?: string;
  delivery_time?: P11Response200ProductsOffersShippingTypesDeliveryTime;
  label: string;
  shipping_deadline?: string;
  shipping_price_type: string;
  shipping_price_unit: number;
  shipping_zone_code: string;
  shipping_zone_label: string;
  standard_code?: string;
}

export interface P11Response200ProductsOffersShippingTypesDeliveryTime {
  earliest_days: number;
  earliest_delivery_date: string;
  latest_days: number;
  latest_delivery_date: string;
}

export interface P11Response200ProductsProductMedia {
  dam_url: string;
  media_url: string;
  type: string;
}

export interface P11Response200ProductsProductReferences {
  reference: string;
  reference_type: string;
}

export interface P31Response200 {
  products: Array<P31Response200Products>;
  total_count: number;
}

export interface P31Response200Products {
  category_code: string;
  category_label: string;
  product_id: string;
  product_id_type: string;
  product_sku: string;
  product_title: string;
}

export interface P41RequestMultipartFormDataConversionOptions {
  ai_enrichment?: P41RequestMultipartFormDataConversionOptionsAiEnrichment;
  ai_rewrite?: P41RequestMultipartFormDataConversionOptionsAiRewrite;
  ai_translation?: P41RequestMultipartFormDataConversionOptionsAiTranslation;
}

export interface P41RequestMultipartFormDataConversionOptionsAiEnrichment {
  status?: string;
}

export interface P41RequestMultipartFormDataConversionOptionsAiRewrite {
  status?: string;
}

export interface P41RequestMultipartFormDataConversionOptionsAiTranslation {
  status?: string;
}

export interface P41Response201 {
  import_id: number;
}

export interface P42Response200 {
  conversion_options?: P42Response200ConversionOptions;
  conversion_type?: string;
  date_created: string;
  has_error_report: boolean;
  has_new_product_report: boolean;
  has_transformation_error_report?: boolean;
  has_transformed_file: boolean;
  import_id: number;
  import_status: string;
  integration_details?: P42Response200IntegrationDetails;
  reason_status?: string;
  shop_id: number;
  transform_lines_in_error: number;
  transform_lines_in_success: number;
  transform_lines_read: number;
  transform_lines_with_warning: number;
}

export interface P42Response200ConversionOptions {
  ai_enrichment?: P42Response200ConversionOptionsAiEnrichment;
  ai_rewrite?: P42Response200ConversionOptionsAiRewrite;
  ai_translation?: P42Response200ConversionOptionsAiTranslation;
}

export interface P42Response200ConversionOptionsAiEnrichment {
  status?: string;
}

export interface P42Response200ConversionOptionsAiRewrite {
  status?: string;
}

export interface P42Response200ConversionOptionsAiTranslation {
  status?: string;
}

export interface P42Response200IntegrationDetails {
  invalid_products?: number;
  products_not_accepted_in_time?: number;
  products_not_synchronized_in_time?: number;
  products_reimported?: number;
  products_successfully_synchronized?: number;
  products_with_synchronization_issues?: number;
  products_with_wrong_identifiers?: number;
  rejected_products?: number;
}

export interface P51Response200 {
  product_import_trackings?: Array<P51Response200ProductImportTrackings>;
  total_count: number;
}

export interface P51Response200ProductImportTrackings {
  conversion_options?: P51Response200ProductImportTrackingsConversionOptions;
  conversion_type?: string;
  date_created: string;
  has_error_report: boolean;
  has_new_product_report: boolean;
  has_transformation_error_report?: boolean;
  has_transformed_file: boolean;
  import_id: number;
  import_status: string;
  integration_details?: P51Response200ProductImportTrackingsIntegrationDetails;
  reason_status?: string;
  shop_id: number;
  transform_lines_in_error: number;
  transform_lines_in_success: number;
  transform_lines_read: number;
  transform_lines_with_warning: number;
}

export interface P51Response200ProductImportTrackingsConversionOptions {
  ai_enrichment?: P51Response200ProductImportTrackingsConversionOptionsAiEnrichment;
  ai_rewrite?: P51Response200ProductImportTrackingsConversionOptionsAiRewrite;
  ai_translation?: P51Response200ProductImportTrackingsConversionOptionsAiTranslation;
}

export interface P51Response200ProductImportTrackingsConversionOptionsAiEnrichment {
  status?: string;
}

export interface P51Response200ProductImportTrackingsConversionOptionsAiRewrite {
  status?: string;
}

export interface P51Response200ProductImportTrackingsConversionOptionsAiTranslation {
  status?: string;
}

export interface P51Response200ProductImportTrackingsIntegrationDetails {
  invalid_products?: number;
  products_not_accepted_in_time?: number;
  products_not_synchronized_in_time?: number;
  products_reimported?: number;
  products_successfully_synchronized?: number;
  products_with_synchronization_issues?: number;
  products_with_wrong_identifiers?: number;
  rejected_products?: number;
}

export interface PC01Response200 {
  features: PC01Response200Features;
  modules: PC01Response200Modules;
  platform_configuration: PC01Response200PlatformConfiguration;
  platform_name: string;
  tenant_name: string;
  timezone: string;
}

export interface PC01Response200Features {
  catalog: PC01Response200FeaturesCatalog;
  circular_economy_data_collection: boolean;
  competitive_pricing_tool: boolean;
  direct_payment_customer_store: PC01Response200FeaturesDirectPaymentCustomerStore;
  disable_seller_alternative_carrier: boolean;
  dropship: PC01Response200FeaturesDropship;
  kyc_status_per_seller: boolean;
  lead_time_to_ship_by_sellers_enabled: string;
  multi_currency: boolean;
  multi_payout_psp_per_seller: boolean;
  no_reply_needed: boolean;
  offer_prices_decimals: string;
  operator_csv_delimiter: string;
  order_conditions: PC01Response200FeaturesOrderConditions;
  order_tax_mode: string;
  order_workflows: PC01Response200FeaturesOrderWorkflows;
  payment_confirmation: boolean;
  pricing: PC01Response200FeaturesPricing;
  product_data_validation_by_channel: boolean;
  promotion: PC01Response200FeaturesPromotion;
  returns: PC01Response200FeaturesReturns;
  shipment: PC01Response200FeaturesShipment;
  shop_tax_options: PC01Response200FeaturesShopTaxOptions;
  tax_collection: PC01Response200FeaturesTaxCollection;
  tax_id_number: PC01Response200FeaturesTaxIdNumber;
  warehouses: PC01Response200FeaturesWarehouses;
}

export interface PC01Response200FeaturesCatalog {
  allow_shop_contribution_to_all_channels: boolean;
  exclude_invalid_products: boolean;
  list_of_multiple_values_separator: string;
  product_acceptance_by_channel: boolean;
  product_data_validation_by_channel: boolean;
  product_import_only_on_leaf: boolean;
}

export interface PC01Response200FeaturesDirectPaymentCustomerStore {
  activated: boolean;
  refund_cancel_authorized: boolean;
}

export interface PC01Response200FeaturesDropship {
  retail_pricing_edition_enabled?: string;
  retail_pricing_enabled?: boolean;
}

export interface PC01Response200FeaturesOrderConditions {
  lead_time_to_ship: boolean;
  maximum_order_quantity: boolean;
  minimum_order_quantity: boolean;
  package_order_quantity: boolean;
}

export interface PC01Response200FeaturesOrderWorkflows {
  no_customer_payment_confirmation: boolean;
  order_acceptance: string;
  pause_debit_workflow: boolean;
  pay_on_due_date: boolean;
  pay_on_shipment: boolean;
  sellers_edit_shipping_origin: boolean;
  shipping_and_billing_details_before_acceptance: boolean;
}

export interface PC01Response200FeaturesPricing {
  channel_pricing: string;
  discount_period_required: boolean;
  discount_price_creation_in_the_past_blocked: boolean;
  scheduled_pricing: boolean;
  volume_discount: boolean;
  volume_pricing: boolean;
}

export interface PC01Response200FeaturesPromotion {
  cart_promotion_campaign: boolean;
  discount_campaign: boolean;
  seller_promotion: boolean;
}

export interface PC01Response200FeaturesReturns {
  drop_ship?: boolean;
  marketplace?: boolean;
  one_creditor?: boolean;
}

export interface PC01Response200FeaturesShipment {
  multi_part_item_shipment: boolean;
  multi_shipment: boolean;
}

export interface PC01Response200FeaturesShopTaxOptions {
  local_tax_number?: PC01Response200FeaturesShopTaxOptionsLocalTaxNumber;
  tax_identification_number: PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber;
}

export interface PC01Response200FeaturesShopTaxOptionsLocalTaxNumber {
  mandatory: boolean;
  validation_regex?: string;
}

export interface PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber {
  mandatory: boolean;
  validation_regex?: string;
}

export interface PC01Response200FeaturesTaxCollection {
  activated: string;
  product_tax_code_mandatory: boolean;
  tax_collection_by_operator: boolean;
}

export interface PC01Response200FeaturesTaxIdNumber {
  mandatory: boolean;
  validation_regex?: string;
}

export interface PC01Response200FeaturesWarehouses {
  geolocation: boolean;
  restricted_countries: Array<string>;
}

export interface PC01Response200Modules {
  mirakl_catalog_integrator: boolean;
  mirakl_catalog_manager: boolean;
  mirakl_catalog_transformer: boolean;
  mirakl_platform_services: boolean;
  offer_management: boolean;
  offer_management_mode?: string;
  order_management: boolean;
  order_management_mode?: string;
  promotions: boolean;
  quotes: boolean;
  tax_manager: PC01Response200ModulesTaxManager;
}

export interface PC01Response200ModulesTaxManager {
  activated: boolean;
  tax_provider: PC01Response200ModulesTaxManagerTaxProvider;
}

export interface PC01Response200ModulesTaxManagerTaxProvider {
  avalara: boolean;
  vertex: boolean;
}

export interface PC01Response200PlatformConfiguration {
  customer_model: PC01Response200PlatformConfigurationCustomerModel;
  enhanced_seller_invoicing: PC01Response200PlatformConfigurationEnhancedSellerInvoicing;
  platform_model: PC01Response200PlatformConfigurationPlatformModel;
}

export interface PC01Response200PlatformConfigurationCustomerModel {
  b2b: boolean;
  b2c: boolean;
}

export interface PC01Response200PlatformConfigurationEnhancedSellerInvoicing {
  enabled: boolean;
}

export interface PC01Response200PlatformConfigurationPlatformModel {
  drop_ship: boolean;
  marketplace: boolean;
  one_creditor: boolean;
}

export interface PL11Response200 {
  data: Array<PL11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface PL11Response200Data {
  date_created: string;
  id: string;
  last_updated: string;
  order_lines: Array<PL11Response200DataOrderLines>;
  picklist_lines: Array<PL11Response200DataPicklistLines>;
  pickrun_code?: string;
  pickup_date: string;
  shop_id?: number;
  state: string;
}

export interface PL11Response200DataOrderLines {
  id: string;
}

export interface PL11Response200DataPicklistLines {
  offer_id: number;
  quantity: number;
}

export interface PM11Response200 {
  attributes: Array<PM11Response200Attributes>;
}

export interface PM11Response200Attributes {
  channels?: Array<PM11Response200AttributesChannels>;
  code: string;
  default_value?: string;
  description?: string;
  description_translations: Array<PM11Response200AttributesDescriptionTranslations>;
  example?: string;
  hierarchy_code?: string;
  label?: string;
  label_translations: Array<PM11Response200AttributesLabelTranslations>;
  locale?: string;
  required: boolean;
  requirement_level: string;
  roles: Array<PM11Response200AttributesRoles>;
  transformations?: string;
  type: string;
  type_parameter: string;
  type_parameters?: Array<PM11Response200AttributesTypeParameters>;
  unique_code?: string;
  validations?: string;
  values?: Array<PM11Response200AttributesValues>;
  values_list?: string;
  variant: boolean;
}

export interface PM11Response200AttributesChannels {
  code: string;
}

export interface PM11Response200AttributesDescriptionTranslations {
  locale: string;
  value: string;
}

export interface PM11Response200AttributesLabelTranslations {
  locale: string;
  value: string;
}

export interface PM11Response200AttributesRoles {
  parameters: Array<PM11Response200AttributesRolesParameters>;
  type: string;
}

export interface PM11Response200AttributesRolesParameters {
  name: string;
  value: string;
}

export interface PM11Response200AttributesTypeParameters {
  name: string;
  value: string;
}

export interface PM11Response200AttributesValues {
  code: string;
}

export interface PM11Response200TextCsvExtFileStructure {
  channels?: string;
  code: string;
  default_value?: string;
  description?: string;
  description_xx: string;
  example?: string;
  hierarchy_code?: string;
  label?: string;
  label_xx: string;
  locale?: string;
  required: boolean;
  requirement_level: string;
  roles: string;
  transformations?: string;
  type: string;
  type_parameter: string;
  type_parameters?: string;
  unique_code?: string;
  validations?: string;
  values?: string;
  values_list?: string;
  variant: boolean;
}

export interface PR01Response200 {
  promotions: Array<PR01Response200Promotions>;
  total_count: number;
}

export interface PR01Response200Promotions {
  amount_off?: number;
  application_to_cart: Array<PR01Response200PromotionsApplicationToCart>;
  campaign?: PR01Response200PromotionsCampaign;
  channels: Array<PR01Response200PromotionsChannels>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  date_created: string;
  end_date: string;
  free_items_quantity?: number;
  internal_description: string;
  internal_id: string;
  last_updated: string;
  max_quantity_to_discount?: number;
  medias: Array<PR01Response200PromotionsMedias>;
  percentage_off?: number;
  public_descriptions: Array<PR01Response200PromotionsPublicDescriptions>;
  reduced_unit_price?: number;
  reward_offer_ids?: Array<number>;
  reward_on_purchased_items: boolean;
  start_date: string;
  state: string;
  trigger_offer_ids?: Array<number>;
  triggers: Array<PR01Response200PromotionsTriggers>;
  type: string;
}

export interface PR01Response200PromotionsApplicationToCart {
  promo_code?: string;
}

export interface PR01Response200PromotionsCampaign {
  identifier: string;
}

export interface PR01Response200PromotionsChannels {
  code: string;
  label: string;
}

export interface PR01Response200PromotionsMedias {
  locale: string;
  url: string;
}

export interface PR01Response200PromotionsPublicDescriptions {
  locale: string;
  value: string;
}

export interface PR01Response200PromotionsTriggers {
  amount_purchased?: number;
  quantity_purchased?: number;
  same_item_purchased?: boolean;
  type: string;
}

export interface PR03Request {
  application_to_cart?: Array<PR03RequestApplicationToCart>;
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  internal_description: string;
  internal_id: string;
  public_descriptions?: Array<PR03RequestPublicDescriptions>;
  reward: PR03RequestReward;
  start_date: string;
  trigger: PR03RequestTrigger;
}

export interface PR03RequestApplicationToCart {
  promo_code: string;
}

export interface PR03RequestPublicDescriptions {
  locale: string;
  value: string;
}

export interface PR03RequestReward {
  selection: PR03RequestRewardSelection;
  type: string;
}

export interface PR03RequestRewardAmountOff extends PR03RequestReward {
  amount_off: number;
}

export interface PR03RequestRewardFreeItems extends PR03RequestReward {
  free_items_quantity: number;
}

export interface PR03RequestRewardPercentageOff extends PR03RequestReward {
  max_quantity_to_discount?: number;
  percentage_off: number;
}

export interface PR03RequestRewardReducedUnitPrice extends PR03RequestReward {
  max_quantity_to_discount?: number;
  reduced_unit_price: number;
}

export interface PR03RequestRewardSelection {
  type: string;
}

export interface PR03RequestRewardSelectionBrand extends PR03RequestRewardSelection {
  values: Array<string>;
}

export interface PR03RequestRewardSelectionCategory extends PR03RequestRewardSelection {
  values: Array<string>;
}

export interface PR03RequestRewardSelectionOffer extends PR03RequestRewardSelection {
  values: Array<string>;
}

export interface PR03RequestRewardSelectionProduct extends PR03RequestRewardSelection {
  values: Array<PR03RequestRewardSelectionProductValues>;
}

export interface PR03RequestRewardSelectionProductValues {
  type: string;
  value: string;
}

export interface PR03RequestRewardSelectionPurchasedItems extends PR03RequestRewardSelection {}

export interface PR03RequestTrigger {
  selection?: PR03RequestTriggerSelection;
  type: string;
}

export interface PR03RequestTriggerEveryAmount extends PR03RequestTrigger {
  amount_purchased: number;
}

export interface PR03RequestTriggerEveryQuantity extends PR03RequestTrigger {
  quantity_purchased: number;
  same_item_purchased?: boolean;
}

export interface PR03RequestTriggerMinimumAmount extends PR03RequestTrigger {
  amount_purchased: number;
}

export interface PR03RequestTriggerMinimumQuantity extends PR03RequestTrigger {
  quantity_purchased: number;
  same_item_purchased?: boolean;
}

export interface PR03RequestTriggerSelection {
  type: string;
}

export interface PR03RequestTriggerSelectionAll extends PR03RequestTriggerSelection {}

export interface PR03RequestTriggerSelectionBrand extends PR03RequestTriggerSelection {
  values: Array<string>;
}

export interface PR03RequestTriggerSelectionCategory extends PR03RequestTriggerSelection {
  values: Array<string>;
}

export interface PR03RequestTriggerSelectionOffer extends PR03RequestTriggerSelection {
  values: Array<string>;
}

export interface PR03RequestTriggerSelectionProduct extends PR03RequestTriggerSelection {
  values: Array<PR03RequestTriggerSelectionProductValues>;
}

export interface PR03RequestTriggerSelectionProductValues {
  type: string;
  value: string;
}

export interface PR04Request {
  application_to_cart?: Array<PR04RequestApplicationToCart>;
  channel_codes?: Array<string>;
  customer_group_ids?: Array<string>;
  customer_organization_ids?: Array<string>;
  end_date?: string;
  internal_description: string;
  public_descriptions?: Array<PR04RequestPublicDescriptions>;
  reward: PR04RequestReward;
  start_date: string;
  trigger: PR04RequestTrigger;
}

export interface PR04RequestApplicationToCart {
  promo_code: string;
}

export interface PR04RequestPublicDescriptions {
  locale: string;
  value: string;
}

export interface PR04RequestReward {
  selection: PR04RequestRewardSelection;
}

export interface PR04RequestRewardSelection {
  type: string;
}

export interface PR04RequestRewardSelectionBrand extends PR04RequestRewardSelection {
  values: Array<string>;
}

export interface PR04RequestRewardSelectionCategory extends PR04RequestRewardSelection {
  values: Array<string>;
}

export interface PR04RequestRewardSelectionOffer extends PR04RequestRewardSelection {
  values: Array<string>;
}

export interface PR04RequestRewardSelectionProduct extends PR04RequestRewardSelection {
  values: Array<PR04RequestRewardSelectionProductValues>;
}

export interface PR04RequestRewardSelectionProductValues {
  type: string;
  value: string;
}

export interface PR04RequestRewardSelectionPurchasedItems extends PR04RequestRewardSelection {}

export interface PR04RequestTrigger {
  selection: PR04RequestTriggerSelection;
}

export interface PR04RequestTriggerSelection {
  type: string;
}

export interface PR04RequestTriggerSelectionAll extends PR04RequestTriggerSelection {}

export interface PR04RequestTriggerSelectionBrand extends PR04RequestTriggerSelection {
  values: Array<string>;
}

export interface PR04RequestTriggerSelectionCategory extends PR04RequestTriggerSelection {
  values: Array<string>;
}

export interface PR04RequestTriggerSelectionOffer extends PR04RequestTriggerSelection {
  values: Array<string>;
}

export interface PR04RequestTriggerSelectionProduct extends PR04RequestTriggerSelection {
  values: Array<PR04RequestTriggerSelectionProductValues>;
}

export interface PR04RequestTriggerSelectionProductValues {
  type: string;
  value: string;
}

export interface PRI01Response201 {
  importId?: string;
  import_id?: string;
}

export interface PRI02Response200 {
  data: Array<PRI02Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface PRI02Response200Data {
  date_created: string;
  has_error_report: boolean;
  import_id: string;
  lines_in_error: number;
  lines_in_success: number;
  offers_in_error: number;
  offers_updated: number;
  origin: string;
  reason_status: string;
  shop_id: number;
  status: string;
}

export interface RE01Response200 {
  reasons: Array<RE01Response200Reasons>;
  total_count: number;
}

export interface RE01Response200Reasons {
  code: string;
  is_shop_right: boolean;
  label: string;
  type: string;
}

export interface RE02Response200 {
  reasons: Array<RE02Response200Reasons>;
  total_count: number;
}

export interface RE02Response200Reasons {
  code: string;
  label: string;
}

export interface RE11Response200 {
  reasons: Array<RE11Response200Reasons>;
  total_count: number;
}

export interface RE11Response200Reasons {
  code: string;
  label: string;
}

export interface RE12Response200 {
  reasons: Array<RE12Response200Reasons>;
  total_count: number;
}

export interface RE12Response200Reasons {
  code: string;
  label: string;
}

export interface RE14Response200 {
  reasons: Array<RE14Response200Reasons>;
  total_count: number;
}

export interface RE14Response200Reasons {
  code: string;
  label: string;
}

export interface RO02Response200 {
  roles?: Array<RO02Response200Roles>;
}

export interface RO02Response200Roles {
  code?: string;
  description?: string;
}

export interface RT01Request {
  returns: Array<RT01RequestReturns>;
}

export interface RT01RequestReturns {
  accepted?: boolean;
  description?: string;
  label_url?: string;
  method_code: string;
  order_commercial_id: string;
  reason_code?: string;
  return_lines: Array<RT01RequestReturnsReturnLines>;
  rma?: string;
}

export interface RT01RequestReturnsReturnLines {
  order_line_id: string;
  quantity: number;
  reason_code: string;
}

export interface RT01Response200 {
  return_errors: Array<RT01Response200ReturnErrors>;
  return_success: Array<RT01Response200ReturnSuccess>;
}

export interface RT01Response200ReturnErrors {
  message?: string;
  order_commercial_id?: string;
}

export interface RT01Response200ReturnSuccess {
  date_created: string;
  description?: string;
  documents?: Array<RT01Response200ReturnSuccessDocuments>;
  id: string;
  label_url?: string;
  last_updated: string;
  method_code: string;
  order_commercial_id: string;
  order_id: string;
  reason_code?: string;
  rejection_reason_code?: string;
  return_address: RT01Response200ReturnSuccessReturnAddress;
  return_lines: Array<RT01Response200ReturnSuccessReturnLines>;
  rma?: string;
  state: string;
  tracking?: RT01Response200ReturnSuccessTracking;
}

export interface RT01Response200ReturnSuccessDocuments {
  id: number;
  type: string;
}

export interface RT01Response200ReturnSuccessReturnAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street1: string;
  street2?: string;
  zip_code: string;
}

export interface RT01Response200ReturnSuccessReturnLines {
  compliance?: Array<RT01Response200ReturnSuccessReturnLinesCompliance>;
  order_line_id: string;
  quantity: number;
  reason_code: string;
}

export interface RT01Response200ReturnSuccessReturnLinesCompliance {
  compliant: boolean;
  non_compliance_additional_info?: string;
  non_compliance_reason_code?: string;
}

export interface RT01Response200ReturnSuccessTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface RT04Request {
  returns: Array<RT04RequestReturns>;
}

export interface RT04RequestReturns {
  id: string;
  label_url?: string;
  method_code?: string;
  return_address?: RT04RequestReturnsReturnAddress;
  rma?: string;
  tracking?: RT04RequestReturnsTracking;
}

export interface RT04RequestReturnsReturnAddress {
  address?: RT04RequestReturnsReturnAddressAddress;
}

export interface RT04RequestReturnsReturnAddressAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street1: string;
  street2?: string;
  zip_code?: string;
}

export interface RT04RequestReturnsTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface RT04Response200 {
  return_errors?: Array<RT04Response200ReturnErrors>;
  return_success?: Array<RT04Response200ReturnSuccess>;
}

export interface RT04Response200ReturnErrors {
  id?: string;
  message?: string;
}

export interface RT04Response200ReturnSuccess {
  date_created: string;
  description?: string;
  documents?: Array<RT04Response200ReturnSuccessDocuments>;
  id: string;
  label_url?: string;
  last_updated: string;
  method_code: string;
  order_commercial_id: string;
  order_id: string;
  reason_code?: string;
  rejection_reason_code?: string;
  return_address: RT04Response200ReturnSuccessReturnAddress;
  return_lines: Array<RT04Response200ReturnSuccessReturnLines>;
  rma?: string;
  state: string;
  tracking?: RT04Response200ReturnSuccessTracking;
}

export interface RT04Response200ReturnSuccessDocuments {
  id: number;
  type: string;
}

export interface RT04Response200ReturnSuccessReturnAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street1: string;
  street2?: string;
  zip_code: string;
}

export interface RT04Response200ReturnSuccessReturnLines {
  compliance?: Array<RT04Response200ReturnSuccessReturnLinesCompliance>;
  order_line_id: string;
  quantity: number;
  reason_code: string;
}

export interface RT04Response200ReturnSuccessReturnLinesCompliance {
  compliant: boolean;
  non_compliance_additional_info?: string;
  non_compliance_reason_code?: string;
}

export interface RT04Response200ReturnSuccessTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface RT11Response200 {
  data: Array<RT11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface RT11Response200Data {
  date_created: string;
  description?: string;
  documents?: Array<RT11Response200DataDocuments>;
  id: string;
  label_url?: string;
  last_updated: string;
  method_code: string;
  order_commercial_id: string;
  order_id: string;
  reason_code?: string;
  rejection_reason_code?: string;
  return_address: RT11Response200DataReturnAddress;
  return_lines: Array<RT11Response200DataReturnLines>;
  rma?: string;
  state: string;
  tracking?: RT11Response200DataTracking;
}

export interface RT11Response200DataDocuments {
  id: number;
  type: string;
}

export interface RT11Response200DataReturnAddress {
  city: string;
  country_iso_code: string;
  state?: string;
  street1: string;
  street2?: string;
  zip_code: string;
}

export interface RT11Response200DataReturnLines {
  compliance?: Array<RT11Response200DataReturnLinesCompliance>;
  order_line_id: string;
  quantity: number;
  reason_code: string;
}

export interface RT11Response200DataReturnLinesCompliance {
  compliant: boolean;
  non_compliance_additional_info?: string;
  non_compliance_reason_code?: string;
}

export interface RT11Response200DataTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface RT12Response200 {
  data: Array<RT12Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface RT12Response200Data {
  available_return_methods?: Array<string>;
  available_return_reasons?: Array<string>;
  order_commercial_id: string;
  order_line_id: string;
  return_window?: number;
  return_window_end_date?: string;
  return_window_start_date?: string;
  returnable_quantity: number;
}

export interface RT21Request {
  returns: Array<RT21RequestReturns>;
}

export interface RT21RequestReturns {
  accepted: boolean;
  id: string;
  rejection_reason_code?: string;
}

export interface RT21Response200 {
  return_errors?: Array<RT21Response200ReturnErrors>;
  return_success?: Array<RT21Response200ReturnSuccess>;
}

export interface RT21Response200ReturnErrors {
  id?: string;
  message?: string;
}

export interface RT21Response200ReturnSuccess {
  id: string;
}

export interface RT25Request {
  returns: Array<RT25RequestReturns>;
}

export interface RT25RequestReturns {
  id: string;
}

export interface RT25Response200 {
  return_errors?: Array<RT25Response200ReturnErrors>;
  return_success?: Array<RT25Response200ReturnSuccess>;
}

export interface RT25Response200ReturnErrors {
  code?: string;
  id?: string;
  message?: string;
}

export interface RT25Response200ReturnSuccess {
  id: string;
}

export interface RT26Request {
  returns: Array<RT26RequestReturns>;
}

export interface RT26RequestReturns {
  id: string;
  return_lines: Array<RT26RequestReturnsReturnLines>;
}

export interface RT26RequestReturnsReturnLines {
  compliant: boolean;
  non_compliance_additional_info?: string;
  non_compliance_reason_code?: string;
  order_line_id: string;
}

export interface RT26Response200 {
  return_errors?: Array<RT26Response200ReturnErrors>;
  return_success?: Array<RT26Response200ReturnSuccess>;
}

export interface RT26Response200ReturnErrors {
  id?: string;
  message?: string;
}

export interface RT26Response200ReturnSuccess {
  id: string;
}

export interface RT27Request {
  returns: Array<RT27RequestReturns>;
}

export interface RT27RequestReturns {
  id: string;
}

export interface RT27Response200 {
  return_errors?: Array<RT27Response200ReturnErrors>;
  return_success?: Array<RT27Response200ReturnSuccess>;
}

export interface RT27Response200ReturnErrors {
  code?: string;
  id?: string;
  message?: string;
}

export interface RT27Response200ReturnSuccess {
  id: string;
}

export interface RT29Request {
  returns: Array<RT29RequestReturns>;
}

export interface RT29RequestReturns {
  id: string;
}

export interface RT29Response200 {
  return_errors?: Array<RT29Response200ReturnErrors>;
  return_success?: Array<RT29Response200ReturnSuccess>;
}

export interface RT29Response200ReturnErrors {
  id?: string;
  message?: string;
}

export interface RT29Response200ReturnSuccess {
  id: string;
}

export interface RT51Request {
  return_labels: Array<RT51RequestReturnLabels>;
}

export interface RT51RequestReturnLabels {
  carrier_code?: string;
  carrier_service_code?: string;
  label_options?: RT51RequestReturnLabelsLabelOptions;
  label_selection_mode?: string;
  _package: RT51RequestReturnLabelsPackage;
  return_id: string;
  shipping_from?: RT51RequestReturnLabelsShippingFrom;
}

export interface RT51RequestReturnLabelsLabelOptions {
  qr_code?: boolean;
}

export interface RT51RequestReturnLabelsPackage {
  dimensions: RT51RequestReturnLabelsPackageDimensions;
  weight: RT51RequestReturnLabelsPackageWeight;
}

export interface RT51RequestReturnLabelsPackageDimensions {
  height: number;
  length: number;
  unit: string;
  width: number;
}

export interface RT51RequestReturnLabelsPackageWeight {
  unit: string;
  value: number;
}

export interface RT51RequestReturnLabelsShippingFrom {
  city: string;
  contact_name: string;
  contact_phone: string;
  country_iso_code: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface RT51Response200 {
  return_label_errors?: Array<RT51Response200ReturnLabelErrors>;
  return_label_successes?: Array<RT51Response200ReturnLabelSuccesses>;
}

export interface RT51Response200ReturnLabelErrors {
  error_message?: string;
  return_id?: string;
}

export interface RT51Response200ReturnLabelSuccesses {
  return_id?: string;
}

export interface RT52Response200 {
  data: Array<RT52Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface RT52Response200Data {
  date_created: string;
  errors?: Array<RT52Response200DataErrors>;
  estimated_cost?: RT52Response200DataEstimatedCost;
  files?: RT52Response200DataFiles;
  label_state: string;
  last_updated: string;
  return_id: string;
  tracking?: RT52Response200DataTracking;
}

export interface RT52Response200DataErrors {
  code?: string;
  message?: string;
}

export interface RT52Response200DataEstimatedCost {
  amount?: number;
  currency_iso_code?: string;
}

export interface RT52Response200DataFiles {
  label?: RT52Response200DataFilesLabel;
  qr_code?: RT52Response200DataFilesQrCode;
}

export interface RT52Response200DataFilesLabel {
  file_type?: string;
  url?: string;
}

export interface RT52Response200DataFilesQrCode {
  file_type?: string;
  url?: string;
}

export interface RT52Response200DataTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_service_code?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface S30Response200 {
  shop_documents: Array<S30Response200ShopDocuments>;
  total_count?: number;
}

export interface S30Response200ShopDocuments {
  date_uploaded?: string;
  file_name: string;
  id: number;
  type: string;
}

export interface S32RequestMultipartFormDataShopDocuments {
  shop_documents: Array<S32RequestMultipartFormDataShopDocumentsShopDocuments>;
}

export interface S32RequestMultipartFormDataShopDocumentsShopDocuments {
  file_name: string;
  type_code: string;
}

export interface S32Response200 {
  documents: Array<S32Response200Documents>;
  errors_count?: number;
}

export interface S32Response200Documents {
  errors: Array<S32Response200DocumentsErrors>;
}

export interface S32Response200DocumentsErrors {
  code: string;
  field: string;
  message: string;
}

export interface SBC11Response200 {
  data: Array<SBC11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface SBC11Response200Data {
  amount_transferred_to_operator?: number;
  amount_transferred_to_seller?: number;
  currency_iso_code?: string;
  date_created?: string;
  id?: string;
  pay_out?: SBC11Response200DataPayOut;
  pay_out_psp_code?: string;
  payment_voucher_number?: string;
  shop?: SBC11Response200DataShop;
  summary?: SBC11Response200DataSummary;
}

export interface SBC11Response200DataPayOut {
  failure_reason?: string;
  reference?: string;
  state?: string;
  transaction_date?: string;
}

export interface SBC11Response200DataShop {
  shop_corporate_name?: string;
  shop_id?: number;
  shop_model?: string;
  shop_name?: string;
  shop_operator_internal_id?: string;
}

export interface SBC11Response200DataSummary {
  total_commissions_excl_tax?: number;
  total_commissions_incl_tax?: number;
  total_fee_excl_tax?: number;
  total_fee_incl_tax?: number;
  total_fee_operator_remitted_excl_tax?: number;
  total_fee_operator_remitted_incl_tax?: number;
  total_mirakl_ads_credit_excl_tax?: number;
  total_mirakl_ads_credit_incl_tax?: number;
  total_mirakl_ads_debit_excl_tax?: number;
  total_mirakl_ads_debit_incl_tax?: number;
  total_non_payable_orders_excl_tax?: number;
  total_non_payable_orders_incl_tax?: number;
  total_operator_paid_shipping_charges_excl_tax?: number;
  total_operator_paid_shipping_charges_incl_tax?: number;
  total_operator_remitted_taxes?: number;
  total_other_credits_excl_tax?: number;
  total_other_credits_incl_tax?: number;
  total_other_invoices_excl_tax?: number;
  total_other_invoices_incl_tax?: number;
  total_payable_orders_excl_tax?: number;
  total_payable_orders_incl_tax?: number;
  total_purchase_taxes?: number;
  total_refund_commissions_excl_tax?: number;
  total_refund_commissions_incl_tax?: number;
  total_refund_fee_excl_tax?: number;
  total_refund_fee_incl_tax?: number;
  total_refund_fee_operator_remitted_excl_tax?: number;
  total_refund_fee_operator_remitted_incl_tax?: number;
  total_refund_non_payable_orders_excl_tax?: number;
  total_refund_non_payable_orders_incl_tax?: number;
  total_refund_operator_paid_shipping_charges_excl_tax?: number;
  total_refund_operator_paid_shipping_charges_incl_tax?: number;
  total_refund_operator_remitted_taxes?: number;
  total_refund_orders_excl_tax?: number;
  total_refund_orders_incl_tax?: number;
  total_refund_payable_orders_excl_tax?: number;
  total_refund_payable_orders_incl_tax?: number;
  total_refund_purchase_taxes?: number;
  total_seller_fees_on_orders_excl_tax?: number;
  total_seller_fees_on_orders_incl_tax?: number;
  total_seller_penalty_fees_excl_tax?: number;
  total_seller_penalty_fees_incl_tax?: number;
  total_subscription_excl_tax?: number;
  total_subscription_incl_tax?: number;
}

export interface SH11Response200 {
  shipping_zones: Array<SH11Response200ShippingZones>;
}

export interface SH11Response200ShippingZones {
  code: string;
  description: string;
  label: string;
}

export interface SH12Response200 {
  shipping_types?: Array<SH12Response200ShippingTypes>;
}

export interface SH12Response200ShippingTypes {
  click_and_collect: boolean;
  code: string;
  delivery_by_operator: boolean;
  description: string;
  ignore_lead_time_to_ship?: boolean;
  label: string;
  mandatory_tracking: boolean;
  standard_code?: string;
}

export interface SH21Response200 {
  carriers: Array<SH21Response200Carriers>;
}

export interface SH21Response200Carriers {
  code: string;
  label: string;
  standard_code?: string;
  tracking_url?: string;
}

export interface SH31Response200 {
  logistic_classes: Array<SH31Response200LogisticClasses>;
}

export interface SH31Response200LogisticClasses {
  code: string;
  description: string;
  label: string;
}

export interface SH42Response200 {
  delivery_times: Array<SH42Response200DeliveryTimes>;
  last_updated_date?: string;
  lead_time_to_ship: SH42Response200LeadTimeToShip;
  order_cut_off_times: Array<SH42Response200OrderCutOffTimes>;
  order_free_shipping: boolean;
  shipping_paid_by_operator: boolean;
  shop_id: string;
}

export interface SH42Response200DeliveryTimes {
  delivery_time?: SH42Response200DeliveryTimesDeliveryTime;
  set_by: string;
  shipping_type_code: string;
  shipping_zone_code: string;
}

export interface SH42Response200DeliveryTimesDeliveryTime {
  earliest_days: number;
  latest_days: number;
}

export interface SH42Response200LeadTimeToShip {
  default_value: number;
  shop_value: number;
}

export interface SH42Response200OrderCutOffTimes {
  cut_off_time: string;
  is_required: boolean;
  set_by: string;
  shipping_type_code: string;
}

export interface SH52Response200 {
  _configuration: Array<SH52Response200Configuration>;
  currency_iso_code: string;
  last_updated_date: string;
  shop_id: number;
}

export interface SH52Response200Configuration {
  logistic_class_code: string;
  overridden_by_shop: boolean;
  prices: SH52Response200ConfigurationPrices;
  shipping_method_code: string;
  shipping_zone_code: string;
}

export interface SH52Response200ConfigurationPrices {
  additional_price?: number;
  free_shipping_threshold?: number;
  initial_price?: number;
  ranges?: Array<SH52Response200ConfigurationPricesRanges>;
  type: string;
}

export interface SH52Response200ConfigurationPricesRanges {
  price: number;
  threshold: number;
}

export interface ST01Request {
  shipments: Array<ST01RequestShipments>;
}

export interface ST01RequestShipments {
  invoice_reference?: string;
  order_id: string;
  shipment_additional_information?: Array<ST01RequestShipmentsShipmentAdditionalInformation>;
  shipment_lines: Array<ST01RequestShipmentsShipmentLines>;
  shipped?: boolean;
  shipping_from?: ST01RequestShipmentsShippingFrom;
  tracking?: ST01RequestShipmentsTracking;
}

export interface ST01RequestShipmentsShipmentAdditionalInformation {
  code: string;
  type: string;
  value: string;
}

export interface ST01RequestShipmentsShipmentAdditionalInformationDate extends ST01RequestShipmentsShipmentAdditionalInformation {
  value: string;
}

export interface ST01RequestShipmentsShipmentAdditionalInformationString extends ST01RequestShipmentsShipmentAdditionalInformation {
  value: string;
}

export interface ST01RequestShipmentsShipmentLines {
  offer_sku?: string;
  order_line_id?: string;
  package_reference?: string;
  quantity: number;
}

export interface ST01RequestShipmentsShippingFrom {
  warehouse?: ST01RequestShipmentsShippingFromWarehouse;
}

export interface ST01RequestShipmentsShippingFromWarehouse {
  code?: string;
}

export interface ST01RequestShipmentsTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface ST01Response201 {
  shipment_errors: Array<ST01Response201ShipmentErrors>;
  shipment_success: Array<ST01Response201ShipmentSuccess>;
}

export interface ST01Response201ShipmentErrors {
  message?: string;
  order_id?: string;
}

export interface ST01Response201ShipmentSuccess {
  created_date: string;
  id: string;
  invoice_reference?: string;
  last_updated_date: string;
  order_id: string;
  payment_details?: ST01Response201ShipmentSuccessPaymentDetails;
  shipment_additional_information?: Array<ST01Response201ShipmentSuccessShipmentAdditionalInformation>;
  shipment_lines?: Array<ST01Response201ShipmentSuccessShipmentLines>;
  shipped_date?: string;
  shipping_from?: ST01Response201ShipmentSuccessShippingFrom;
  status: string;
  status_customer_debit: string;
  tracking?: ST01Response201ShipmentSuccessTracking;
}

export interface ST01Response201ShipmentSuccessPaymentDetails {
  customer_debited_date: string;
  transaction_date: string;
  transaction_number?: string;
}

export interface ST01Response201ShipmentSuccessShipmentAdditionalInformation {
  code?: string;
  type?: string;
}

export interface ST01Response201ShipmentSuccessShipmentAdditionalInformationDate extends ST01Response201ShipmentSuccessShipmentAdditionalInformation {
  value?: string;
}

export interface ST01Response201ShipmentSuccessShipmentAdditionalInformationString extends ST01Response201ShipmentSuccessShipmentAdditionalInformation {
  value?: string;
}

export interface ST01Response201ShipmentSuccessShipmentLines {
  offer_sku?: string;
  order_line_id?: string;
  package_reference?: string;
  quantity: number;
}

export interface ST01Response201ShipmentSuccessShippingFrom {
  address?: ST01Response201ShipmentSuccessShippingFromAddress;
  warehouse?: ST01Response201ShipmentSuccessShippingFromWarehouse;
}

export interface ST01Response201ShipmentSuccessShippingFromAddress {
  city?: string;
  country_iso_code?: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface ST01Response201ShipmentSuccessShippingFromWarehouse {
  code?: string;
}

export interface ST01Response201ShipmentSuccessTracking {
  carrier_code?: string;
  carrier_expected_delivery_date?: ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate;
  carrier_name?: string;
  carrier_standard_code?: string;
  last_known_location?: ST01Response201ShipmentSuccessTrackingLastKnownLocation;
  milestones?: Array<ST01Response201ShipmentSuccessTrackingMilestones>;
  tracking_number?: string;
  tracking_url?: string;
  validity_status?: string;
}

export interface ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate {
  earliest?: ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateEarliest;
  latest?: ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateLatest;
}

export interface ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateEarliest {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateLatest {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST01Response201ShipmentSuccessTrackingLastKnownLocation {
  location?: string;
  occurrence_date?: ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate;
}

export interface ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST01Response201ShipmentSuccessTrackingMilestones {
  additional_info?: ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo;
  occurrence_date?: ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate;
  type?: string;
}

export interface ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo {
  occurrence_date?: ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfoOccurrenceDate;
  type?: string;
}

export interface ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfoOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST06Request {
  shipments: Array<ST06RequestShipments>;
}

export interface ST06RequestShipments {
  id: string;
}

export interface ST06Response200 {
  shipment_errors?: Array<ST06Response200ShipmentErrors>;
  shipment_success?: Array<ST06Response200ShipmentSuccess>;
}

export interface ST06Response200ShipmentErrors {
  id?: string;
  message?: string;
}

export interface ST06Response200ShipmentSuccess {
  id: string;
}

export interface ST07Request {
  shipments: Array<ST07RequestShipments>;
}

export interface ST07RequestShipments {
  id: string;
  shipping_from: ST07RequestShipmentsShippingFrom;
}

export interface ST07RequestShipmentsShippingFrom {
  warehouse: ST07RequestShipmentsShippingFromWarehouse;
}

export interface ST07RequestShipmentsShippingFromWarehouse {
  code: string;
}

export interface ST07Response200 {
  shipment_errors: Array<ST07Response200ShipmentErrors>;
  shipment_success: Array<ST07Response200ShipmentSuccess>;
}

export interface ST07Response200ShipmentErrors {
  id?: string;
  message?: string;
}

export interface ST07Response200ShipmentSuccess {
  id?: string;
  shipping_from?: ST07Response200ShipmentSuccessShippingFrom;
}

export interface ST07Response200ShipmentSuccessShippingFrom {
  address?: ST07Response200ShipmentSuccessShippingFromAddress;
  warehouse?: ST07Response200ShipmentSuccessShippingFromWarehouse;
}

export interface ST07Response200ShipmentSuccessShippingFromAddress {
  city?: string;
  country_iso_code?: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface ST07Response200ShipmentSuccessShippingFromWarehouse {
  code?: string;
}

export interface ST11Response200 {
  data: Array<ST11Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface ST11Response200Data {
  created_date: string;
  id: string;
  invoice_reference?: string;
  last_updated_date: string;
  order_id: string;
  payment_details?: ST11Response200DataPaymentDetails;
  shipment_additional_information?: Array<ST11Response200DataShipmentAdditionalInformation>;
  shipment_lines?: Array<ST11Response200DataShipmentLines>;
  shipped_date?: string;
  shipping_from?: ST11Response200DataShippingFrom;
  status: string;
  status_customer_debit: string;
  tracking?: ST11Response200DataTracking;
}

export interface ST11Response200DataPaymentDetails {
  customer_debited_date: string;
  transaction_date: string;
  transaction_number?: string;
}

export interface ST11Response200DataShipmentAdditionalInformation {
  code?: string;
  type?: string;
}

export interface ST11Response200DataShipmentAdditionalInformationDate extends ST11Response200DataShipmentAdditionalInformation {
  value?: string;
}

export interface ST11Response200DataShipmentAdditionalInformationString extends ST11Response200DataShipmentAdditionalInformation {
  value?: string;
}

export interface ST11Response200DataShipmentLines {
  offer_sku?: string;
  order_line_id?: string;
  package_reference?: string;
  quantity: number;
}

export interface ST11Response200DataShippingFrom {
  address?: ST11Response200DataShippingFromAddress;
  warehouse?: ST11Response200DataShippingFromWarehouse;
}

export interface ST11Response200DataShippingFromAddress {
  city?: string;
  country_iso_code?: string;
  state?: string;
  street_1?: string;
  street_2?: string;
  zip_code?: string;
}

export interface ST11Response200DataShippingFromWarehouse {
  code?: string;
}

export interface ST11Response200DataTracking {
  carrier_code?: string;
  carrier_expected_delivery_date?: ST11Response200DataTrackingCarrierExpectedDeliveryDate;
  carrier_name?: string;
  carrier_standard_code?: string;
  last_known_location?: ST11Response200DataTrackingLastKnownLocation;
  milestones?: Array<ST11Response200DataTrackingMilestones>;
  tracking_number?: string;
  tracking_url?: string;
  validity_status?: string;
}

export interface ST11Response200DataTrackingCarrierExpectedDeliveryDate {
  earliest?: ST11Response200DataTrackingCarrierExpectedDeliveryDateEarliest;
  latest?: ST11Response200DataTrackingCarrierExpectedDeliveryDateLatest;
}

export interface ST11Response200DataTrackingCarrierExpectedDeliveryDateEarliest {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST11Response200DataTrackingCarrierExpectedDeliveryDateLatest {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST11Response200DataTrackingLastKnownLocation {
  location?: string;
  occurrence_date?: ST11Response200DataTrackingLastKnownLocationOccurrenceDate;
}

export interface ST11Response200DataTrackingLastKnownLocationOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST11Response200DataTrackingMilestones {
  additional_info?: ST11Response200DataTrackingMilestonesAdditionalInfo;
  occurrence_date?: ST11Response200DataTrackingMilestonesOccurrenceDate;
  type?: string;
}

export interface ST11Response200DataTrackingMilestonesAdditionalInfo {
  occurrence_date?: ST11Response200DataTrackingMilestonesAdditionalInfoOccurrenceDate;
  type?: string;
}

export interface ST11Response200DataTrackingMilestonesAdditionalInfoOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST11Response200DataTrackingMilestonesOccurrenceDate {
  date?: string;
  offset?: string;
  time?: string;
}

export interface ST12Response200 {
  data: Array<ST12Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface ST12Response200Data {
  fulfillment?: ST12Response200DataFulfillment;
  order_id: string;
  references?: ST12Response200DataReferences;
  shipment_lines?: Array<ST12Response200DataShipmentLines>;
  shipping_address: ST12Response200DataShippingAddress;
  shipping_date: string;
  shipping_deadline?: string;
  shipping_type_code: string;
  shipping_type_standard_code?: string;
}

export interface ST12Response200DataFulfillment {
  center: ST12Response200DataFulfillmentCenter;
}

export interface ST12Response200DataFulfillmentCenter {
  code: string;
}

export interface ST12Response200DataReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface ST12Response200DataShipmentLines {
  offer_sku?: string;
  order_line_id?: string;
  package_description?: string;
  package_reference?: string;
  product_title?: string;
  quantity: number;
}

export interface ST12Response200DataShippingAddress {
  additional_info?: string;
  city: string;
  civility?: string;
  company?: string;
  company_2?: string;
  country: string;
  country_iso_code: string;
  firstname?: string;
  lastname: string;
  phone?: string;
  phone_secondary?: string;
  state?: string;
  street_1: string;
  street_2?: string;
  zip_code?: string;
}

export interface ST23Request {
  shipments: Array<ST23RequestShipments>;
}

export interface ST23RequestShipments {
  id: string;
  tracking: ST23RequestShipmentsTracking;
}

export interface ST23RequestShipmentsTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface ST23Response200 {
  shipment_errors?: Array<ST23Response200ShipmentErrors>;
  shipment_success?: Array<ST23Response200ShipmentSuccess>;
}

export interface ST23Response200ShipmentErrors {
  id?: string;
  message?: string;
}

export interface ST23Response200ShipmentSuccess {
  id: string;
}

export interface ST24Request {
  shipments: Array<ST24RequestShipments>;
}

export interface ST24RequestShipments {
  id: string;
}

export interface ST24Response200 {
  shipment_errors?: Array<ST24Response200ShipmentErrors>;
  shipment_success?: Array<ST24Response200ShipmentSuccess>;
}

export interface ST24Response200ShipmentErrors {
  id?: string;
  message?: string;
}

export interface ST24Response200ShipmentSuccess {
  id: string;
}

export interface ST26Request {
  shipments: Array<ST26RequestShipments>;
}

export interface ST26RequestShipments {
  id: string;
}

export interface ST26Response200 {
  shipment_errors?: Array<ST26Response200ShipmentErrors>;
  shipment_success?: Array<ST26Response200ShipmentSuccess>;
}

export interface ST26Response200ShipmentErrors {
  id?: string;
  message?: string;
}

export interface ST26Response200ShipmentSuccess {
  id: string;
}

export interface ST31Request {
  shipments: Array<ST31RequestShipments>;
}

export interface ST31RequestShipments {
  id: string;
  shipment_additional_information: Array<ST31RequestShipmentsShipmentAdditionalInformation>;
}

export interface ST31RequestShipmentsShipmentAdditionalInformation {
  code: string;
  type: string;
  value: string;
}

export interface ST31RequestShipmentsShipmentAdditionalInformationDate extends ST31RequestShipmentsShipmentAdditionalInformation {
  value: string;
}

export interface ST31RequestShipmentsShipmentAdditionalInformationString extends ST31RequestShipmentsShipmentAdditionalInformation {
  value: string;
}

export interface ST31Response200 {
  shipment_update_errors?: Array<ST31Response200ShipmentUpdateErrors>;
  shipment_update_success?: Array<ST31Response200ShipmentUpdateSuccess>;
}

export interface ST31Response200ShipmentUpdateErrors {
  errors?: Array<ST31Response200ShipmentUpdateErrorsErrors>;
  shipment_id?: string;
}

export interface ST31Response200ShipmentUpdateErrorsErrors {
  code: string;
  field: string;
  message: string;
}

export interface ST31Response200ShipmentUpdateSuccess {
  shipment_additional_information?: Array<ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation>;
  shipment_id?: string;
}

export interface ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation {
  code: string;
  type: string;
  value: string;
}

export interface ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformationDate extends ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation {
  value: string;
}

export interface ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformationString extends ST31Response200ShipmentUpdateSuccessShipmentAdditionalInformation {
  value: string;
}

export interface ST41Request {
  shipments: Array<ST41RequestShipments>;
}

export interface ST41RequestShipments {
  carrier_code?: string;
  carrier_service_code?: string;
  _package?: ST41RequestShipmentsPackage;
  shipment_id: string;
}

export interface ST41RequestShipmentsPackage {
  dimensions: ST41RequestShipmentsPackageDimensions;
  weight: ST41RequestShipmentsPackageWeight;
}

export interface ST41RequestShipmentsPackageDimensions {
  height: number;
  length: number;
  unit: string;
  width: number;
}

export interface ST41RequestShipmentsPackageWeight {
  unit: string;
  value: number;
}

export interface ST41Response200 {
  shipping_label_rate_errors: Array<ST41Response200ShippingLabelRateErrors>;
  shipping_label_rate_successes: Array<ST41Response200ShippingLabelRateSuccesses>;
}

export interface ST41Response200ShippingLabelRateErrors {
  code: string;
  message: string;
  shipment_id: string;
}

export interface ST41Response200ShippingLabelRateSuccesses {
  shipment_id: string;
}

export interface ST42Response200 {
  data: Array<ST42Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface ST42Response200Data {
  date_created: string;
  errors?: Array<ST42Response200DataErrors>;
  label_rate_state: string;
  last_updated: string;
  rates?: Array<ST42Response200DataRates>;
  shipment_id: string;
}

export interface ST42Response200DataErrors {
  code: string;
  message: string;
}

export interface ST42Response200DataRates {
  carrier_code: string;
  carrier_name: string;
  carrier_service_code?: string;
  carrier_standard_code: string;
  estimated_cost?: ST42Response200DataRatesEstimatedCost;
  estimated_delivery_days?: number;
  estimated_delivery_promise_status?: string;
  label_selection_tags: Array<string>;
}

export interface ST42Response200DataRatesEstimatedCost {
  amount: number;
  currency_iso_code: string;
}

export interface ST51Request {
  shipments: Array<ST51RequestShipments>;
}

export interface ST51RequestShipments {
  carrier_code?: string;
  carrier_service_code?: string;
  label_selection_mode?: string;
  _package?: ST51RequestShipmentsPackage;
  shipment_id: string;
}

export interface ST51RequestShipmentsPackage {
  dimensions: ST51RequestShipmentsPackageDimensions;
  weight: ST51RequestShipmentsPackageWeight;
}

export interface ST51RequestShipmentsPackageDimensions {
  height: number;
  length: number;
  unit: string;
  width: number;
}

export interface ST51RequestShipmentsPackageWeight {
  unit: string;
  value: number;
}

export interface ST51Response200 {
  shipping_label_errors: Array<ST51Response200ShippingLabelErrors>;
  shipping_label_successes: Array<ST51Response200ShippingLabelSuccesses>;
}

export interface ST51Response200ShippingLabelErrors {
  code: string;
  message: string;
  shipment_id: string;
}

export interface ST51Response200ShippingLabelSuccesses {
  shipment_id: string;
}

export interface ST52Response200 {
  data: Array<ST52Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface ST52Response200Data {
  date_created: string;
  errors?: Array<ST52Response200DataErrors>;
  estimated_cost?: ST52Response200DataEstimatedCost;
  files?: ST52Response200DataFiles;
  label_state: string;
  last_updated: string;
  shipment_id: string;
  tracking?: ST52Response200DataTracking;
}

export interface ST52Response200DataErrors {
  code: string;
  message: string;
}

export interface ST52Response200DataEstimatedCost {
  amount: number;
  currency_iso_code: string;
}

export interface ST52Response200DataFiles {
  label?: ST52Response200DataFilesLabel;
}

export interface ST52Response200DataFilesLabel {
  file_type: string;
  url: string;
}

export interface ST52Response200DataTracking {
  carrier_code?: string;
  carrier_name?: string;
  carrier_service_code?: string;
  carrier_standard_code?: string;
  tracking_number?: string;
  tracking_url?: string;
}

export interface STO01Response201 {
  import_id?: string;
}

export interface STO02Response200 {
  date_created: string;
  has_error_report: boolean;
  import_id: string;
  lines_in_error?: number;
  lines_in_success?: number;
  shop_id: number;
  status: string;
}

export interface TL02Response200 {
  data: Array<TL02Response200Data>;
  next_page_token?: string;
  previous_page_token?: string;
}

export interface TL02Response200Data {
  accounting_document_creation_date?: string;
  accounting_document_id?: string;
  accounting_document_number?: string;
  amount?: number;
  amount_credited?: number;
  amount_debited?: number;
  balance?: number;
  currency_iso_code?: string;
  date_created?: string;
  entities?: TL02Response200DataEntities;
  id?: string;
  last_updated?: string;
  pay_out_psp_code?: string;
  payment_state?: string;
  psp_balance?: number;
  seller_billing_cycle_id?: string;
  type?: string;
}

export interface TL02Response200DataEntities {
  channel?: TL02Response200DataEntitiesChannel;
  debit?: TL02Response200DataEntitiesDebit;
  domain?: string;
  fee?: TL02Response200DataEntitiesFee;
  manual_accounting_document?: TL02Response200DataEntitiesManualAccountingDocument;
  one_off_item?: TL02Response200DataEntitiesOneOffItem;
  order?: TL02Response200DataEntitiesOrder;
  order_fee?: TL02Response200DataEntitiesOrderFee;
  order_line?: TL02Response200DataEntitiesOrderLine;
  order_tax?: TL02Response200DataEntitiesOrderTax;
  refund?: TL02Response200DataEntitiesRefund;
  shipment?: TL02Response200DataEntitiesShipment;
  shop_tax?: TL02Response200DataEntitiesShopTax;
  transaction_info?: TL02Response200DataEntitiesTransactionInfo;
}

export interface TL02Response200DataEntitiesChannel {
  code?: string;
}

export interface TL02Response200DataEntitiesDebit {
  id?: string;
}

export interface TL02Response200DataEntitiesFee {
  cancelations?: Array<TL02Response200DataEntitiesFeeCancelations>;
  code?: string;
  refunds?: Array<TL02Response200DataEntitiesFeeRefunds>;
}

export interface TL02Response200DataEntitiesFeeCancelations {
  id?: string;
}

export interface TL02Response200DataEntitiesFeeRefunds {
  id?: string;
}

export interface TL02Response200DataEntitiesManualAccountingDocument {
  emission_date?: string;
  number?: string;
}

export interface TL02Response200DataEntitiesOneOffItem {
  description?: string;
  operation_date?: string;
  quantity?: number;
  references?: Array<TL02Response200DataEntitiesOneOffItemReferences>;
  unit_price?: number;
}

export interface TL02Response200DataEntitiesOneOffItemReferences {
  type?: string;
  value?: string;
}

export interface TL02Response200DataEntitiesOrder {
  commercial_id?: string;
  creation_date?: string;
  id?: string;
  payment_info?: TL02Response200DataEntitiesOrderPaymentInfo;
  references?: TL02Response200DataEntitiesOrderReferences;
}

export interface TL02Response200DataEntitiesOrderFee {
  code?: string;
}

export interface TL02Response200DataEntitiesOrderLine {
  id?: string;
}

export interface TL02Response200DataEntitiesOrderPaymentInfo {
  imprint_number?: string;
  payment_type?: string;
}

export interface TL02Response200DataEntitiesOrderReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface TL02Response200DataEntitiesOrderTax {
  code?: string;
  rate?: number;
}

export interface TL02Response200DataEntitiesRefund {
  id?: string;
}

export interface TL02Response200DataEntitiesShipment {
  id?: string;
}

export interface TL02Response200DataEntitiesShopTax {
  code?: string;
  rate?: number;
}

export interface TL02Response200DataEntitiesTransactionInfo {
  date?: string;
  number?: string;
}

export interface TL03Request {
  accounting_document_id?: string;
  accounting_document_number?: string;
  date_created_from?: string;
  date_created_to?: string;
  format?: string;
  items_per_chunk?: number;
  last_updated_from?: string;
  megabytes_per_chunk?: number;
  order_id?: Array<string>;
  order_line_id?: Array<string>;
  order_reference_for_customer?: Array<string>;
  order_reference_for_seller?: Array<string>;
  other_reference?: Array<string>;
  pay_out_psp_codes?: Array<string>;
  payment_state?: Array<string>;
  payment_voucher_number?: string;
  seller_billing_cycle_id?: Array<string>;
  shop_domain?: Array<string>;
  shop_id?: number;
  shop_model?: Array<string>;
  transaction_date_from?: string;
  transaction_date_to?: string;
  transaction_type?: Array<string>;
}

export interface TL03Response200 {
  tracking_id?: string;
}

export interface TL04Response200 {
  error?: TL04Response200Error;
  last_updated?: string;
  status?: string;
  urls?: Array<string>;
}

export interface TL04Response200Error {
  code?: string;
  detail?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructure {
  accounting_document_creation_date?: string;
  accounting_document_id?: string;
  accounting_document_number?: string;
  amount?: number;
  amount_credited?: number;
  amount_debited?: number;
  balance?: number;
  currency_iso_code?: string;
  date_created?: string;
  entities?: TL05Response200ApplicationXNdjsonExtFileStructureEntities;
  id?: string;
  last_updated?: string;
  pay_out_psp_code?: string;
  payment_state?: string;
  psp_balance?: number;
  seller_billing_cycle_id?: string;
  type?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntities {
  channel?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesChannel;
  debit?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesDebit;
  domain?: string;
  fee?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFee;
  manual_accounting_document?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesManualAccountingDocument;
  one_off_item?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem;
  order?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder;
  order_fee?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderFee;
  order_line?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderLine;
  order_tax?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderTax;
  refund?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesRefund;
  shipment?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShipment;
  shop_tax?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShopTax;
  transaction_info?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesTransactionInfo;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesChannel {
  code?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesDebit {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFee {
  cancelations?: Array<TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFeeCancelations>;
  code?: string;
  refunds?: Array<TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFeeRefunds>;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFeeCancelations {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesFeeRefunds {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesManualAccountingDocument {
  emission_date?: string;
  number?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItem {
  description?: string;
  operation_date?: string;
  quantity?: number;
  references?: Array<TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItemReferences>;
  unit_price?: number;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOneOffItemReferences {
  type?: string;
  value?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder {
  commercial_id?: string;
  creation_date?: string;
  id?: string;
  payment_info?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderPaymentInfo;
  references?: TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderReferences;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderFee {
  code?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderLine {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderPaymentInfo {
  imprint_number?: string;
  payment_type?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderTax {
  code?: string;
  rate?: number;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesRefund {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShipment {
  id?: string;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesShopTax {
  code?: string;
  rate?: number;
}

export interface TL05Response200ApplicationXNdjsonExtFileStructureEntitiesTransactionInfo {
  date?: string;
  number?: string;
}

export interface TL05Response200ExtFileStructure {
  accounting_document_creation_date?: string;
  accounting_document_id?: string;
  accounting_document_number?: string;
  amount?: number;
  amount_credited?: number;
  amount_debited?: number;
  balance?: number;
  currency_iso_code?: string;
  date_created?: string;
  entities?: TL05Response200ExtFileStructureEntities;
  id?: string;
  last_updated?: string;
  pay_out_psp_code?: string;
  payment_state?: string;
  psp_balance?: number;
  seller_billing_cycle_id?: string;
  type?: string;
}

export interface TL05Response200ExtFileStructureEntities {
  channel?: TL05Response200ExtFileStructureEntitiesChannel;
  debit?: TL05Response200ExtFileStructureEntitiesDebit;
  domain?: string;
  fee?: TL05Response200ExtFileStructureEntitiesFee;
  manual_accounting_document?: TL05Response200ExtFileStructureEntitiesManualAccountingDocument;
  one_off_item?: TL05Response200ExtFileStructureEntitiesOneOffItem;
  order?: TL05Response200ExtFileStructureEntitiesOrder;
  order_fee?: TL05Response200ExtFileStructureEntitiesOrderFee;
  order_line?: TL05Response200ExtFileStructureEntitiesOrderLine;
  order_tax?: TL05Response200ExtFileStructureEntitiesOrderTax;
  refund?: TL05Response200ExtFileStructureEntitiesRefund;
  shipment?: TL05Response200ExtFileStructureEntitiesShipment;
  shop_tax?: TL05Response200ExtFileStructureEntitiesShopTax;
  transaction_info?: TL05Response200ExtFileStructureEntitiesTransactionInfo;
}

export interface TL05Response200ExtFileStructureEntitiesChannel {
  code?: string;
}

export interface TL05Response200ExtFileStructureEntitiesDebit {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesFee {
  cancelations?: Array<TL05Response200ExtFileStructureEntitiesFeeCancelations>;
  code?: string;
  refunds?: Array<TL05Response200ExtFileStructureEntitiesFeeRefunds>;
}

export interface TL05Response200ExtFileStructureEntitiesFeeCancelations {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesFeeRefunds {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesManualAccountingDocument {
  emission_date?: string;
  number?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOneOffItem {
  description?: string;
  operation_date?: string;
  quantity?: number;
  references?: Array<TL05Response200ExtFileStructureEntitiesOneOffItemReferences>;
  unit_price?: number;
}

export interface TL05Response200ExtFileStructureEntitiesOneOffItemReferences {
  type?: string;
  value?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOrder {
  commercial_id?: string;
  creation_date?: string;
  id?: string;
  payment_info?: TL05Response200ExtFileStructureEntitiesOrderPaymentInfo;
  references?: TL05Response200ExtFileStructureEntitiesOrderReferences;
}

export interface TL05Response200ExtFileStructureEntitiesOrderFee {
  code?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOrderLine {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOrderPaymentInfo {
  imprint_number?: string;
  payment_type?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOrderReferences {
  order_reference_for_customer?: string;
  order_reference_for_seller?: string;
}

export interface TL05Response200ExtFileStructureEntitiesOrderTax {
  code?: string;
  rate?: number;
}

export interface TL05Response200ExtFileStructureEntitiesRefund {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesShipment {
  id?: string;
}

export interface TL05Response200ExtFileStructureEntitiesShopTax {
  code?: string;
  rate?: number;
}

export interface TL05Response200ExtFileStructureEntitiesTransactionInfo {
  date?: string;
  number?: string;
}

export interface VL11Response200 {
  values_lists?: Array<VL11Response200ValuesLists>;
}

export interface VL11Response200ValuesLists {
  code: string;
  label?: string;
  label_translations: Array<VL11Response200ValuesListsLabelTranslations>;
  values?: Array<VL11Response200ValuesListsValues>;
}

export interface VL11Response200ValuesListsLabelTranslations {
  locale?: string;
  value?: string;
}

export interface VL11Response200ValuesListsValues {
  code: string;
  label?: string;
  label_translations: Array<VL11Response200ValuesListsValuesLabelTranslations>;
}

export interface VL11Response200ValuesListsValuesLabelTranslations {
  locale?: string;
  value?: string;
}
