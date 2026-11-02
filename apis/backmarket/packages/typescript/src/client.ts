import { toError } from './errors.js';
import { Resources } from './resources.js';
import { Transport, type Logger } from './runtime/index.js';

export type Region = 'ap' | 'eu' | 'na';
export type Environment = 'production' | 'preprod';

const SERVERS: Record<Region, Record<Environment, string>> = {
  ap: { production: 'https://www.backmarket.co.jp', preprod: 'https://preprod.backmarket.co.jp' },
  eu: { production: 'https://www.backmarket.fr', preprod: 'https://preprod.backmarket.fr' },
  na: { production: 'https://www.backmarket.com', preprod: 'https://preprod.backmarket.com' },
};

export interface ClientOptions {
  /** Your API token, sent verbatim. It is never stored beyond this client or logged. */
  token: string;
  /** Required, in the form `BM-{Company}-{Integration};contact@example.com`. */
  userAgent: string;
  /** Sent as `Accept-Language` on every call, for example `fr-fr`. */
  locale: string;
  /** The marketplace region. Pass this or `baseUrl`. */
  region?: Region;
  /** Defaults to production. */
  environment?: Environment;
  /** A server root, for tests against a mock. The token is sent to it. */
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
  /** Receives methods, URLs and statuses, never your token or response bodies. Silent by default. */
  logger?: Logger;
}

function serverUrl({ region, environment = 'production', baseUrl }: ClientOptions): string {
  if ((region === undefined) === (baseUrl === undefined)) throw new TypeError('Pass exactly one of region and baseUrl');
  if (baseUrl !== undefined) return baseUrl.replace(/\/+$/, '');
  const url = SERVERS[region as Region]?.[environment];
  if (url === undefined) throw new TypeError(`Unknown server: ${region} ${environment}`);
  return url;
}

function transport(options: ClientOptions): Transport {
  const { token, userAgent, locale } = options;
  if (!token) throw new TypeError('token is required');
  if (!userAgent) throw new TypeError('userAgent is required; the API may refuse a request without it');
  return new Transport({
    baseUrl: serverUrl(options),
    secret: token,
    headers: {
      Authorization: `Basic ${token}`,
      'User-Agent': userAgent,
      Accept: 'application/json',
      'Accept-Language': locale,
    },
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

/** Client for the Back Market Seller API. Unofficial; not affiliated with Back Market. */
export class BackMarketClient extends Resources {
  constructor(options: ClientOptions) {
    super(transport(options));
  }
}
