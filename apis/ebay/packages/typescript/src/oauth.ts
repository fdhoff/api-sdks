// OAuth 2 as eBay implements it: application tokens from the client credentials grant, and user tokens from the
// authorization code grant, both from one token endpoint with HTTP Basic client authentication.
import { DecodeError, type AuthRequest, type Credentials, type Operation, type Transport } from './runtime/index.js';
import type { SigningKey } from './signing.js';

/** The scope of an application token, which the public operations accept. */
export const API_SCOPE = 'https://api.ebay.com/oauth/api_scope';

// The scopes eBay's client credentials grant gives. An operation that accepts any of them takes an application
// token, and every other operation a user token.
const APP_SCOPES: ReadonlySet<string> = new Set([API_SCOPE, `${API_SCOPE}/metadata.insights`]);

export type Environment = 'production' | 'sandbox';

export const AUTHORIZATION_URLS: Readonly<Record<Environment, string>> = {
  production: 'https://auth.ebay.com/oauth2/authorize',
  sandbox: 'https://auth.sandbox.ebay.com/oauth2/authorize',
};

// An application token this close to expiry is replaced before use.
const EXPIRY_MARGIN_MS = 60_000;
const REMEMBERED = 16;
const TOKEN_FIELDS = ['grant_type', 'code', 'redirect_uri', 'refresh_token', 'scope'];

export const TOKEN: Operation = {
  id: 'oauthToken',
  method: 'POST',
  path: '/identity/v1/oauth2/token',
  resource: 'oauth',
  name: 'token',
  host: 'api',
  params: TOKEN_FIELDS.map((name) => ({ wire: name, name, location: 'urlencoded' })),
  returnsJson: true,
  security: [],
};

/** An access token, and for a user token the refresh token that replaces it. eBay's refresh returns a new access
 * token only, so the refresh token carries over. */
export interface Token {
  readonly accessToken: string;
  /** Seconds the access token lasts, when eBay says. */
  readonly expiresIn?: number;
  readonly refreshToken?: string;
  readonly refreshTokenExpiresIn?: number;
  readonly tokenType: string;
}

/** Called with every new user token, so you can store it. */
export type TokenCallback = (token: Token) => void | Promise<void>;

/** Send the user to `url`. Keep `state` until eBay redirects to your RuName's accept URL, check that the redirect's
 * `state` matches, then pass its `code` to `exchangeCode`. */
export interface AuthorizationRequest {
  readonly url: string;
  readonly state: string;
}

export interface AuthorizationOptions {
  /** Defaults to a fresh random value. */
  state?: string;
  /** `login` makes the user sign in even if they already are. */
  prompt?: string;
}

function base64Url(bytes: Uint8Array): string {
  return btoa(String.fromCharCode(...bytes))
    .replaceAll('+', '-')
    .replaceAll('/', '_')
    .replace(/=+$/, '');
}

const randomText = (length: number): string => base64Url(crypto.getRandomValues(new Uint8Array(length)));

function checkEnvironment(environment: string): asserts environment is Environment {
  if (!Object.hasOwn(AUTHORIZATION_URLS, environment)) {
    const known = Object.keys(AUTHORIZATION_URLS).join(', ');
    throw new TypeError(`Unknown environment "${environment}"; expected one of: ${known}`);
  }
}

/** Build the URL that asks a user to grant your app `scopes`, with a fresh state unless you pass your own. `ruName`
 * is your app's redirect URL name, which eBay takes as `redirect_uri`. */
export function authorizationUrl(
  clientId: string,
  ruName: string,
  scopes: readonly string[],
  {
    state = randomText(32),
    prompt,
    environment = 'production',
  }: AuthorizationOptions & { environment?: Environment } = {},
): AuthorizationRequest {
  if (scopes.length === 0) throw new TypeError('Request at least one scope');
  checkEnvironment(environment);
  const query = new URLSearchParams({
    client_id: clientId,
    redirect_uri: ruName,
    response_type: 'code',
    scope: scopes.join(' '),
    state,
  });
  if (prompt !== undefined) query.set('prompt', prompt);
  return { url: `${AUTHORIZATION_URLS[environment]}?${query}`, state };
}

/** eBay lists the scopes an operation accepts, any one of which is enough. */
export const takesAppToken = (operation: Operation): boolean =>
  operation.security?.some((requirement) =>
    requirement.some((part) => part.scopes.some((scope) => APP_SCOPES.has(scope))),
  ) ?? false;

const isObject = (value: unknown): value is Record<string, unknown> => typeof value === 'object' && value !== null;
const integer = (value: unknown): number | undefined => (Number.isInteger(value) ? (value as number) : undefined);

function toToken(reply: unknown): Token {
  const fields = isObject(reply) ? reply : {};
  const { access_token: access, refresh_token: refresh, token_type: type } = fields;
  if (typeof access !== 'string' || !access) throw new DecodeError('The token response has no access token');
  return {
    accessToken: access,
    expiresIn: integer(fields['expires_in']),
    refreshToken: typeof refresh === 'string' && refresh ? refresh : undefined,
    refreshTokenExpiresIn: integer(fields['refresh_token_expires_in']),
    tokenType: typeof type === 'string' ? type : 'Bearer',
  };
}

export interface CredentialOptions {
  clientId?: string;
  clientSecret?: string;
  appToken?: string;
  userToken?: string;
  refreshToken?: string;
  onToken?: TokenCallback;
  signingKey?: SigningKey;
}

/**
 * Sends an application token on operations that accept one and a user token on the rest, then signs the request
 * when there is a signing key. Mints an application token when there is none or it is about to expire. After a 401,
 * mints a new application token, or refreshes the user token once when there is a refresh token.
 */
export class EbayCredentials implements Credentials {
  readonly clientId: string | undefined;
  readonly #clientSecret: string | undefined;
  readonly #basic: string | undefined;
  readonly #onToken: TokenCallback | undefined;
  readonly #signingKey: SigningKey | undefined;
  readonly #now: () => number;
  readonly #seen: string[] = [];
  #appToken: string | undefined;
  #appExpiresAt: number | undefined;
  #userToken: string | undefined;
  #refreshToken: string | undefined;
  /** Set by the client to its OAuth's `appToken` and `refresh`. */
  minter?: () => Promise<Token>;
  refresher?: () => Promise<Token>;

  constructor(
    { clientId, clientSecret, appToken, userToken, refreshToken, onToken, signingKey }: CredentialOptions,
    now: () => number = Date.now,
  ) {
    if (Boolean(clientId) !== Boolean(clientSecret)) throw new TypeError('Pass clientId and clientSecret together');
    if (!(clientId || appToken || userToken || refreshToken)) {
      throw new TypeError('Pass clientId and clientSecret, or a token');
    }
    this.clientId = clientId || undefined;
    this.#clientSecret = clientSecret || undefined;
    this.#basic = clientId && clientSecret ? btoa(`${clientId}:${clientSecret}`) : undefined;
    this.#appToken = appToken || undefined;
    this.#userToken = userToken || undefined;
    this.#refreshToken = refreshToken || undefined;
    this.#onToken = onToken;
    this.#signingKey = signingKey;
    this.#now = now;
  }

  get canMint(): boolean {
    return this.#basic !== undefined;
  }

  get userToken(): string | undefined {
    return this.#userToken;
  }

  get refreshToken(): string | undefined {
    return this.#refreshToken;
  }

  /** The application token, unless it is about to expire. A token passed in has no known expiry. */
  freshAppToken(): string | undefined {
    const expires = this.#appExpiresAt;
    if (this.#appToken && (expires === undefined || this.#now() < expires - EXPIRY_MARGIN_MS)) return this.#appToken;
    return undefined;
  }

  async apply(request: AuthRequest): Promise<void> {
    const { operation, headers } = request;
    if (operation === TOKEN) {
      if (this.#basic === undefined) throw new TypeError('A token request needs clientId and clientSecret');
      headers.set('Authorization', `Basic ${this.#basic}`);
      return;
    }
    let token: string | undefined;
    if (takesAppToken(operation)) {
      token = this.freshAppToken();
      if (token === undefined && this.canMint && this.minter) token = (await this.minter()).accessToken;
      token ??= this.#userToken;
      if (token === undefined) {
        throw new TypeError(`${operation.id} needs an application token: pass clientId and clientSecret, or appToken`);
      }
    } else {
      token = this.#userToken;
      if (token === undefined) {
        throw new TypeError(`${operation.id} needs a user token: pass userToken, or call oauth.exchangeCode first`);
      }
    }
    headers.set('Authorization', `Bearer ${token}`);
    if (this.#signingKey) {
      headers.set('x-ebay-signature-key', this.#signingKey.jwe);
      await this.#signingKey.signer.sign(request);
    }
  }

  secrets(): readonly string[] {
    const current = [this.#clientSecret, this.#basic, this.#appToken, this.#userToken, this.#refreshToken];
    const signing = this.#signingKey?.secrets() ?? [];
    return [...current, ...signing, ...this.#seen].filter((value): value is string => Boolean(value));
  }

  /** Keep values out of logs and errors from now on, such as a code about to be exchanged. Only the most recent
   * values are kept, so a long-lived client does not grow. */
  remember(...values: (string | undefined)[]): void {
    this.#seen.push(...values.filter((value): value is string => Boolean(value)));
    this.#seen.splice(0, Math.max(0, this.#seen.length - REMEMBERED));
  }

  storeApp(token: Token): Token {
    this.remember(this.#appToken);
    this.#appToken = token.accessToken;
    this.#appExpiresAt = token.expiresIn === undefined ? undefined : this.#now() + token.expiresIn * 1000;
    return token;
  }

  /** Keeps the refresh token when the response has none, as eBay's refresh does not return one. */
  async storeUser(token: Token): Promise<Token> {
    const kept = token.refreshToken ? token : { ...token, refreshToken: this.#refreshToken };
    this.remember(this.#userToken, this.#refreshToken);
    this.#userToken = kept.accessToken;
    this.#refreshToken = kept.refreshToken;
    await this.#onToken?.(kept);
    return kept;
  }

  /** Whether a 401 on `operation` replaces the application token rather than the user token. */
  #refreshesApp(operation: Operation): boolean {
    return takesAppToken(operation) && (this.canMint || this.#appToken !== undefined);
  }

  /** An application token and a user token refresh separately, so a 401 on one never waits out a refresh of the
   * other. */
  refreshGroup(operation: Operation): string {
    return this.#refreshesApp(operation) ? 'app' : 'user';
  }

  async refresh({ operation }: AuthRequest): Promise<boolean> {
    if (this.#refreshesApp(operation)) {
      if (!this.canMint || !this.minter) return false;
      this.#appExpiresAt = -Infinity;
      await this.minter();
      return true;
    }
    if (!this.#refreshToken || !this.refresher) return false;
    await this.refresher();
    return true;
  }
}

export interface OAuthConfig {
  ruName?: string;
  appScopes: readonly string[];
  userScopes?: readonly string[];
  environment: Environment;
}

/** OAuth 2 for a client. Tokens it obtains are used for the client's later calls, and each new user token is passed
 * to the client's `onToken` callback for you to store. A refresh waits for that callback, so it must not call these
 * methods. */
export class OAuth {
  readonly #credentials: EbayCredentials;
  readonly #transport: Transport;
  readonly #config: OAuthConfig;
  #minting: Promise<Token> | undefined;
  #refreshing: Promise<Token> | undefined;

  constructor(credentials: EbayCredentials, transport: Transport, config: OAuthConfig) {
    checkEnvironment(config.environment);
    this.#credentials = credentials;
    this.#transport = transport;
    this.#config = config;
  }

  #ruName(): string {
    if (!this.#config.ruName) throw new TypeError('Pass ruName to the client to use the authorization code grant');
    return this.#config.ruName;
  }

  /** Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`. */
  authorizationUrl(scopes: readonly string[], options: AuthorizationOptions = {}): AuthorizationRequest {
    const { clientId } = this.#credentials;
    if (!clientId)
      throw new TypeError('Pass clientId and clientSecret to the client to use the authorization code grant');
    return authorizationUrl(clientId, this.#ruName(), scopes, { ...options, environment: this.#config.environment });
  }

  /** Trade the code from eBay's redirect for a user token and its refresh token. */
  async exchangeCode(code: string): Promise<Token> {
    this.#credentials.remember(code);
    const params = { grant_type: 'authorization_code', code, redirect_uri: this.#ruName() };
    return this.#credentials.storeUser(toToken(await this.#transport.fetch(TOKEN, undefined, params)));
  }

  /** Replace the user token now. The client also does this itself after a 401. `scopes` must be the original
   * grant's or fewer, and default to the client's `userScopes`. A refresh asked for while another is under way
   * shares it. */
  refresh(scopes?: readonly string[]): Promise<Token> {
    this.#refreshing ??= this.#refresh(scopes).finally(() => {
      this.#refreshing = undefined;
    });
    return this.#refreshing;
  }

  async #refresh(scopes: readonly string[] | undefined): Promise<Token> {
    const refreshToken = this.#credentials.refreshToken;
    if (!refreshToken) throw new TypeError('There is no refresh token: pass refreshToken, or exchange a code first');
    const params: Record<string, string> = { grant_type: 'refresh_token', refresh_token: refreshToken };
    const chosen = scopes?.length ? scopes : this.#config.userScopes;
    if (chosen?.length) params['scope'] = chosen.join(' ');
    return this.#credentials.storeUser(toToken(await this.#transport.fetch(TOKEN, undefined, params)));
  }

  /** Mint an application token with the client's `appScopes`, unless the current one is still fresh. A mint asked
   * for while another is under way shares it. */
  appToken({ force = false }: { force?: boolean } = {}): Promise<Token> {
    const current = this.#credentials.freshAppToken();
    if (current !== undefined && !force) return Promise.resolve({ accessToken: current, tokenType: 'Bearer' });
    this.#minting ??= this.#mint().finally(() => {
      this.#minting = undefined;
    });
    return this.#minting;
  }

  async #mint(): Promise<Token> {
    const params = { grant_type: 'client_credentials', scope: this.#config.appScopes.join(' ') };
    return this.#credentials.storeApp(toToken(await this.#transport.fetch(TOKEN, undefined, params)));
  }
}
