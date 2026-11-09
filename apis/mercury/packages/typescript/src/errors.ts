import {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  DecodeError,
  type ApiErrorFields,
  type ErrorContext,
} from './runtime/index.js';

/** A response with an error status. Mercury declares no error body, so `rawBody` holds it as text, with your token
 * removed. */
export class HttpError extends ApiError {
  override readonly kind:
    | 'api'
    | 'bad_request'
    | 'authentication'
    | 'permission'
    | 'not_found'
    | 'conflict'
    | 'validation'
    | 'rate_limited'
    | 'server' = 'api';
}

/** HTTP 400. */
export class BadRequestError extends HttpError {
  override readonly kind = 'bad_request';
}

/** HTTP 401: the token is missing, wrong or revoked. */
export class AuthenticationError extends HttpError {
  override readonly kind = 'authentication';
}

/** HTTP 403: the token lacks the scope, or the request did not come from an allowed IP address. */
export class PermissionDeniedError extends HttpError {
  override readonly kind = 'permission';
}

/** HTTP 404. */
export class NotFoundError extends HttpError {
  override readonly kind = 'not_found';
}

/** HTTP 409. */
export class ConflictError extends HttpError {
  override readonly kind = 'conflict';
}

/** HTTP 422. */
export class UnprocessableError extends HttpError {
  override readonly kind = 'validation';
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
  | ConflictError
  | DecodeError
  | NotFoundError
  | PermissionDeniedError
  | RateLimitedError
  | ServerError
  | UnprocessableError;

/** The `kind` of every error the client throws. */
export type ErrorKind = ClientError['kind'];

type ErrorType = new (message: string, fields: ApiErrorFields) => HttpError;

const BY_STATUS: Record<number, ErrorType> = {
  400: BadRequestError,
  401: AuthenticationError,
  403: PermissionDeniedError,
  404: NotFoundError,
  409: ConflictError,
  422: UnprocessableError,
  429: RateLimitedError,
};

export function toError({ status, headers, text }: ErrorContext): ApiError {
  const type = BY_STATUS[status] ?? (status >= 500 ? ServerError : HttpError);
  return new type(`HTTP ${status}`, { status, rawBody: text, retryAfter: headers.get('retry-after') ?? undefined });
}

export { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError };
