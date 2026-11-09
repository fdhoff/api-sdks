// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface AwaitingFeedback {
  listingId?: string;
  listingPrice?: ListingPrice;
  listingTitle?: string;
  orderLineItemId?: string;
  ratingTemplates?: Array<FeedbackRatingTemplateType>;
  transactionId?: string;
}

export interface AwaitingFeedbackResponse {
  itemsAwaitingFeedbackCount?: ItemsAwaitingFeedbackCount;
  lineItems?: Array<AwaitingFeedback>;
  pagination?: Pagination;
}

export interface Comment {
  commentPeriod?: CommentCommentPeriod;
  commentText?: string;
  commentTextRemovedPerPolicy?: boolean;
  state?: string;
}

export interface CommentCommentPeriod {
  unit?: string;
  value?: number;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FeedbackDetail {
  automatedFeedback?: boolean;
  commentType?: string;
  eligibleForRevision?: boolean;
  feedbackComment?: Comment;
  feedbackEnteredDate?: string;
  feedbackEnteredPeriod?: FeedbackEnteredPeriod;
  feedbackId?: string;
  feedbackRatings?: Array<FeedbackRating>;
  feedbackScore?: number;
  feedbackState?: string;
  followupComment?: Comment;
  hasImages?: boolean;
  images?: Array<Image>;
  orderLineItemSummary?: OrderLineItemSummary;
  providerUserDetail?: ProviderUserDetail;
  repliedBeforeFollowup?: boolean;
  replyComment?: Comment;
  topics?: Array<Topic>;
}

export interface FeedbackEnteredPeriod {
  unit?: string;
  value?: number;
}

export interface FeedbackMetrics {
  metricName?: string;
  metricValue?: number;
}

export interface FeedbackRating {
  ratingType?: string;
  value?: string;
}

export interface FeedbackRatingAcceptableValue {
  enabled?: boolean;
  value?: string;
  valueLabel?: string;
}

export interface FeedbackRatingSummary {
  ratingSummaryByRatingType?: Array<RatingSummaryByRatingType>;
  ratingType?: string;
}

export interface FeedbackRatingTemplateType {
  acceptableValues?: Array<FeedbackRatingAcceptableValue>;
  defaultValue?: string;
  earlyFeedbackMessage?: string;
  enabled?: boolean;
  maximumCharactersAllowed?: number;
  multiValueRating?: boolean;
  ratingKey?: string;
  ratingLabel?: string;
  ratingValueType?: string;
  required?: boolean;
}

export interface FeedbackRatingValueDistribution {
  count?: number;
  value?: string;
}

export interface GetFeedbackRatingSummaryResponse {
  feedbackRatingSummary?: Array<FeedbackRatingSummary>;
}

export interface GetFeedbackResponse {
  feedbackEntries?: Array<FeedbackDetail>;
  pagination?: Pagination;
}

export interface GetItemsAwaitingFeedback429Response {
  errors?: Array<Error>;
}

export interface Image {
  url?: string;
}

export interface ItemsAwaitingFeedbackCount {
  asBuyer?: number;
  asSeller?: number;
}

export interface LeaveFeedbackRequest {
  commentText?: string;
  commentType?: string;
  images?: Array<Image>;
  listingId?: string;
  orderLineItemId?: string;
  sellerRatings?: Array<SellerRating>;
  transactionId?: string;
}

export interface LeaveFeedbackResponse {
  feedbackId?: string;
}

export interface ListingPrice {
  currency?: string;
  value?: number;
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

export interface OrderLineItemAttribute {
  name?: string;
  value?: string;
}

export interface OrderLineItemSummary {
  listingId?: string;
  listingPrice?: ListingPrice;
  listingTitle?: string;
  orderLineItemAttributes?: Array<OrderLineItemAttribute>;
  orderLineItemId?: string;
  transactionPeriod?: TransactionPeriod;
}

export interface Pagination {
  count?: number;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface Period {
  unit?: string;
  value?: number;
}

export interface ProviderUserDetail {
  feedbackScore?: number;
  feedbackStar?: string;
  role?: string;
  userAttributes?: Array<ProviderUserDetailUserAttributes>;
  userId?: string;
}

export interface ProviderUserDetailUserAttributes {
  name?: string;
  value?: string;
}

export interface RatingSummaryByRatingType {
  feedbackMetrics?: Array<FeedbackMetrics>;
  feedbackRatingValueDistribution?: Array<FeedbackRatingValueDistribution>;
  period?: Period;
  userRoleType?: string;
}

export interface RespondToFeedbackRequest {
  feedbackId?: string;
  recipientUserId?: string;
  responseText?: string;
  responseType?: string;
}

export interface SellerRating {
  key?: string;
  value?: string;
}

export interface Topic {
  coarseTopic?: string;
  fineTopic?: string;
  highlightedTexts?: Array<string>;
  sentiment?: string;
}

export interface TransactionPeriod {
  period?: Period;
  thresholdType?: string;
}
