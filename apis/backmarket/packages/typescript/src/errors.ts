import { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, type ErrorContext } from './runtime/index.js';

const BOT_CHALLENGE_CODE = 'bot-need-challenge';

/** HTTP 400. */
export class BadRequestError extends ApiError {
  override readonly kind = 'bad_request';
}

/** HTTP 401. */
export class AuthenticationError extends ApiError {
  override readonly kind = 'authentication';
}

/** HTTP 403 that is neither of the two below. */
export class PermissionDeniedError extends ApiError {
  override readonly kind: 'permission' | 'waf_blocked' | 'bot_challenge' = 'permission';
}

/** HTTP 403 HTML block from the firewall. Give `cfRay` to your seller contact. */
export class WafBlockedError extends PermissionDeniedError {
  override readonly kind = 'waf_blocked';
}

/** HTTP 403 from bot management. */
export class BotChallengeError extends PermissionDeniedError {
  override readonly kind = 'bot_challenge';
}

/** HTTP 404. */
export class NotFoundError extends ApiError {
  override readonly kind = 'not_found';
}

/** HTTP 422. */
export class UnprocessableError extends ApiError {
  override readonly kind = 'validation';
}

/** HTTP 429, after retries. */
export class RateLimitedError extends ApiError {
  override readonly kind = 'rate_limited';
}

/** HTTP 5xx, after retries. */
export class ServerError extends ApiError {
  override readonly kind = 'server';
}

/** Every error the client throws. Compare `kind`, and the type narrows to that class. */
export type ClientError =
  | (ApiError & { readonly kind: 'api' })
  | ApiConnectionError
  | ApiTimeoutError
  | AuthenticationError
  | BadRequestError
  | BotChallengeError
  | DecodeError
  | NotFoundError
  | PermissionDeniedError
  | RateLimitedError
  | ServerError
  | UnprocessableError
  | WafBlockedError;

/** The `kind` of every error the client throws. */
export type ErrorKind = ClientError['kind'];

type ErrorType = new (...args: ConstructorParameters<typeof ApiError>) => ApiError;

const BY_STATUS: Record<number, ErrorType> = {
  400: BadRequestError,
  401: AuthenticationError,
  404: NotFoundError,
  422: UnprocessableError,
  429: RateLimitedError,
};

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;

function firstErrorCode(body: unknown): unknown {
  const errors = isObject(body) ? body['errors'] : undefined;
  const first: unknown = Array.isArray(errors) ? errors[0] : undefined;
  return isObject(first) ? first['code'] : undefined;
}

function errorCode(body: unknown): unknown {
  const error = isObject(body) ? body['error'] : undefined;
  return (isObject(error) ? error['code'] : undefined) ?? firstErrorCode(body);
}

function errorType({ status, headers, json }: ErrorContext): ErrorType {
  if (status === 403) {
    if (firstErrorCode(json) === BOT_CHALLENGE_CODE) return BotChallengeError;
    return headers.get('cf-ray') && (json === undefined || json === null) ? WafBlockedError : PermissionDeniedError;
  }
  if (status >= 500) return ServerError;
  return BY_STATUS[status] ?? ApiError;
}

/** Map on status first, then read the body best-effort. */
export function toError(context: ErrorContext): ApiError {
  const { status, headers, text, json } = context;
  const code = errorCode(json);
  const requestId = isObject(json) ? json['requestId'] : undefined;
  return new (errorType(context))(`HTTP ${status}${code === undefined ? '' : `: ${String(code)}`}`, {
    status,
    rawBody: text,
    code,
    requestId: typeof requestId === 'string' ? requestId : undefined,
    retryAfter: headers.get('retry-after') ?? undefined,
    cfRay: headers.get('cf-ray') ?? undefined,
  });
}

export { ApiConnectionError, ApiError, ApiTimeoutError, DecodeError };
