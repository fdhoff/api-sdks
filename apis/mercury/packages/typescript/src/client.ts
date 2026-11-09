import { toError } from './errors.js';
import { Resources } from './resources.js';
import { selectHosts, StaticCredentials, Transport, type Logger } from './runtime/index.js';

/** The base URL of each host the API uses, by environment. `vault` serves only `cards.reveal`. */
export const ENVIRONMENTS = {
  production: { api: 'https://api.mercury.com/api/v1', vault: 'https://vault-api.mercury.com/api/v1' },
  // Mercury documents no sandbox host for card details, so those calls go to the sandbox's own API host.
  sandbox: { api: 'https://api-sandbox.mercury.com/api/v1', vault: 'https://api-sandbox.mercury.com/api/v1' },
} as const;

export type Environment = keyof typeof ENVIRONMENTS;
export type HostKey = keyof (typeof ENVIRONMENTS)['production'];

export interface ClientOptions {
  /** Your API token, sent verbatim as a bearer token. The `secret-token:` prefix is part of it. It is never stored
   * beyond this client or logged. */
  token: string;
  /** `production` or `sandbox`. A sandbox token works only in the sandbox. Defaults to `production`. */
  environment?: Environment;
  /** Your own base URL for each of `api` and `vault`, such as a mock's, instead of the environment's. The token is
   * sent to them. */
  hosts?: Readonly<Record<HostKey, string>>;
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
  /** A `fetch` to use instead of the global one. */
  fetch?: typeof globalThis.fetch;
  /** Receives methods, URLs and statuses, never your token or response bodies. Silent by default. */
  logger?: Logger;
}

function transport(options: ClientOptions): Transport {
  if (!options.token) throw new TypeError('token is required');
  const hosts = selectHosts(ENVIRONMENTS, options.environment ?? 'production', options.hosts);
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.userAgent) headers['User-Agent'] = options.userAgent;
  return new Transport({
    baseUrl: hosts['api']!,
    hosts,
    credentials: new StaticCredentials({ Authorization: `Bearer ${options.token}` }, [options.token]),
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

/** Client for the Mercury API. Unofficial; not affiliated with, endorsed by or sponsored by Mercury Technologies,
 * Inc. */
export class MercuryClient extends Resources {
  constructor(options: ClientOptions) {
    super(transport(options));
  }
}
