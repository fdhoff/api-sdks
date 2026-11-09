import { toError } from './errors.js';
import { Resources } from './resources.js';
import {
  StaticCredentials,
  Transport,
  type Credentials,
  type Download,
  type Logger,
  type RequestOptions,
} from './runtime/index.js';

export interface ClientOptions {
  /** Your operator's Mirakl instance, such as `https://your-operator.mirakl.net`, from its seller back office. Every
   * operator runs its own, so there is no default. Your key is sent to it. */
  baseUrl: string;
  /** Your shop API key, sent as the whole `Authorization` header with no scheme. It is never stored beyond this
   * client or logged. Pass this or `credentials`. */
  apiKey?: string;
  /** Your own credential provider, instead of `apiKey`. */
  credentials?: Credentials;
  /** The shop to act for, when your key covers several. Sent as `shop_id` on every call that leaves it unset. */
  shopId?: number | string;
  /** Sent as `User-Agent`, when given. */
  userAgent?: string;
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
  /** A `fetch` to use instead of the global one. It must return a redirect as it is when asked for
   * `redirect: 'manual'`, as Node's does, so that `downloadUrl` decides where your key goes. */
  fetch?: typeof globalThis.fetch;
  /** Receives methods, URLs and statuses, never your key or response bodies. Silent by default. */
  logger?: Logger;
}

// TODO: partner OAuth2 client-credentials tokens, if users ask; a custom `credentials` can already send one.
function credentialsFor({ apiKey, credentials }: ClientOptions): Credentials {
  if ((apiKey === undefined) === (credentials === undefined))
    throw new TypeError('Pass exactly one of apiKey and credentials');
  if (credentials !== undefined) return credentials;
  if (!apiKey) throw new TypeError('apiKey must not be empty');
  return new StaticCredentials({ Authorization: apiKey }, [apiKey]);
}

function baseUrlOf({ baseUrl }: ClientOptions): string {
  if (!baseUrl) throw new TypeError("baseUrl is required: your operator's Mirakl instance");
  const protocol = URL.canParse(baseUrl) ? new URL(baseUrl).protocol : '';
  if (!['http:', 'https:'].includes(protocol)) throw new TypeError('baseUrl must be an http or https URL');
  return baseUrl.replace(/\/+$/, '');
}

function transport(options: ClientOptions): Transport {
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.userAgent) headers['User-Agent'] = options.userAgent;
  return new Transport({
    baseUrl: baseUrlOf(options),
    credentials: credentialsFor(options),
    queryDefaults: options.shopId === undefined ? {} : { shop_id: String(options.shopId) },
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

/** Client for a Mirakl operator's seller API. Unofficial; not affiliated with, endorsed by or sponsored by Mirakl
 * SAS. */
export class MiraklClient extends Resources {
  readonly #transport: Transport;

  constructor(options: ClientOptions) {
    const shared = transport(options);
    super(shared);
    this.#transport = shared;
  }

  /** Download a file from a URL an export status returned, such as `offers.waitForExport`'s `urls`. Your key goes
   * only to `baseUrl`'s scheme, host and port, and never again once a redirect leaves them. */
  downloadUrl(url: string, options?: RequestOptions): Promise<Download> {
    return this.#transport.downloadUrl(url, options);
  }
}
