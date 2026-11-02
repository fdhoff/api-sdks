export interface ApiErrorFields {
  status?: number;
  rawBody?: string;
  code?: unknown;
  requestId?: string;
  retryAfter?: string;
  cfRay?: string;
}

/** Base class for every error the client throws. */
export class ApiError extends Error {
  readonly kind: string = 'api';
  readonly status?: number;
  readonly rawBody?: string;
  readonly code?: unknown;
  readonly requestId?: string;
  readonly retryAfter?: string;
  readonly cfRay?: string;

  constructor(message: string, fields: ApiErrorFields = {}) {
    super(message);
    this.name = new.target.name;
    this.status = fields.status;
    this.rawBody = fields.rawBody;
    this.code = fields.code;
    this.requestId = fields.requestId;
    this.retryAfter = fields.retryAfter;
    this.cfRay = fields.cfRay;
  }
}

/** No response arrived in time, after retries. */
export class ApiTimeoutError extends ApiError {
  override readonly kind: string = 'timeout';
}

/** The connection failed or dropped before a full response, after retries. */
export class ApiConnectionError extends ApiError {
  override readonly kind: string = 'connection';
}

/** A success response could not be read as the API declares it. */
export class DecodeError extends ApiError {
  override readonly kind: string = 'decode';
}

/** A failed response, with the credential already removed from `text` and `json`. */
export interface ErrorContext {
  status: number;
  headers: Headers;
  text: string;
  json: unknown;
}
