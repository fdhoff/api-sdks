/** Unofficial client for the Back Market Seller API. Not affiliated with Back Market. */
export { BackMarketClient } from './client.js';
export type { ClientOptions, Environment, Region } from './client.js';
export {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  AuthenticationError,
  BadRequestError,
  BotChallengeError,
  DecodeError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
  UnprocessableError,
  WafBlockedError,
} from './errors.js';
export type { ClientError, ErrorKind } from './errors.js';
export type { FileContent, FileInput, Logger, RequestOptions } from './runtime/index.js';
export type * from './models/index.js';
