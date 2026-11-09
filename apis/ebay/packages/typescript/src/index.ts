/** Unofficial client for eBay's Sell, Commerce and Developer REST APIs. Not affiliated with, endorsed by or
 * sponsored by eBay Inc. Each API's models are in its own subpath, such as `ebay-sell/fulfillment`. */
export { EbayClient, ENVIRONMENTS } from './client.js';
export type { ClientOptions, HostKey } from './client.js';
export {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  AuthenticationError,
  BadRequestError,
  ConflictError,
  DecodeError,
  HttpError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
  UnprocessableError,
} from './errors.js';
export type { ClientError, ErrorDetail, ErrorKind, ErrorParameter } from './errors.js';
export { API_SCOPE, AUTHORIZATION_URLS, authorizationUrl } from './oauth.js';
export type { AuthorizationOptions, AuthorizationRequest, Environment, OAuth, Token, TokenCallback } from './oauth.js';
export { SigningKey } from './signing.js';
export type { SigningKeyOptions } from './signing.js';
export type { Download, FileContent, FileInput, Logger, RawBody, RequestOptions } from './runtime/index.js';
