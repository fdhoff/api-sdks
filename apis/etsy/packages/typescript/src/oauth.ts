// OAuth 2 authorization code flow with PKCE, as Etsy implements it.
import { DecodeError, type AuthRequest, type Credentials, type Operation, type Transport } from './runtime/index.js';

export const AUTHORIZATION_URL = 'https://www.etsy.com/oauth/connect';
const VERIFIER = /^[A-Za-z0-9\-._~]{43,128}$/;
const REMEMBERED = 16;
const TOKEN_FIELDS = ['grant_type', 'client_id', 'redirect_uri', 'code', 'code_verifier', 'refresh_token'];

const TOKEN: Operation = {
  id: 'oauthToken',
  method: 'POST',
  path: '/v3/public/oauth/token',
  resource: 'oauth',
  name: 'token',
  params: TOKEN_FIELDS.map((name) => ({ wire: name, name, location: 'urlencoded' })),
  returnsJson: true,
  security: [],
};

/** An access token and the refresh token that replaces it. Etsy prefixes both with the user's ID. */
export interface Token {
  readonly accessToken: string;
  readonly refreshToken: string;
  /** Seconds the access token lasts, when Etsy says. */
  readonly expiresIn?: number;
  readonly tokenType: string;
  /** The numeric prefix of the access token, when it has one. */
  readonly userId?: number;
}

/** Called with every new token pair, so you can store it. The previous refresh token stops working. */
export type TokenCallback = (token: Token) => void | Promise<void>;

/**
 * Send the user to `url`. Keep `state` and `codeVerifier` until Etsy redirects back, check that the redirect's
 * `state` matches, then pass its `code` and this `codeVerifier` to `exchangeCode`.
 */
export interface AuthorizationRequest {
  readonly url: string;
  readonly state: string;
  readonly codeVerifier: string;
}

export interface AuthorizationOptions {
  /** Defaults to a fresh random value. */
  state?: string;
  /** Defaults to a fresh random value: 43 to 128 unreserved characters. */
  codeVerifier?: string;
}

function base64Url(bytes: Uint8Array): string {
  return btoa(String.fromCharCode(...bytes))
    .replaceAll('+', '-')
    .replaceAll('/', '_')
    .replace(/=+$/, '');
}

const randomText = (length: number): string => base64Url(crypto.getRandomValues(new Uint8Array(length)));

/** The S256 challenge for a PKCE code verifier. */
export async function codeChallenge(codeVerifier: string): Promise<string> {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(codeVerifier));
  return base64Url(new Uint8Array(digest));
}

/** Build the URL that asks a user to grant your app `scopes`, with a fresh state and PKCE verifier unless you
 * pass your own. */
export async function authorizationUrl(
  apiKey: string,
  redirectUri: string,
  scopes: readonly string[],
  { state = randomText(32), codeVerifier = randomText(64) }: AuthorizationOptions = {},
): Promise<AuthorizationRequest> {
  if (scopes.length === 0) throw new TypeError('Request at least one scope');
  if (!VERIFIER.test(codeVerifier)) throw new TypeError('codeVerifier must be 43 to 128 unreserved characters');
  const query = new URLSearchParams({
    response_type: 'code',
    client_id: apiKey,
    redirect_uri: redirectUri,
    scope: scopes.join(' '),
    state,
    code_challenge: await codeChallenge(codeVerifier),
    code_challenge_method: 'S256',
  });
  return { url: `${AUTHORIZATION_URL}?${query}`, state, codeVerifier };
}

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;

function toToken(reply: unknown): Token {
  const fields = isObject(reply) ? reply : {};
  const { access_token: access, refresh_token: refresh, expires_in: expires, token_type: type } = fields;
  if (typeof access !== 'string' || typeof refresh !== 'string' || !access || !refresh) {
    throw new DecodeError('The token response has no access and refresh token');
  }
  const prefix = access.split('.', 1)[0] ?? '';
  return {
    accessToken: access,
    refreshToken: refresh,
    expiresIn: Number.isInteger(expires) ? (expires as number) : undefined,
    tokenType: typeof type === 'string' ? type : 'Bearer',
    userId: /^\d+$/.test(prefix) ? Number(prefix) : undefined,
  };
}

const needs = (operation: Operation, scheme: string): boolean =>
  operation.security?.some((requirement) => requirement.some((part) => part.scheme === scheme)) ?? false;

export interface CredentialOptions {
  apiKey: string;
  sharedSecret: string;
  accessToken?: string;
  refreshToken?: string;
  onToken?: TokenCallback;
}

/** Sends `x-api-key` on every operation and the access token on those that need OAuth. After a 401 on one of
 * those, refreshes the access token once, when there is a refresh token. */
export class EtsyCredentials implements Credentials {
  readonly apiKey: string;
  readonly #sharedSecret: string;
  readonly #onToken: TokenCallback | undefined;
  readonly #seen: string[];
  #accessToken: string | undefined;
  #refreshToken: string | undefined;
  readonly #refresher: (() => Promise<Token>) | undefined;

  constructor(
    { apiKey, sharedSecret, accessToken, refreshToken, onToken }: CredentialOptions,
    refresher?: () => Promise<Token>,
  ) {
    if (!apiKey || !sharedSecret) throw new TypeError('apiKey and sharedSecret are required');
    this.apiKey = apiKey;
    this.#sharedSecret = sharedSecret;
    this.#accessToken = accessToken || undefined;
    this.#refreshToken = refreshToken || undefined;
    this.#onToken = onToken;
    this.#refresher = refresher;
    this.#seen = [accessToken, refreshToken].filter((value): value is string => Boolean(value));
  }

  get refreshToken(): string | undefined {
    return this.#refreshToken;
  }

  apply({ operation, headers }: AuthRequest): void {
    if (needs(operation, 'api_key')) headers.set('x-api-key', `${this.apiKey}:${this.#sharedSecret}`);
    if (this.#accessToken && needs(operation, 'oauth2')) headers.set('Authorization', `Bearer ${this.#accessToken}`);
  }

  secrets(): readonly string[] {
    return [this.apiKey, this.#sharedSecret, ...this.#seen];
  }

  /** Keep values out of logs and errors from now on, such as a code about to be exchanged. Only the most recent
   * values are kept, so a long-lived client does not grow. */
  remember(...values: string[]): void {
    this.#seen.push(...values.filter(Boolean));
    this.#seen.splice(0, Math.max(0, this.#seen.length - REMEMBERED));
  }

  async store(token: Token): Promise<Token> {
    this.remember(token.accessToken, token.refreshToken);
    this.#accessToken = token.accessToken;
    this.#refreshToken = token.refreshToken;
    await this.#onToken?.(token);
    return token;
  }

  async refresh({ operation }: AuthRequest): Promise<boolean> {
    if (this.#refresher === undefined || !this.#refreshToken || !needs(operation, 'oauth2')) return false;
    await this.#refresher();
    return true;
  }
}

/** OAuth 2 for a client. A token it obtains is used for the client's later calls, and is passed to the client's
 * `onToken` callback for you to store. */
export class OAuth {
  readonly #credentials: EtsyCredentials;
  readonly #transport: Transport;
  #refreshing: Promise<Token> | undefined;

  constructor(credentials: EtsyCredentials, transport: Transport) {
    this.#credentials = credentials;
    this.#transport = transport;
  }

  /** Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`. */
  authorizationUrl(
    redirectUri: string,
    scopes: readonly string[],
    options: AuthorizationOptions = {},
  ): Promise<AuthorizationRequest> {
    return authorizationUrl(this.#credentials.apiKey, redirectUri, scopes, options);
  }

  /** Trade the code from Etsy's redirect for a token. `redirectUri` must match the authorization URL's. */
  exchangeCode(
    code: string,
    { codeVerifier, redirectUri }: { codeVerifier: string; redirectUri: string },
  ): Promise<Token> {
    this.#credentials.remember(code, codeVerifier);
    return this.#request({
      grant_type: 'authorization_code',
      client_id: this.#credentials.apiKey,
      redirect_uri: redirectUri,
      code,
      code_verifier: codeVerifier,
    });
  }

  /** Replace the access token now. The client also does this itself after a 401. A refresh asked for while
   * another is under way shares it, since each refresh token works only once. */
  refresh(): Promise<Token> {
    this.#refreshing ??= this.#refresh().finally(() => {
      this.#refreshing = undefined;
    });
    return this.#refreshing;
  }

  async #refresh(): Promise<Token> {
    const refreshToken = this.#credentials.refreshToken;
    if (!refreshToken) throw new TypeError('There is no refresh token: pass refreshToken, or exchange a code first');
    return this.#request({
      grant_type: 'refresh_token',
      client_id: this.#credentials.apiKey,
      refresh_token: refreshToken,
    });
  }

  async #request(params: Record<string, string>): Promise<Token> {
    const reply = await this.#transport.fetch(TOKEN, undefined, params);
    return this.#credentials.store(toToken(reply));
  }
}
