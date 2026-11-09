/** Unofficial client for the Mirakl seller API. Not affiliated with, endorsed by or sponsored by Mirakl SAS. */
export { MiraklClient } from './client.js';
export type { ClientOptions } from './client.js';
export {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  AuthenticationError,
  BadRequestError,
  DecodeError,
  HttpError,
  JobTimeoutError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
} from './errors.js';
export type { ClientError, ErrorKind } from './errors.js';
export { StaticCredentials } from './runtime/index.js';
export type {
  AuthRequest,
  Credentials,
  Download,
  FileContent,
  FileInput,
  Logger,
  RawBody,
  RequestOptions,
  Requirement,
  Scheme,
  WaitOptions,
} from './runtime/index.js';
export type * from './models/index.js';
