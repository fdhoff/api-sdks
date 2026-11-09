// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Ad {
  adGroupId?: string;
  adId?: string;
  adStatus?: string;
  alerts?: Array<Alert>;
  bidPercentage?: string;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
  listingId?: string;
}

export interface AdGroup {
  adGroupId?: string;
  adGroupStatus?: string;
  defaultBid?: Amount;
  name?: string;
}

export interface AdGroupPagedCollectionResponse {
  adGroups?: Array<AdGroup>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface AdIds {
  adIds?: Array<string>;
}

export interface AdPagedCollectionResponse {
  ads?: Array<Ad>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface AdReference {
  adId?: string;
  href?: string;
}

export interface AdReferences {
  ads?: Array<AdReference>;
}

export interface AdResponse {
  adGroupId?: string;
  adId?: string;
  errors?: Array<Error>;
  href?: string;
  listingId?: string;
  statusCode?: number;
}

export interface AdUpdateResponse {
  adId?: string;
  errors?: Array<Error>;
  href?: string;
  listingId?: string;
  statusCode?: number;
}

export interface AdUpdateStatusByListingIdResponse {
  adGroupId?: string;
  errors?: Array<Error>;
  href?: string;
  listingId?: string;
  statusCode?: number;
}

export interface AdUpdateStatusResponse {
  adId?: string;
  errors?: Array<Error>;
  href?: string;
  statusCode?: number;
}

export interface AdditionalInfo {
  infoType?: string;
  metrics?: Array<AdditionalInfoData>;
}

export interface AdditionalInfoData {
  metricKey?: string;
  value?: string;
}

export interface Ads {
  ads?: Array<Ad>;
}

export interface Alert {
  alertType?: string;
  details?: Array<AlertDetails>;
}

export interface AlertDetails {
  dimension?: AlertDimension;
  aspect?: Aspect;
}

export interface AlertDimension {
  key?: string;
  value?: string;
}

export interface Amount {
  currency?: string;
  value?: string;
}

export interface Aspect {
  key?: string;
  value?: string;
}

export interface BaseResponse {
  warnings?: Array<Error>;
}

export interface BidPreference {
  maxCpc?: MaxCpc;
}

export interface Budget {
  amount?: Amount;
  budgetStatus?: string;
}

export interface BudgetRecommendationResponse {
  budget?: CampaignBudget;
  campaignId?: string;
  channels?: Array<string>;
}

export interface BudgetRequest {
  amount?: Amount;
}

export interface BulkAdResponse {
  responses?: Array<AdResponse>;
}

export interface BulkAdUpdateResponse {
  responses?: Array<AdUpdateResponse>;
}

export interface BulkAdUpdateStatusByListingIdResponse {
  responses?: Array<AdUpdateStatusByListingIdResponse>;
}

export interface BulkAdUpdateStatusResponse {
  responses?: Array<AdUpdateStatusResponse>;
}

export interface BulkCreateAdRequest {
  requests?: Array<CreateAdRequest>;
}

export interface BulkCreateAdsByInventoryReference429Response {
  errors?: Array<Error>;
}

export interface BulkCreateAdsByInventoryReferenceRequest {
  requests?: Array<CreateAdsByInventoryReferenceRequest>;
}

export interface BulkCreateAdsByInventoryReferenceResponse {
  responses?: Array<CreateAdsByInventoryReferenceResponse>;
}

export interface BulkCreateKeywordRequest {
  requests?: Array<CreateKeywordRequest>;
}

export interface BulkCreateKeywordResponse {
  responses?: Array<KeywordResponse>;
}

export interface BulkCreateNegativeKeywordRequest {
  requests?: Array<CreateNegativeKeywordRequest>;
}

export interface BulkCreateNegativeKeywordResponse {
  responses?: Array<NegativeKeywordResponse>;
}

export interface BulkDeleteAdRequest {
  requests?: Array<DeleteAdRequest>;
}

export interface BulkDeleteAdResponse {
  responses?: Array<DeleteAdResponse>;
}

export interface BulkDeleteAdsByInventoryReferenceRequest {
  requests?: Array<DeleteAdsByInventoryReferenceRequest>;
}

export interface BulkDeleteAdsByInventoryReferenceResponse {
  responses?: Array<DeleteAdsByInventoryReferenceResponse>;
}

export interface BulkUpdateAdStatusByListingIdRequest {
  requests?: Array<UpdateAdStatusByListingIdRequest>;
}

export interface BulkUpdateAdStatusRequest {
  requests?: Array<UpdateAdStatusRequest>;
}

export interface BulkUpdateAdsByInventoryReferenceResponse {
  responses?: Array<UpdateAdsByInventoryReferenceResponse>;
}

export interface BulkUpdateKeywordRequest {
  requests?: Array<UpdateKeywordByKeywordIdRequest>;
}

export interface BulkUpdateKeywordResponse {
  responses?: Array<UpdateKeywordResponse>;
}

export interface BulkUpdateNegativeKeywordRequest {
  requests?: Array<UpdateNegativeKeywordIdRequest>;
}

export interface BulkUpdateNegativeKeywordResponse {
  responses?: Array<UpdateNegativeKeywordResponse>;
}

export interface Campaign {
  alerts?: Array<Alert>;
  budget?: CampaignBudget;
  campaignCriterion?: CampaignCriterion;
  campaignId?: string;
  campaignName?: string;
  campaignStatus?: string;
  campaignTargetingType?: string;
  channels?: Array<string>;
  endDate?: string;
  fundingStrategy?: FundingStrategy;
  marketplaceId?: string;
  startDate?: string;
}

export interface CampaignAudience {
  audienceType?: string;
  code?: string;
  name?: string;
}

export interface CampaignBudget {
  daily?: Budget;
}

export interface CampaignBudgetRequest {
  daily?: BudgetRequest;
}

export interface CampaignCriterion {
  autoSelectFutureInventory?: boolean;
  criterionType?: string;
  selectionRules?: Array<SelectionRule>;
}

export interface CampaignDTO {
  audiences?: Array<CampaignAudience>;
  creationDate?: string;
  emailCampaignId?: string;
  emailCampaignStatus?: string;
  emailCampaignType?: string;
  marketplaceId?: string;
  modificationDate?: string;
  scheduleDate?: string;
  scheduleDateType?: string;
  sentDate?: string;
  subject?: string;
}

export interface CampaignPagedCollectionResponse {
  campaigns?: Array<Campaign>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface Campaigns {
  campaigns?: Array<Campaign>;
}

export interface CloneCampaignRequest {
  campaignName?: string;
  endDate?: string;
  fundingStrategy?: FundingStrategy;
  startDate?: string;
}

export interface CouponConfiguration {
  couponCode?: string;
  couponType?: string;
  maxCouponRedemptionPerUser?: number;
}

export interface CreateAdGroupRequest {
  defaultBid?: Amount;
  name?: string;
}

export interface CreateAdRequest {
  adGroupId?: string;
  bidPercentage?: string;
  listingId?: string;
}

export interface CreateAdsByInventoryReferenceRequest {
  adGroupId?: string;
  bidPercentage?: string;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
}

export interface CreateAdsByInventoryReferenceResponse {
  adGroupId?: string;
  ads?: Array<AdReference>;
  errors?: Array<Error>;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
  statusCode?: number;
}

export interface CreateCampaignRequest {
  budget?: CampaignBudgetRequest;
  campaignCriterion?: CampaignCriterion;
  campaignName?: string;
  campaignTargetingType?: string;
  channels?: Array<string>;
  endDate?: string;
  fundingStrategy?: FundingStrategy;
  marketplaceId?: string;
  startDate?: string;
}

export interface CreateEmailCampaignRequest {
  audienceCodes?: Array<string>;
  categoryId?: string;
  categoryType?: string;
  emailCampaignType?: string;
  itemIds?: Array<string>;
  itemSelectMode?: string;
  personalizedMessage?: string;
  priceRange?: PriceRange;
  promotionId?: string;
  promotionSelectModeEnum?: string;
  scheduleDate?: string;
  sort?: string;
  subject?: string;
}

export interface CreateEmailCampaignResponse {
  emailCampaignId?: string;
  emailCampaignStatus?: string;
}

export interface CreateKeywordRequest {
  adGroupId?: string;
  bid?: Amount;
  keywordText?: string;
  matchType?: string;
}

export interface CreateNegativeKeywordRequest {
  adGroupId?: string;
  campaignId?: string;
  negativeKeywordMatchType?: string;
  negativeKeywordText?: string;
}

export interface CreateReportTask {
  additionalRecords?: Array<string>;
  campaignIds?: Array<string>;
  channels?: Array<string>;
  dateFrom?: string;
  dateTo?: string;
  dimensions?: Array<Dimension>;
  fundingModels?: Array<string>;
  inventoryReferences?: Array<InventoryReference>;
  listingIds?: Array<string>;
  marketplaceId?: string;
  metricKeys?: Array<string>;
  reportFormat?: string;
  reportType?: string;
}

export interface DeleteAdRequest {
  listingId?: string;
}

export interface DeleteAdResponse {
  adId?: string;
  errors?: Array<Error>;
  listingId?: string;
  statusCode?: number;
}

export interface DeleteAdsByInventoryReferenceRequest {
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
}

export interface DeleteAdsByInventoryReferenceResponse {
  adIds?: Array<string>;
  errors?: Array<Error>;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
  statusCode?: number;
}

export interface DeleteEmailCampaignResponse {
  emailCampaignId?: string;
}

export interface Dimension {
  annotationKeys?: Array<string>;
  dimensionKey?: string;
}

export interface DimensionKeyAnnotation {
  annotationKey?: string;
  dataType?: string;
}

export interface DimensionMetadata {
  dataType?: string;
  dimensionKey?: string;
  dimensionKeyAnnotations?: Array<DimensionKeyAnnotation>;
}

export interface DiscountBenefit {
  amountOffItem?: Amount;
  amountOffOrder?: Amount;
  percentageOffItem?: string;
  percentageOffOrder?: string;
}

export interface DiscountRule {
  discountBenefit?: DiscountBenefit;
  discountSpecification?: DiscountSpecification;
  maxDiscountAmount?: Amount;
  ruleOrder?: number;
}

export interface DiscountSpecification {
  forEachAmount?: Amount;
  forEachQuantity?: number;
  minAmount?: Amount;
  minQuantity?: number;
  numberOfDiscountedItems?: number;
}

export interface DynamicAdRatePreference {
  adRateAdjustmentPercent?: string;
  adRateCapPercent?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FundingStrategy {
  adRateStrategy?: string;
  biddingStrategy?: string;
  bidPercentage?: string;
  bidPreferences?: Array<BidPreference>;
  dynamicAdRatePreferences?: Array<DynamicAdRatePreference>;
  fundingModel?: string;
}

export interface GetEmailCampaignAudiencesResponse {
  audiences?: Array<CampaignAudience>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface GetEmailCampaignResponse {
  audiences?: Array<CampaignAudience>;
  categoryId?: string;
  categoryType?: string;
  creationDate?: string;
  emailCampaignId?: string;
  emailCampaignStatus?: string;
  emailCampaignType?: string;
  itemIds?: Array<string>;
  itemSelectMode?: string;
  marketplaceId?: string;
  modificationDate?: string;
  personalizedMessage?: string;
  priceRange?: PriceRange;
  promotionId?: string;
  promotionSelectMode?: string;
  scheduleDate?: string;
  scheduleDateType?: string;
  sentDate?: string;
  sort?: string;
  subject?: string;
}

export interface GetEmailCampaignsResponse {
  campaigns?: Array<CampaignDTO>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface GetEmailPreviewResponse {
  content?: string;
  renderDate?: string;
}

export interface GetEmailReportResponse {
  clickCount?: number;
  openCount?: number;
  totalSales?: Amount;
}

export interface InventoryCriterion {
  inventoryCriterionType?: string;
  inventoryItems?: Array<InventoryItem>;
  listingIds?: Array<string>;
  ruleCriteria?: RuleCriteria;
}

export interface InventoryItem {
  inventoryReferenceId?: string;
}

export interface InventoryReference {
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
}

export interface ItemBasis {
  estimatedValue?: number;
  metric?: string;
}

export interface ItemMarkdownStatus {
  listingMarkdownStatus?: string;
  statusChangedDate?: string;
  statusMessage?: string;
}

export interface ItemPriceMarkdown {
  applyFreeShipping?: boolean;
  autoSelectFutureInventory?: boolean;
  blockPriceIncreaseInItemRevision?: boolean;
  description?: string;
  endDate?: string;
  marketplaceId?: string;
  name?: string;
  priority?: string;
  promotionImageUrl?: string;
  promotionStatus?: string;
  selectedInventoryDiscounts?: Array<SelectedInventoryDiscount>;
  startDate?: string;
}

export interface ItemPromotion {
  applyDiscountToSingleItemOnly?: boolean;
  budget?: Amount;
  couponConfiguration?: CouponConfiguration;
  description?: string;
  discountRules?: Array<DiscountRule>;
  endDate?: string;
  inventoryCriterion?: InventoryCriterion;
  marketplaceId?: string;
  name?: string;
  priority?: string;
  promotionImageUrl?: string;
  promotionStatus?: string;
  promotionType?: string;
  startDate?: string;
}

export interface ItemPromotionResponse {
  applyDiscountToSingleItemOnly?: boolean;
  budget?: Amount;
  couponConfiguration?: CouponConfiguration;
  description?: string;
  discountRules?: Array<DiscountRule>;
  endDate?: string;
  inventoryCriterion?: InventoryCriterion;
  marketplaceId?: string;
  name?: string;
  priority?: string;
  promotionId?: string;
  promotionImageUrl?: string;
  promotionStatus?: string;
  promotionType?: string;
  startDate?: string;
}

export interface ItemsPagedCollection {
  href?: string;
  limit?: number;
  listings?: Array<ListingDetail>;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
  warnings?: Array<Error>;
}

export interface Keyword {
  adGroupId?: string;
  bid?: Amount;
  keywordId?: string;
  keywordStatus?: string;
  keywordText?: string;
  matchType?: string;
}

export interface KeywordPagedCollectionResponse {
  href?: string;
  keywords?: Array<Keyword>;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface KeywordRequest {
  keywordText?: string;
  matchType?: string;
}

export interface KeywordResponse {
  adGroupId?: string;
  errors?: Array<Error>;
  href?: string;
  keywordId?: string;
  keywordText?: string;
  matchType?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface ListingDetail {
  currentPrice?: Amount;
  freeShipping?: boolean;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
  listingCategoryId?: string;
  listingCondition?: string;
  listingConditionId?: string;
  listingId?: string;
  listingPromotionStatuses?: Array<ItemMarkdownStatus>;
  quantity?: number;
  storeCategoryId?: string;
  title?: string;
}

export interface MaxCpc {
  amount?: Amount;
}

export interface MetricMetadata {
  dataType?: string;
  metricKey?: string;
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

export interface NegativeKeyword {
  adGroupId?: string;
  campaignId?: string;
  negativeKeywordId?: string;
  negativeKeywordMatchType?: string;
  negativeKeywordStatus?: string;
  negativeKeywordText?: string;
}

export interface NegativeKeywordPagedCollectionResponse {
  href?: string;
  limit?: number;
  negativeKeywords?: Array<NegativeKeyword>;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface NegativeKeywordResponse {
  adGroupId?: string;
  campaignId?: string;
  errors?: Array<Error>;
  href?: string;
  negativeKeywordId?: string;
  negativeKeywordMatchType?: string;
  negativeKeywordText?: string;
  statusCode?: number;
}

export interface PriceRange {
  currency?: string;
  gte?: number;
  lte?: number;
}

export interface PromotionDetail {
  couponCode?: string;
  description?: string;
  endDate?: string;
  marketplaceId?: string;
  name?: string;
  priority?: string;
  promotionHref?: string;
  promotionId?: string;
  promotionImageUrl?: string;
  promotionStatus?: string;
  promotionType?: string;
  startDate?: string;
}

export interface PromotionReportDetail {
  averageItemDiscount?: Amount;
  averageItemRevenue?: Amount;
  averageOrderDiscount?: Amount;
  averageOrderRevenue?: Amount;
  averageOrderSize?: string;
  baseSale?: Amount;
  itemsSoldQuantity?: number;
  numberOfOrdersSold?: number;
  percentageSalesLift?: string;
  promotionHref?: string;
  promotionId?: string;
  promotionReportId?: string;
  promotionSale?: Amount;
  promotionType?: string;
  totalDiscount?: Amount;
  totalSale?: Amount;
}

export interface PromotionsPagedCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  promotions?: Array<PromotionDetail>;
  total?: number;
}

export interface PromotionsReportPagedCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  promotionReports?: Array<PromotionReportDetail>;
  total?: number;
}

export interface ProposedBid {
  currency?: string;
  rangeEnd?: string;
  rangeStart?: string;
  value?: string;
}

export interface ReportMetadata {
  dimensionMetadata?: Array<DimensionMetadata>;
  maxNumberOfDimensionsToRequest?: number;
  maxNumberOfMetricsToRequest?: number;
  channel?: string;
  metricMetadata?: Array<MetricMetadata>;
  reportType?: string;
}

export interface ReportMetadatas {
  reportMetadata?: Array<ReportMetadata>;
}

export interface ReportTask {
  campaignIds?: Array<string>;
  channels?: Array<string>;
  dateFrom?: string;
  dateTo?: string;
  dimensions?: Array<Dimension>;
  fundingModels?: Array<string>;
  inventoryReferences?: Array<InventoryReference>;
  listingIds?: Array<string>;
  marketplaceId?: string;
  metricKeys?: Array<string>;
  reportExpirationDate?: string;
  reportFormat?: string;
  reportHref?: string;
  reportId?: string;
  reportName?: string;
  reportTaskCompletionDate?: string;
  reportTaskCreationDate?: string;
  reportTaskExpectedCompletionDate?: string;
  reportTaskId?: string;
  reportTaskStatus?: string;
  reportTaskStatusMessage?: string;
  reportType?: string;
}

export interface ReportTaskPagedCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
  reportTasks?: Array<ReportTask>;
}

export interface RuleCriteria {
  excludeInventoryItems?: Array<InventoryItem>;
  excludeListingIds?: Array<string>;
  markupInventoryItems?: Array<InventoryItem>;
  markupListingIds?: Array<string>;
  selectionRules?: Array<SelectionRule>;
}

export interface SelectedInventoryDiscount {
  discountBenefit?: DiscountBenefit;
  discountId?: string;
  inventoryCriterion?: InventoryCriterion;
  ruleOrder?: number;
}

export interface SelectionRule {
  brands?: Array<string>;
  categoryIds?: Array<string>;
  categoryScope?: string;
  listingConditionIds?: Array<string>;
  maxPrice?: Amount;
  minPrice?: Amount;
}

export interface SuggestBudgetResponse {
  suggestedBudget?: Array<BudgetRecommendationResponse>;
}

export interface SuggestMaxCpcRequest {
  listingIds?: Array<string>;
  marketplaceId?: string;
}

export interface SuggestMaxCpcResponse {
  amount?: Amount;
  marketplaceId?: string;
}

export interface SuggestedBids {
  keywordText?: string;
  matchType?: string;
  proposedBid?: ProposedBid;
}

export interface SuggestedKeywords {
  additionalInfo?: Array<AdditionalInfo>;
  keywordText?: string;
  matchType?: string;
}

export interface SummaryReportResponse {
  baseSale?: Amount;
  lastUpdated?: string;
  percentageSalesLift?: string;
  promotionSale?: Amount;
  totalSale?: Amount;
}

export interface TargetedAdsPagedCollection {
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  suggestedItems?: Array<TargetingItems>;
  total?: number;
}

export interface TargetedBidRequest {
  keywords?: Array<KeywordRequest>;
}

export interface TargetedBidsPagedCollection {
  suggestedBids?: Array<SuggestedBids>;
}

export interface TargetedKeywordRequest {
  additionalInfo?: Array<string>;
  exclusions?: Array<string>;
  listingIds?: Array<string>;
  matchType?: string;
}

export interface TargetedKeywordsPagedCollection {
  suggestedKeywords?: Array<SuggestedKeywords>;
}

export interface TargetingItems {
  bases?: Array<ItemBasis>;
  listingId?: string;
}

export interface UpdateAdGroupRequest {
  adGroupStatus?: string;
  defaultBid?: Amount;
  name?: string;
}

export interface UpdateAdStatusByListingIdRequest {
  adGroupId?: string;
  adStatus?: string;
  listingId?: string;
}

export interface UpdateAdStatusRequest {
  adId?: string;
  adStatus?: string;
}

export interface UpdateAdrateStrategyRequest {
  adRateStrategy?: string;
  bidPercentage?: string;
  dynamicAdRatePreferences?: Array<DynamicAdRatePreference>;
}

export interface UpdateAdsByInventoryReferenceResponse {
  ads?: Array<AdReference>;
  errors?: Array<Error>;
  inventoryReferenceId?: string;
  inventoryReferenceType?: string;
  statusCode?: number;
}

export interface UpdateBidPercentageRequest {
  bidPercentage?: string;
}

export interface UpdateBiddingStrategyRequest {
  biddingStrategy?: string;
  bidPreferences?: Array<BidPreference>;
}

export interface UpdateCampaignBudgetRequest {
  daily?: BudgetRequest;
}

export interface UpdateCampaignIdentificationRequest {
  campaignName?: string;
  endDate?: string;
  startDate?: string;
}

export interface UpdateCampaignRequest {
  audienceCodes?: Array<string>;
  categoryId?: string;
  categoryType?: string;
  itemIds?: Array<string>;
  itemSelectMode?: string;
  personalizedMessage?: string;
  priceRange?: PriceRange;
  promotionId?: string;
  promotionSelectModeEnum?: string;
  scheduleDate?: string;
  sort?: string;
  subject?: string;
}

export interface UpdateEmailCampaignResponse {
  emailCampaignId?: string;
  emailCampaignStatus?: string;
}

export interface UpdateKeywordByKeywordIdRequest {
  bid?: Amount;
  keywordId?: string;
  keywordStatus?: string;
}

export interface UpdateKeywordRequest {
  bid?: Amount;
  keywordStatus?: string;
}

export interface UpdateKeywordResponse {
  errors?: Array<Error>;
  keywordId?: string;
  statusCode?: number;
  warnings?: Array<Error>;
}

export interface UpdateNegativeKeywordIdRequest {
  negativeKeywordId?: string;
  negativeKeywordStatus?: string;
}

export interface UpdateNegativeKeywordRequest {
  negativeKeywordStatus?: string;
}

export interface UpdateNegativeKeywordResponse {
  errors?: Array<Error>;
  negativeKeywordId?: string;
  statusCode?: number;
}
