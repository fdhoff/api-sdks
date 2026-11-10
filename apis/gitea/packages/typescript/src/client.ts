import { toError } from './errors.js';
import { Resources } from './resources.js';
import { StaticCredentials, Transport, type Credentials, type Logger } from './runtime/index.js';

/** The path the client adds to the instance URL. */
export const API_PATH = '/api/v1';

export interface ClientOptions {
  /** Your Gitea instance's URL, such as `https://gitea.example.com`, or `https://example.com/git` for an instance
   * under a sub-path. There is no default. The client adds `/api/v1`. Your credentials are sent to it. */
  baseUrl: string;
  /** An access token, sent as `Authorization: token <token>`. Pass this, or `username` and `password`, or
   * `credentials`. */
  token?: string;
  /** Your username, for Basic authentication with `password`. */
  username?: string;
  /** Your password, for Basic authentication. */
  password?: string;
  /** A current one-time password, sent as `X-GITEA-OTP` with Basic authentication, when your account has
   * two-factor authentication on. */
  otp?: string;
  /** A user to act as, sent as `Sudo`, with a token or Basic authentication. Needs an admin's credentials. */
  sudo?: string;
  /** Your own credential provider, instead of the others. */
  credentials?: Credentials;
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
  /** Receives methods, URLs and statuses, never your credentials or response bodies. Silent by default. */
  logger?: Logger;
}

// TODO: OAuth2 bearer tokens, if users ask; a custom `credentials` can already send one.
function credentialsFor({ token, username, password, otp, sudo, credentials }: ClientOptions): Credentials {
  const basic = username !== undefined || password !== undefined;
  if ([token !== undefined, basic, credentials !== undefined].filter(Boolean).length !== 1)
    throw new TypeError('Pass exactly one of token, username and password, and credentials');
  if (credentials !== undefined) {
    if (otp !== undefined || sudo !== undefined)
      throw new TypeError('otp and sudo go with a token or username and password; a credentials provider sets its own');
    return credentials;
  }
  if (otp !== undefined && !basic) throw new TypeError('otp goes only with username and password');
  for (const [name, value] of Object.entries({ token, username, password, otp, sudo }))
    if (value === '') throw new TypeError(`${name} must not be empty`);
  const headers: Record<string, string> = {};
  const secrets: string[] = [];
  if (basic) {
    if (username === undefined || password === undefined) throw new TypeError('Pass both username and password');
    const encoded = Buffer.from(`${username}:${password}`).toString('base64');
    headers['Authorization'] = `Basic ${encoded}`;
    secrets.push(password, encoded);
    if (otp !== undefined) {
      headers['X-GITEA-OTP'] = otp;
      secrets.push(otp);
    }
  } else {
    headers['Authorization'] = `token ${token}`;
    secrets.push(token!);
  }
  if (sudo !== undefined) headers['Sudo'] = sudo;
  return new StaticCredentials(headers, secrets);
}

function apiUrl({ baseUrl }: ClientOptions): string {
  const url = URL.canParse(baseUrl) ? new URL(baseUrl) : undefined;
  if (!url || !['http:', 'https:'].includes(url.protocol) || !url.hostname)
    throw new TypeError("baseUrl must be your Gitea instance's URL, such as https://gitea.example.com");
  const root = baseUrl.replace(/\/+$/, '');
  if (root.endsWith(API_PATH))
    throw new TypeError(`baseUrl is the instance's URL; leave out ${API_PATH}, which the client adds`);
  return root + API_PATH;
}

function transport(options: ClientOptions): Transport {
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.userAgent) headers['User-Agent'] = options.userAgent;
  return new Transport({
    baseUrl: apiUrl(options),
    credentials: credentialsFor(options),
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

/** Client for a Gitea instance's API. Unofficial; not affiliated with, endorsed by or sponsored by the Gitea project
 * or Gitea Limited. Your token, password and one-time password are never stored beyond this client, and never
 * logged. */
export class GiteaClient extends Resources {
  constructor(options: ClientOptions) {
    super(transport(options));
  }
}
