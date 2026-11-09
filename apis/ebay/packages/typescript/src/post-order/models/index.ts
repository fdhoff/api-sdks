// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface ActionDeadlines {
  daysForBuyerToProvideProofOfShipment?: number;
  daysToExpireWithoutResponse?: number;
  daysToExpireWithResponse?: number;
  daysToReturnItem?: number;
  maxDaysToFileClaim?: number;
}

export type ActivityOptionEnum =
  | 'BUYER_CREATE_RETURN'
  | 'BUYER_CLOSE_RETURN'
  | 'BUYER_PROVIDE_TRACKING_INFO'
  | 'BUYER_ESCALATE'
  | 'BUYER_MARK_RETURN_SHIPPED'
  | 'BUYER_DECLINE_PARTIAL_REFUND'
  | 'BUYER_MARK_REFUND_RECEIVED'
  | 'BUYER_PRINT_SHIPPING_LABEL'
  | 'EMAIL_SHIPPING_LABEL'
  | 'BUYER_MARK_AS_RECEIVED'
  | 'BUYER_ACCEPTS_PARTIAL_REFUND'
  | 'BUYER_ACCEPTS_NON_PAYPAL_PARTIAL_REFUND'
  | 'BUYER_SEND_MESSAGE'
  | 'BUYER_PROVIDE_LABEL'
  | 'BUYER_VOID_LABEL'
  | 'BUYER_UPDATE_TRACKING'
  | 'EXTERNAL_CLAIM_OPENED'
  | 'SELLER_ESCALATE'
  | 'SELLER_MARK_REPLACEMENT_SHIPPED'
  | 'SELLER_MARK_REFUND_SENT'
  | 'SELLER_ISSUE_REFUND'
  | 'SELLER_ISSUE_STORE_CREDIT_REFUND'
  | 'SELLER_PROVIDE_RMA'
  | 'SELLER_APPROVE_REQUEST'
  | 'SELLER_DECLINE_REQUEST'
  | 'SELLER_PRINT_SHIPPING_LABEL'
  | 'SELLER_PROVIDE_TRACKING_INFO'
  | 'SELLER_MARK_AS_RECEIVED'
  | 'SELLER_OFFER_PARTIAL_REFUND'
  | 'SELLER_OFFER_RETURNS'
  | 'SELLER_SEND_MESSAGE'
  | 'SELLER_PROVIDE_LABEL'
  | 'SELLER_VOID_LABEL'
  | 'SELLER_UPDATE_TRACKING'
  | 'SELLER_OFFER_REPLACEMENT'
  | 'BUYER_ACCEPT_REPLACEMENT_OFFER'
  | 'BUYER_DECLINE_REPLACEMENT_OFFER'
  | 'NOTIFIED_SHIPPED'
  | 'NOTIFIED_DELIVERED'
  | 'TIME_OUT_FOR_RMA'
  | 'TIME_OUT_FOR_PROVIDE_LABEL'
  | 'TIME_OUT_FOR_AUTHORIZE'
  | 'TIME_OUT_FOR_SHIPPING'
  | 'TIME_OUT_FOR_SHIPPING_SYSTEM_CLOSE'
  | 'TIME_OUT_FOR_REFUND'
  | 'TIME_OUT_FOR_ESCALATION'
  | 'TIME_OUT_FOR_ESCALATION_AFTER_SMIR'
  | 'TIME_OUT_FOR_REPLACEMENT_DELIVERED_ITEM_NOT_RETURNED'
  | 'TIME_OUT_FOR_PAYOUT'
  | 'TIME_OUT_FOR_MASS_PAYOUT'
  | 'TIME_OUT_FOR_AUTO_REFUND'
  | 'TIME_OUT_FOR_SELLER_INVOICE'
  | 'TIME_OUT_FOR_BUYER_RECOUP'
  | 'TIME_OUT_FOR_SELLER_PAYOUT'
  | 'TIME_OUT_FOR_REPLACEMENT_SHIPPED'
  | 'TIME_OUT_FOR_ITEM_REPLACED'
  | 'TIME_OUT_FOR_RETURN_SHIPPING'
  | 'TIME_OUT_AFTER_DECLINE'
  | 'TIME_OUT_AFTER_REPLACED'
  | 'GENERAL_TIME_OUT'
  | 'NOTIFY_REPLACEMENT_SHIPPED'
  | 'NOTIFY_REPLACEMENT_DELIVERED'
  | 'AUTO_APPROVE_REMORSE'
  | 'REMINDER_FOR_RMA'
  | 'REMINDER_FOR_SHIPPING'
  | 'REMINDER_FOR_REFUND'
  | 'REMINDER_FOR_REFUND_NO_SHIPPING'
  | 'REMINDER_BUYER_TO_SHIP'
  | 'REMINDER_SELLER_TO_SHIP'
  | 'REMINDER_BUYER_TO_RESPOND_RE_OFFER'
  | 'REMINDER_SELLER_TO_RESPOND'
  | 'NOTIFY_UPDATE_REFUND_STATUS'
  | 'TIME_OUT_AFTER_REFUNDED'
  | 'TIME_OUT_AFTER_REFUNDED_AS_PAYOUT'
  | 'TIME_OUT_FOR_DELIVERY'
  | 'TIME_OUT_FOR_SHIPMENT_TRACKING'
  | 'TIME_OUT_FOR_MARK_REFUND_RECEIVED'
  | 'TIME_OUT_FOR_MARK_REFUND_SENT'
  | 'SYSTEM_CREATE_RETURN'
  | 'SYSTEM_CLOSE_RETURN'
  | 'DELETE_FILE'
  | 'SUBMIT_FILE'
  | 'SYSTEM_IMMEDIATE_REFUND'
  | 'EBAY_RULE_AUTO_APPROVE'
  | 'SYSTEM_BUYER_REFUND_AS_PAYOUT'
  | 'SYSTEM_BUYER_PARTIAL_REFUND_AS_PAYOUT'
  | 'SELLER_RETRY_REFUND'
  | 'CHARGEBACK_OPEN'
  | 'TIME_OUT_FOR_AUTHENTICATION'
  | 'SYSTEM_INITIATED_REFUND'
  | 'SYSTEM_SELLER_CHARGE'
  | 'OTHER';

export interface ActualRefund {
  totalAmount?: Amount;
  feeCreditAmount?: Amount;
  donationAmount?: Amount;
}

export interface ActualRefundDetail {
  actualRefund?: ActualRefund;
  netChargeAmount?: Amount;
  refundIssuedDate?: Timestamp;
  refundStatus?: string;
  outstandingAmount?: Amount;
  fundings?: Array<RefundFundingType>;
}

export interface ActualRefundDetailType {
  actualRefund?: RefundDetailType;
  fundings?: Array<RefundFundingType>;
  netChargeAmount?: Amount;
  outstandingAmount?: Amount;
  refundInitiationType?: ReturnRefundInitiatorEnum;
  refundIssuedDate?: Timestamp;
  refundStatus?: RefundMoneyMovementStatusEnum;
}

export interface Address {
  addressLine1?: string;
  addressLine2?: string;
  addressType?: string;
  city?: string;
  country?: string;
  county?: string;
  isTransliterated?: boolean;
  nationalRegion?: string;
  postalCode?: string;
  script?: string;
  stateOrProvince?: string;
  transliteratedFromScript?: string;
  worldRegion?: string;
}

export type AddressTypeEnum = 'PO_BOX' | 'RESIDENCE' | 'BUSINESS' | 'MILITARY' | 'DIPLOMATIC' | 'OTHER';

export interface Amount {
  value?: number;
  convertedFromValue?: number;
  convertedFromCurrency?: string;
  currency?: string;
  exchangeRate?: string;
}

export type AppealCloseReasonEnum =
  | 'APPEAL_BUYER_WINS'
  | 'APPEAL_SELLER_WINS_FULL_CREDIT'
  | 'APPEAL_SELLER_WINS_PARTIAL_CREDIT'
  | 'APPEAL_BUYER_DENIED'
  | 'APPEAL_SELLER_DENIED'
  | 'APPEAL_SELLER_WINS_FULL_CREDIT_CANCEL_RECOUP'
  | 'APPEAL_BUYER_WINS_PARTIAL_CREDIT'
  | 'OTHER';

export interface AppealDetails {
  appealCloseReasonEnum?: string;
  appealDate?: Timestamp;
  appealReasonCode?: string;
  appealRefundAmount?: Amount;
  appealStatus?: AppealGrantStatusEnum;
  appealStatusEnum?: string;
  eligibleForAppeal?: boolean;
}

export type AppealGrantStatusEnum = 'GRANTED' | 'DENIED' | 'OTHER';

export interface AppealRequest {
  comments?: Text;
}

export type AppealStatusEnum =
  | 'BUYER_APPEALED'
  | 'SELLER_APPEALED'
  | 'BUYER_SELLER_APPEALED'
  | 'SELLER_RECOUPED_BUYER_APPEALED'
  | 'SELLER_RECOUPED_BUYER_APPEALED_CLOSED_CASE'
  | 'SELLER_RECOUP_APPEALED'
  | 'SELLER_RECOUP_NEEDED_BUYER_APPEALED'
  | 'SELLER_RECOUP_NEEDED_BUYER_APPEALED_CLOSED_CASE'
  | 'SELLER_INVOICED_BUYER_APPEALED'
  | 'OTHER';

export interface AvailableOptionType {
  actionType?: ActivityOptionEnum;
  actionURL?: string;
}

export interface BuyerCloseCaseRequest {
  closeReason?: BuyerCloseReasonEnum;
  comments?: Text;
}

export interface BuyerCloseInquiryRequest {
  closeReason?: BuyerCloseReasonEnum;
  comments?: Text;
}

export type BuyerCloseReasonEnum = 'ITEM_ARRIVED' | 'WORKED_OUT_WITH_SELLER' | 'WOULD_RATHER_KEEP_THE_ITEM' | 'OTHER';

export type BuyerCloseReturnReasonEnum =
  | 'UNKNOWN'
  | 'BUYER_RECEIVED_REFUND'
  | 'BUYER_RECEIVED_REPLACEMENT'
  | 'BUYER_STARTED_RETURN_ACCIDENTALLY'
  | 'CHARGE_BACK_OPENED'
  | 'BUYER_NO_LONGER_WANTS_RETURN'
  | 'OTHER';

export type CanEligibilityCheckTypeEnum = 'fullCheck';

export interface CanMoneyMovementDetailType {
  actualAmount?: Amount;
  creationDate?: Timestamp;
  moneyMovementType?: CanMoneyMovementTypeEnum;
  requestedAmount?: Amount;
  status?: string;
}

export type CanMoneyMovementStatusEnum = 'UNKNOWN' | 'REQUESTED' | 'PENDING' | 'SUCCESS' | 'FAILED' | 'SKIPPED';

export type CanMoneyMovementTypeEnum =
  'UNKNOWN' | 'SELLER_VOLUNTARY_REFUND' | 'PAYPAL_REFUND' | 'BUYER_PAYOUT' | 'RECOUP_FROM_SELLER';

export interface CancelActivityHistory {
  actionDate?: Timestamp;
  activityParty?: PartyEnum;
  activityType?: string;
  stateFrom?: string;
  stateTo?: string;
}

export type CancelActivityTypeEnum =
  | 'UNKNOWN'
  | 'BUYER_CREATE_CANCEL'
  | 'SYSTEM_CREATE_CANCEL'
  | 'SYSTEM_REFUND'
  | 'SYSTEM_NOTIFY_REFUND_STATUS'
  | 'SELLER_CREATE_CANCEL'
  | 'SELLER_APPROVE'
  | 'SELLER_REJECT'
  | 'BUYER_CONFIRM_REFUND'
  | 'SYSTEM_REJECT'
  | 'SYSTEM_TIMEOUT_FOR_APPROVAL'
  | 'SYSTEM_TIMEOUT_FOR_CONFIRMATION'
  | 'SYSTEM_NOTIFYPP_REFUND'
  | 'SYSTEM_TIMEOUT_FOR_NOTIFY_REFUND_STATUS'
  | 'SYSTEM_PAYOUT'
  | 'SYSTEM_NOTIFY_PAYOUT_STATUS'
  | 'SYSTEM_TIMEOUT_FOR_NOTIFY_PAYOUT_STATUS'
  | 'SYSTEM_CHARGEBACK_OPENED';

export type CancelCloseReasonEnum =
  | 'UNKNOWN'
  | 'INELIGIBLE_FOR_CANCEL'
  | 'FULL_REFUNDED'
  | 'FULL_REFUNDED_T2_FAILED'
  | 'FULL_REFUNDED_T2_ONLY'
  | 'REFUND_FAILED'
  | 'SELLER_DECLINE'
  | 'SYSTEM_NOTIFY_SHIPPING_STATUS'
  | 'SELLER_APPROVE_TIMEOUT_PAID'
  | 'SELLER_APPROVE_TIMEOUT_UNPAID'
  | 'SELLER_APPROVE_UNPAID'
  | 'BUYER_CONFIRM_REFUND'
  | 'BUYER_CONFIRM_NOT_PAID'
  | 'BUYER_CONFIRM_TIMEOUT_NON_PAYPAL_PAID'
  | 'BUYER_CONFIRM_TIMEOUT_PAYPAL_PAID'
  | 'SELLER_CANCEL_UNPAID'
  | 'FULL_REFUNDED_AS_PAYOUT'
  | 'PAYOUT_FAILED'
  | 'CHARGEBACK_DISPUTE_FILED';

export interface CancelDetail {
  activityHistories?: Array<CancelActivityHistory>;
  buyerLoginName?: string;
  buyerResponseDueDate?: Timestamp;
  cancelCloseDate?: Timestamp;
  cancelCloseReason?: object;
  cancelId?: string;
  cancelReason?: object;
  cancelRequestDate?: Timestamp;
  cancelState?: string;
  cancelStatus?: string;
  legacyOrderId?: string;
  marketplaceId?: string;
  moneyMovementInfo?: Array<CanMoneyMovementDetailType>;
  partialOrderType?: PartialOrderTypeEnum;
  paymentStatus?: PaymentStatusEnum;
  payoutRecoupInfo?: PayoutRecoupInfo;
  refundInfo?: RefundInfo;
  requestorType?: PartyEnum;
  requestRefundAmount?: Amount;
  sellerLoginName?: string;
  sellerResponseDueDate?: Timestamp;
  shipmentDate?: Timestamp;
}

export type CancelReasonEnum =
  | 'ORDER_MISTAKE'
  | 'FOUND_CHEAPER_PRICE'
  | 'WONT_ARRIVE_IN_TIME'
  | 'WRONG_SHIPPING_ADDRESS'
  | 'WRONG_SHIPPING_METHOD'
  | 'WRONG_PAYMENT_METHOD'
  | 'UNKNOWN'
  | 'PRICE_TOO_HIGH'
  | 'OTHER'
  | 'BUYER_CANCEL_OR_ADDRESS_ISSUE'
  | 'OUT_OF_STOCK_OR_CANNOT_FULFILL'
  | 'BUYER_ASKED_CANCEL'
  | 'ADDRESS_ISSUES'
  | 'ORDER_UNPAID';

export interface CancelSortField {
  ascending?: boolean;
  enumValue?: object;
  field?: string;
}

export type CancelSortTypeEnum = 'CANCEL_ID' | 'CANCEL_REQUEST_DATE';

export type CancelStateEnum =
  | 'INITIAL'
  | 'REFUND_PENDING'
  | 'REFUND_INITIATED'
  | 'APPROVAL_PENDING'
  | 'CONFIRM_REFUND_PENDING'
  | 'CLOSED'
  | 'REFUND_FAILED_RETRY'
  | 'OTHER';

export type CancelStatusEnum =
  | 'INVALID'
  | 'CANCEL_REQUESTED'
  | 'CANCEL_PENDING'
  | 'CANCEL_REJECTED'
  | 'CANCEL_CLOSED_NO_REFUND'
  | 'CANCEL_CLOSED_WITH_REFUND'
  | 'CANCEL_CLOSED_UNKNOWN_REFUND'
  | 'CANCEL_CLOSED_FOR_COMMITMENT';

export interface CancelSummary {
  buyerLoginName?: string;
  buyerResponseDueDate?: Timestamp;
  cancelCloseDate?: Timestamp;
  cancelCloseReason?: string;
  cancelId?: string;
  cancelReason?: string;
  cancelRequestDate?: Timestamp;
  cancelState?: string;
  cancelStatus?: string;
  legacyOrderId?: string;
  marketplaceId?: string;
  partialOrderType?: PartialOrderTypeEnum;
  paymentStatus?: PaymentStatusEnum;
  payoutRecoupInfo?: PayoutRecoupInfo;
  requestorType?: PartyEnum;
  requestRefundAmount?: Amount;
  sellerLoginName?: string;
  sellerResponseDueDate?: Timestamp;
  shipmentDate?: Timestamp;
}

export type CaseCloseReasonEnum =
  | 'UNDEFINED'
  | 'BUYER_CLOSE'
  | 'SELLER_FULL_REFUND_PP'
  | 'BUYER_CONFIRM_FULL_REFUND_PP'
  | 'BUYER_CONFIRM_FULL_REFUND_NPP'
  | 'SELLER_PARTIAL_REFUND_PP'
  | 'BUYER_CONFIRM_PARTIAL_REFUND_PP'
  | 'BUYER_CONFIRM_PARTIAL_REFUND_NPP'
  | 'RETURN_TRACKING_DELIVERED'
  | 'CLOSED_CS_CLOSE'
  | 'AUTO_DISPOSE_BUYER_WIN_NO_SELLER_FAULT'
  | 'AUTO_DISPOSE_SELLER_WIN_BUYER_FAULT'
  | 'ESCALATE_CS_AUTO_DISPOSE_BUYER_WIN_SELLER_FAULT'
  | 'ESCALATE_CS_AUTO_DISPOSE_SELLER_WIN_BUYER_FAULT'
  | 'ESCALATE_CS_AUTO_DISPOSE_BUYER_WIN_SELLER_FAULT_NO_RECOUP'
  | 'BUYER_WINS_SELLER_FAULT'
  | 'BUYER_WINS_NO_SELLER_FAULT'
  | 'SELLER_WINS_BUYER_FAULT'
  | 'NO_SELLER_FAULT_BUYER_DESTROYS_ITEM'
  | 'BUYER_WINS_DESTROY_ITEM'
  | 'BUYER_WINS_NO_ITEM_RETURNS'
  | 'BUYER_WINS_SELLER_FAULT_BUYER_RETURNS_ITEM'
  | 'NO_SELLER_FAULT_BUYER_RETURNS_ITEM'
  | 'AGENT_CLOSE_FOR_BUYER'
  | 'AGENT_CLOSE_FOR_SELLER'
  | 'AGENT_CLOSE_FOR_EBAY'
  | 'EXPIRE_ENTER_TRACKING_AFTER_CS_DECISION'
  | 'ITEM_DELIVERED_FOR_FORCED_RETURN'
  | 'EXPIRE_AFTER_ENTER_TRACKING_FOR_FORCED_RETURN'
  | 'BUYER_WINS_SELLER_FAULT_FOR_FORCED_RETURN'
  | 'BUYER_WINS_NO_SELLER_FAULT_FOR_FORCED_RETURN'
  | 'SELLER_WINS_BUYER_FAULT_FOR_FORCED_RETURN'
  | 'BUYER_WINS_NO_SELLER_FAULT_PARTIAL_CREDIT'
  | 'BUYER_REFUNDED'
  | 'BUYER_WINS_SELLER_FAULT_NO_CREDIT'
  | 'ESCALATE_CS_AUTO_DISPOSE_BUYER_WINS_NO_SELLER_FAULT_NO_CREDIT'
  | 'ECHECK_TIMEOUT'
  | 'PAYMENT_PROCESSOR_CLAIM_FILED'
  | 'CLOSED_ON_CHARGEBACK_NOTIFICATION'
  | 'CLOSED_ON_MONEY_MOVEMENT_AFTER_CHARGEBACK_NOTIFICATION'
  | 'OTHER';

export interface CaseDetails {
  buyerFinalAcceptResolution?: string;
  buyerInitExpectResolution?: string;
  creationDate?: Timestamp;
  escalationDate?: Timestamp;
  expirationDate?: Timestamp;
  lastBuyerRespDate?: Timestamp;
  lastSellerRespDate?: Timestamp;
  paypalPaid?: boolean;
  refundAmounts?: RefundAmounts;
  refundChargeAmount?: Amount;
  refundDeadlineDate?: Timestamp;
  refundType?: RefundType;
}

export interface CaseDetailsResponse {
  actionDeadlines?: ActionDeadlines;
  appealDetails?: AppealDetails;
  buyerClosureReason?: string;
  buyerProtectedProgramLink?: string;
  caseDetails?: CaseDetails;
  caseHistoryDetails?: ClaimHistoryResponse;
  caseId?: string;
  caseQuantity?: number;
  caseType?: CaseTypeEnum;
  claimAmount?: Amount;
  creationDate?: Timestamp;
  escalatedBy?: UserPartyEnum;
  escalateReason?: string;
  eventTicketsLink?: string;
  extTransactionId?: string;
  fsnadDaysToAddTrackingAfterShippingItem?: number;
  fsnadShipToSellerByDate?: Timestamp;
  initiator?: UserPartyEnum;
  caseContentOnHold?: boolean;
  itemId?: string;
  itemOnHold?: boolean;
  lastModifiedDate?: Timestamp;
  payForItemLink?: string;
  priceSignatureConfirmationAmount?: string;
  recalledItemLink?: string;
  returnDetails?: ReturnAddress;
  returnId?: string;
  sellerClosureReason?: string;
  shippingFee?: Amount;
  status?: string;
  transactionId?: string;
}

export type CaseSearchFieldGroupEnum = 'DEFAULT' | 'SUMMARY';

export interface CaseSearchResponse {
  members?: Array<CaseSummaryType>;
  paginationOutput?: PaginationOutput;
  totalNumberOfCases?: number;
}

export type CaseStatusEnum =
  | 'WAITING_DELIVERY'
  | 'WAITING_CS'
  | 'OPEN'
  | 'ON_HOLD'
  | 'REFUND_AGREED_BUT_FAILED'
  | 'CLOSED'
  | 'CS_CLOSED'
  | 'OTHER';

export type CaseStatusFilter =
  | 'WAITING_DELIVERY'
  | 'WAITING_CS'
  | 'OPEN'
  | 'ON_HOLD'
  | 'REFUND_AGREED_BUT_FAILED'
  | 'CLOSED'
  | 'CS_CLOSED'
  | 'OTHER';

export interface CaseSummaryType {
  buyer?: string;
  caseId?: number;
  caseStatusEnum?: string;
  claimAmount?: Amount;
  creationDate?: Timestamp;
  itemId?: number;
  lastModifiedDate?: Timestamp;
  respondByDate?: Timestamp;
  seller?: string;
  transactionId?: number;
}

export type CaseTypeEnum = 'ITEM_NOT_RECEIVED' | 'RETURN';

export interface CaseVoluntaryRefundRequest {
  comments?: Text;
}

export interface CheckCancellationEligibility429Response {
  errors?: Array<Error>;
}

export interface ClaimHistoryEventModel {
  action?: string;
  actor?: UserPartyEnum;
  date?: Timestamp;
  description?: string;
  moneyMovement?: MoneyMovementEntries;
}

export interface ClaimHistoryResponse {
  history?: Array<ClaimHistoryEventModel>;
  shipmentTrackingDetails?: ShipmentTrackingDetailType;
}

export type CloseReturnReasonEnum =
  | 'BUYER_CLOSED'
  | 'FULL_REFUNDED'
  | 'FULL_REFUNDED_BY_DISPOSITION_RULE'
  | 'PARTIALLY_REFUNDED'
  | 'SHIPMENT_TIMEOUT'
  | 'REFUND_TIMEOUT'
  | 'RETURN_REJECTED'
  | 'AUTO_REFUNDED'
  | 'AUTO_PARTIAL_REFUNDED'
  | 'STORE_CREDIT_REFUNDED'
  | 'BUYER_PAYOUT'
  | 'SELLER_INVOICED'
  | 'REPLACEMENT_PAYOUT_RECOUP'
  | 'REQUEST_TIMEOUT'
  | 'REQUEST_DECLINED'
  | 'SELLER_PAYOUT_FAILED'
  | 'BUYER_PAYOUT_FAILED'
  | 'REPLACED'
  | 'MARK_REFUND_RECEIVED'
  | 'MARK_REFUND_RECEIVED_TIMEOUT'
  | 'MARK_PARTIAL_REFUND_RECEIVED'
  | 'BUYER_NO_ACTION'
  | 'ESCALATED'
  | 'LVT_IMMEDIATE_REFUND'
  | 'BUYER_REFUND_AS_PAYOUT'
  | 'BUYER_PARTIAL_REFUND_AS_PAYOUT'
  | 'CHARGEBACK_DISPUTE_FILED'
  | 'BUYER_ACCEPT_LESS_THAN_FULL_REFUND'
  | 'BUYER_ACCEPT_LESS_THAN_FULL_REFUND_AS_PAYOUT'
  | 'ITEM_REJECTED'
  | 'OTHER';

export interface ConfirmRefundRequest {
  refundDate?: Timestamp;
  unpaidOrder?: boolean;
}

export interface CountSummaryType {
  count?: number;
  type?: ReturnCountFilterEnum;
}

export type CountryCodeEnum =
  | 'AD'
  | 'AE'
  | 'AF'
  | 'AG'
  | 'AI'
  | 'AL'
  | 'AM'
  | 'AN'
  | 'AO'
  | 'AQ'
  | 'AR'
  | 'AS'
  | 'AT'
  | 'AU'
  | 'AW'
  | 'AX'
  | 'AZ'
  | 'BA'
  | 'BB'
  | 'BD'
  | 'BE'
  | 'BF'
  | 'BG'
  | 'BH'
  | 'BI'
  | 'BJ'
  | 'BL'
  | 'BM'
  | 'BN'
  | 'BO'
  | 'BQ'
  | 'BR'
  | 'BS'
  | 'BT'
  | 'BV'
  | 'BW'
  | 'BY'
  | 'BZ'
  | 'CA'
  | 'CC'
  | 'CD'
  | 'CF'
  | 'CG'
  | 'CH'
  | 'CI'
  | 'CK'
  | 'CL'
  | 'CM'
  | 'CN'
  | 'CO'
  | 'CR'
  | 'CU'
  | 'CV'
  | 'CW'
  | 'CX'
  | 'CY'
  | 'CZ'
  | 'DE'
  | 'DJ'
  | 'DK'
  | 'DM'
  | 'DO'
  | 'DZ'
  | 'EC'
  | 'EE'
  | 'EG'
  | 'EH'
  | 'ER'
  | 'ES'
  | 'ET'
  | 'FI'
  | 'FJ'
  | 'FK'
  | 'FM'
  | 'FO'
  | 'FR'
  | 'GA'
  | 'GB'
  | 'GD'
  | 'GE'
  | 'GF'
  | 'GG'
  | 'GH'
  | 'GI'
  | 'GL'
  | 'GM'
  | 'GN'
  | 'GP'
  | 'GQ'
  | 'GR'
  | 'GS'
  | 'GT'
  | 'GU'
  | 'GW'
  | 'GY'
  | 'HK'
  | 'HM'
  | 'HN'
  | 'HR'
  | 'HT'
  | 'HU'
  | 'ID'
  | 'IE'
  | 'IL'
  | 'IM'
  | 'IN'
  | 'IO'
  | 'IQ'
  | 'IR'
  | 'IS'
  | 'IT'
  | 'JE'
  | 'JM'
  | 'JO'
  | 'JP'
  | 'KE'
  | 'KG'
  | 'KH'
  | 'KI'
  | 'KM'
  | 'KN'
  | 'KP'
  | 'KR'
  | 'KW'
  | 'KY'
  | 'KZ'
  | 'LA'
  | 'LB'
  | 'LC'
  | 'LI'
  | 'LK'
  | 'LR'
  | 'LS'
  | 'LT'
  | 'LU'
  | 'LV'
  | 'LY'
  | 'MA'
  | 'MC'
  | 'MD'
  | 'ME'
  | 'MF'
  | 'MG'
  | 'MH'
  | 'MK'
  | 'ML'
  | 'MM'
  | 'MN'
  | 'MO'
  | 'MP'
  | 'MQ'
  | 'MR'
  | 'MS'
  | 'MT'
  | 'MU'
  | 'MV'
  | 'MW'
  | 'MX'
  | 'MY'
  | 'MZ'
  | 'NA'
  | 'NC'
  | 'NE'
  | 'NF'
  | 'NG'
  | 'NI'
  | 'NL'
  | 'NO'
  | 'NP'
  | 'NR'
  | 'NU'
  | 'NZ'
  | 'OM'
  | 'PA'
  | 'PE'
  | 'PF'
  | 'PG'
  | 'PH'
  | 'PK'
  | 'PL'
  | 'PM'
  | 'PN'
  | 'PR'
  | 'PS'
  | 'PT'
  | 'PW'
  | 'PY'
  | 'QA'
  | 'RE'
  | 'RO'
  | 'RS'
  | 'RU'
  | 'RW'
  | 'SA'
  | 'SB'
  | 'SC'
  | 'SD'
  | 'SE'
  | 'SG'
  | 'SH'
  | 'SI'
  | 'SJ'
  | 'SK'
  | 'SL'
  | 'SM'
  | 'SN'
  | 'SO'
  | 'SR'
  | 'ST'
  | 'SV'
  | 'SX'
  | 'SY'
  | 'SZ'
  | 'TC'
  | 'TD'
  | 'TF'
  | 'TG'
  | 'TH'
  | 'TJ'
  | 'TK'
  | 'TL'
  | 'TM'
  | 'TN'
  | 'TO'
  | 'TR'
  | 'TT'
  | 'TV'
  | 'TW'
  | 'TZ'
  | 'UA'
  | 'UG'
  | 'UM'
  | 'US'
  | 'UY'
  | 'UZ'
  | 'VA'
  | 'VC'
  | 'VE'
  | 'VG'
  | 'VI'
  | 'VN'
  | 'VU'
  | 'WF'
  | 'WS'
  | 'YE'
  | 'YT'
  | 'ZA'
  | 'ZM'
  | 'ZW';

export interface CreateCancelRequest {
  buyerPaid?: boolean;
  buyerPaidDate?: Timestamp;
  cancelReason?: string;
  legacyOrderId?: string;
  relistLineItem?: Array<RelistLineItem>;
}

export interface CreateCancelResponse {
  cancelId?: string;
  orderEligibilityResult?: OrderEligibilityResult;
  warnings?: Array<ErrorData>;
}

export interface CreateInquiryRequest {
  claimQuantity?: number;
  comments?: Text;
  desiredOutcome?: DesiredOutcomeTypeEnum;
  itemId?: string;
  transactionId?: string;
}

export interface CreateReturnRequest {
  draftId?: string;
  returnRequest?: ReturnRequestType;
}

export interface CreateReturnResponse {
  detail?: GetDetailResponse;
  eligibilityResult?: ReturnEligibilityPerItemType;
  returnId?: string;
  summary?: ReturnSummaryType;
}

export type CurrencyCodeEnum =
  | 'AED'
  | 'AFN'
  | 'ALL'
  | 'AMD'
  | 'ANG'
  | 'AOA'
  | 'ARS'
  | 'AUD'
  | 'AWG'
  | 'AZN'
  | 'BAM'
  | 'BBD'
  | 'BDT'
  | 'BGN'
  | 'BHD'
  | 'BIF'
  | 'BMD'
  | 'BND'
  | 'BOB'
  | 'BRL'
  | 'BSD'
  | 'BTN'
  | 'BWP'
  | 'BYR'
  | 'BZD'
  | 'CAD'
  | 'CDF'
  | 'CHF'
  | 'CLP'
  | 'CNY'
  | 'COP'
  | 'CRC'
  | 'CUP'
  | 'CVE'
  | 'CZK'
  | 'DJF'
  | 'DKK'
  | 'DOP'
  | 'DZD'
  | 'EGP'
  | 'ERN'
  | 'ETB'
  | 'EUR'
  | 'FJD'
  | 'FKP'
  | 'GBP'
  | 'GEL'
  | 'GHS'
  | 'GIP'
  | 'GMD'
  | 'GNF'
  | 'GTQ'
  | 'GYD'
  | 'HKD'
  | 'HNL'
  | 'HRK'
  | 'HTG'
  | 'HUF'
  | 'IDR'
  | 'ILS'
  | 'INR'
  | 'IQD'
  | 'IRR'
  | 'ISK'
  | 'JMD'
  | 'JOD'
  | 'JPY'
  | 'KES'
  | 'KGS'
  | 'KHR'
  | 'KMF'
  | 'KPW'
  | 'KRW'
  | 'KWD'
  | 'KYD'
  | 'KZT'
  | 'LAK'
  | 'LBP'
  | 'LKR'
  | 'LRD'
  | 'LSL'
  | 'LTL'
  | 'LYD'
  | 'MAD'
  | 'MDL'
  | 'MGA'
  | 'MKD'
  | 'MMK'
  | 'MNT'
  | 'MOP'
  | 'MRO'
  | 'MUR'
  | 'MVR'
  | 'MWK'
  | 'MXN'
  | 'MYR'
  | 'MZN'
  | 'NAD'
  | 'NGN'
  | 'NIO'
  | 'NOK'
  | 'NPR'
  | 'NZD'
  | 'OMR'
  | 'PAB'
  | 'PEN'
  | 'PGK'
  | 'PHP'
  | 'PKR'
  | 'PLN'
  | 'PYG'
  | 'QAR'
  | 'RON'
  | 'RSD'
  | 'RUB'
  | 'RWF'
  | 'SAR'
  | 'SBD'
  | 'SCR'
  | 'SDG'
  | 'SEK'
  | 'SGD'
  | 'SHP'
  | 'SLL'
  | 'SOS'
  | 'SRD'
  | 'STD'
  | 'SYP'
  | 'SZL'
  | 'THB'
  | 'TJS'
  | 'TMT'
  | 'TND'
  | 'TOP'
  | 'TRY'
  | 'TTD'
  | 'TWD'
  | 'TZS'
  | 'UAH'
  | 'UGX'
  | 'USD'
  | 'UYU'
  | 'UZS'
  | 'VEF'
  | 'VND'
  | 'VUV'
  | 'WST'
  | 'XAF'
  | 'XCD'
  | 'XOF'
  | 'XPF'
  | 'YER'
  | 'ZAR'
  | 'ZMW'
  | 'ZWL';

export interface DecideReturnRequest {
  comments?: Text;
  decision?: DecisionEnum;
  keepOriginalItem?: boolean;
  partialRefundAmount?: Amount;
  RMANumber?: string;
  rMAProvided?: boolean;
}

export interface DecideReturnResponse {
  refundStatus?: RefundMoneyMovementStatusEnum;
}

export type DecisionEnum =
  | 'PROVIDE_RMA'
  | 'APPROVE'
  | 'APPROVE_WITHOUT_EBAY_LABEL'
  | 'DECLINE'
  | 'OFFER_RETURN'
  | 'OFFER_RETURN_WITHOUT_LABEL'
  | 'OFFER_PARTIAL_REFUND'
  | 'ACCEPT_PARTIAL_REFUND'
  | 'DECLINE_PARTIAL_REFUND'
  | 'OFFER_REPLACEMENT'
  | 'ACCEPT_REPLACEMENT_OFFER'
  | 'DECLINE_REPLACEMENT_OFFER'
  | 'UNKNOWN';

export type DesiredOutcomeTypeEnum = 'FULL_REFUND' | 'STILL_WANT_ITEM';

export interface EligibilityErrorType {
  code?: string;
  content?: string;
  description?: string;
}

export type EligibilityFailureReasonEnum =
  | 'UNKNOWN'
  | 'INSTORE_PICKUP_MADE'
  | 'IN_STORE_PICKUP_READY'
  | 'UNPAID_ORDER'
  | 'UNSUPPORTED_PAYMENT_METHOD'
  | 'CANCELLATION_EXIST'
  | 'CASE_EXIST'
  | 'RETURN_EXIST'
  | 'PAYPAL_DISPUTE_EXIST'
  | 'FULL_REFUNDED_ORDER'
  | 'PARTIAL_REFUNDED_ORDER'
  | 'CROSS_SITE_ORDER'
  | 'SHIPPED_ORDER'
  | 'CANCEL_WINDOW_ELAPSED'
  | 'ELV_RETURN_OR_REVERSAL_EXISTS'
  | 'DELETED_BUYER'
  | 'PAYMENT_PENDING'
  | 'CHARGEBACK_OPENED'
  | 'PARTIAL_CANCEL_NOT_ALLOWED'
  | 'PARTIAL_QUANTITY_NOT_ALLOWED'
  | 'REQUESTED_QUANTITY_NOT_AVAILABLE'
  | 'ITEM_LEVEL_ELIGIBILITY_FAILURE'
  | 'INVALID_LINEITEM'
  | 'DUPLICATE_LINEITEM'
  | 'FULL_REFUNDED_LINEITEM'
  | 'INTERNAL_SYSTEM_ERROR'
  | 'INVALID_ORDER'
  | 'INVALID_USER'
  | 'UNSUPPORTED_SITE';

export interface EligibilityResultType {
  caseId?: string;
  eligibilityErrorDetail?: Array<ReturnEligibilityErrorDetailType>;
  eligibilityStatus?: StatusType;
  eligibleStartDate?: Timestamp;
  returnCreationDate?: Timestamp;
  returnDeadline?: Timestamp;
  returnId?: string;
}

export type ErrorCategory = 'SYSTEM' | 'APPLICATION' | 'REQUEST';

export interface ErrorData {
  category?: ErrorCategory;
  domain?: string;
  errorId?: number;
  httpStatusCode?: number;
  longMessage?: string;
  message?: string;
  parameter?: Array<ErrorParameter>;
  severity?: ErrorSeverity;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export type ErrorSeverity = 'ERROR' | 'WARNING';

export interface EscalateInquiryRequest {
  comments?: Text;
  escalateInquiryReason?: string;
}

export type EscalateReasonEnum =
  | 'SELLER_NO_RESPONSE'
  | 'TROUBLE_COMMUNICATION_WITH_SELLER'
  | 'TROUBLE_COMMUNICATION_WITH_BUYER'
  | 'NO_REFUND_RECEIVED'
  | 'NO_REFUND_FOR_RETURN_SHIPPING'
  | 'BUYER_RETURNED_WRONG_ITEM'
  | 'BUYER_NORESPONSE'
  | 'DISAGREE_WITH_RETURN_REASON'
  | 'ITEM_RECEIVED_IN_DIFFERENT_CONDITION'
  | 'ITEM_NOT_RECEIVED'
  | 'NEW_ITEM_NOT_RECEIVED'
  | 'RECEIVED_WRONG_ITEM'
  | 'RECEIVED_EMPTY_BOX'
  | 'RESOLVED_WITH_BUYER'
  | 'RECEIVED_DAMAGED_ITEM'
  | 'ESCALATED_BY_EBAY'
  | 'OTHER';

export interface EscalateRequest {
  comments?: Text;
  reason?: string;
}

export interface EscalateResponse {
  caseId?: string;
  caseUrl?: string;
}

export interface EscalationEligibilityInfo {
  eligible?: boolean;
  endTime?: Timestamp;
  startTime?: Timestamp;
}

export interface EscalationInfoType {
  buyerEscalationEligibilityInfo?: EscalationEligibilityInfo;
  caseId?: string;
  sellerEscalationEligibilityInfo?: EscalationEligibilityInfo;
}

export interface EstimatedRefundDetailType {
  itemizedRefundDetails?: Array<EstimatedRefundType>;
  optionalRefundLineItems?: Array<EstimatedRefundType>;
}

export interface EstimatedRefundType {
  estimatedAmount?: Amount;
  maxAmount?: Amount;
  minAmount?: Amount;
  purchasePriceDeductedPercentageList?: Array<number>;
  refundFeeType?: RefundFeeTypeEnum;
  restockingFeePercentage?: string;
}

export type FileFormatEnum = 'JPG' | 'JPEG' | 'PNG' | 'GIF' | 'BMP' | 'UNKNOWN';

export type FilePurposeEnum = 'ITEM_RELATED' | 'LABEL_RELATED' | 'REFUND_RELATED' | 'UNKNOWN';

export type FileStatusEnum = 'CREATED' | 'PUBLISHED' | 'DELETED' | 'UNKNOWN';

export interface FindCancelResponse {
  cancellations?: Array<CancelSummary>;
  paginationOutput?: PaginationOutput;
  total?: number;
}

export type FundingMethodBrandEnum = 'VISA' | 'MASTERCARD' | 'AMERICAN_EXPRESS' | 'DISCOVER';

export type FundingMethodTypeEnum = 'CREDIT_CARD' | 'DIRECT_DEBIT' | 'PAY_UPON_INVOICE' | 'AVAILABLE_FUNDS';

export interface FundingSource {
  brand?: FundingMethodBrandEnum;
  memo?: string;
  type?: FundingMethodTypeEnum;
}

export interface FundingSourceType {
  brand?: FundingMethodBrandEnum;
  memo?: string;
  type?: FundingMethodTypeEnum;
}

export type FundingStatusEnum = 'FUNDED' | 'FAILED';

export interface GetCancelDetailResponse {
  cancelDetail?: CancelDetail;
}

export type GetCancelFieldGroup = 'SUMMARY' | 'FULL';

export interface GetDetailResponse {
  detail?: ReturnDetailType;
  summary?: ReturnSummaryType;
}

export interface GetFileResponse {
  files?: Array<ReturnFileType>;
}

export type GetReturnFieldGroupEnum = 'NONE' | 'SUMMARY' | 'FULL';

export interface GetSellerReturnPreferenceResponse {
  advanceRulesEnabled?: boolean;
  rmaRequired?: boolean;
  versionId?: number;
}

export interface GetSummaryResponse {
  countSummary?: Array<CountSummaryType>;
  members?: Array<ReturnSummaryType>;
  paginationOutput?: PaginationOutput;
  total?: number;
}

export interface GetTrackingHistoryResponse {
  carrierUsed?: string;
  scanHistory?: Array<ScanDetailType>;
  trackingNumber?: string;
  trackingStatus?: string;
}

export type INRCreationReasonEnum =
  | 'TRACKING_INFO_UNAVAILABLE'
  | 'INCOMPLETE_ORDER'
  | 'ITEM_NOT_RECEIVED_TRACKING_SHOWS_DELIVERED'
  | 'ITEM_NOT_RECEIVED_ASK_FOR_REFUND'
  | 'LATE_ORDER'
  | 'EMPTY_BOX'
  | 'UNKNOWN';

export interface InquiryDetails {
  appealDetails?: AppealDetails;
  creationDate?: Timestamp;
  escalationDate?: Timestamp;
  expirationDate?: Timestamp;
  lastBuyerRespDate?: Timestamp;
  provisionalRefund?: ProvisionalRefund;
  refundAmounts?: RefundAmounts;
  refundChargeAmount?: Amount;
  refundDeadlineDate?: Timestamp;
  totalAmount?: Amount;
}

export interface InquiryDetailsResponse {
  claimAmount?: Amount;
  creationReason?: string;
  extTransactionId?: string;
  initiator?: UserPartyEnum;
  inquiryClosureDate?: Timestamp;
  inquiryContentOnHold?: boolean;
  inquiryDetails?: InquiryDetails;
  inquiryHistoryDetails?: ClaimHistoryResponse;
  inquiryId?: string;
  inquiryQuantity?: number;
  itemDetails?: ItemDetails;
  itemId?: string;
  returnDetails?: ReturnAddress;
  sellerMakeItRightByDate?: Timestamp;
  resolutionEstimate?: ResolutionEstimate;
  shippingCost?: Amount;
  state?: string;
  status?: string;
  transactionId?: string;
  viewPPTrasanctionUrl?: string;
}

export type InquiryEscalationReasonEnum =
  | 'SELLER_NORESPONSE'
  | 'TROUBLE_COMMUNICATION'
  | 'NOT_RECEIVED'
  | 'NO_REFUND'
  | 'BUYER_UNHAPPY'
  | 'BUYER_TROUBLE'
  | 'SHIPPED_ITEM'
  | 'OTHERS';

export type InquirySearchFieldGroupEnum = 'DEFAULT' | 'SUMMARY';

export interface InquirySearchResponse {
  members?: Array<InquirySummaryType>;
  paginationOutput?: PaginationOutput;
  totalNumberOfInquiries?: number;
}

export type InquiryStateEnum =
  | 'INITIAL'
  | 'PENDING_CREATED'
  | 'CREATED'
  | 'FULL_REFUND_AGREED'
  | 'PARTIAL_REFUND_OFFERED'
  | 'PARTIAL_REFUND_ACCEPTED'
  | 'SELLER_ECHECK_FULL_REFUND_INITIATED'
  | 'SELLER_ECHECK_PARTIAL_REFUND_INITIATED'
  | 'SELLER_ECHECK_REFUND_GRACE_EXPIRED'
  | 'TRACKING_PROVIDED'
  | 'SHIPPING_INFO_PROVIDED'
  | 'AUTO_DISPOSE_MONEY_MOVEMENT_PENDING'
  | 'VOLUNTARY_REFUND_PAYOUT_PENDING'
  | 'ON_HOLD'
  | 'ON_HOLD_FOR_UPLOAD'
  | 'CLOSED'
  | 'OTHER';

export type InquiryStatusEnum =
  | 'PENDING'
  | 'OPEN'
  | 'WAITING_BUYER_RESPONSE'
  | 'WAITING_SELLER_RESPONSE'
  | 'CLOSED'
  | 'CS_CLOSED'
  | 'CLOSED_WITH_ESCALATION'
  | 'OTHER';

export type InquiryStatusFilter =
  | 'PENDING'
  | 'OPEN'
  | 'WAITING_BUYER_RESPONSE'
  | 'WAITING_SELLER_RESPONSE'
  | 'CLOSED'
  | 'CS_CLOSED'
  | 'CLOSED_WITH_ESCALATION'
  | 'OTHER';

export interface InquirySummaryType {
  buyer?: string;
  claimAmount?: Amount;
  creationDate?: Timestamp;
  inquiryId?: number;
  inquiryStatusEnum?: string;
  itemId?: number;
  lastModifiedDate?: Timestamp;
  respondByDate?: Timestamp;
  seller?: string;
  transactionId?: number;
}

export interface InquiryVoluntaryRefundRequest {
  comments?: Text;
}

export interface IssueRefundRequest {
  comments?: Text;
  refundDetail?: RefundDetailType;
  relistItem?: boolean;
}

export interface IssueRefundResponse {
  refundStatus?: RefundMoneyMovementStatusEnum;
}

export interface ItemDetailType {
  ebayPlusTxn?: boolean;
  itemId?: string;
  itemOnHold?: boolean;
  listingSiteId?: number;
  relistedItemId?: string;
  relistStatus?: RelistStatusEnum;
  returnQuantity?: number;
  transactionId?: string;
  transactionDate?: Timestamp;
  itemPrice?: Amount;
  itemPicUrl?: string;
  itemTitle?: string;
}

export interface ItemDetails {
  itemOnHold?: boolean;
  itemPictureUrl?: string;
  itemPrice?: Amount;
  itemTitle?: string;
  viewPurchasedItemUrl?: string;
}

export interface ItemEligibilityResult {
  cancelQuantity?: number;
  eligible?: boolean;
  failureReason?: Array<string>;
  itemId?: string;
  transactionId?: string;
}

export interface ItemizedRefundDetailType {
  refundAmount?: Amount;
  refundFeeType?: string;
  restockingFeePercentage?: string;
}

export interface ItemizedReturnShippingCostType {
  amount?: Amount;
  returnShippingCostType?: ReturnShippingCostType;
}

export type LabelActionEnum =
  'NO_LABEL' | 'UPLOAD_LABEL' | 'MARK_AS_SENT' | 'EBAY_LABEL' | 'PURCHASE_LABEL' | 'AU_LABEL' | 'UNKNOWN';

export type LanguageEnum =
  | 'hy'
  | 'zh'
  | 'nl'
  | 'en'
  | 'eo'
  | 'fr'
  | 'ka'
  | 'de'
  | 'el'
  | 'it'
  | 'ja'
  | 'ko'
  | 'pl'
  | 'pt'
  | 'ru'
  | 'es'
  | 'sv'
  | 'tr'
  | 'vi'
  | 'xx';

export type LanguageScriptEnum =
  | 'LATIN'
  | 'CYRILLIC'
  | 'ARABIC'
  | 'HEBREW'
  | 'GREEK'
  | 'JAPANESE'
  | 'CHINESE'
  | 'GEORGIAN'
  | 'ARMENIAN'
  | 'THAI'
  | 'KOREAN'
  | 'INDIC';

export interface MarkAsReceivedRequest {
  comments?: Text;
}

export type MarketplaceIdEnum =
  | 'EBAY_AT'
  | 'EBAY_AU'
  | 'EBAY_BE'
  | 'EBAY_CA'
  | 'EBAY_CH'
  | 'EBAY_CN'
  | 'EBAY_CZ'
  | 'EBAY_DE'
  | 'EBAY_DK'
  | 'EBAY_ES'
  | 'EBAY_FI'
  | 'EBAY_FR'
  | 'EBAY_GB'
  | 'EBAY_GR'
  | 'EBAY_HK'
  | 'EBAY_HU'
  | 'EBAY_ID'
  | 'EBAY_IE'
  | 'EBAY_IL'
  | 'EBAY_IN'
  | 'EBAY_IT'
  | 'EBAY_JP'
  | 'EBAY_MY'
  | 'EBAY_NL'
  | 'EBAY_NO'
  | 'EBAY_NZ'
  | 'EBAY_PE'
  | 'EBAY_PH'
  | 'EBAY_PL'
  | 'EBAY_PR'
  | 'EBAY_PT'
  | 'EBAY_RU'
  | 'EBAY_SE'
  | 'EBAY_SG'
  | 'EBAY_TH'
  | 'EBAY_TW'
  | 'EBAY_US'
  | 'EBAY_VN'
  | 'EBAY_ZA'
  | 'EBAY_HALF_US'
  | 'EBAY_MOTORS_US';

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

export interface MoneyMovementEntries {
  moneyMovementEntryList?: Array<MoneyMovementEntry>;
}

export interface MoneyMovementEntry {
  amount?: Amount;
  date?: Timestamp;
  fundingSource?: FundingSource;
  fundingStatus?: FundingStatusEnum;
  type?: string;
}

export interface MoneyMovementRef {
  idref?: string;
}

export type NoSellerUploadLabelReasonEnum =
  'ITEM_TOO_LARGE' | 'RETURN_TO_INTL_LOCATION' | 'OTHER' | 'REIMBURSE' | 'WORK_WITH_BUYER' | 'RETURN_TO_STORE';

export interface OrderEligibilityCheckInfo {
  legacyOrderId?: string;
}

export interface OrderEligibilityResult {
  eligible?: boolean;
  eligibleCancelReason?: Array<string>;
  failureReason?: Array<string>;
  itemEligibilityResult?: Array<ItemEligibilityResult>;
  legacyOrderId?: string;
}

export type OrderTypeEnum = 'IN_STORE_PICKUP' | 'EBAY_NOW' | 'ONLINE' | 'OTHER';

export interface PaginationOutput {
  limit?: number;
  offset?: number;
  totalEntries?: number;
  totalPages?: number;
}

export type PartialOrderTypeEnum = 'UNKNOWN' | 'FULL_ORDER' | 'PARTIAL_ORDER';

export type PartyEnum = 'UNKNOWN' | 'SELLER' | 'BUYER';

export type PaymentDenialReasonEnum =
  | 'PP_PAYPAL_GUEST'
  | 'PP_DISALLOWED_DISPUTE'
  | 'PP_ADMINISTRATIVE_FRAUD_REVIEW'
  | 'PP_CREDITCARD_CHARGEBACK'
  | 'PP_ELV_REVERSAL'
  | 'PP_ACH_RETURN'
  | 'PP_UNAUTHORIZED_TRANSACTION'
  | 'OTHER';

export type PaymentProviderEnum = 'UNKNOWN' | 'PAYPAL';

export type PaymentStatusEnum = 'UNKNOWN' | 'PAYPAL_PAID' | 'ONLINE_PAID' | 'MARK_AS_PAID' | 'NOT_PAID';

export interface PayoutRecoupInfo {
  amountToRecoup?: Amount;
  payoutId?: number;
}

export interface ProvideLabelRequest {
  carrierEnum?: string;
  carrierName?: string;
  comments?: Text;
  fileId?: string;
  forwardShippingLabelProvided?: boolean;
  labelAction?: LabelActionEnum;
  labelSentDate?: Timestamp;
  noLabelReason?: NoSellerUploadLabelReasonEnum;
  returnLabelCost?: Amount;
  trackingNumber?: string;
}

export interface ProvideLabelResponse {
  labelData?: string;
  labelId?: string;
  labelURL?: string;
  trackingNumber?: string;
}

export interface ProvideShipmentInfoRequest {
  shippingCarrierName?: string;
  trackingNumber?: string;
}

export interface ProvisionalRefund {
  refundProvided?: boolean;
  refundReversed?: boolean;
}

export interface ProvisionalRefundType {
  refundProvided?: boolean;
  refundReversed?: boolean;
}

export interface RefundAmounts {
  buyerFinalAcceptRefundAmt?: Amount;
  buyerInitExpectRefundAmt?: Amount;
  donationAmount?: Amount;
  feeCreditAmount?: Amount;
  internationalRefundAmount?: Amount;
  refundAmount?: Amount;
}

export interface RefundDeductionType {
  refundDeductionAmount?: Amount;
  refundDeductionPercentage?: number;
}

export interface RefundDetailType {
  donationAmount?: Amount;
  itemizedRefundDetail?: Array<ItemizedRefundDetailType>;
  totalAmount?: Amount;
  feeCreditAmount?: Amount;
}

export type RefundFeeTypeEnum =
  | 'PURCHASE_PRICE'
  | 'ORIGINAL_SHIPPING'
  | 'DOMESTIC_SHIPPING'
  | 'INTERNATIONAL_SHIPPING'
  | 'IMPORT_CHARGE'
  | 'REFUND_FROM_PAYPAL'
  | 'RETURN_SHIPPING'
  | 'ORDER_ADJUSTMENT'
  | 'ITEM_IMPORT_TAX'
  | 'SHIPPING_IMPORT_TAX'
  | 'ITEM_TAX'
  | 'SHIPPING_TAX'
  | 'OTHER';

export interface RefundFundingType {
  date?: Timestamp;
  amount?: Amount;
  fundingSource?: FundingSourceType;
  fundingStatus?: FundingStatusEnum;
}

export interface RefundInfo {
  actualRefundDetail?: ActualRefundDetail;
}

export interface RefundInfoType {
  actualRefundDetail?: ActualRefundDetailType;
  estimatedRefundDetail?: EstimatedRefundDetailType;
  provisionalRefund?: ProvisionalRefundType;
}

export type RefundMoneyMovementStatusEnum = 'REQUESTED' | 'SUCCESS' | 'PENDING' | 'FAILED' | 'UNKNOWN';

export type RefundPaymentTypeEnum = 'INSTANT_REFUND' | 'ECHECK' | 'PAYOUT' | 'INTERMEDIATED_REFUND' | 'OTHER';

export type RefundStatusEnum = 'PENDING' | 'SUCCESS' | 'FAILED' | 'OTHER';

export type RefundType = 'FULL' | 'PARTIAL' | 'OTHER';

export interface RejectCancelRequest {
  shipmentDate?: Timestamp;
  trackingNumber?: string;
}

export interface RelistLineItem {
  itemId?: number;
  quantity?: number;
  transactionId?: number;
}

export type RelistStatusEnum = 'RELIST_ELIGIBLE' | 'SUCCESS' | 'FAILED';

export type RequestTypeEnum = 'CREATE' | 'REQUEST' | 'UNKNOWN';

export interface ResolutionEstimate {
  resolutionEstimateDate?: Timestamp;
}

export interface ResponseHistoryAttributesType {
  escalateReason?: string;
  keepOriginalItem?: boolean;
  moneyMovementRef?: MoneyMovementRef;
  partialRefundAmount?: Amount;
  refundDeductionType?: RefundDeductionType;
  rlspType?: RlspTypeEnum;
  RMA?: string;
  sellerReturnAddress?: ReturnAddressType;
  toEmailAddress?: string;
  updatedTrackingNumber?: string;
}

export type RetEligibilityCheckTypeEnum =
  | 'ITEM_SELECTION'
  | 'RETURN_CREATION'
  | 'PRE_TRANSACTION'
  | 'UNPAID_TRANSACTION'
  | 'RETURN_REASON_SELECTION'
  | 'REPLACEMENT_CREATION'
  | 'REPLACEMENT_ITEM_SELECTION';

export interface RetMoneyMovementDetailType {
  actualAmount?: Amount;
  creationDate?: Timestamp;
  externalPaymentId?: string;
  moneyMovementType?: string;
  paymentProvider?: PaymentProviderEnum;
  requestedAmount?: Amount;
  status?: string;
}

export type RetMoneyMovementStatusEnum =
  'UNKNOWN' | 'REQUESTED' | 'PENDING' | 'SUCCESS' | 'FAILED' | 'REVERSED' | 'TIMEDOUT';

export type RetMoneyMovementTypeEnum =
  | 'UNKNOWN'
  | 'SELLER_VOLUNTARY_REFUND'
  | 'INVOICE_SELLER_FOR_RETURN_SHIPPING'
  | 'CHARGE_BUYER_FOR_RETURN_SHIPPING'
  | 'REFUND_FVF_ITEM_COST'
  | 'REFUND_PROMOTED_LISTING_FEE'
  | 'BUYER_PAYOUT'
  | 'BUYER_MASS_PAYOUT'
  | 'REFUND_FVF_SHIPPING_COST'
  | 'PAYPAL_REFUND'
  | 'AUTO_REFUND'
  | 'CHARGE_BUYER_FOR_REPLACEMENT'
  | 'BUYER_RECOUP'
  | 'SELLER_PAYOUT'
  | 'STORE_CREDIT'
  | 'NON_PAYPAL_FULL_REFUND'
  | 'PAYPAL_PARTIAL_REFUND'
  | 'LVT_IMMEDIATE_REFUND'
  | 'NON_PAYPAL_PARTIAL_REFUND'
  | 'REFUND_IMPORT_TAX_FEE'
  | 'BUYER_REFUND_AS_PAYOUT'
  | 'BUYER_PARTIAL_REFUND_AS_PAYOUT'
  | 'RECOUP_FROM_SELLER_T1'
  | 'REFUND_PPF'
  | 'REFUND_STATE_TAX'
  | 'REFUND_SNAD_FVF'
  | 'REFUND_SNAD_FVF_SHIPPING'
  | 'DONATION';

export interface ReturnAddress {
  address?: Address;
  editable?: boolean;
  firstName?: string;
  lastName?: string;
  RMA?: string;
}

export interface ReturnAddressRequest {
  firstName?: string;
  lastName?: string;
  returnAddress?: Address;
  RMA?: string;
}

export interface ReturnAddressType {
  address?: Address;
  name?: string;
}

export interface ReturnCloseInfoType {
  buyerCloseComment?: string;
  buyerCloseReason?: BuyerCloseReturnReasonEnum;
  returnCloseDate?: Timestamp;
  returnCloseReason?: CloseReturnReasonEnum;
}

export type ReturnCountFilterEnum =
  | 'RETURN_STARTED'
  | 'ITEM_SHIPPED'
  | 'ITEM_DELIVERED'
  | 'CLOSED'
  | 'ALL_OPEN_REPLACEMENT'
  | 'ALL_OPEN'
  | 'ALL_OPEN_RETURN'
  | 'SELLER_ACTION_DUE'
  | 'SELLER_ACTION_OVERDUE'
  | 'SELLER_NO_ACTION'
  | 'EBAY_PLUS'
  | 'UNKNOWN';

export interface ReturnCreationInfoType {
  comments?: Text;
  creationDate?: Timestamp;
  item?: ReturnItemType;
  reason?: string;
  reasonType?: ReturnReasonTypeEnum;
  type?: ReturnTypeEnum;
}

export interface ReturnDetailType {
  buyerAddress?: ReturnAddressType;
  buyerLoginName?: string;
  closeInfo?: ReturnCloseInfoType;
  files?: Array<ReturnFileType>;
  holdInfo?: ReturnHoldInfoType;
  itemDetail?: ItemDetailType;
  marketplaceId?: MarketplaceIdEnum;
  moneyMovementInfo?: Array<RetMoneyMovementDetailType>;
  payoutRecoupInfo?: ReturnPayoutRecoupInfoType;
  refundInfo?: RefundInfoType;
  replacementShipmentInfo?: ShipmentType;
  responseHistory?: Array<ReturnResponseHistoryType>;
  returnShipmentInfo?: ShipmentType;
  returnContentOnHold?: boolean;
  RMANumber?: string;
  sellerAddress?: ReturnAddressType;
  sellerLoginName?: string;
}

export interface ReturnEligibilityErrorDetailType {
  eligibilityError?: EligibilityErrorType;
}

export interface ReturnEligibilityItemPerCheckTypeResult {
  checkType?: RetEligibilityCheckTypeEnum;
  eligibilityInfo?: EligibilityResultType;
}

export interface ReturnEligibilityItemType {
  itemId?: string;
  reason?: string;
  returnQuantity?: number;
  transactionId?: string;
}

export interface ReturnEligibilityPerItemType {
  eligibilityResultsPerCheckType?: Array<ReturnEligibilityItemPerCheckTypeResult>;
  returnItem?: ReturnEligibilityItemType;
}

export interface ReturnFileType {
  creationDate?: Timestamp;
  fileData?: string;
  fileFormat?: FileFormatEnum;
  fileId?: string;
  fileName?: string;
  filePurpose?: FilePurposeEnum;
  fileStatus?: FileStatusEnum;
  resizedFileData?: string;
  secureUrl?: string;
  submitter?: ReturnUserRoleEnum;
}

export interface ReturnHoldInfoType {
  holdCreationDate?: Timestamp;
  holdReferenceId?: string;
  holdReleaseDate?: Timestamp;
  holdStatus?: ReturnHoldStatusEnum;
  holdTransactionId?: string;
}

export type ReturnHoldStatusEnum =
  'HOLD_CREATION_SUCCESS' | 'HOLD_RELEASE_SUCCESS' | 'HOLD_RELEASE_FAILED' | 'INELIGIBLE_TO_RELEASE_HOLD' | 'OTHER';

export interface ReturnItemType {
  itemId?: string;
  returnQuantity?: number;
  transactionId?: string;
}

export interface ReturnPayoutRecoupInfoType {
  amountToRecoup?: Amount;
  payoutId?: number;
}

export interface ReturnPolicyType {
  rmaRequired?: boolean;
}

export type ReturnReasonEnum =
  | 'NO_REASON'
  | 'ORDERED_WRONG_ITEM'
  | 'ORDERED_ACCIDENTALLY'
  | 'FOUND_BETTER_PRICE'
  | 'MISSING_PARTS'
  | 'ORDERED_DIFFERENT_ITEM'
  | 'ARRIVED_DAMAGED'
  | 'NO_LONGER_NEED_ITEM'
  | 'NOT_AS_DESCRIBED'
  | 'DEFECTIVE_ITEM'
  | 'MISCATEGORIZED'
  | 'CUSTOMIZED'
  | 'EXPIRED_ITEM'
  | 'RETURNING_GIFT'
  | 'WRONG_SIZE'
  | 'FAKE_OR_COUNTERFEIT'
  | 'ARRIVED_LATE'
  | 'DIFFERENT_FROM_LISTING'
  | 'IN_STORE_RETURN'
  | 'OUT_OF_STOCK'
  | 'BUYER_REFUSED_TO_PICKUP'
  | 'BUYER_NO_SHOW'
  | 'BUYER_NOT_SCHEDULED'
  | 'BUYER_CANCEL_ORDER'
  | 'VALET_DELIVERY_ISSUES'
  | 'VALET_UNAVAILABLE'
  | 'DOES_NOT_FIT'
  | 'OTHER';

export type ReturnReasonTypeEnum = 'UNKNOWN' | 'SNAD' | 'REMORSE' | 'INSTORE' | 'CANCEL';

export type ReturnRefundInitiatorEnum = 'SELLER_INITIATED' | 'AUTO_REFUND' | 'OTHER';

export interface ReturnRequestType {
  carrier?: string;
  comments?: Text;
  itemId?: string;
  reason?: string;
  requestType?: RequestTypeEnum;
  returnQuantity?: number;
  transactionId?: string;
  type?: ReturnTypeEnum;
}

export interface ReturnResponseDueType {
  activityDue?: ActivityOptionEnum;
  respondByDate?: Timestamp;
}

export interface ReturnResponseHistoryType {
  activity?: ActivityOptionEnum;
  attributes?: ResponseHistoryAttributesType;
  author?: ReturnUserRoleEnum;
  creationDate?: Timestamp;
  fromState?: ReturnStateEnum;
  notes?: string;
  toState?: ReturnStateEnum;
}

export interface ReturnShippingCostDetailType {
  itemizedReturnShippingCost?: Array<ItemizedReturnShippingCostType>;
  totalAmount?: Amount;
}

export type ReturnShippingCostType = 'LABEL_COST' | 'SIGNATURE_CONFIRMATION_COST' | 'INSURANCE' | 'OTHER';

export type ReturnSortEnum =
  | 'FILING_DATE'
  | 'REASON'
  | 'STATUS'
  | 'ESTIMATED_AMOUNT'
  | 'BUYER_LOGIN_NAME'
  | 'ACTUAL_AMOUNT'
  | 'REFUND_DUE_DATE'
  | 'RETURN_ID'
  | 'UNKNOWN';

export interface ReturnSortField {
  ascending?: boolean;
  enumValue?: string;
  field?: string;
}

export type ReturnStateEnum =
  | 'UNKNOWN'
  | 'INITIAL'
  | 'RMA_PENDING'
  | 'ITEM_READY_TO_SHIP'
  | 'ITEM_SHIPPED'
  | 'ITEM_DELIVERED'
  | 'ITEM_KEPT'
  | 'REFUND_TIMEOUT'
  | 'PARTIAL_REFUNDED'
  | 'REFUND_INITIATED'
  | 'RETURN_REQUESTED'
  | 'RETURN_LABEL_REQUESTED'
  | 'RETURN_LABEL_REQUESTED_TIMEOUT'
  | 'RETURN_REQUEST_TIMEOUT'
  | 'RETURN_REJECTED'
  | 'RETURN_LABEL_PENDING'
  | 'RETURN_LABEL_PENDING_TIMEOUT'
  | 'REPLACEMENT_LABEL_PENDING'
  | 'REPLACEMENT_LABEL_PENDING_TIMEOUT'
  | 'PARTIAL_REFUND_REQUESTED'
  | 'PARTIAL_REFUND_INITIATED'
  | 'PARTIAL_REFUND_FAILED'
  | 'PARTIAL_REFUND_DECLINED'
  | 'PARTIAL_REFUND_NON_PAYPAL_INITIATED'
  | 'PARTIAL_REFUND_AS_PAYOUT_INITIATED'
  | 'REPLACEMENT_REQUESTED'
  | 'REPLACEMENT_LABEL_REQUESTED'
  | 'REPLACEMENT_LABEL_REQUESTED_TIMEOUT'
  | 'REPLACEMENT_REQUEST_TIMEOUT'
  | 'REPLACEMENT_OFFER_PENDING'
  | 'PAYOUT_INITIATED'
  | 'AUTO_REFUND_INITIATED'
  | 'REFUND_AS_PAYOUT_INITIATED'
  | 'REFUND_SENT_PENDING_CONFIRMATION'
  | 'REFUND_FAILED'
  | 'LESS_THAN_A_FULL_REFUND_ISSUED'
  | 'CLOSED'
  | 'REPLACEMENT_STARTED'
  | 'REPLACEMENT_RMA_PENDING'
  | 'REPLACEMENT_SHIPPED'
  | 'REPLACEMENT_DELIVERED'
  | 'REPLACED'
  | 'REPLACEMENT_CLOSED';

export type ReturnStatusEnum =
  | 'WAITING_FOR_RMA'
  | 'WAITING_FOR_RETURN_LABEL'
  | 'READY_FOR_SHIPPING'
  | 'ITEM_SHIPPED'
  | 'ITEM_DELIVERED'
  | 'RETURN_REQUESTED'
  | 'RETURN_REQUESTED_TIMEOUT'
  | 'RETURN_REJECTED'
  | 'RETURN_LABEL_REQUESTED'
  | 'PARTIAL_REFUND_REQUESTED'
  | 'PARTIAL_REFUND_INITIATED'
  | 'PARTIAL_REFUND_DECLINED'
  | 'PARTIAL_REFUND_FAILED'
  | 'LESS_THAN_A_FULL_REFUND_ISSUED'
  | 'CLOSED'
  | 'ESCALATED'
  | 'REPLACEMENT_STARTED'
  | 'REPLACEMENT_SHIPPED'
  | 'REPLACEMENT_DELIVERED'
  | 'REPLACED'
  | 'REPLACEMENT_CLOSED'
  | 'REPLACEMENT_WAITING_FOR_RMA'
  | 'REPLACEMENT_REQUESTED'
  | 'REPLACEMENT_LABEL_REQUESTED'
  | 'UNKNOWN';

export interface ReturnSummaryType {
  buyerAvailableOptions?: Array<AvailableOptionType>;
  buyerLoginName?: string;
  buyerResponseDue?: ReturnResponseDueType;
  buyerTotalRefund?: TotalRefundAmountType;
  creationInfo?: ReturnCreationInfoType;
  currentType?: ReturnTypeEnum;
  escalationInfo?: EscalationInfoType;
  orderId?: string;
  returnId?: string;
  returnPolicy?: ReturnPolicyType;
  sellerAvailableOptions?: Array<AvailableOptionType>;
  sellerLoginName?: string;
  sellerResponseDue?: ReturnResponseDueType;
  sellerTotalRefund?: TotalRefundAmountType;
  state?: ReturnStateEnum;
  status?: ReturnStatusEnum;
  timeoutDate?: Timestamp;
}

export type ReturnTypeEnum = 'MONEY_BACK' | 'REPLACEMENT' | 'EXCHANGE' | 'UNKNOWN';

export type ReturnUserRoleEnum = 'BUYER' | 'SELLER' | 'EBAY' | 'SYSTEM' | 'OTHER';

export type RlspTypeEnum =
  | 'AU_PARCELPOINT'
  | 'AU_PARCELPOINT_AUPOST'
  | 'AU_PARCELPOINT_COURIER_PICKUP'
  | 'AU_PARCELPOINT_AUPOST_DROP'
  | 'UNKNOWN';

export interface ScanDetailType {
  eventCity?: string;
  eventCode?: string;
  eventDesc?: string;
  eventPostalCode?: string;
  eventStateOrProvince?: string;
  eventStatus?: string;
  eventTime?: Timestamp;
}

export interface SellerProvideRefundInfoRequest {
  message?: Text;
}

export interface SendMessageRequest {
  message?: Text;
}

export interface SetSellerReturnPreferenceRequest {
  rmaRequired?: boolean;
}

export interface ShipmentInfoRequest {
  proofOfShipmentUploaded?: boolean;
  sellerComments?: Text;
  shippedWithTracking?: boolean;
  shippingCarrierName?: string;
  shippingDate?: Timestamp;
  trackingNumber?: string;
}

export interface ShipmentTrackingDetailType {
  carrier?: string;
  currentStatus?: string;
  estimateFromDate?: Timestamp;
  estimateToDate?: Timestamp;
  trackingNumber?: string;
  trackingURL?: string;
}

export interface ShipmentTrackingType {
  active?: boolean;
  actualDeliveryDate?: Timestamp;
  actualShipDate?: Timestamp;
  carrierEnum?: string;
  carrierId?: number;
  carrierName?: string;
  carrierUsed?: string;
  deliveryDate?: Timestamp;
  deliveryStatus?: TrackingStatusEnum;
  destinationAddress?: ReturnAddressType;
  errorCode?: string;
  labelAvailableUntilDate?: string;
  labelDate?: Timestamp;
  labelId?: string;
  labelPrintExpired?: boolean;
  labelVoidExpired?: boolean;
  markAsReceived?: boolean;
  maxDeliveryEstimate?: Timestamp;
  minDeliveryEstimate?: Timestamp;
  originAddress?: ReturnAddressType;
  shipDate?: Timestamp;
  shipmentId?: string;
  shippedBy?: ReturnUserRoleEnum;
  shippingMethod?: ShippingMethodEnum;
  trackingNumber?: string;
}

export interface ShipmentType {
  allShipmentTrackings?: Array<ShipmentTrackingType>;
  payee?: ReturnUserRoleEnum;
  shipmentTracking?: ShipmentTrackingType;
  shippingLabelCost?: ReturnShippingCostDetailType;
}

export type ShippingCarrierEnum =
  | 'UNKNOWN'
  | 'OTHER'
  | 'USPS'
  | 'UPS'
  | 'FEDEX'
  | 'COLLECT_PLUS'
  | 'ROYAL_MAIL'
  | 'PARCEL_FORCE'
  | 'HERMES'
  | 'AUSTRALIA_POST'
  | 'CANADA_POST'
  | 'DEUTSCHE_POST'
  | 'DHL'
  | 'POSTE'
  | 'BARTOLINI'
  | 'NEXIVE'
  | 'LA_POSTE'
  | 'MONDIAL_RELAY'
  | 'COLISSIMO'
  | 'CORREOS'
  | 'SEUR'
  | 'MRW';

export type ShippingMethodEnum = 'SELF_MAIL' | 'SHIPPING_LABEL' | 'UNKNOWN';

export type StatusType = 'SUCCESS' | 'SELLER_APPROVAL' | 'FAILED' | 'WARNING' | 'UNKNOWN';

export interface Text {
  content?: string;
  language?: string;
  translatedFromContent?: string;
  translatedFromLanguage?: string;
}

export interface Timestamp {
  formattedValue?: string;
  value?: string;
}

export interface TotalRefundAmountType {
  actualRefundAmount?: Amount;
  estimatedRefundAmount?: Amount;
}

export type TrackingStatusEnum = 'DELIVERED' | 'IN_TRANSIT' | 'CREATED' | 'CANCELLED' | 'UNKNOWN';

export interface UploadFileRequest {
  data: string;
  fileName?: string;
  filePurpose: FilePurposeEnum;
}

export interface UploadFileResponse {
  compressedFileData?: string;
  fileId?: string;
}

export type UserPartyEnum = 'UNKNOWN' | 'SELLER' | 'BUYER' | 'CSR' | 'SYSTEM';

export type UserRoleFilterEnum = 'SELLER' | 'BUYER';

export interface VoluntaryRefundResponse {
  refundResult?: VoluntaryRefundResult;
}

export interface VoluntaryRefundResult {
  refundSource?: RefundPaymentTypeEnum;
  refundStatus?: RefundStatusEnum;
}

export type WorldRegionEnum =
  | 'AFRICA'
  | 'AMERICAS'
  | 'ASIA'
  | 'CARIBBEAN'
  | 'CENTRALAMERICA'
  | 'EUROPE'
  | 'EUROPEANUNION'
  | 'LATINAMERICA'
  | 'MIDDLEEAST'
  | 'NORTHAMERICA'
  | 'OCEANIA'
  | 'SOUTHAMERICA'
  | 'SOUTHEASTASIA';
