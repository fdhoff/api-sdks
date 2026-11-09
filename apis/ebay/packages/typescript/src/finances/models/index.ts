// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Amount {
  convertedFromCurrency?: string;
  convertedFromValue?: string;
  convertedToCurrency?: string;
  convertedToValue?: string;
  currency?: string;
  exchangeRate?: string;
  value?: string;
}

export interface BalanceAdjustment {
  adjustmentAmount?: Amount;
  adjustmentType?: string;
}

export interface BillingActivityLineItem {
  amount?: Amount;
  billingTransactionDate?: string;
  billingTransactionId?: string;
  bookingEntry?: string;
  feeType?: string;
  feeTypeDescription?: string;
  listingId?: string;
  orderId?: string;
  promotionalOffers?: Array<DiscountDetail>;
}

export interface BillingActivityResponse {
  billingActivities?: Array<BillingActivityLineItem>;
  count?: number;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface Buyer {
  username?: string;
}

export interface BuyerWithId {
  userId?: string;
  username?: string;
}

export interface Charge {
  cancellationId?: string;
  caseId?: string;
  chargeNetAmount?: Amount;
  inquiryId?: string;
  orderId?: string;
  paymentDisputeId?: string;
  refundId?: string;
  returnId?: string;
}

export interface DiscountDetail {
  amount?: Amount;
  offerType?: string;
}

export interface EarningsSummary {
  expenses?: Expense;
  grossAmount?: Amount;
  orderEarnings?: Amount;
  refunds?: Amount;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface Expense {
  currency?: string;
  donations?: Array<OrderEarningFee>;
  marketplaceFees?: Array<OrderEarningFee>;
  shippingLabels?: Amount;
  value?: string;
}

export interface Fee {
  amount?: Amount;
  feeJurisdiction?: FeeJurisdiction;
  feeMemo?: string;
  feeType?: string;
}

export interface FeeJurisdiction {
  regionName?: string;
  regionType?: string;
}

export interface FundingSource {
  brand?: string;
  memo?: string;
  type?: string;
}

export interface GetOrderEarnings429Response {
  errors?: Array<Error>;
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

export interface OrderEarning {
  buyer?: BuyerWithId;
  orderCreationDate?: string;
  orderEarningsSummary?: EarningsSummary;
  orderId?: string;
  orderLastModifiedDate?: string;
  orderSummary?: OrderSummary;
}

export interface OrderEarningFee {
  amount?: Amount;
  feeType?: string;
}

export interface OrderEarnings {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  orders?: Array<OrderEarning>;
  prev?: string;
  total?: number;
}

export interface OrderEarningsSummary {
  expenses?: Amount;
  grossAmount?: Amount;
  orderCount?: number;
  orderEarnings?: Amount;
  refunds?: Amount;
}

export interface OrderLineItem {
  donations?: Array<Fee>;
  feeBasisAmount?: Amount;
  lineItemId?: string;
  marketplaceFees?: Array<Fee>;
}

export interface OrderSummary {
  discounts?: Amount;
  itemSubtotal?: Amount;
  sellerCollectedTaxes?: Amount;
  shippingAndHandlingCosts?: Amount;
}

export interface Payout {
  amount?: Amount;
  bankReference?: string;
  lastAttemptedPayoutDate?: string;
  payoutDate?: string;
  payoutId?: string;
  payoutInstrument?: PayoutInstrument;
  payoutMemo?: string;
  payoutReference?: string;
  payoutStatus?: string;
  payoutStatusDescription?: string;
  totalAmount?: Amount;
  totalFee?: Amount;
  totalFeeDetails?: Array<Fee>;
  transactionCount?: number;
}

export interface PayoutDetails {
  payoutIds?: Array<string>;
  payoutReference?: string;
}

export interface PayoutInstrument {
  accountLastFourDigits?: string;
  instrumentType?: string;
  nickname?: string;
  payoutPercentage?: string;
}

export interface PayoutSummaryResponse {
  amount?: Amount;
  payoutCount?: number;
  transactionCount?: number;
}

export interface Payouts {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  payouts?: Array<Payout>;
  prev?: string;
  total?: number;
}

export interface Reference {
  referenceId?: string;
  referenceType?: string;
}

export interface SellerFundsSummaryResponse {
  availableFunds?: Amount;
  fundsOnHold?: Amount;
  processingFunds?: Amount;
  totalFunds?: Amount;
}

export interface Tax {
  taxType?: string;
  amount?: Amount;
}

export interface Transaction {
  amount?: Amount;
  bookingEntry?: string;
  buyer?: Buyer;
  eBayCollectedTaxAmount?: Amount;
  feeJurisdiction?: FeeJurisdiction;
  feeType?: string;
  orderId?: string;
  orderLineItems?: Array<OrderLineItem>;
  paymentsEntity?: string;
  payoutDetails?: PayoutDetails;
  payoutId?: string;
  references?: Array<Reference>;
  salesRecordReference?: string;
  taxes?: Array<Tax>;
  totalFeeAmount?: Amount;
  totalFeeBasisAmount?: Amount;
  transactionDate?: string;
  transactionId?: string;
  transactionMemo?: string;
  transactionStatus?: string;
  transactionType?: string;
}

export interface TransactionSummaryResponse {
  adjustmentAmount?: Amount;
  adjustmentBookingEntry?: string;
  adjustmentCount?: number;
  balanceTransferAmount?: Amount;
  balanceTransferBookingEntry?: string;
  balanceTransferCount?: number;
  creditAmount?: Amount;
  creditBookingEntry?: string;
  creditCount?: number;
  disputeAmount?: Amount;
  disputeBookingEntry?: string;
  disputeCount?: number;
  loanRepaymentAmount?: Amount;
  loanRepaymentBookingEntry?: string;
  loanRepaymentCount?: number;
  nonSaleChargeAmount?: Amount;
  nonSaleChargeBookingEntry?: string;
  nonSaleChargeCount?: number;
  onHoldAmount?: Amount;
  onHoldBookingEntry?: string;
  onHoldCount?: number;
  purchaseAmount?: Amount;
  purchaseBookingEntry?: string;
  purchaseCount?: number;
  refundAmount?: Amount;
  refundBookingEntry?: string;
  refundCount?: number;
  shippingLabelAmount?: Amount;
  shippingLabelBookingEntry?: string;
  shippingLabelCount?: number;
  transferAmount?: Amount;
  transferBookingEntry?: string;
  transferCount?: number;
  withdrawalAmount?: Amount;
  withdrawalBookingEntry?: string;
  withdrawalCount?: number;
}

export interface Transactions {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
  transactions?: Array<Transaction>;
}

export interface Transfer {
  fundingSource?: FundingSource;
  transactionDate?: string;
  transferAmount?: Amount;
  transferDetail?: TransferDetail;
  transferId?: string;
}

export interface TransferDetail {
  balanceAdjustment?: BalanceAdjustment;
  charges?: Array<Charge>;
  totalChargeNetAmount?: Amount;
}
