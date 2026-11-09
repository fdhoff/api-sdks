// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Amount {
  currency?: string;
  value?: string;
}

export interface CreateOffersRequest {
  allowCounterOffer?: boolean;
  message?: string;
  offerDuration?: TimeDuration;
  offeredItems?: Array<OfferedItem>;
}

export interface EligibleItem {
  listingId?: string;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface FindEligibleItems429Response {
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

export interface Offer {
  allowCounterOffer?: boolean;
  buyer?: User;
  creationDate?: string;
  initiatedBy?: string;
  lastModifiedDate?: string;
  message?: string;
  offerDuration?: TimeDuration;
  offeredItems?: Array<OfferedItem>;
  offerId?: string;
  offerStatus?: string;
  offerType?: string;
  revision?: string;
}

export interface OfferedItem {
  discountPercentage?: string;
  listingId?: string;
  price?: Amount;
  quantity?: number;
}

export interface PagedEligibleItemCollection {
  eligibleItems?: Array<EligibleItem>;
  href?: string;
  limit?: number;
  next?: string;
  offset?: number;
  prev?: string;
  total?: number;
}

export interface SendOfferToInterestedBuyersCollectionResponse {
  offers?: Array<Offer>;
}

export interface TimeDuration {
  unit?: string;
  value?: number;
}

export interface User {
  maskedUsername?: string;
}
