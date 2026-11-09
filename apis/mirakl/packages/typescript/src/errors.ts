import {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  DecodeError,
  JobTimeoutError,
  type ApiErrorFields,
  type ErrorContext,
} from './runtime/index.js';

/** A response with an error status. Mirakl's docs define no error body, so `rawBody` holds it as text, with your
 * key removed. */
export class HttpError extends ApiError {
  override readonly kind:
    'api' | 'bad_request' | 'authentication' | 'permission' | 'not_found' | 'rate_limited' | 'server' = 'api';
}

/** HTTP 400. */
export class BadRequestError extends HttpError {
  override readonly kind = 'bad_request';
}

/** HTTP 401: the key is missing, wrong or revoked. */
export class AuthenticationError extends HttpError {
  override readonly kind = 'authentication';
}

/** HTTP 403: the key's role does not allow the call, or the shop is not one the key covers. */
export class PermissionDeniedError extends HttpError {
  override readonly kind = 'permission';
}

/** HTTP 404. */
export class NotFoundError extends HttpError {
  override readonly kind = 'not_found';
}

/** HTTP 429, after retries. */
export class RateLimitedError extends HttpError {
  override readonly kind = 'rate_limited';
}

/** HTTP 5xx, after retries. */
export class ServerError extends HttpError {
  override readonly kind = 'server';
}

/** Every error the client throws. Compare `kind`, and the type narrows to that class. */
export type ClientError =
  | (HttpError & { readonly kind: 'api' })
  | ApiConnectionError
  | ApiTimeoutError
  | AuthenticationError
  | BadRequestError
  | DecodeError
  | JobTimeoutError
  | NotFoundError
  | PermissionDeniedError
  | RateLimitedError
  | ServerError;

/** The `kind` of every error the client throws. */
export type ErrorKind = ClientError['kind'];

type ErrorType = new (message: string, fields: ApiErrorFields) => HttpError;

const BY_STATUS: Record<number, ErrorType> = {
  400: BadRequestError,
  401: AuthenticationError,
  403: PermissionDeniedError,
  404: NotFoundError,
  429: RateLimitedError,
};

export function toError({ status, headers, text }: ErrorContext): ApiError {
  const type = BY_STATUS[status] ?? (status >= 500 ? ServerError : HttpError);
  return new type(`HTTP ${status}`, { status, rawBody: text, retryAfter: headers.get('retry-after') ?? undefined });
}

export { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, JobTimeoutError };
