import { toError } from './errors.js';
import { API_SCOPE, EbayCredentials, OAuth, type Environment, type TokenCallback } from './oauth.js';
import { selectHosts, Transport, type Logger } from './runtime/index.js';
import type { SigningKey } from './signing.js';
import { Resources as Account } from './account/resources.js';
import { Resources as AccountV2 } from './account-v2/resources.js';
import { Resources as Analytics } from './analytics/resources.js';
import { Resources as Feed } from './feed/resources.js';
import { Resources as Finances } from './finances/resources.js';
import { Resources as Fulfillment } from './fulfillment/resources.js';
import { Resources as Inventory } from './inventory/resources.js';
import { Resources as Marketing } from './marketing/resources.js';
import { Resources as Metadata } from './metadata/resources.js';
import { Resources as Negotiation } from './negotiation/resources.js';
import { Resources as Recommendation } from './recommendation/resources.js';
import { Resources as Stores } from './stores/resources.js';
import { Resources as PostOrder } from './post-order/resources.js';
import { Resources as Feedback } from './feedback/resources.js';
import { Resources as Identity } from './identity/resources.js';
import { Resources as Media } from './media/resources.js';
import { Resources as Message } from './message/resources.js';
import { Resources as Notification } from './notification/resources.js';
import { Resources as Taxonomy } from './taxonomy/resources.js';
import { Resources as DeveloperAnalytics } from './developer-analytics/resources.js';
import { Resources as KeyManagement } from './key-management/resources.js';

/** The base URL of each host the APIs use, by environment. */
export const ENVIRONMENTS = {
  production: { api: 'https://api.ebay.com', apiz: 'https://apiz.ebay.com', apim: 'https://apim.ebay.com' },
  sandbox: {
    api: 'https://api.sandbox.ebay.com',
    apiz: 'https://apiz.sandbox.ebay.com',
    apim: 'https://apim.sandbox.ebay.com',
  },
} as const satisfies Record<Environment, Record<string, string>>;

export type HostKey = keyof (typeof ENVIRONMENTS)['production'];

export interface ClientOptions {
  /** Your keyset's App ID. With `clientSecret`, the client mints application tokens itself and can exchange and
   * refresh user tokens. */
  clientId?: string;
  /** Your keyset's Cert ID. Sent with the App ID only to the token endpoint. */
  clientSecret?: string;
  /** Your app's redirect URL name, for the authorization code grant. */
  ruName?: string;
  /** An application token to use instead of minting one. */
  appToken?: string;
  /** A user access token, sent on operations that act for a seller. */
  userToken?: string;
  /** Lets the client replace an expired user token by itself, once per call. */
  refreshToken?: string;
  /** Called with every new user token, from `oauth.exchangeCode` and every refresh, so you can store it. The call
   * that caused the refresh waits for it, so it must not call `oauth` or make calls with this client, which would
   * never settle. */
  onToken?: TokenCallback;
  /** The scopes of minted application tokens, at least one. Defaults to `[API_SCOPE]`. */
  appScopes?: readonly string[];
  /** The scopes to ask for when refreshing a user token. eBay keeps the original grant's when this is not given. */
  userScopes?: readonly string[];
  /** Picks the API hosts and the authorization URL. Defaults to `production`. */
  environment?: Environment;
  /** Your own base URL for each of `api`, `apiz` and `apim`, such as a mock's, instead of the environment's.
   * Your credentials are sent to them. */
  hosts?: Readonly<Record<HostKey, string>>;
  /** Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes its own. */
  marketplaceId?: string;
  /** Sent as `Content-Language` on operations that take it, unless a call passes its own. */
  contentLanguage?: string;
  /** Signs every request, as eBay requires of EU and UK sellers on some calls. */
  signingKey?: SigningKey;
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

function headerDefaults({ marketplaceId, contentLanguage }: ClientOptions): Record<string, string> {
  const defaults: Record<string, string> = {};
  if (marketplaceId) defaults['X-EBAY-C-MARKETPLACE-ID'] = marketplaceId;
  if (contentLanguage) defaults['Content-Language'] = contentLanguage;
  return defaults;
}

function transport(options: ClientOptions, credentials: EbayCredentials, environment: Environment): Transport {
  const hosts = selectHosts(ENVIRONMENTS, environment, options.hosts);
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.userAgent) headers['User-Agent'] = options.userAgent;
  return new Transport({
    baseUrl: hosts['api']!,
    hosts,
    headerDefaults: headerDefaults(options),
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

/** Client for eBay's Sell, Commerce and Developer REST APIs, one property per API. Unofficial; not affiliated
 * with, endorsed by or sponsored by eBay Inc. */
export class EbayClient {
  readonly account: Account;
  readonly accountV2: AccountV2;
  readonly analytics: Analytics;
  readonly feed: Feed;
  readonly finances: Finances;
  readonly fulfillment: Fulfillment;
  readonly inventory: Inventory;
  readonly marketing: Marketing;
  readonly metadata: Metadata;
  readonly negotiation: Negotiation;
  readonly recommendation: Recommendation;
  readonly stores: Stores;
  readonly postOrder: PostOrder;
  readonly feedback: Feedback;
  readonly identity: Identity;
  readonly media: Media;
  readonly message: Message;
  readonly notification: Notification;
  readonly taxonomy: Taxonomy;
  readonly developerAnalytics: DeveloperAnalytics;
  readonly keyManagement: KeyManagement;
  /** The OAuth 2 flows: application tokens, the authorization URL, code exchange and refresh. */
  readonly oauth: OAuth;

  constructor(options: ClientOptions) {
    const environment = options.environment ?? 'production';
    const appScopes = options.appScopes ?? [API_SCOPE];
    if (!appScopes.some((scope) => scope.trim())) throw new TypeError('appScopes needs at least one scope');
    const credentials = new EbayCredentials(options);
    const shared = transport(options, credentials, environment);
    this.account = new Account(shared);
    this.accountV2 = new AccountV2(shared);
    this.analytics = new Analytics(shared);
    this.feed = new Feed(shared);
    this.finances = new Finances(shared);
    this.fulfillment = new Fulfillment(shared);
    this.inventory = new Inventory(shared);
    this.marketing = new Marketing(shared);
    this.metadata = new Metadata(shared);
    this.negotiation = new Negotiation(shared);
    this.recommendation = new Recommendation(shared);
    this.stores = new Stores(shared);
    this.postOrder = new PostOrder(shared);
    this.feedback = new Feedback(shared);
    this.identity = new Identity(shared);
    this.media = new Media(shared);
    this.message = new Message(shared);
    this.notification = new Notification(shared);
    this.taxonomy = new Taxonomy(shared);
    this.developerAnalytics = new DeveloperAnalytics(shared);
    this.keyManagement = new KeyManagement(shared);
    this.oauth = new OAuth(credentials, shared, {
      ruName: options.ruName,
      appScopes,
      userScopes: options.userScopes,
      environment,
    });
    credentials.minter = () => this.oauth.appToken();
    credentials.refresher = () => this.oauth.refresh();
  }
}
