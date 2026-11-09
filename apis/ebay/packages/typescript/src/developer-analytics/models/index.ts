// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetRateLimits429Response {
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

export interface Rate {
  count?: number;
  limit?: number;
  remaining?: number;
  reset?: string;
  timeWindow?: number;
}

export interface RateLimit {
  apiContext?: string;
  apiName?: string;
  apiVersion?: string;
  resources?: Array<Resource>;
}

export interface RateLimitsResponse {
  rateLimits?: Array<RateLimit>;
}

export interface Resource {
  name?: string;
  rates?: Array<Rate>;
}
