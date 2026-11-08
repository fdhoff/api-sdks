/** Unofficial client for the Etsy Open API v3. Not affiliated with Etsy. */
export { BASE_URL, EtsyClient } from './client.js';
export type { ClientOptions } from './client.js';
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
export type { ClientError, ErrorKind } from './errors.js';
export { AUTHORIZATION_URL, authorizationUrl, codeChallenge, OAuth } from './oauth.js';
export type { AuthorizationOptions, AuthorizationRequest, Token, TokenCallback } from './oauth.js';
export type { FileContent, FileInput, Logger, RequestOptions } from './runtime/index.js';
export type * from './models/index.js';
