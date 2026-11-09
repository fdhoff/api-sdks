// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Ad {
  bidPercentages?: Array<BidPercentages>;
  promoteWithAd?: string;
}

export interface BidPercentages {
  basis?: string;
  value?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FindListingRecommendationRequest {
  listingIds?: Array<string>;
}

export interface FindListingRecommendations429Response {
  errors?: Array<Error>;
}

export interface ListingRecommendation {
  listingId?: string;
  marketing?: MarketingRecommendation;
}

export interface MarketingRecommendation {
  ad?: Ad;
  message?: string;
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

export interface PagedListingRecommendationCollection {
  href?: string;
  limit?: number;
  listingRecommendations?: Array<ListingRecommendation>;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}
