// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export type APIApplicationType = 'PendingEINApplication' | 'DefaultApplication';

export interface APIBeneficialOwner {
  address1?: string | null;
  address2?: string | null;
  citizenshipStatus?: CitizenshipStatus | null;
  city?: string | null;
  country?: string | null;
  dateOfBirth?: string | null;
  email?: string | null;
  firstName?: string | null;
  identificationBlob?: string | null;
  identificationType?: IdentificationType | null;
  isPep?: IsPep | null;
  jobTitle?: BeneficialOwnerJobTitle | null;
  lastName?: string | null;
  otherJobTitle?: string | null;
  percentOwnership?: number | null;
  phoneNumber?: string | null;
  postalCode?: string | null;
  region?: string | null;
  socialProfileLinks?: Array<string> | null;
  state?: string | null;
}

export interface APIBusinessAddress {
  address1?: string | null;
  address2?: string | null;
  city?: string | null;
  country?: string | null;
  postalCode?: string | null;
  region?: string | null;
}

export interface APIBusinessContactDetails {
  address1?: string | null;
  address2?: string | null;
  city?: string | null;
  country?: string | null;
  phoneNumber?: string | null;
  postalCode?: string | null;
  state?: string | null;
}

export interface APIFormationDetails {
  companyOriginCountry?: string | null;
  companyStructure?: MainQuestionnaireCompanyStructure | null;
  eINDocumentFileBlob?: string | null;
  einDocumentFileBlob?: string | null;
  federalEin?: string | null;
  foreignBusinessNumber?: string | null;
  formationDocumentFileBlob?: string | null;
  formationDocumentType?: MainQuestionnaireEntityFormationDocumentType | null;
}

export interface APIOnboardingDataAbout {
  countriesOfOperations?: Array<string> | null;
  countryOfOperation?: string | null;
  description?: string | null;
  industry?: string | null;
  legalBusinessName?: string | null;
  website?: string | null;
}

export interface APISafeRequest {
  canceledAt?: string | null;
  discountRate?: number | null;
  documentUrl: string;
  expiresAt: string;
  governingState?: USState | null;
  id: string;
  includesMostFavoredNationClause: boolean;
  includesProRataRightsLetter: boolean;
  investmentAmount: number;
  investmentDate: string;
  investor: APISafeRequestInvestor;
  organization: APISafeRequestOrganization;
  paidAt?: string | null;
  signedByInvestorAt?: string | null;
  signedByOwnerAt?: string | null;
  valuationCap?: number | null;
  valuationType: ValuationType;
}

export interface APISafeRequestInvestor {
  additionalBylines?: string | null;
  address?: string | null;
  investorType: SafeRequestInvestorType;
  legalEntityName: string;
  signatoryEmail: string;
  signatoryName: string;
  signatoryTitle?: string | null;
}

export interface APISafeRequestOrganization {
  legalEntityName: string;
  signatoryEmail: string;
  signatoryName: string;
  signatoryTitle: string;
}

export interface APISubmitOnboardingDataParams {
  about?: APIOnboardingDataAbout | null;
  applicationType?: APIApplicationType | null;
  beneficialOwners: Array<APIBeneficialOwner>;
  businessContactDetails?: APIBusinessContactDetails | null;
  businessLegalAddress?: APIBusinessAddress | null;
  businessPhysicalAddress?: APIBusinessAddress | null;
  formationDetails?: APIFormationDetails | null;
  inviteEmail?: string | null;
  partner: string;
  webhookURL?: string | null;
}

export interface APISubmitOnboardingDataResponse {
  onboardingDataId: string;
  signupLink: string;
}

export interface Account {
  accountNumber: string;
  availableBalance: number;
  canReceiveTransactions?: boolean | null;
  canSendRealTimePayments: boolean;
  createdAt: string;
  currentBalance: number;
  dashboardLink: string;
  id: string;
  kind: string;
  legalBusinessName: string;
  name: string;
  nickname?: string | null;
  routingNumber: string;
  status: AccountStatus;
  type: AccountType;
}

export interface AccountCard {
  cardId: string;
  createdAt: string;
  lastFourDigits: string;
  nameOnCard: string;
  network: CardNetwork;
  physicalCardStatus?: PhysicalCardStatus | null;
  spendLimit: SpendLimit;
  status: CardStatus;
  type: CardType;
  updatedAt: string;
  userId: string;
}

export interface AccountCardsResponse {
  cards: Array<AccountCard>;
}

export interface AccountStatement {
  companyLegalAddress: Address;
  companyLegalName: string;
  details: AccountStatementPayload;
  downloadUrl: string;
  ein?: string | null;
  endDate: string;
  endingBalance: number;
  id: string;
  startDate: string;
  transactions: Array<AccountStatementTransaction>;
}

export interface AccountStatementPayload {
  accountDetails: AccountStatementPayloadAccountDetails;
  accountType: AccountStatementPayloadAccountTypeEnum;
}

export type AccountStatementPayloadAccountTypeEnum = 'depository' | 'credit';

export type AccountStatementPayloadAccountDetails = CreditAccountStatementPayload | DepositoryAccountStatementPayload;

export interface AccountStatementTransaction {
  createdAt: string;
  id: string;
  postedAt?: string | null;
}

export type AccountStatus = 'active' | 'deleted' | 'pending' | 'archived';

export type AccountType = 'mercury' | 'external' | 'recipient';

export type AccountingSyncStatus = 'pending' | 'reviewed' | 'syncing' | 'synced' | 'errored' | 'excluded';

export interface AccountsPaginatedResponse {
  accounts: Array<Account>;
  page: AccountsPaginatedResponsePage;
}

export interface AccountsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface AddRecipientRequest {
  address?: AddressData;
  checkInfo?: CheckInfoRaw;
  contactEmail?: string;
  domesticWireRoutingInfo?: DomesticWireRoutingInfoRaw;
  electronicRoutingInfo?: ElectronicRoutingInfoRaw;
  emails: Array<string>;
  name: string;
  nickname?: string;
  realTimePaymentRoutingInfo?: RealTimePaymentRoutingInfoRaw;
}

export interface Address {
  address1: string;
  address2?: string | null;
  city: string;
  country: string;
  name: string;
  postalCode: string;
  region: string;
}

export interface AddressData {
  address1: string;
  address2?: string | null;
  city: string;
  postalCode: string;
  state?: USState | null;
}

export interface AddressWithoutName {
  address1: string;
  address2?: string | null;
  city: string;
  country: string;
  postalCode: string;
  region: string;
}

export interface AgentCardConfig {
  manualApprovalThreshold?: number | null;
}

export interface AgenticCardState {
  manualApprovalThreshold?: number | null;
}

export type ApiBillingCadence = 'monthly' | 'annual';

export type ApiEventOperationType = 'create' | 'update' | 'delete';

export type ApiEventResourceType =
  'transaction' | 'checkingAccount' | 'savingsAccount' | 'treasuryAccount' | 'investmentAccount' | 'creditAccount';

export interface ApiEventResponse {
  changedPaths: Array<string>;
  id: string;
  mergePatch: object;
  occurredAt: string;
  operationType: ApiEventOperationType;
  previousValues?: object | null;
  resourceId: string;
  resourceType: ApiEventResourceType;
  resourceVersion: number;
}

export interface ApiEventsPaginatedResponse {
  events: Array<ApiEventResponse>;
  page: ApiEventsPaginatedResponsePage;
}

export interface ApiEventsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type ApiOrganizationKind = 'personal' | 'business';

export type ApiSendEmailOption = 'DontSend' | 'SendNow';

export type ApiSubscriptionTier = 'free' | 'plus' | 'premium' | 'pro' | 'enterprise';

export interface ApiUpdateTransactionRequest {
  categoryId?: string | null;
  note?: string | null;
}

export type ApiUserRole = 'administrator' | 'bookkeeper' | 'customUser' | 'cardOnlyUser' | 'employee';

export interface ApiV1ArAttachmentResponseData {
  fileName: string;
  id: string;
  url: string;
}

export interface ApiV1ArAttachmentsResponseData {
  attachments: Array<ApiV1ArAttachmentResponseData>;
}

export interface ApiV1ArCustomerAddress {
  address1: string;
  address2?: string | null;
  city: string;
  country: string;
  postalCode: string;
  region: string;
}

export interface ApiV1ArCustomerAddressInput {
  address1: string;
  address2?: string | null;
  city: string;
  country: string;
  name: string;
  postalCode: string;
  region: string;
}

export interface ApiV1ArCustomerCreateRequest {
  address?: ApiV1ArCustomerAddressInput | null;
  email: string;
  name: string;
}

export interface ApiV1ArCustomerPaginatedResponseData {
  customers: Array<ApiV1ArCustomerResponseData>;
  page: ApiV1ArCustomerPaginatedResponseDataPage;
}

export interface ApiV1ArCustomerPaginatedResponseDataPage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1ArCustomerResponseData {
  address?: ApiV1ArCustomerAddress | null;
  deletedAt?: string | null;
  email: string;
  id: string;
  name: string;
}

export interface ApiV1ArCustomerUpdateRequest {
  address?: ApiV1ArCustomerAddressInput | null;
  email: string;
  name: string;
  resendOpenInvoices: boolean;
}

export interface ApiV1ArInvoiceCreateRequest {
  achDebitEnabled: boolean;
  ccEmails: Array<string>;
  creditCardEnabled: boolean;
  currencyCode?: string | null;
  customerId: string;
  destinationAccountId: string;
  dueDate: string;
  internalNote?: string | null;
  invoiceDate: string;
  invoiceNumber?: string | null;
  lineItems: Array<ApiV1ArLineItemData>;
  payerMemo?: string | null;
  poNumber?: string | null;
  sendEmailOption?: ApiSendEmailOption | null;
  servicePeriodEndDate?: string | null;
  servicePeriodStartDate?: string | null;
  useRealAccountNumber: boolean;
}

export interface ApiV1ArInvoiceResponse {
  achDebitEnabled: boolean;
  amount: number;
  canceledAt?: string | null;
  ccEmails: Array<string>;
  createdAt: string;
  creditCardEnabled: boolean;
  currencyCode: string;
  customerId: string;
  destinationAccountId: string;
  dueDate: string;
  id: string;
  internalNote?: string | null;
  invoiceDate: string;
  invoiceNumber: string;
  lineItems: Array<ApiV1ArLineItemData>;
  payerMemo?: string | null;
  poNumber?: string | null;
  servicePeriodEndDate?: string | null;
  servicePeriodStartDate?: string | null;
  slug: string;
  status: PaymentLinkStatus;
  updatedAt: string;
  useRealAccountNumber: boolean;
}

export interface ApiV1ArInvoiceUpdateRequest {
  achDebitEnabled: boolean;
  ccEmails: Array<string>;
  creditCardEnabled: boolean;
  dueDate: string;
  internalNote?: string | null;
  invoiceDate: string;
  invoiceNumber: string;
  lineItems: Array<ApiV1ArLineItemData>;
  payerMemo?: string | null;
  poNumber?: string | null;
  servicePeriodEndDate?: string | null;
  servicePeriodStartDate?: string | null;
  useRealAccountNumber: boolean;
}

export interface ApiV1ArInvoicesData {
  achDebitEnabled: boolean;
  amount: number;
  canceledAt?: string | null;
  ccEmails: Array<string>;
  createdAt: string;
  creditCardEnabled: boolean;
  currencyCode: string;
  customerId: string;
  destinationAccountId: string;
  dueDate: string;
  id: string;
  internalNote?: string | null;
  invoiceDate: string;
  invoiceNumber: string;
  payerMemo?: string | null;
  poNumber?: string | null;
  slug: string;
  status: PaymentLinkStatus;
  updatedAt: string;
  useRealAccountNumber: boolean;
}

export interface ApiV1ArInvoicesPaginatedResponse {
  invoices: Array<ApiV1ArInvoicesData>;
  page: ApiV1ArInvoicesPaginatedResponsePage;
}

export interface ApiV1ArInvoicesPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1ArLineItemData {
  name: string;
  quantity: number;
  salesTaxRate?: number | null;
  unitPrice: number;
}

export interface ApiV1ArProductCreateRequest {
  description?: string | null;
  name: string;
  unitPrice: number;
}

export interface ApiV1ArProductPaginatedResponseData {
  page: ApiV1ArProductPaginatedResponseDataPage;
  products: Array<ApiV1ArProductResponseData>;
}

export interface ApiV1ArProductPaginatedResponseDataPage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1ArProductResponseData {
  description?: string | null;
  id: string;
  name: string;
  unitPrice: number;
  updatedAt: string;
}

export interface ApiV1AssignTransactionRequest {
  allowOverspend?: boolean | null;
  transactionId: string;
}

export interface ApiV1BudgetExpenditure {
  assignedAmount?: number | null;
  expenseId?: string | null;
  id: string;
  transactionId?: string | null;
}

export interface ApiV1BudgetExpendituresResponse {
  expenditures: Array<ApiV1BudgetExpenditure>;
  page: ApiV1BudgetExpendituresResponsePage;
}

export interface ApiV1BudgetExpendituresResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type ApiV1BudgetFrequency = 'oneTime' | 'daily' | 'weekly' | 'monthly' | 'yearly';

export interface ApiV1BudgetIdResponse {
  id: string;
}

export interface ApiV1BudgetMember {
  cycleRemaining: number;
  cycleSpent: number;
  email: string;
  firstName: string;
  lastName: string;
  orgUserId: string;
}

export interface ApiV1BudgetMembersResponse {
  members: Array<ApiV1BudgetMember>;
  page: ApiV1BudgetMembersResponsePage;
}

export interface ApiV1BudgetMembersResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type ApiV1BudgetPublishStatus = 'draft' | 'published' | 'archived';

export interface ApiV1CreateBudgetRequest {
  amountPerUserPerPeriod?: number | null;
  description?: string | null;
  endDate?: string | null;
  frequency: ApiV1BudgetFrequency;
  name?: string | null;
  startDate?: string | null;
}

export interface ApiV1CreateReimbursementRequest {
  amount: number;
  categoryId?: string | null;
  currency: string;
  datePaidFor: string;
  merchantName: string;
  notes?: string | null;
}

export interface ApiV1CreateReimbursementResponse {
  id: string;
}

export interface ApiV1DenyReimbursementRequest {
  reason: string;
}

export interface ApiV1ReceiptResponse {
  createdAt: string;
  fileName: string;
  id: string;
  matchedTransactionId?: string | null;
  status: ApiV1ReceiptStatus;
  uploadedAt?: string | null;
}

export type ApiV1ReceiptStatus = 'pending' | 'matched' | 'unmatched' | 'notAttempted' | 'failed';

export interface ApiV1ReceiptUploadUrlRequest {
  fileName: string;
}

export interface ApiV1ReceiptUploadUrlResponse {
  id: string;
  upload: string;
}

export interface ApiV1ReceiptsPaginatedResponse {
  page: ApiV1ReceiptsPaginatedResponsePage;
  receipts: Array<ApiV1ReceiptResponse>;
}

export interface ApiV1ReceiptsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1ReimbursementAttachment {
  fileName: string;
  id: string;
  url: string;
}

export interface ApiV1ReimbursementListItem {
  amount: number;
  attachments: Array<ApiV1ReimbursementAttachment>;
  currency: string;
  id: string;
  paymentStatus: ReimbursementPaymentStatus;
  reviewStatus: ReimbursementReviewStatus;
  submittedAt: string;
  submitterUserId: string;
}

export interface ApiV1ReimbursementResponse {
  amount: number;
  attachments: Array<ApiV1ReimbursementAttachment>;
  categoryId?: string | null;
  currency: string;
  datePaidFor: string;
  id: string;
  merchantName?: string | null;
  notes?: string | null;
  paymentStatus: ReimbursementPaymentStatus;
  reviewStatus: ReimbursementReviewStatus;
  submittedAt: string;
  submitterUserId: string;
  transactionId?: string | null;
}

export interface ApiV1ReimbursementsPaginatedResponse {
  page: ApiV1ReimbursementsPaginatedResponsePage;
  reimbursements: Array<ApiV1ReimbursementListItem>;
}

export interface ApiV1ReimbursementsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1SpendBudgetResponse {
  amountPerUserPerPeriod?: number | null;
  description?: string | null;
  endDate?: string | null;
  frequency: ApiV1BudgetFrequency;
  id: string;
  name?: string | null;
  startDate?: string | null;
  status: ApiV1BudgetPublishStatus;
}

export interface ApiV1SpendBudgetsResponse {
  budgets: Array<ApiV1SpendBudgetResponse>;
  page: ApiV1SpendBudgetsResponsePage;
}

export interface ApiV1SpendBudgetsResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface ApiV1UpdateBudgetRequest {
  amountPerUserPerPeriod?: number | null;
  description?: string | null;
  endDate?: string | null;
  frequency?: ApiV1BudgetFrequency | null;
  name?: string | null;
  startDate?: string | null;
}

export interface ApiWebhookResponse {
  createdAt: string;
  eventTypes?: Array<WebhookEventType> | null;
  filterPaths?: Array<ResourceField> | null;
  id: string;
  secret?: string | null;
  status: ApiWebhookStatus;
  updatedAt: string;
  url: string;
}

export type ApiWebhookStatus = 'active' | 'paused' | 'disabled';

export interface ApiWebhooksPaginatedResponse {
  page: ApiWebhooksPaginatedResponsePage;
  webhooks: Array<ApiWebhookResponse>;
}

export interface ApiWebhooksPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface AutoTransferRule {
  controlledAccountId: string;
  description: string;
  details: AutoTransferRuleKind;
  frequency: string;
  id: string;
  isPaused: boolean;
  name: string;
  nextTransferAt?: string | null;
  nickname?: string | null;
}

export interface AutoTransferRuleDistributeAmount {
  reservoirAccounts: Array<AutoTransferRuleReservoirAmount>;
}

export interface AutoTransferRuleDistributePercentage {
  reservoirAccounts: Array<AutoTransferRuleReservoirPercentage>;
}

export type AutoTransferRuleKind =
  | AutoTransferRuleKindDistributeAmount
  | AutoTransferRuleKindDistributePercentage
  | AutoTransferRuleKindMaintainTargetBalance;

export interface AutoTransferRuleKindDistributeAmount {
  contents: AutoTransferRuleDistributeAmount;
  kind: AutoTransferRuleKindDistributeAmountKindEnum;
}

export type AutoTransferRuleKindDistributeAmountKindEnum = 'distributeAmount';

export interface AutoTransferRuleKindDistributePercentage {
  contents: AutoTransferRuleDistributePercentage;
  kind: AutoTransferRuleKindDistributePercentageKindEnum;
}

export type AutoTransferRuleKindDistributePercentageKindEnum = 'distributePercentage';

export interface AutoTransferRuleKindMaintainTargetBalance {
  contents: AutoTransferRuleMaintainTargetBalance;
  kind: AutoTransferRuleKindMaintainTargetBalanceKindEnum;
}

export type AutoTransferRuleKindMaintainTargetBalanceKindEnum = 'maintainTargetBalance';

export interface AutoTransferRuleMaintainTargetBalance {
  lowerBound?: number | null;
  reservoirAccountId: string;
  targetBalance: number;
  upperBound?: number | null;
}

export interface AutoTransferRuleReservoirAmount {
  accountId: string;
  amount: number;
}

export interface AutoTransferRuleReservoirPercentage {
  accountId: string;
  percentage: number;
}

export interface AutoTransferRulesResponse {
  page: AutoTransferRulesResponsePage;
  rules: Array<AutoTransferRule>;
}

export interface AutoTransferRulesResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type BeneficialOwnerJobTitle =
  | 'ChiefExecutiveOfficer'
  | 'ChiefOperatingOfficer'
  | 'ChiefTechnologyOfficer'
  | 'ChiefFinancialOfficer'
  | 'Founder'
  | 'President'
  | 'GeneralPartner'
  | 'FinanceTeam'
  | 'Other';

export interface BooksAPIBill {
  amountRemaining: number;
  displayStatus: BooksAccrualSourceDisplayStatus;
  dueDate?: string | null;
  effectiveDate: string;
  grossAmount: number;
  id: string;
  lines: Array<BooksAPIBillLine>;
  notes?: string | null;
  paymentApplications: Array<BooksAPIBillPaymentApplication>;
  referenceNumber?: string | null;
  status: BooksAccrualSourceStatus;
  vendor?: BooksAPIBillVendor | null;
}

export interface BooksAPIBillLine {
  amount: number;
  description: string;
  id: string;
  ledgerId: string;
}

export interface BooksAPIBillPaymentApplication {
  amount: number;
  lineEntryId: string;
}

export interface BooksAPIBillVendor {
  id: string;
  name: string;
}

export interface BooksAPICashBalanceRow {
  balances: Array<number>;
  children: Array<BooksAPICashBalanceRow>;
  ledgerId: string;
  name: string;
  parentId?: string | null;
  sortCode: string;
  totalBalances: Array<number>;
}

export interface BooksAPICashFlowLedgerRow {
  children: Array<BooksAPICashFlowLedgerRow>;
  ledgerId: string;
  name: string;
  netCashFlows: Array<number>;
  parentId?: string | null;
  totalNetCashFlows: Array<number>;
}

export interface BooksAPICashFlowReport {
  columns: Array<BooksAPIReportColumn>;
  endingBalances: Array<BooksAPICashBalanceRow>;
  endingCashBalances: Array<number>;
  ledgers: Array<BooksAPICashFlowLedgerRow>;
  startingBalances: Array<BooksAPICashBalanceRow>;
  startingCashBalances: Array<number>;
}

export interface BooksAPICategorizationRule {
  conditions: Array<BooksAPICategorizationRuleCondition>;
  glCodeName?: string | null;
  id: string;
  lastApplied?: string | null;
  outputs: Array<BooksAPICategorizationRuleOutput>;
  status: BooksAPICategorizationRuleStatus;
}

export interface BooksAPICategorizationRuleAmountCondition {
  amount: number;
  operator: BooksAPICategorizationRuleAmountOperator;
}

export type BooksAPICategorizationRuleAmountOperator =
  'lessThan' | 'lessThanOrEqualTo' | 'greaterThan' | 'greaterThanOrEqualTo' | 'equalTo';

export type BooksAPICategorizationRuleCondition =
  | BooksAPICategorizationRuleConditionAmount
  | BooksAPICategorizationRuleConditionCounterparty
  | BooksAPICategorizationRuleConditionCreditCard
  | BooksAPICategorizationRuleConditionCustomCategory
  | BooksAPICategorizationRuleConditionDebitCard
  | BooksAPICategorizationRuleConditionDescription
  | BooksAPICategorizationRuleConditionUser;

export interface BooksAPICategorizationRuleConditionAmount {
  contents: BooksAPICategorizationRuleAmountCondition;
  tag: BooksAPICategorizationRuleConditionAmountTagEnum;
}

export type BooksAPICategorizationRuleConditionAmountTagEnum = 'amount';

export interface BooksAPICategorizationRuleConditionCounterparty {
  contents: BooksAPICategorizationRuleCounterpartyCondition;
  tag: BooksAPICategorizationRuleConditionCounterpartyTagEnum;
}

export type BooksAPICategorizationRuleConditionCounterpartyTagEnum = 'counterparty';

export interface BooksAPICategorizationRuleConditionCreditCard {
  contents: BooksAPICategorizationRuleCreditCardCondition;
  tag: BooksAPICategorizationRuleConditionCreditCardTagEnum;
}

export type BooksAPICategorizationRuleConditionCreditCardTagEnum = 'creditCard';

export interface BooksAPICategorizationRuleConditionCustomCategory {
  contents: BooksAPICategorizationRuleCustomCategoryCondition;
  tag: BooksAPICategorizationRuleConditionCustomCategoryTagEnum;
}

export type BooksAPICategorizationRuleConditionCustomCategoryTagEnum = 'customCategory';

export interface BooksAPICategorizationRuleConditionDebitCard {
  contents: BooksAPICategorizationRuleDebitCardCondition;
  tag: BooksAPICategorizationRuleConditionDebitCardTagEnum;
}

export type BooksAPICategorizationRuleConditionDebitCardTagEnum = 'debitCard';

export interface BooksAPICategorizationRuleConditionDescription {
  contents: BooksAPICategorizationRuleDescriptionCondition;
  tag: BooksAPICategorizationRuleConditionDescriptionTagEnum;
}

export type BooksAPICategorizationRuleConditionDescriptionTagEnum = 'description';

export interface BooksAPICategorizationRuleConditionUser {
  contents: BooksAPICategorizationRuleUserCondition;
  tag: BooksAPICategorizationRuleConditionUserTagEnum;
}

export type BooksAPICategorizationRuleConditionUserTagEnum = 'user';

export interface BooksAPICategorizationRuleCounterpartyCondition {
  name: string;
}

export interface BooksAPICategorizationRuleCreditCardCondition {
  creditCardId: string;
}

export interface BooksAPICategorizationRuleCustomCategoryCondition {
  customCategoryId: string;
}

export interface BooksAPICategorizationRuleDebitCardCondition {
  debitCardId: string;
}

export interface BooksAPICategorizationRuleDescriptionCondition {
  contains: string;
}

export interface BooksAPICategorizationRuleOutput {
  contents: BooksAPICategorizationRuleSetLedgerOutput;
  tag: BooksAPICategorizationRuleOutputTagEnum;
}

export type BooksAPICategorizationRuleOutputTagEnum = 'setLedger';

export interface BooksAPICategorizationRuleSetLedgerOutput {
  ledgerId: string;
}

export type BooksAPICategorizationRuleStatus = 'active' | 'inactive' | 'invalid';

export interface BooksAPICategorizationRuleUserCondition {
  userId: string;
}

export interface BooksAPICategorizationSplit {
  amount: number;
  description?: string | null;
  ledgerId: string;
  tagIds?: Array<string> | null;
}

export interface BooksAPICategorizeTransactionItem {
  journalEntryId: string;
  splits: Array<BooksAPICategorizationSplit>;
}

export interface BooksAPICategorizedTransaction {
  categorizationLines: Array<BooksAPITransactionCategorizationLine>;
  journalEntryId: string;
}

export interface BooksAPICreateJournalEntryLineEntry {
  amount: number;
  debitCredit: BooksDebitCredit;
  description: string;
  ledgerId: string;
  tagIds?: Array<string> | null;
}

export interface BooksAPICreateLedgerResult {
  error?: BooksAPILedgerWriteError | null;
  ledger?: BooksAPILedger | null;
}

export interface BooksAPIDeleteLedgerResult {
  deleted: boolean;
  error?: BooksAPILedgerWriteError | null;
  ledgerId: string;
}

export interface BooksAPIInstance {
  booksId: string;
  callsign: string;
  companyName: string;
  organizationId: string;
  relationship: BooksAPIInstanceRelationship;
}

export type BooksAPIInstanceRelationship = 'self' | 'client';

export interface BooksAPIInvoice {
  amountRemaining: number;
  customer?: BooksAPIInvoiceCustomer | null;
  displayStatus: BooksAccrualSourceDisplayStatus;
  dueDate?: string | null;
  effectiveDate: string;
  grossAmount: number;
  id: string;
  lines: Array<BooksAPIInvoiceLine>;
  notes?: string | null;
  paymentApplications: Array<BooksAPIInvoicePaymentApplication>;
  referenceNumber?: string | null;
  status: BooksAccrualSourceStatus;
}

export interface BooksAPIInvoiceCustomer {
  id: string;
  name: string;
}

export interface BooksAPIInvoiceLine {
  amount: number;
  description: string;
  id: string;
  ledgerId: string;
}

export interface BooksAPIInvoicePaymentApplication {
  amount: number;
  lineEntryId: string;
}

export type BooksAPIInvoiceSyncStatus = 'pending';

export interface BooksAPILedger {
  debitCredit: BooksDebitCredit;
  deletable: boolean;
  deleteBlockedReason?: BooksAPILedgerDeleteBlockedReason | null;
  editable: boolean;
  financialAccountType?: BooksFinancialAccountType | null;
  id: string;
  isRequired: boolean;
  name: string;
  openingBalance?: number | null;
  parentId?: string | null;
  requiredLedgerPurpose?: BooksRequiredLedgerPurpose | null;
  sortCode: string;
  subType: BooksLedgerSubType;
  type: BooksLedgerType;
}

export interface BooksAPILedgerBalance {
  closingBalance: number;
  debitCredit: BooksDebitCredit;
  ledgerId: string;
  name: string;
  netActivity: number;
  openingBalance: number;
  specialType?: BooksRequiredLedgerPurpose | null;
  subType: BooksLedgerSubType;
  type: BooksLedgerType;
}

export type BooksAPILedgerDeleteBlockedReason = 'required' | 'hasActivity' | 'linkedSource' | 'integrationMapped';

export interface BooksAPILedgerWriteError {
  code: BooksAPILedgerWriteErrorCode;
  message: string;
}

export type BooksAPILedgerWriteErrorCode =
  | 'invalidLedger'
  | 'missingParameters'
  | 'duplicateName'
  | 'duplicateSortCode'
  | 'invalidLedgerType'
  | 'invalidLedgerParent'
  | 'invalidLedgerReportCashFlow'
  | 'deletingRequiredLedger'
  | 'deletingLedgerWithActivity'
  | 'deletingLinkedLedger'
  | 'deletingParentLedger'
  | 'modifyingRequiredLedger'
  | 'integrationMapped'
  | 'mercuryAccountLedger'
  | 'unknownError';

export interface BooksAPILineEntry {
  amount: number;
  datetime: string;
  debitCredit: BooksDebitCredit;
  description?: string | null;
  id: string;
  journalEntryDescription: string;
  journalEntryId: string;
  ledgerId: string;
  ledgerName: string;
  opposingLedgerIds: Array<string>;
  tags: Array<BooksTag>;
}

export interface BooksAPIPendingInvoice {
  customer: BooksAPIInvoiceCustomer;
  dueDate: string;
  effectiveDate: string;
  grossAmount: number;
  message: string;
  referenceNumber: string;
  syncStatus: BooksAPIInvoiceSyncStatus;
}

export interface BooksAPIReport {
  columns: Array<BooksAPIReportColumn>;
  retainedEarnings?: BooksAPIRetainedEarnings | null;
  rows: Array<BooksAPIReportRow>;
}

export interface BooksAPIReportColumn {
  endDate?: string | null;
  isPartial: boolean;
  label: string;
  startDate?: string | null;
}

export interface BooksAPIReportRow {
  amounts: Array<number>;
  children: Array<BooksAPIReportRow>;
  debitCredit: BooksDebitCredit;
  ledgerId?: string | null;
  name: string;
  parentId?: string | null;
  rowKind: BooksAPIReportRowKind;
  sortCode?: string | null;
  subType?: BooksLedgerSubType | null;
  totalAmounts: Array<number>;
  type?: BooksLedgerType | null;
}

export type BooksAPIReportRowKind = 'ledger' | 'summary' | 'computed';

export interface BooksAPIRetainedEarnings {
  calculatedCurrentYearEarnings: Array<number>;
  calculatedRetainedEarnings: Array<number>;
}

export interface BooksAPISetLedgerOpeningBalanceResult {
  error?: BooksAPILedgerWriteError | null;
  ledgerId: string;
  success: boolean;
}

export interface BooksAPISourceAccount {
  businessPersonal: BooksAPISourceAccountUsage;
  debitCredit: BooksDebitCredit;
  id: string;
  ledgerId: string;
  name: string;
  origin: BooksAPISourceAccountOrigin;
}

export type BooksAPISourceAccountOrigin = 'mercury' | 'plaid' | 'rutterCommerce' | 'manual';

export type BooksAPISourceAccountUsage = 'business' | 'personal';

export interface BooksAPITransaction {
  amount: number;
  attachments?: Array<BooksAPITransactionAttachment> | null;
  cardLastFourDigits?: string | null;
  categorizationLines: Array<BooksAPITransactionCategorizationLine>;
  categorizationMethod?: BooksAPITransactionCategorizationMethod | null;
  counterpartyName?: string | null;
  customCategoryId?: string | null;
  customCategoryName?: string | null;
  datetime: string;
  description: string;
  id: string;
  journalEntryId?: string | null;
  ledgerId?: string | null;
  lineEntryId?: string | null;
  merchantType?: string | null;
  note?: string | null;
  personal: boolean;
  postedStatus: BooksTransactionPostedStatus;
  reviewStatus: BooksTransactionReviewStatus;
  sourceAccountId: string;
  teamMemberId?: string | null;
  teamMemberName?: string | null;
  transactionMethodKind?: TransactionMethodKind | null;
}

export interface BooksAPITransactionAttachment {
  downloadUrl: string;
  fileName: string;
  id: string;
}

export interface BooksAPITransactionCategorizationLine {
  amount: number;
  debitCredit: BooksDebitCredit;
  ledgerId: string;
  ledgerName: string;
  lineEntryId: string;
}

export type BooksAPITransactionCategorizationMethod =
  'ai' | 'rules' | 'similarity' | 'transferBetweenAccounts' | 'uncategorized' | 'user';

export interface BooksAPIUpdateJournalEntryChanges {
  create?: Array<BooksAPIUpdateJournalEntryLECreate> | null;
  _delete?: Array<string> | null;
  update?: Array<BooksAPIUpdateJournalEntryLEUpdate> | null;
}

export interface BooksAPIUpdateJournalEntryLECreate {
  amount: number;
  debitCredit: BooksDebitCredit;
  description: string;
  ledgerId: string;
  sortOrder?: number | null;
  tagIds?: Array<string> | null;
}

export interface BooksAPIUpdateJournalEntryLEUpdate {
  amount?: number | null;
  debitCredit?: BooksDebitCredit | null;
  description?: string | null;
  id: string;
  ledgerId?: string | null;
  sortOrder?: number | null;
  tagIds?: Array<string> | null;
}

export interface BooksAPIUpdateLedgerResult {
  error?: BooksAPILedgerWriteError | null;
  ledger?: BooksAPILedger | null;
}

export interface BooksAccrualSourceBaseResponse {
  amountOutstanding: number;
  amountPaid: number;
  displayStatus: BooksAccrualSourceDisplayStatus;
  dueDate?: string | null;
  effectiveDate: string;
  externalId?: string | null;
  externalPartyId?: BooksExternalPartyId | null;
  grossAmount: number;
  id: string;
  lines?: Array<BooksAccrualSourceLine> | null;
  notes?: string | null;
  referenceNumber?: string | null;
  status: BooksAccrualSourceStatus;
  type: BooksAccrualSourceBaseResponseTypeEnum;
}

export type BooksAccrualSourceBaseResponseTypeEnum = 'invoice' | 'bill' | 'payroll';

export type BooksAccrualSourceDisplayStatus =
  'open' | 'paid' | 'draft' | 'cancelled' | 'overdue' | 'partiallyPaid' | 'processing';

export interface BooksAccrualSourceFile {
  fileName: string;
  id: string;
}

export interface BooksAccrualSourceLine {
  accountId: string;
  accrualSourceId: string;
  amount: number;
  description: string;
  externalId?: string | null;
  id: string;
  lineNumber: number;
}

export interface BooksAccrualSourcePaymentApplication {
  adjustments: Array<BooksPaymentApplicationAccrualAdjustment>;
  lineEntry: BooksAccrualSourcePaymentApplicationLineEntry;
  matchedAmount: number;
  paymentApplicationId: string;
  sourceType: BooksAccrualSourcePaymentApplicationSourceTypeEnum;
  status: BooksAccrualSourcePaymentApplicationStatusEnum;
}

export type BooksAccrualSourcePaymentApplicationSourceTypeEnum = 'bankTransaction' | 'customerCredit' | 'manual';

export type BooksAccrualSourcePaymentApplicationStatusEnum = 'proposed' | 'confirmed' | 'rejected';

export interface BooksAccrualSourcePaymentApplicationLineEntry {
  journalEntryDescription: string;
  journalEntryId: string;
  lineEntryAmount: number;
  lineEntryDescription: string;
  lineEntryId: string;
}

export interface BooksAccrualSourceResponse {
  amountOutstanding: number;
  amountPaid: number;
  billPayInvoiceAttachment?: BooksBillPayInvoiceAttachment | null;
  displayStatus: BooksAccrualSourceDisplayStatus;
  dueDate?: string | null;
  effectiveDate: string;
  externalId?: string | null;
  externalPartyId?: BooksExternalPartyId | null;
  files?: Array<BooksAccrualSourceFile> | null;
  grossAmount: number;
  id?: string | null;
  journalEntryIds: Array<string>;
  lines?: Array<BooksAccrualSourceLine> | null;
  needsActionReason?: BooksNeedsActionReason | null;
  notes?: string | null;
  paymentApplications?: Array<BooksAccrualSourcePaymentApplication> | null;
  referenceNumber?: string | null;
  status: BooksAccrualSourceStatus;
  type: BooksAccrualSourceResponseTypeEnum;
  unappliedPayments?: Array<BooksAccrualSourceUnappliedPayment> | null;
}

export type BooksAccrualSourceResponseTypeEnum = 'invoice' | 'bill' | 'payroll';

export type BooksAccrualSourceStatus = 'open' | 'paid' | 'draft' | 'cancelled' | 'processing';

export interface BooksAccrualSourceUnappliedPayment {
  amount: number;
  needsActionReason: BooksNeedsActionReason;
}

export type BooksAutocatMethod =
  'rule' | 'transactionKindDefaults' | 'similarity' | 'embedding' | 'llmClassifier' | 'transfersBetweenAccounts';

export interface BooksAutocatResult {
  confidence: number;
  createdAt: string;
  id: string;
  ledgerId: string;
  method: BooksAutocatMethod;
  ruleId?: string | null;
}

export interface BooksBillPayInvoiceAttachment {
  downloadUrl: string;
  fileName: string;
  id: string;
}

export type BooksCategorizerType = 'aI' | 'rules' | 'similarity' | 'transferBetweenAccounts' | 'uncategorized' | 'user';

export type BooksDebitCredit = 'debit' | 'credit';

export type BooksExternalPartyId = BooksExternalPartyIdCounterpartyId | BooksExternalPartyIdCustomerId;

export interface BooksExternalPartyIdCounterpartyId {
  contents: string;
  tag: BooksExternalPartyIdCounterpartyIdTagEnum;
}

export type BooksExternalPartyIdCounterpartyIdTagEnum = 'counterpartyId';

export interface BooksExternalPartyIdCustomerId {
  contents: string;
  tag: BooksExternalPartyIdCustomerIdTagEnum;
}

export type BooksExternalPartyIdCustomerIdTagEnum = 'customerId';

export type BooksFinancialAccountType =
  | 'bankAccount'
  | 'creditCard'
  | 'payments'
  | 'payroll'
  | 'loan'
  | 'prepaidCard'
  | 'accountsReceivable'
  | 'accountsPayable'
  | 'investment'
  | 'treasury';

export interface BooksJournalEntry {
  accrualSource?: BooksAccrualSourceResponse | null;
  autocatResult?: BooksAutocatResult | null;
  categorizationStatus: BooksJournalEntryCategorizationStatus;
  creationDate: string;
  creationSource: BooksJournalEntryCreationSource;
  datetime: string;
  description: string;
  id: string;
  isOpeningBalance: boolean;
  lineEntries?: Array<BooksLineEntry> | null;
  lineEntryIds?: Array<string> | null;
  reviewStatus: BooksJournalEntryReviewStatus;
  reviewStatusSetAt?: string | null;
  transfer?: BooksTransfer | null;
}

export type BooksJournalEntryCategorizationStatus = 'pending' | 'delayed' | 'completed' | 'notAttempted';

export type BooksJournalEntryCreationSource = 'manual' | 'transaction' | 'accrual' | 'paymentApplication' | 'legacy';

export type BooksJournalEntryReviewStatus = 'unreviewed' | 'reviewed';

export type BooksLedgerClearField = 'parentId';

export type BooksLedgerSubType =
  | 'currentAssets'
  | 'nonCurrentAssets'
  | 'transfersBetweenAccounts'
  | 'uncategorizedAssets'
  | 'currentLiabilities'
  | 'nonCurrentLiabilities'
  | 'equity'
  | 'operatingRevenues'
  | 'otherIncome'
  | 'costOfGoodsSold'
  | 'operatingExpenses'
  | 'otherExpenses'
  | 'retainedEarnings';

export type BooksLedgerType = 'asset' | 'liability' | 'equity' | 'revenue' | 'expense';

export interface BooksLineEntry {
  accrualSource?: BooksAccrualSourceBaseResponse | null;
  amount: number;
  categorizationStatus: BooksJournalEntryCategorizationStatus;
  datetime: string;
  debitCredit: BooksDebitCredit;
  description?: string | null;
  editable: boolean;
  id: string;
  journalEntryDescription: string;
  journalEntryId: string;
  ledgerId: string;
  ledgerName: string;
  opposingLedgerIds?: Array<string> | null;
  paymentApplications?: Array<BooksLineEntryPaymentApplication> | null;
  relatedLineEntryId?: string | null;
  sortOrder?: number | null;
  tags?: Array<BooksTag> | null;
  transaction?: BooksTransaction | null;
  transactionId?: string | null;
}

export interface BooksLineEntryLinePaymentApplication {
  accrualSource: BooksLineEntryLinePaymentApplicationAccrualSource;
  linePaymentApplicationId: string;
  matchedAmount: number;
  sourceType: BooksLineEntryLinePaymentApplicationSourceTypeEnum;
  status: BooksLineEntryLinePaymentApplicationStatusEnum;
}

export type BooksLineEntryLinePaymentApplicationSourceTypeEnum = 'bankTransaction' | 'customerCredit' | 'manual';

export type BooksLineEntryLinePaymentApplicationStatusEnum = 'proposed' | 'confirmed' | 'rejected';

export interface BooksLineEntryLinePaymentApplicationAccrualSource {
  accrualSourceId: string;
  endDate: string;
  startDate: string;
  type: BooksLineEntryLinePaymentApplicationAccrualSourceTypeEnum;
}

export type BooksLineEntryLinePaymentApplicationAccrualSourceTypeEnum = 'payroll';

export type BooksLineEntryPaymentApplication =
  BooksLineEntryLinePaymentApplication | BooksLineEntryPaymentApplicationSource;

export interface BooksLineEntryPaymentApplicationAccrualSource {
  accrualSourceId: string;
  effectiveDate: string;
  externalId?: string | null;
  externalPartyId?: BooksExternalPartyId | null;
  grossAmount: number;
  referenceNumber?: string | null;
  type: BooksLineEntryPaymentApplicationAccrualSourceTypeEnum;
}

export type BooksLineEntryPaymentApplicationAccrualSourceTypeEnum = 'invoice' | 'bill' | 'payroll';

export interface BooksLineEntryPaymentApplicationSource {
  accrualSource?: BooksLineEntryPaymentApplicationAccrualSource | null;
  adjustments: Array<BooksPaymentApplicationAccrualAdjustment>;
  matchedAmount: number;
  paymentApplicationId: string;
  sourceType: BooksLineEntryPaymentApplicationSourceSourceTypeEnum;
  status: BooksLineEntryPaymentApplicationSourceStatusEnum;
}

export type BooksLineEntryPaymentApplicationSourceSourceTypeEnum = 'bankTransaction' | 'customerCredit' | 'manual';

export type BooksLineEntryPaymentApplicationSourceStatusEnum = 'proposed' | 'confirmed' | 'rejected';

export type BooksNeedsActionReason =
  | 'transactionNotInTeal'
  | 'transactionAmountExceedsInvoiceBalance'
  | 'transactionAmountDoesNotCoverInvoices'
  | 'sourceAccountNotMapped'
  | 'transactionPredatesBooksStartDate'
  | 'transactionAppliedToOtherInvoices'
  | 'cardChargeStripeNotConnected'
  | 'cardChargeStripeSetupPending';

export interface BooksPaymentApplicationAccrualAdjustment {
  accrualAdjustmentId: string;
  amount: number;
  creditAccountId: string;
  debitAccountId: string;
}

export type BooksRequiredLedgerPurpose =
  | 'uncatInflow'
  | 'uncatOutflow'
  | 'accountTransfers'
  | 'openingBalances'
  | 'accountsReceivable'
  | 'accountsPayable'
  | 'wagesExpense'
  | 'bonusExpense'
  | 'commissionsExpense'
  | 'contractorExpense'
  | 'employeeReimbursements'
  | 'severanceExpense'
  | 'payrollTaxExpense'
  | 'employerBenefitsExpense'
  | 'healthInsuranceExpense'
  | 'wagesPayable'
  | 'payrollTaxPayable'
  | 'employeeBenefitLiabilities'
  | 'payrollLiabilities'
  | 'payrollAdjustmentsClearing'
  | 'retainedEarnings'
  | 'currentYearEarnings'
  | 'benefitsExpense'
  | 'donationsExpense'
  | 'benefitsPayable'
  | 'payrollTaxAccruals'
  | 'stockExerciseClearing'
  | 'payrollClearing';

export interface BooksTag {
  id: string;
  name: string;
  tagGroupId: string;
}

export interface BooksTransaction {
  amount: number;
  attachments?: Array<BooksTransactionAttachment> | null;
  cardLastFourDigits?: string | null;
  categorizationMethod?: BooksCategorizerType | null;
  counterpartyName?: string | null;
  customCategoryId?: string | null;
  customCategoryName?: string | null;
  datetime: string;
  description: string;
  externalMetadataId?: string | null;
  id: string;
  journalEntryId?: string | null;
  ledgerId?: string | null;
  lineEntryId?: string | null;
  merchantType?: MercuryCategoryWithDisplay | null;
  note?: string | null;
  opposingLineEntryIds?: Array<string> | null;
  personal: boolean;
  postedStatus: BooksTransactionPostedStatus;
  reviewStatus: BooksTransactionReviewStatus;
  sourceAccountId: string;
  teamMemberId?: string | null;
  teamMemberName?: string | null;
  transactionMethodKind?: TransactionMethodKind | null;
}

export interface BooksTransactionAttachment {
  downloadUrl: string;
  fileName: string;
  id: string;
}

export type BooksTransactionPostedStatus = 'notPosted' | 'posted' | 'deleted';

export type BooksTransactionReviewStatus = 'reviewed' | 'unreviewed';

export interface BooksTransfer {
  fromEntry: BooksTransferEntry;
  toEntry: BooksTransferEntry;
}

export interface BooksTransferEntry {
  datetime: string;
  description: string;
  journalEntryId: string;
  lineEntries: Array<BooksLineEntry>;
}

export interface Card {
  accountId: string;
  budgets: Array<CardBudget>;
  categoryLocks: Array<MercuryCategory>;
  createdAt: string;
  expiration: CardExpiration;
  id: string;
  isAgentCard: boolean;
  isSingleUse: boolean;
  kind: CardKind;
  lastFour: string;
  merchantLock?: MerchantInfo | null;
  nameOnCard: string;
  nickname?: string | null;
  physicalCardStatus?: PhysicalCardStatus | null;
  spendLimit?: SpendLimit | null;
  spendLimitType: SpendLimitType;
  status: CardStatus;
  type: CardType;
  updatedAt: string;
  userId: string;
}

export interface CardBudget {
  amountCents: number;
  id: string;
  name: string;
  remainingAmountCents: number;
}

export interface CardConfiguration {
  singleUse: boolean;
}

export interface CardExpiration {
  month: number;
  year: number;
}

export type CardKind = 'debit' | 'credit';

export interface CardListResponse {
  cards: Array<Card>;
  page: CardListResponsePage;
}

export interface CardListResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type CardNetwork = 'visa' | 'mastercard';

export interface CardRevealResponse {
  cardNumber: string;
  cvc: string;
  expiration: CardExpiration;
}

export interface CardSpendManagementState {
  agenticCardState?: AgenticCardState | null;
  isSingleUse: boolean;
}

export type CardStatus = 'active' | 'frozen' | 'cancelled' | 'inactive' | 'expired' | 'suspended' | 'singleUseConsumed';

export type CardType = 'virtual' | 'physical';

export interface CategoriesPaginatedResponse {
  categories: Array<CategoryData>;
  page: CategoriesPaginatedResponsePage;
}

export interface CategoriesPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface CategorizeBooksAPITransactionsRequest {
  items: Array<BooksAPICategorizeTransactionItem>;
}

export interface CategorizeBooksAPITransactionsResponse {
  items: Array<BooksAPICategorizedTransaction>;
}

export interface CategoryData {
  id: string;
  name: string;
  visibleForCardSpend: boolean;
  visibleForOther: boolean;
  visibleForReimbursements: boolean;
}

export interface CheckInfo {
  address: AddressWithoutName;
}

export interface CheckInfoRaw {
  address: AddressWithoutName;
}

export type CitizenshipStatus = 'USCitizen' | 'USResident' | 'NonResident';

export interface CreateBooksAPIBillLine {
  amount: number;
  description: string;
  ledgerId: string;
}

export interface CreateBooksAPIBillRequest {
  dueDate: string;
  effectiveDate: string;
  lines: Array<CreateBooksAPIBillLine>;
  notes?: string | null;
  referenceNumber?: string;
  vendor: CreateBooksAPIBillVendor;
}

export type CreateBooksAPIBillVendor = CreateBooksAPIBillVendorCounterpartyId | CreateBooksAPIBillVendorRecipientId;

export interface CreateBooksAPIBillVendorCounterpartyId {
  contents: string;
  tag: CreateBooksAPIBillVendorCounterpartyIdTagEnum;
}

export type CreateBooksAPIBillVendorCounterpartyIdTagEnum = 'counterpartyId';

export interface CreateBooksAPIBillVendorRecipientId {
  contents: string;
  tag: CreateBooksAPIBillVendorRecipientIdTagEnum;
}

export type CreateBooksAPIBillVendorRecipientIdTagEnum = 'recipientId';

export interface CreateBooksAPICategorizationRuleRequest {
  conditions: Array<BooksAPICategorizationRuleCondition>;
  outputs: Array<BooksAPICategorizationRuleOutput>;
}

export interface CreateBooksAPICategorizationRuleResponse {
  rule: BooksAPICategorizationRule;
}

export interface CreateBooksAPIInvoiceLine {
  amount: number;
  description: string;
  ledgerId: string;
}

export interface CreateBooksAPIInvoiceRequest {
  customer: string;
  dueDate: string;
  effectiveDate: string;
  lines: Array<CreateBooksAPIInvoiceLine>;
  notes?: string | null;
  referenceNumber: string;
}

export interface CreateBooksAPIJournalEntriesBulkResponse {
  journalEntries: Array<BooksJournalEntry>;
}

export interface CreateBooksAPIJournalEntryRequest {
  datetime: string;
  description: string;
  lineEntries: Array<BooksAPICreateJournalEntryLineEntry>;
}

export interface CreateBooksAPILedger {
  debitCredit: BooksDebitCredit;
  name: string;
  parentId?: string | null;
  sortCode: string;
  subType: BooksLedgerSubType;
  type: BooksLedgerType;
}

export interface CreateBooksAPILedgersRequest {
  ledgers: Array<CreateBooksAPILedger>;
}

export interface CreateBooksAPILedgersResponse {
  failedCount: number;
  results: Array<BooksAPICreateLedgerResult>;
  succeededCount: number;
}

export interface CreateCardRequest {
  accountId?: string | null;
  cardConfiguration?: CardConfiguration | null;
  kind: CardKind;
  nickname?: string | null;
  spendLimit?: CreateSpendLimit | null;
  type: CreateCardType;
  userId: string;
}

export type CreateCardType = 'virtual';

export interface CreateCategoryApiRequest {
  name: string;
  visibleForCardSpend: boolean;
  visibleForOther: boolean;
  visibleForReimbursements: boolean;
}

export interface CreateRecipientInviteApiRequest {
  contactEmail: string;
  name?: string | null;
  notes?: string | null;
  organizationNameOnRequest?: string | null;
  paymentMethods: Array<PaymentMethod>;
  recipientId?: string | null;
  requireTaxDocument: boolean;
  sendEmail: boolean;
}

export interface CreateSpendLimit {
  amountCents: number;
  interval: SpendLimitInterval;
}

export interface CreateWebhookParams {
  eventTypes?: Array<WebhookEventType> | null;
  filterPaths?: Array<ResourceField> | null;
  url: string;
}

export interface CreditAccount {
  availableBalance: number;
  createdAt: string;
  currentBalance: number;
  id: string;
  status: AccountStatus;
}

export interface CreditAccountStatementPayload {
  creditLimit: number;
  creditPeriodId: string;
  dueDate: string;
  startingBalance: number;
  totalAutopayPayments: number;
  totalCashbackEarned: number;
  totalOneTimePayments: number;
  totalTransactions: number;
}

export interface CreditAccountStatementsPaginatedResponse {
  page: CreditAccountStatementsPaginatedResponsePage;
  statements: Array<AccountStatement>;
}

export interface CreditAccountStatementsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface CreditAccountsResponse {
  accounts: Array<CreditAccount>;
}

export interface CreditCardInfo {
  email?: string | null;
  id: string;
  paymentMethod: string;
}

export interface CurrencyExchangeInfo {
  convertedFromAmount: number;
  convertedFromCurrency: string;
  convertedToAmount: number;
  convertedToCurrency: string;
  exchangeRate: number;
  feeAmount: number;
  feePercentage: number;
  feeTransactionId?: string | null;
}

export interface DebitCardInfo {
  id: string;
}

export interface DeleteBooksAPIJournalEntriesRequest {
  journalEntryIds: Array<string>;
}

export interface DeleteBooksAPILedgersRequest {
  ledgerIds: Array<string>;
}

export interface DeleteBooksAPILedgersResponse {
  failedCount: number;
  results: Array<BooksAPIDeleteLedgerResult>;
  succeededCount: number;
}

export interface DepositoryAccountStatement {
  accountNumber: string;
  companyLegalAddress: Address;
  companyLegalName: string;
  downloadUrl: string;
  ein?: string | null;
  endDate: string;
  endingBalance: number;
  id: string;
  routingNumber: string;
  startDate: string;
  transactions: Array<AccountStatementTransaction>;
}

export interface DepositoryAccountStatementPayload {
  accountNumber: string;
  routingNumber: string;
}

export interface DepositoryAccountStatementsPaginatedResponse {
  page: CreditAccountStatementsPaginatedResponsePage;
  statements: Array<DepositoryAccountStatement>;
}

export interface DomesticWireRoutingInfo {
  accountNumber: string;
  address?: AddressWithoutName | null;
  bankName?: string | null;
  routingNumber: string;
}

export interface DomesticWireRoutingInfoRaw {
  accountNumber: string;
  address: AddressWithoutName;
  routingNumber: string;
}

export interface EditCategoryApiRequest {
  name?: string | null;
  visibleForCardSpend?: boolean | null;
  visibleForOther?: boolean | null;
  visibleForReimbursements?: boolean | null;
}

export interface EditRecipientRequest {
  address?: AddressData;
  checkInfo?: CheckInfoRaw;
  contactEmail?: string;
  domesticWireRoutingInfo?: DomesticWireRoutingInfoRaw;
  electronicRoutingInfo?: ElectronicRoutingInfoRaw;
  emails?: Array<string>;
  name?: string;
  nickname?: string;
  realTimePaymentRoutingInfo?: RealTimePaymentRoutingInfoRaw;
}

export type ElectronicAccountType =
  | 'businessChecking'
  | 'businessSavings'
  | 'personalChecking'
  | 'personalSavings'
  | 'businessGeneralLedger'
  | 'personalGeneralLedger'
  | 'businessLoan'
  | 'personalLoan';

export interface ElectronicRoutingInfo {
  accountNumber: string;
  address?: AddressWithoutName | null;
  bankName?: string | null;
  electronicAccountType: ElectronicAccountType;
  routingNumber: string;
}

export interface ElectronicRoutingInfoRaw {
  accountNumber: string;
  address: AddressWithoutName;
  electronicAccountType: ElectronicAccountType;
  routingNumber: string;
}

export interface GetBooksAPIBillResponse {
  bill: BooksAPIBill;
}

export interface GetBooksAPIBillsResponse {
  bills: Array<BooksAPIBill>;
  nextPageToken?: string | null;
  prevPageToken?: string | null;
}

export interface GetBooksAPICategorizationRulesResponse {
  nextPageToken?: string | null;
  rules: Array<BooksAPICategorizationRule>;
}

export interface GetBooksAPIInstancesResponse {
  instances: Array<BooksAPIInstance>;
  nextPageToken?: string | null;
}

export interface GetBooksAPIInvoicesResponse {
  invoices: Array<BooksAPIInvoice>;
  nextPageToken?: string | null;
  prevPageToken?: string | null;
}

export interface GetBooksAPIJournalEntriesResponse {
  journalEntries: Array<BooksJournalEntry>;
  nextPageToken?: string | null;
  prevPageToken?: string | null;
}

export interface GetBooksAPIJournalEntryResponse {
  journalEntry: BooksJournalEntry;
}

export interface GetBooksAPILedgerBalancesResponse {
  ledgerBalances: Array<BooksAPILedgerBalance>;
}

export interface GetBooksAPILedgerResponse {
  ledger: BooksAPILedger;
}

export interface GetBooksAPILedgersResponse {
  ledgers: Array<BooksAPILedger>;
  nextPageToken?: string | null;
  prevPageToken?: string | null;
}

export interface GetBooksAPILineEntriesResponse {
  lineEntries: Array<BooksAPILineEntry>;
  nextPageToken?: string | null;
  prevPageToken?: string | null;
}

export interface GetBooksAPISourceAccountsResponse {
  sourceAccounts: Array<BooksAPISourceAccount>;
}

export interface GetBooksAPITransactionResponse {
  transaction: BooksAPITransaction;
}

export interface GetBooksAPITransactionsResponse {
  nextPageToken?: string | null;
  prevPageToken?: string | null;
  transactions: Array<BooksAPITransaction>;
}

export interface GlAllocation {
  amount: number;
  className?: string | null;
  departmentName?: string | null;
  description?: string | null;
  glCodeName: string;
}

export type IdentificationType =
  | 'Passport'
  | 'DriversLicense'
  | 'StateID'
  | 'AlienRegistrationCard'
  | 'EmployeeAuthorizationDocument'
  | 'VerifiedByThirdParty'
  | 'NationalID'
  | 'ResidencePermit'
  | 'Visa';

export interface InternalTransferAPIRequest {
  amount: number;
  destinationAccountId: string;
  idempotencyKey: string;
  note?: string | null;
  sourceAccountId: string;
}

export interface InternalTransferAPIResponse {
  creditTransaction: Transaction;
  debitTransaction: Transaction;
}

export interface InternationalWireAustraliaSpecificData {
  bsbCode: string;
}

export interface InternationalWireBrazilSpecificData {
  legalId: string;
}

export interface InternationalWireCanadaSpecificData {
  bankCode: string;
  transitNumber: string;
}

export interface InternationalWireChileSpecificData {
  legalId: string;
}

export interface InternationalWireColombiaSpecificData {
  legalId: string;
}

export interface InternationalWireCorrespondentInfo {
  bankName?: string | null;
  routingNumber?: string | null;
  swiftCode?: string | null;
}

export interface InternationalWireCountrySpecificData {
  australia?: InternationalWireAustraliaSpecificData | null;
  brazil?: InternationalWireBrazilSpecificData | null;
  canada?: InternationalWireCanadaSpecificData | null;
  chile?: InternationalWireChileSpecificData | null;
  colombia?: InternationalWireColombiaSpecificData | null;
  dominicanRepublic?: InternationalWireDominicanRepublicSpecificData | null;
  honduras?: InternationalWireHondurasSpecificData | null;
  india?: InternationalWireIndiaSpecificData | null;
  kazakhstan?: InternationalWireKazakhstanSpecificData | null;
  pakistan?: InternationalWirePakistanSpecificData | null;
  paraguay?: InternationalWireParaguaySpecificData | null;
  philippines?: InternationalWirePhilippinesSpecificData | null;
  russia?: InternationalWireRussiaSpecificData | null;
  southAfrica?: InternationalWireSouthAfricaSpecificData | null;
}

export interface InternationalWireDominicanRepublicSpecificData {
  accountType: SwiftBankAccountType;
  legalId: string;
}

export interface InternationalWireHondurasSpecificData {
  accountType: SwiftBankAccountType;
  legalId: string;
}

export interface InternationalWireIndiaSpecificData {
  ifscCode: string;
}

export interface InternationalWireKazakhstanSpecificData {
  legalId: string;
}

export interface InternationalWirePakistanSpecificData {
  legalId: string;
  legalIdType: PakistaniLegalIdType;
}

export interface InternationalWireParaguaySpecificData {
  legalId: string;
}

export interface InternationalWirePhilippinesSpecificData {
  routingNumber: string;
}

export interface InternationalWireRoutingInfo {
  address?: AddressWithoutName | null;
  bankDetails?: SwiftCodeData | null;
  correspondentInfo?: InternationalWireCorrespondentInfo | null;
  countrySpecific: InternationalWireCountrySpecificData;
  emailAddress?: string | null;
  iban: string;
  phoneNumber?: string | null;
  swiftCode: string;
}

export interface InternationalWireRussiaSpecificData {
  inn: string;
}

export interface InternationalWireSouthAfricaSpecificData {
  branchCode: string;
}

export interface InvestAccount {
  availableBalance: number;
  createdAt: string;
  currentBalance: number;
  id: string;
  status: AccountStatus;
}

export interface InvestAccountsPaginatedResponse {
  accounts: Array<InvestAccount>;
  page: AccountsPaginatedResponsePage;
}

export interface InvestActivityCredit {
  amount: number;
}

export interface InvestActivityDividend {
  amount: number;
  security: string;
}

export interface InvestActivityFee {
  amount: number;
  status: InvestActivityStatus;
}

export interface InvestActivityInterestPayment {
  amount: number;
}

export interface InvestActivityItem {
  day: string;
  details: InvestActivityPayload;
}

export type InvestActivityPayload =
  | InvestActivityPayloadCredit
  | InvestActivityPayloadDividend
  | InvestActivityPayloadFee
  | InvestActivityPayloadInterestPayment
  | InvestActivityPayloadPortfolioChange
  | InvestActivityPayloadTrade
  | InvestActivityPayloadTransfer;

export interface InvestActivityPayloadCredit {
  contents: InvestActivityCredit;
  kind: InvestActivityPayloadCreditKindEnum;
}

export type InvestActivityPayloadCreditKindEnum = 'credit';

export interface InvestActivityPayloadDividend {
  contents: InvestActivityDividend;
  kind: InvestActivityPayloadDividendKindEnum;
}

export type InvestActivityPayloadDividendKindEnum = 'dividend';

export interface InvestActivityPayloadFee {
  contents: InvestActivityFee;
  kind: InvestActivityPayloadFeeKindEnum;
}

export type InvestActivityPayloadFeeKindEnum = 'fee';

export interface InvestActivityPayloadInterestPayment {
  contents: InvestActivityInterestPayment;
  kind: InvestActivityPayloadInterestPaymentKindEnum;
}

export type InvestActivityPayloadInterestPaymentKindEnum = 'interestPayment';

export interface InvestActivityPayloadPortfolioChange {
  contents: InvestActivityPortfolioChange;
  kind: InvestActivityPayloadPortfolioChangeKindEnum;
}

export type InvestActivityPayloadPortfolioChangeKindEnum = 'portfolioChange';

export interface InvestActivityPayloadTrade {
  contents: InvestActivityTrade;
  kind: InvestActivityPayloadTradeKindEnum;
}

export type InvestActivityPayloadTradeKindEnum = 'trade';

export interface InvestActivityPayloadTransfer {
  contents: InvestActivityTransfer;
  kind: InvestActivityPayloadTransferKindEnum;
}

export type InvestActivityPayloadTransferKindEnum = 'transfer';

export interface InvestActivityPortfolioChange {
  from: string;
  status: InvestActivityStatus;
  to: string;
}

export interface InvestActivityResponse {
  activity: Array<InvestActivityItem>;
}

export type InvestActivityStatus = 'pending' | 'canceled' | 'failed' | 'complete';

export interface InvestActivityTrade {
  action: InvestActivityTradeAction;
  price: number;
  quantity: string;
  security: string;
  status: InvestActivityStatus;
  total: number;
}

export type InvestActivityTradeAction = 'buy' | 'sell';

export interface InvestActivityTransfer {
  amount: number;
  counterpartyId: string;
  counterpartyName: string;
  isAutomated: boolean;
  kind: InvestActivityTransferKind;
  postedAt?: string | null;
  status: InvestActivityStatus;
  transactionId: string;
}

export type InvestActivityTransferKind = 'investment' | 'liquidation';

export type IsPep = 'IsPep' | 'IsNotPep';

export type MainQuestionnaireCompanyStructure =
  | 'CCorp'
  | 'LLC'
  | 'LLP'
  | 'NonProfit'
  | 'Partnership'
  | 'ProfessionalAssociation'
  | 'ProfessionalCorporation'
  | 'SCorp'
  | 'GeneralPartnership'
  | 'LimitedPartnership'
  | 'JointVenture'
  | 'LLCTaxedAsSoleProprietorship'
  | 'SoleProprietorship'
  | 'ExemptedCompany'
  | 'Limited';

export type MainQuestionnaireEntityFormationDocumentType =
  | 'ArticlesOfIncorporation'
  | 'ArticlesOfOrganization'
  | 'CertificateOfFormation'
  | 'PartnershipAgreement'
  | 'SecretaryOfStateRegistrationPage';

export interface McpAgentFeedbackRequest {
  attempted?: string;
  category: McpAgentFeedbackRequestCategoryEnum;
  expected?: string;
  impact: McpAgentFeedbackRequestImpactEnum;
  mcpClientName?: string;
  mcpClientVersion?: string;
  mcpSessionId?: string;
  summary: string;
  toolName?: string;
}

export type McpAgentFeedbackRequestCategoryEnum =
  'unclear_schema' | 'tool_error' | 'unexpected_result' | 'missing_capability' | 'suggestion';

export type McpAgentFeedbackRequestImpactEnum = 'blocked' | 'degraded' | 'minor';

export interface McpAgentFeedbackResponse {
  id: string;
}

export interface MerchantData {
  amount?: number | null;
  category?: MercuryCategory | null;
  categoryCode?: string | null;
  currency?: string | null;
  id?: string | null;
}

export interface MerchantInfo {
  id: string;
  name: string;
}

export interface MerchantsResponse {
  data: Array<MerchantInfo>;
  page: MerchantsResponsePage;
}

export interface MerchantsResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type MercuryCategory =
  | 'Other'
  | 'Advertising'
  | 'Airlines'
  | 'AlcoholAndBars'
  | 'BooksAndNewspaper'
  | 'CarRental'
  | 'Charity'
  | 'Clothing'
  | 'Conferences'
  | 'Education'
  | 'Electronics'
  | 'Entertainment'
  | 'FacilitiesExpenses'
  | 'Fees'
  | 'FoodDelivery'
  | 'FuelAndGas'
  | 'Gambling'
  | 'GovernmentServices'
  | 'Grocery'
  | 'GroundTransportation'
  | 'Insurance'
  | 'InternetAndTelephone'
  | 'Legal'
  | 'Lodging'
  | 'Medical'
  | 'Memberships'
  | 'OfficeSupplies'
  | 'OtherTravel'
  | 'Parking'
  | 'Political'
  | 'ProfessionalServices'
  | 'Restaurants'
  | 'Retail'
  | 'RideshareAndTaxis'
  | 'Shipping'
  | 'Software'
  | 'Taxes'
  | 'Utilities'
  | 'VehicleExpenses';

export interface MercuryCategoryWithDisplay {
  category: MercuryCategory;
  display: string;
  icon: StandardIcon;
}

export interface OrganizationDBA {
  dbaIsDefault: boolean;
  dbaName: string;
}

export interface OrganizationInfo {
  billingCadence: ApiBillingCadence;
  dbas: Array<OrganizationDBA>;
  ein?: string | null;
  id: string;
  kind: ApiOrganizationKind;
  legalBusinessName: string;
  subscriptionTier: ApiSubscriptionTier;
}

export interface OrganizationResponse {
  organization: OrganizationInfo;
}

export type PakistaniLegalIdType = 'CNIC' | 'SNIC' | 'Passport' | 'NTN';

export interface PaymentApprovalReview {
  reviewedAt: string;
  reviewerUserId: string;
  status: PaymentApprovalReviewStatus;
}

export type PaymentApprovalReviewStatus = 'approved' | 'rejected';

export type PaymentLinkStatus = 'Unpaid' | 'Paid' | 'Cancelled' | 'Processing';

export type PaymentMethod = 'ach' | 'check' | 'domesticWire' | 'internationalWire' | 'realTimePayment';

export type PhysicalCardStatus = 'inactive' | 'active' | 'locked';

export interface PostTransactionAPIRequest {
  amount: number;
  duplicateCheckOverride?: boolean;
  externalMemo?: string;
  idempotencyKey: string;
  note?: string;
  paymentMethod: PostTransactionPaymentMethod;
  purpose?: PostTransactionSendMoneyPurpose;
  recipientId: string;
}

export type PostTransactionPaymentMethod = 'ach' | 'check' | 'domesticWire' | 'realTimePayment';

export interface PostTransactionSendMoneyPurpose {
  simple?: SimplePurpose | null;
}

export interface RealTimePaymentRoutingInfo {
  accountNumber: string;
  address?: AddressWithoutName | null;
  bankName?: string | null;
  routingNumber: string;
}

export interface RealTimePaymentRoutingInfoRaw {
  accountNumber: string;
  address: AddressWithoutName;
  routingNumber: string;
}

export interface RecipientAttachment {
  fileName: string;
  formType?: TaxFormType | null;
  uploadedAt: string;
  url: string;
}

export interface RecipientAttachmentWithId {
  fileName: string;
  formType?: TaxFormType | null;
  id: string;
  recipientId: string;
  uploadedAt: string;
  url: string;
}

export interface RecipientInfo {
  address?: Address | null;
  attachments: Array<RecipientAttachment>;
  checkInfo?: CheckInfo | null;
  contactEmail?: string | null;
  dateLastPaid?: string | null;
  defaultAddress?: AddressWithoutName | null;
  defaultPaymentMethod: PaymentMethod;
  domesticWireRoutingInfo?: DomesticWireRoutingInfo | null;
  electronicRoutingInfo?: ElectronicRoutingInfo | null;
  emails: Array<string>;
  id: string;
  internationalWireRoutingInfo?: InternationalWireRoutingInfo | null;
  inviteId?: string | null;
  isBusiness?: boolean | null;
  name: string;
  nickname?: string | null;
  realTimePaymentRoutingInfo?: RealTimePaymentRoutingInfo | null;
  status: RecipientStatus;
}

export interface RecipientInviteApiPaginatedResponse {
  invites: Array<RecipientInviteApiResponse>;
  page: RecipientInviteApiPaginatedResponsePage;
}

export interface RecipientInviteApiPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface RecipientInviteApiResponse {
  contactEmail: string;
  createdAt: string;
  expiresAt?: string | null;
  id: string;
  name: string;
  notes?: string | null;
  onboardingUrl: string;
  paymentMethods: Array<PaymentMethod>;
  recipientId?: string | null;
  requireTaxDocument: boolean;
  status: RecipientInviteStatus;
}

export type RecipientInviteStatus = 'created' | 'completed' | 'expired' | 'declined';

export type RecipientStatus = 'active' | 'deleted';

export interface RecipientsAttachmentsPaginatedResponse {
  attachments: Array<RecipientAttachmentWithId>;
  page: RecipientsAttachmentsPaginatedResponsePage;
  total: number;
}

export interface RecipientsAttachmentsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface RecipientsPaginatedResponse {
  page: RecipientsPaginatedResponsePage;
  recipients: Array<RecipientInfo>;
  total: number;
}

export interface RecipientsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type ReimbursementPaymentStatus = 'pending' | 'initiated' | 'paid' | 'failed' | 'paidOutsideMercury';

export type ReimbursementReviewStatus = 'submitted' | 'updatesRequested' | 'approved' | 'denied' | 'canceled';

export interface RelatedTransactionData {
  accountId: string;
  amount: number;
  id: string;
  relationKind: TransactionRelationKind;
}

export type RequestSendMoneyPaymentMethod = 'ach' | 'check' | 'domesticWire' | 'internationalWire' | 'realTimePayment';

export type ResourceField =
  | 'transaction.amount'
  | 'transaction.bankDescription'
  | 'transaction.categoryData'
  | 'transaction.customCategory'
  | 'transaction.customCategory.id'
  | 'transaction.customCategory.name'
  | 'transaction.mercuryCategory'
  | 'transaction.estimatedDeliveryDate'
  | 'transaction.externalMemo'
  | 'transaction.failedAt'
  | 'transaction.note'
  | 'transaction.postedAt'
  | 'transaction.reasonForFailure'
  | 'transaction.status'
  | 'checkingAccount.availableBalance'
  | 'checkingAccount.currentBalance'
  | 'checkingAccount.inFlightBalance'
  | 'savingsAccount.availableBalance'
  | 'savingsAccount.currentBalance'
  | 'savingsAccount.inFlightBalance'
  | 'treasuryAccount.availableBalance'
  | 'treasuryAccount.currentBalance'
  | 'treasuryAccount.inFlightBalance'
  | 'investmentAccount.availableBalance'
  | 'investmentAccount.currentBalance'
  | 'investmentAccount.inFlightBalance'
  | 'creditAccount.availableBalance'
  | 'creditAccount.currentBalance'
  | 'creditAccount.inFlightBalance';

export type ReviewRequestStatus = 'pendingApproval' | 'approved' | 'rejected' | 'cancelled';

export type SafeRequestInvestorType =
  'SafeRequestInvestorTypeIndividual' | 'SafeRequestInvestorTypeVentureFund' | 'SafeRequestInvestorTypeOther';

export type SecurityIdType = 'cusip';

export interface SendMoneyAPIRequest {
  amount: number;
  chargeType?: SendMoneyAPIRequestChargeTypeEnum;
  duplicateCheckOverride?: boolean;
  externalMemo?: string;
  idempotencyKey: string;
  note?: string;
  paymentMethod: RequestSendMoneyPaymentMethod;
  purpose?: PostTransactionSendMoneyPurpose;
  recipientId: string;
}

export type SendMoneyAPIRequestChargeTypeEnum = 'ours' | 'shared';

export interface SendMoneyApprovalRequestResponse {
  accountId: string;
  amount: number;
  createdAt: string;
  memo?: string | null;
  numberOfApproversRequired?: number | null;
  paymentMethod: RequestSendMoneyPaymentMethod;
  recipientId: string;
  requestId: string;
  requestedByUserId: string;
  requesterMayApprove?: boolean | null;
  reviews: Array<PaymentApprovalReview>;
  scheduledSendDate?: string | null;
  status: ReviewRequestStatus;
}

export interface SendMoneyApprovalRequestsPaginatedResponse {
  page: SendMoneyApprovalRequestsPaginatedResponsePage;
  requests: Array<SendMoneyApprovalRequestResponse>;
}

export interface SendMoneyApprovalRequestsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface SetBooksAPILedgerOpeningBalance {
  balance: number;
  ledgerId: string;
}

export interface SetBooksAPILedgerOpeningBalancesRequest {
  openingBalances: Array<SetBooksAPILedgerOpeningBalance>;
}

export interface SetBooksAPILedgerOpeningBalancesResponse {
  failedCount: number;
  results: Array<BooksAPISetLedgerOpeningBalanceResult>;
  succeededCount: number;
}

export interface SimplePurpose {
  additionalInfo?: string;
  category: SimplePurposeCategoryEnum;
}

export type SimplePurposeCategoryEnum =
  | 'employee'
  | 'landlord'
  | 'vendor'
  | 'contractor'
  | 'subsidiary'
  | 'transferToMyExternalAccount'
  | 'familyMemberOrFriend'
  | 'forGoodsOrServices'
  | 'angelInvestment'
  | 'savingsOrInvestments'
  | 'expenses'
  | 'travel'
  | 'other';

export interface SpendLimit {
  amountCents: number;
  atmAmountCents?: number | null;
  interval: SpendLimitInterval;
}

export type SpendLimitInterval = 'daily' | 'weekly' | 'monthly' | 'yearly';

export type SpendLimitType = 'cardLimit' | 'budgets';

export type StandardIcon =
  | 'arrowsLeftRightIcon'
  | 'arrowsRotateIcon'
  | 'atomSimpleIcon'
  | 'ballotCheckIcon'
  | 'bankIcon'
  | 'bellConciergeIcon'
  | 'boltIcon'
  | 'bookOpenCoverIcon'
  | 'booksIcon'
  | 'boxIcon'
  | 'buildingIcon'
  | 'burgerIcon'
  | 'carIcon'
  | 'cartShoppingFastIcon'
  | 'carWrenchIcon'
  | 'chartLineUpIcon'
  | 'circleParkingIcon'
  | 'computerIcon'
  | 'creditCardIcon'
  | 'crownIcon'
  | 'envelopeOpenTextIcon'
  | 'faucetIcon'
  | 'fileInvoiceIcon'
  | 'fileInvoiceDollarIcon'
  | 'fingerprintIcon'
  | 'gasPumpIcon'
  | 'gavelIcon'
  | 'gearIcon'
  | 'giftIcon'
  | 'globeIcon'
  | 'graduationCapIcon'
  | 'handHoldingDollarIcon'
  | 'handshakeIcon'
  | 'headSideMedicalIcon'
  | 'heartIcon'
  | 'homeIcon'
  | 'idBadgeIcon'
  | 'keyIcon'
  | 'keynoteIcon'
  | 'landmarkFlagIcon'
  | 'laptopIcon'
  | 'laptopMobileIcon'
  | 'listCheckIcon'
  | 'lockIcon'
  | 'lockOpenIcon'
  | 'martiniGlassIcon'
  | 'masksTheaterIcon'
  | 'messagesIcon'
  | 'mobileIcon'
  | 'moneyBillTransferIcon'
  | 'moneyBillWaveIcon'
  | 'moneyCheckIcon'
  | 'mugSaucerIcon'
  | 'planeIcon'
  | 'planetRingedIcon'
  | 'receiptIcon'
  | 'rectanglesMixedIcon'
  | 'seedlingIcon'
  | 'shieldCheckIcon'
  | 'shieldHavedIcon'
  | 'shirtIcon'
  | 'shopIcon'
  | 'shoppingCartIcon'
  | 'signInIcon'
  | 'signOutIcon'
  | 'slotMachineIcon'
  | 'staplerIcon'
  | 'starsIcon'
  | 'sunBrightIcon'
  | 'taxiBusIcon'
  | 'taxiIcon'
  | 'towerBroadcastIcon'
  | 'trainIcon'
  | 'tvIcon'
  | 'userIcon'
  | 'userPlusIcon'
  | 'usersIcon'
  | 'utensilsIcon'
  | 'warningIcon'
  | 'wifiIcon'
  | 'wineGlassIcon'
  | 'wrenchIcon';

export type SwiftBankAccountType = 'checking' | 'savings';

export interface SwiftCodeData {
  bankCityState: string;
  bankCountry: string;
  bankName: string;
}

export type TaxFormType = 'w9' | 'w8BEN' | 'w8BENE' | 'unknown';

export interface Transaction {
  accountId: string;
  accountingStatus?: TransactionAccountingStatus | null;
  amount: number;
  attachments: Array<TransactionAttachment>;
  bankDescription?: string | null;
  cardId?: string | null;
  categoryData?: CategoryData | null;
  checkNumber?: string | null;
  compliantWithReceiptPolicy: boolean;
  counterpartyId: string;
  counterpartyName: string;
  counterpartyNickname?: string | null;
  createdAt: string;
  creditAccountPeriodId?: string | null;
  currencyExchangeInfo?: CurrencyExchangeInfo | null;
  dashboardLink: string;
  details?: TransactionMethodData | null;
  estimatedDeliveryDate: string;
  externalMemo?: string | null;
  failedAt?: string | null;
  feeId?: string | null;
  generalLedgerCodeName?: string | null;
  glAllocations: Array<GlAllocation>;
  hasGeneratedReceipt: boolean;
  id: string;
  kind: TransactionKind;
  merchant?: MerchantData | null;
  mercuryCategory?: MercuryCategory | null;
  note?: string | null;
  postedAt?: string | null;
  reasonForFailure?: string | null;
  relatedTransactions: Array<RelatedTransactionData>;
  requestId?: string | null;
  status: TransactionStatus;
  trackingNumber?: string | null;
}

export interface TransactionAccountingStatus {
  erroredAt?: string | null;
  excludedAt?: string | null;
  reviewedAt?: string | null;
  status: AccountingSyncStatus;
  syncStartedAt?: string | null;
  syncedAt?: string | null;
}

export interface TransactionAttachment {
  attachmentType: TransactionAttachmentType;
  fileName: string;
  url: string;
}

export type TransactionAttachmentType = 'checkImage' | 'receipt' | 'other';

export type TransactionKind =
  | 'externalTransfer'
  | 'internalTransfer'
  | 'outgoingPayment'
  | 'creditCardCredit'
  | 'creditCardTransaction'
  | 'debitCardCredit'
  | 'debitCardTransaction'
  | 'cardInternationalTransactionFee'
  | 'cardInternationalTransactionFeeRebate'
  | 'cardInternationalTransactionFeeReversal'
  | 'cardInternationalTransactionFeeRebateReversal'
  | 'incomingDomesticWire'
  | 'checkDeposit'
  | 'incomingInternationalWire'
  | 'treasuryTransfer'
  | 'currencyCloudReturn'
  | 'wireFee'
  | 'personalBankingSubscriptionFee'
  | 'billingEngineSubscriptionFee'
  | 'expenseReimbursement'
  | 'exogenousWireDrawdown'
  | 'interestPayment'
  | 'other';

export interface TransactionMethodData {
  address?: AddressData | null;
  creditCardInfo?: CreditCardInfo | null;
  debitCardInfo?: DebitCardInfo | null;
  domesticWireRoutingInfo?: DomesticWireRoutingInfo | null;
  electronicRoutingInfo?: ElectronicRoutingInfo | null;
  internationalWireRoutingInfo?: InternationalWireRoutingInfo | null;
}

export type TransactionMethodKind =
  | 'outgoingElectronicPayment'
  | 'outgoingCheckPayment'
  | 'endogenousOutgoingAchTransfer'
  | 'endogenousIncomingAchTransfer'
  | 'exogenousOutgoingAch'
  | 'exogenousIncomingAch'
  | 'incomingCredit'
  | 'outgoingCredit'
  | 'incomingDebit'
  | 'outgoingDebit'
  | 'internalTransfer'
  | 'incomingCheck'
  | 'outgoingInternationalWire'
  | 'incomingInternationalWire'
  | 'outgoingDomesticWire'
  | 'incomingDomesticWire'
  | 'wireFee'
  | 'conversionFee'
  | 'personalBankingSubscriptionFee'
  | 'billingEngineSubscriptionFee'
  | 'physicalCardUpgradeFee'
  | 'exogenousOutgoingCheck'
  | 'exogenousOutgoingWire'
  | 'treasuryTransfer'
  | 'investTransfer'
  | 'currencyCloudReturn'
  | 'internationalWirePartnerReturn'
  | 'internalCreditAccountPayment'
  | 'autoRoutingTransfer'
  | 'ventureDebtFunding'
  | 'ventureDebtRepayment'
  | 'creditCashbackRewardsDeposit'
  | 'externalCreditCashbackRewardsDeposit'
  | 'interestPayment'
  | 'outgoingProvisionalCredit'
  | 'incomingProvisionalCredit'
  | 'lineOfCreditFunding'
  | 'lineOfCreditRepayment'
  | 'lineOfCreditInterestRepayment'
  | 'atmFeeReimbursement'
  | 'atmFeeReimbursementReversal'
  | 'expenseReimbursement'
  | 'requestedPayment'
  | 'exogenousWireDrawdown'
  | 'incomingCreditAccountRepayment'
  | 'cardIntlTransactionFee'
  | 'cardIntlTransactionFeeRebate'
  | 'cardIntlTransactionFeeReversal'
  | 'cardIntlTransactionFeeRebateReversal'
  | 'externalCreditAccountPayment'
  | 'realtimePayment'
  | 'outgoingRealTimePayment'
  | 'balanceHold'
  | 'linkedMercuryAccountTransfer';

export type TransactionRelationKind =
  | 'ProvisionalCreditReversalToMerchantRefund'
  | 'MerchantRefundToProvisionalCreditReversal'
  | 'MerchantRefundToFraudulentCharge'
  | 'FraudulentChargeToMerchantRefund'
  | 'PaymentRefundToFailedPayment'
  | 'FailedPaymentToPaymentRefund'
  | 'GiftCompensationToOriginalTransaction'
  | 'FeePaymentToOriginalTransaction'
  | 'OriginalTransactionToFeePayment'
  | 'FeePaymentToFeeRebate'
  | 'FeeRebateToFeePayment'
  | 'FeePaymentToFeeReversal'
  | 'FeeReversalToFeePayment'
  | 'FeeRebateToFeeRebateReversal'
  | 'FeeRebateReversalToFeeRebate'
  | 'TreasurySplitLiquidation'
  | 'ProvisionalCreditToOriginalCharge'
  | 'OriginalChargeToProvisionalCredit'
  | 'FeeAtmReimbursementToAtmTransaction'
  | 'AtmTransactionToFeeAtmReimbursement'
  | 'AtmTransactionToAtmReimbursementReversal'
  | 'AtmReimbursementReversalToAtmTransaction'
  | 'ReturnToOriginalTransaction'
  | 'OriginalTransactionToReturn'
  | 'ProvisionalCreditToReversal'
  | 'ReversalToProvisionalCredit'
  | 'MerchantRefundToOriginalCharge'
  | 'OriginalChargeToMerchantRefund';

export type TransactionStatus = 'pending' | 'sent' | 'cancelled' | 'failed' | 'reversed' | 'blocked';

export interface TransactionsPaginatedResponse {
  page: AutoTransferRulesResponsePage;
  transactions: Array<Transaction>;
}

export interface TransactionsResponse {
  total: number;
  transactions: Array<Transaction>;
}

export interface TransferMoneyApprovalRequestAPIRequest {
  amount: number;
  destinationAccountId: string;
  idempotencyKey: string;
  note?: string | null;
  sourceAccountId: string;
}

export interface TransferMoneyApprovalRequestResponse {
  amount: number;
  createdAt: string;
  destinationAccountId: string;
  memo?: string | null;
  note?: string | null;
  numberOfApproversRequired?: number | null;
  requestId: string;
  requestedByUserId: string;
  requesterMayApprove?: boolean | null;
  reviews: Array<PaymentApprovalReview>;
  sourceAccountId: string;
  status: ReviewRequestStatus;
}

export interface TransferMoneyApprovalRequestsPaginatedResponse {
  page: TransferMoneyApprovalRequestsPaginatedResponsePage;
  requests: Array<TransferMoneyApprovalRequestResponse>;
}

export interface TransferMoneyApprovalRequestsPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export interface TreasuryAccount {
  availableBalance: number;
  createdAt: string;
  currentBalance: number;
  id: string;
  netReturns: Array<TreasuryNetReturn>;
  status: AccountStatus;
}

export interface TreasuryAccountsPaginatedResponse {
  accounts: Array<TreasuryAccount>;
  page: AccountsPaginatedResponsePage;
}

export interface TreasuryDividend {
  amount: number;
  id: string;
  securityName: string;
  type: SecurityIdType;
}

export interface TreasuryNetReturn {
  dividends: Array<TreasuryDividend>;
  month: string;
  netAmount: number;
  status: TreasuryNetReturnStatus;
  treasuryFee: number;
}

export type TreasuryNetReturnStatus = 'processing' | 'pending' | 'charged' | 'error';

export interface TreasuryStatement {
  accountId: string;
  createdAt: string;
  creationDate: string;
  description: string;
  documentType: TreasuryStatementDocumentType;
  downloadUrl: string;
  id: string;
  periodEnd: string;
  periodStart: string;
  updatedAt: string;
}

export type TreasuryStatementDocumentType =
  | 'MonthlyStatement'
  | 'TradeConfirmation'
  | '1099'
  | '1099R'
  | '1042S'
  | '5498'
  | '5498ESA'
  | '1099Q'
  | 'FMV'
  | 'SDIRA';

export interface TreasuryStatementsPaginatedResponse {
  page: CreditAccountStatementsPaginatedResponsePage;
  statements: Array<TreasuryStatement>;
}

export interface TreasuryTransactionDetails {
  creditDescription?: string | null;
  depositCounterpartyId?: string | null;
  feeDescription?: string | null;
  manualAmendmentDescription?: string | null;
  security?: string | null;
  sweepDirection?: string | null;
  tradeAction?: string | null;
  withdrawalCounterpartyId?: string | null;
}

export type TreasuryTransactionType =
  | 'depositCanceled'
  | 'depositComplete'
  | 'depositFailed'
  | 'depositReturned'
  | 'mercuryFeePosted'
  | 'mercuryFeeFailed'
  | 'mercuryFeeRefunded'
  | 'mercuryFeeCanceled'
  | 'withdrawalPosted'
  | 'withdrawalFailed'
  | 'withdrawalCanceled'
  | 'withdrawalReturned'
  | 'revertTxn'
  | 'interestPosted'
  | 'interestCanceled'
  | 'manualAmendmentPosted'
  | 'mercuryCreditPosted'
  | 'mercuryCreditFailed'
  | 'dividendPosted'
  | 'dividendCanceled'
  | 'dividendReinvestmentPosted'
  | 'mutualFundTradeFailed'
  | 'mutualFundTradePosted'
  | 'sweepInPosted'
  | 'sweepOutPosted'
  | 'sweepReconcilePosted'
  | 'valuationChangePosted'
  | 'oemsMutualFundOrderSettled'
  | 'oemsMutualFundOrderCanceled'
  | 'oemsMutualFundOrderRejected'
  | 'oemsFixedIncomeOrderSettled'
  | 'oemsFixedIncomeOrderCanceled'
  | 'oemsFixedIncomeOrderRejected'
  | 'couponPosted'
  | 'couponCanceled'
  | 'maturityPosted'
  | 'maturityCanceled';

export interface TreasuryTransactionsResponse {
  cursor?: number | null;
  transactions: Array<TreasuryTxn>;
}

export interface TreasuryTxn {
  accountId: string;
  additionalDetails?: string | null;
  amount: number;
  balance: number;
  canonicalDay: string;
  description: string;
  details?: TreasuryTransactionDetails | null;
  id: string;
  security?: string | null;
  type: TreasuryTransactionType;
}

export type USState =
  | 'AL'
  | 'AK'
  | 'AZ'
  | 'AR'
  | 'CA'
  | 'CO'
  | 'CT'
  | 'DE'
  | 'DC'
  | 'FL'
  | 'GA'
  | 'HI'
  | 'ID'
  | 'IL'
  | 'IN'
  | 'IA'
  | 'KS'
  | 'KY'
  | 'LA'
  | 'ME'
  | 'MD'
  | 'MA'
  | 'MI'
  | 'MN'
  | 'MS'
  | 'MO'
  | 'MT'
  | 'NE'
  | 'NV'
  | 'NH'
  | 'NJ'
  | 'NM'
  | 'NY'
  | 'NC'
  | 'ND'
  | 'OH'
  | 'OK'
  | 'OR'
  | 'PA'
  | 'RI'
  | 'SC'
  | 'SD'
  | 'TN'
  | 'TX'
  | 'UT'
  | 'VT'
  | 'VA'
  | 'WA'
  | 'WV'
  | 'WI'
  | 'WY';

export interface UpdateBooksAPIBillLine {
  amount?: number | null;
  description?: string | null;
  id: string;
  ledgerId?: string | null;
}

export interface UpdateBooksAPIBillLineChanges {
  create?: Array<CreateBooksAPIBillLine> | null;
  _delete?: Array<string> | null;
  update?: Array<UpdateBooksAPIBillLine> | null;
}

export interface UpdateBooksAPIBillRequest {
  dueDate?: string | null;
  effectiveDate?: string | null;
  lineChanges?: UpdateBooksAPIBillLineChanges | null;
  notes?: string | null;
  referenceNumber?: string | null;
  vendor?: string | null;
}

export interface UpdateBooksAPIJournalEntriesRequest {
  updates: Array<UpdateBooksAPIJournalEntryRequest>;
}

export interface UpdateBooksAPIJournalEntryRequest {
  datetime?: string | null;
  description?: string | null;
  journalEntryId: string;
  lineEntryChanges?: BooksAPIUpdateJournalEntryChanges | null;
  reviewStatus?: BooksJournalEntryReviewStatus | null;
}

export interface UpdateBooksAPILedger {
  clearFields?: Array<BooksLedgerClearField> | null;
  debitCredit?: BooksDebitCredit | null;
  ledgerId: string;
  name?: string | null;
  parentId?: string | null;
  sortCode?: string | null;
  subType?: BooksLedgerSubType | null;
  type?: BooksLedgerType | null;
}

export interface UpdateBooksAPILedgersRequest {
  ledgers: Array<UpdateBooksAPILedger>;
}

export interface UpdateBooksAPILedgersResponse {
  failedCount: number;
  results: Array<BooksAPIUpdateLedgerResult>;
  succeededCount: number;
}

export interface UpdateCardRequest {
  nickname?: string | null;
  spendLimit?: SpendLimit | null;
}

export interface UpdateWebhookParams {
  eventTypes?: Array<WebhookEventType> | null;
  filterPaths?: Array<ResourceField> | null;
  status?: WebhookUpdateStatus | null;
  url?: string | null;
}

export interface UploadedAttachment {
  attachmentId?: string;
  downloadUrl?: string;
}

export interface UserDetails {
  email: string;
  firstName: string;
  lastName: string;
  organizationRole: ApiUserRole;
  userId: string;
}

export interface UsersPaginatedResponse {
  page: UsersPaginatedResponsePage;
  users: Array<UserDetails>;
}

export interface UsersPaginatedResponsePage {
  nextPage?: string;
  previousPage?: string;
}

export type ValuationType = 'PreMoney' | 'PostMoney' | 'NoValuation';

export interface VerifyWebhookParams {
  eventType?: WebhookEventType | null;
}

export type WebhookEventType =
  | 'transaction.created'
  | 'transaction.updated'
  | 'checkingAccount.balance.updated'
  | 'savingsAccount.balance.updated'
  | 'treasuryAccount.balance.updated'
  | 'investmentAccount.balance.updated'
  | 'creditAccount.balance.updated';

export type WebhookUpdateStatus = 'active' | 'paused';
