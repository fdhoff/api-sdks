import {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  DecodeError,
  type ApiErrorFields,
  type ErrorContext,
} from './runtime/index.js';

export interface ErrorParameter {
  readonly name?: string;
  readonly value?: string;
}

/** One entry of an eBay error response's `errors` list. */
export interface ErrorDetail {
  readonly errorId?: number;
  readonly domain?: string;
  readonly subdomain?: string;
  readonly category?: string;
  readonly message?: string;
  readonly longMessage?: string;
  readonly parameters: readonly ErrorParameter[];
}

interface HttpErrorFields extends ApiErrorFields {
  detail?: string;
  errors?: readonly ErrorDetail[];
}

/** A response with an error status. `errors` holds the body's `errors` list, and `detail` and `code` are the
 * first entry's `message` and `errorId`, when the body has them. */
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
  readonly errors: readonly ErrorDetail[];

  constructor(message: string, fields: HttpErrorFields = {}) {
    super(message, fields);
    this.detail = fields.detail;
    this.errors = fields.errors ?? [];
  }
}

/** HTTP 400. */
export class BadRequestError extends HttpError {
  override readonly kind = 'bad_request';
}

/** HTTP 401, after any new token. */
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

type ErrorType = new (message: string, fields: HttpErrorFields) => HttpError;

const BY_STATUS: Record<number, ErrorType> = {
  400: BadRequestError,
  401: AuthenticationError,
  403: PermissionDeniedError,
  404: NotFoundError,
  409: ConflictError,
  422: UnprocessableError,
  429: RateLimitedError,
};

const isObject = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);
const text = (value: unknown): string | undefined => (typeof value === 'string' ? value : undefined);

function parameters(value: unknown): ErrorParameter[] {
  if (!Array.isArray(value)) return [];
  return value.filter(isObject).map((item) => ({ name: text(item['name']), value: text(item['value']) }));
}

/** The `errors` list of a body, best-effort: fields of the wrong type read as undefined. */
export function errorDetails(body: unknown): ErrorDetail[] {
  const items = isObject(body) ? body['errors'] : undefined;
  if (!Array.isArray(items)) return [];
  return items.filter(isObject).map((item) => ({
    errorId: Number.isInteger(item['errorId']) ? (item['errorId'] as number) : undefined,
    domain: text(item['domain']),
    subdomain: text(item['subdomain']),
    category: text(item['category']),
    message: text(item['message']),
    longMessage: text(item['longMessage']),
    parameters: parameters(item['parameters']),
  }));
}

/** Map on status first, then read the body best-effort. */
export function toError({ status, headers, text: body, json }: ErrorContext): ApiError {
  const type = BY_STATUS[status] ?? (status >= 500 ? ServerError : HttpError);
  const errors = errorDetails(json);
  const detail = errors[0]?.message;
  const error = new type('', {
    status,
    rawBody: body,
    detail,
    errors,
    code: errors[0]?.errorId,
    retryAfter: headers.get('retry-after') ?? undefined,
  });
  error.message = `HTTP ${status} (${error.kind})${detail ? `: ${detail}` : ''}`;
  return error;
}

export { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError };
