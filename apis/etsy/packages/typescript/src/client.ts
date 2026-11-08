import { toError } from './errors.js';
import { EtsyCredentials, OAuth, type TokenCallback } from './oauth.js';
import { Resources } from './resources.js';
import { Transport, type Logger } from './runtime/index.js';

export const BASE_URL = 'https://openapi.etsy.com';

export interface ClientOptions {
  /** Your app's keystring. */
  apiKey: string;
  /** Your app's shared secret. Both are sent as `x-api-key` on every call, and never logged. */
  sharedSecret: string;
  /** An OAuth access token, sent verbatim as a bearer token on calls that need one. */
  accessToken?: string;
  /** Lets the client replace an expired access token by itself, once per call. */
  refreshToken?: string;
  /** Called with every new token pair, from `oauth.exchangeCode` and every refresh, so you can store it. The old
   * refresh token stops working. The call that caused the refresh waits for it. */
  onToken?: TokenCallback;
  /** Sent as `User-Agent`, when given. */
  userAgent?: string;
  /** The server root. Point it at a mock in tests; your credentials are sent to it. */
  baseUrl?: string;
  /** Milliseconds to wait on each attempt. Defaults to 30000. */
  timeoutMs?: number;
  /** Retries after the first attempt. Defaults to 3. */
  maxRetries?: number;
  /** Base in milliseconds of the exponential backoff. Defaults to 500. */
  retryBaseDelayMs?: number;
  /** Milliseconds to wait after a 429 with no usable `Retry-After`. Defaults to 10000. */
  rateLimitWaitMs?: number;
  /** Longest `Retry-After` to wait for, in milliseconds. A longer one throws at once. Defaults to 60000. */
  maxRetryWaitMs?: number;
  /** A `fetch` to use instead of the global one. */
  fetch?: typeof globalThis.fetch;
  /** Receives methods, URLs and statuses, never your credentials or response bodies. Silent by default. */
  logger?: Logger;
}

function transport(options: ClientOptions, credentials: EtsyCredentials): Transport {
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.userAgent) headers['User-Agent'] = options.userAgent;
  return new Transport({
    baseUrl: (options.baseUrl ?? BASE_URL).replace(/\/+$/, ''),
    credentials,
    headers,
    toError,
    fetch: options.fetch ?? globalThis.fetch,
    logger: options.logger,
    timeoutMs: options.timeoutMs ?? 30_000,
    maxRetries: options.maxRetries ?? 3,
    retryBaseDelayMs: options.retryBaseDelayMs ?? 500,
    rateLimitWaitMs: options.rateLimitWaitMs ?? 10_000,
    maxRetryWaitMs: options.maxRetryWaitMs ?? 60_000,
  });
}

/** Client for the Etsy Open API v3. Unofficial; not affiliated with Etsy. */
export class EtsyClient extends Resources {
  /** The OAuth 2 flow: authorization URL, code exchange and refresh. */
  readonly oauth: OAuth;

  constructor(options: ClientOptions) {
    const credentials = new EtsyCredentials(options);
    const shared = transport(options, credentials);
    super(shared);
    this.oauth = new OAuth(credentials, shared);
    credentials.refresher = () => this.oauth.refresh();
  }
}
