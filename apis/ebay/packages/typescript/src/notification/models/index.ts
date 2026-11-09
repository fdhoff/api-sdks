// Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

export interface Config {
  alertEmail?: string;
}

export interface CreateSubscriptionFilterRequest {
  filterSchema?: { [key: string]: object };
}

export interface CreateSubscriptionRequest {
  destinationId?: string;
  payload?: SubscriptionPayloadDetail;
  status?: string;
  topicId?: string;
}

export interface DeliveryConfig {
  endpoint?: string;
  verificationToken?: string;
}

export interface Destination {
  deliveryConfig?: DeliveryConfig;
  destinationId?: string;
  name?: string;
  status?: string;
}

export interface DestinationRequest {
  deliveryConfig?: DeliveryConfig;
  name?: string;
  status?: string;
}

export interface DestinationSearchResponse {
  destinations?: Array<Destination>;
  href?: string;
  limit?: number;
  next?: string;
  total?: number;
}

export interface ErrorParameter {
  name?: string;
  value?: string;
}

export interface GetConfig429Response {
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

export interface PayloadDetail {
  deliveryProtocol?: string;
  deprecated?: boolean;
  format?: Array<string>;
  schemaVersion?: string;
}

export interface PublicKey {
  algorithm?: string;
  digest?: string;
  key?: string;
}

export interface Subscription {
  creationDate?: string;
  destinationId?: string;
  filterId?: string;
  payload?: SubscriptionPayloadDetail;
  status?: string;
  subscriptionId?: string;
  topicId?: string;
}

export interface SubscriptionFilter {
  creationDate?: string;
  filterId?: string;
  filterSchema?: { [key: string]: object };
  filterStatus?: string;
  subscriptionId?: string;
}

export interface SubscriptionPayloadDetail {
  deliveryProtocol?: string;
  format?: string;
  schemaVersion?: string;
}

export interface SubscriptionSearchResponse {
  href?: string;
  limit?: number;
  next?: string;
  subscriptions?: Array<Subscription>;
  total?: number;
}

export interface Topic {
  authorizationScopes?: Array<string>;
  context?: string;
  description?: string;
  filterable?: boolean;
  scope?: string;
  status?: string;
  supportedPayloads?: Array<PayloadDetail>;
  topicId?: string;
}

export interface TopicSearchResponse {
  href?: string;
  limit?: number;
  next?: string;
  topics?: Array<Topic>;
  total?: number;
}

export interface UpdateSubscriptionRequest {
  destinationId?: string;
  payload?: SubscriptionPayloadDetail;
  status?: string;
}
