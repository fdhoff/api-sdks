import {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  DecodeError,
  type ApiErrorFields,
  type ErrorContext,
} from './runtime/index.js';

/** A response with an error status. `detail` is the `error` text of its body, when it has one. */
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
  readonly detail?: string;

  constructor(message: string, fields: ApiErrorFields & { detail?: string } = {}) {
    super(message, fields);
    this.detail = fields.detail;
  }
}

/** HTTP 400. */
export class BadRequestError extends HttpError {
  override readonly kind = 'bad_request';
}

/** HTTP 401, after any refresh of the access token. */
export class AuthenticationError extends HttpError {
  override readonly kind = 'authentication';
}

/** HTTP 403. */
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

type ErrorType = new (message: string, fields: ApiErrorFields & { detail?: string }) => HttpError;

const BY_STATUS: Record<number, ErrorType> = {
  400: BadRequestError,
  401: AuthenticationError,
  403: PermissionDeniedError,
  404: NotFoundError,
  409: ConflictError,
  422: UnprocessableError,
  429: RateLimitedError,
};

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;

/** Map on status first, then read the body best-effort. */
export function toError({ status, headers, text, json }: ErrorContext): ApiError {
  const type = BY_STATUS[status] ?? (status >= 500 ? ServerError : HttpError);
  const error = isObject(json) ? json['error'] : undefined;
  const detail = typeof error === 'string' ? error : undefined;
  return new type(`HTTP ${status}${detail === undefined ? '' : `: ${detail}`}`, {
    status,
    rawBody: text,
    detail,
    retryAfter: headers.get('retry-after') ?? undefined,
  });
}

export { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError };
