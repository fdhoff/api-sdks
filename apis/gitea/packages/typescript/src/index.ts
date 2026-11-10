/** Unofficial client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea
 * Limited. */
export { GiteaClient } from './client.js';
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
} from './runtime/index.js';
export type * from './models/index.js';
