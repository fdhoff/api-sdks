import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { test } from 'node:test';
import {
  AuthenticationError,
  authorizationUrl,
  BadRequestError,
  codeChallenge,
  ConflictError,
  DecodeError,
  EtsyClient,
  HttpError,
  NotFoundError,
  PermissionDeniedError,
  ServerError,
  UnprocessableError,
  type ClientOptions,
  type Token,
} from 'etsy-seller';
import { EtsyCredentials } from '../dist/esm/oauth.js';
import { OPERATIONS } from '../dist/esm/resources.js';

const BASE = 'http://mock.invalid';
const KEY = 'synthetic-keystring';
const SHARED = 'synthetic-shared-secret';
const ACCESS = '12345678.synthetic-access';
const REFRESH = '12345678.synthetic-refresh';
const NEW = { access_token: '12345678.synthetic-new-access', refresh_token: '12345678.synthetic-new-refresh' };
const TOKEN_PATH = '/v3/public/oauth/token';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;
type Sent = { url: URL; init: RequestInit; headers: Headers; body: string };

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

const tokenReply = () => json({ ...NEW, expires_in: 3600, token_type: 'Bearer' });

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const tokens: Token[] = [];
  const logs: string[] = [];
  const client = new EtsyClient({
    apiKey: KEY,
    sharedSecret: SHARED,
    baseUrl: BASE,
    retryBaseDelayMs: 1,
    onToken: (token) => void tokens.push(token),
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    fetch: async (input, init = {}) => {
      const url = new URL(String(input));
      const { body } = init;
      const text = typeof body === 'string' ? body : body ? new TextDecoder().decode(body as Uint8Array) : '';
      sent.push({ url, init, headers: new Headers(init.headers), body: text });
      return handler(url, init);
    },
    ...options,
  });
  return { client, sent, tokens, logs };
}

/** Accepts only the given access token on OAuth calls, and answers the token endpoint with a new pair. */
const accepting =
  (access: string): Handler =>
  (url, init) => {
    if (url.pathname === TOKEN_PATH) return tokenReply();
    const authorization = new Headers(init.headers).get('authorization');
    return authorization === `Bearer ${access}`
      ? json({ user_id: 12345678, shop_id: 1 })
      : json({ error: 'expired' }, 401);
  };

test('every operation has a public method', () => {
  const { client } = clientFor(() => json({}));
  assert.equal(OPERATIONS.size, 107);
  for (const operation of OPERATIONS.values()) {
    const resource = (client as unknown as Record<string, Record<string, unknown>>)[operation.resource];
    assert.equal(typeof resource?.[operation.name], 'function', operation.id);
    if (operation.iterator) assert.equal(typeof resource?.[operation.iterator], 'function', operation.id);
  }
});

test('key-only operations send no access token', async () => {
  const { client, sent } = clientFor(() => json({ listing_id: 1 }), { accessToken: ACCESS });
  await client.listings.get(1);
  assert.equal(sent[0]?.headers.get('x-api-key'), `${KEY}:${SHARED}`);
  assert.equal(sent[0]?.headers.get('authorization'), null);
});

test('OAuth operations send both headers', async () => {
  const { client, sent } = clientFor(() => json({ user_id: 1 }), { accessToken: ACCESS });
  await client.users.getMe();
  assert.equal(sent[0]?.headers.get('x-api-key'), `${KEY}:${SHARED}`);
  assert.equal(sent[0]?.headers.get('authorization'), `Bearer ${ACCESS}`);
});

test('form bodies are form-encoded, with repeated fields and query parameters apart', async () => {
  const { client, sent } = clientFor(() => json({ receipt_id: 2 }), { accessToken: ACCESS });
  await client.receipts.update(1, 2, { wasShipped: true, legacy: false });
  await client.listings.createDraft(1, {
    quantity: 1,
    title: 'Synthetic & mug',
    description: 'Synthetic',
    price: 1.5,
    whoMade: 'i_did',
    whenMade: 'made_to_order',
    taxonomyId: 1,
    tags: ['a', 'b'],
  });
  const [update, draft] = sent;
  assert.equal(update?.url.pathname, '/v3/application/shops/1/receipts/2');
  assert.equal(update?.url.search, '?legacy=false');
  assert.equal(update?.body, 'was_shipped=true');
  assert.match(update?.headers.get('content-type') ?? '', /^application\/x-www-form-urlencoded/);
  const fields = new URLSearchParams(draft?.body);
  assert.equal(fields.get('title'), 'Synthetic & mug');
  assert.equal(fields.get('who_made'), 'i_did');
  assert.deepEqual(fields.getAll('tags'), ['a', 'b']);
});

test('the offset iterator walks every page', async () => {
  const pages = [
    { count: 3, results: [{ listing_id: 1 }, { listing_id: 2 }] },
    { count: 3, results: [{ listing_id: 3 }] },
  ];
  const { client, sent } = clientFor(() => json(pages.shift()));
  const ids: unknown[] = [];
  for await (const listing of client.listings.iterActive({ limit: 2 })) ids.push(listing.listing_id);
  assert.deepEqual(ids, [1, 2, 3]);
  assert.deepEqual(
    sent.map(({ url }) => url.search),
    ['?limit=2', '?limit=2&offset=2'],
  );
});

test('errors carry the body message', async () => {
  const cases = [
    [400, BadRequestError, 'bad_request'],
    [401, AuthenticationError, 'authentication'],
    [403, PermissionDeniedError, 'permission'],
    [404, NotFoundError, 'not_found'],
    [409, ConflictError, 'conflict'],
    [422, UnprocessableError, 'validation'],
    [503, ServerError, 'server'],
    [418, HttpError, 'api'],
  ] as const;
  for (const [status, type, kind] of cases) {
    const { client } = clientFor(() => json({ error: 'Synthetic failure' }, status), { maxRetries: 0 });
    const error = await client.shops.get(1).catch((caught: unknown) => caught);
    assert.ok(error instanceof type, String(status));
    assert.equal(error.kind, kind);
    assert.equal(error.status, status);
    assert.equal(error.detail, 'Synthetic failure');
    assert.equal(error.rawBody, '{"error":"Synthetic failure"}');
  }
});

test('a 401 refreshes once, then retries with the new token', async () => {
  const { client, sent, tokens } = clientFor(accepting(NEW.access_token), {
    accessToken: ACCESS,
    refreshToken: REFRESH,
  });
  assert.deepEqual(await client.users.getMe(), { user_id: 12345678, shop_id: 1 });
  assert.deepEqual(
    sent.map(({ url }) => url.pathname),
    ['/v3/application/users/me', TOKEN_PATH, '/v3/application/users/me'],
  );
  const refresh = new URLSearchParams(sent[1]?.body);
  assert.equal(refresh.get('grant_type'), 'refresh_token');
  assert.equal(refresh.get('client_id'), KEY);
  assert.equal(refresh.get('refresh_token'), REFRESH);
  assert.equal(sent[1]?.headers.get('x-api-key'), null);
  assert.equal(sent[1]?.headers.get('authorization'), null);
  assert.equal(sent[2]?.headers.get('authorization'), `Bearer ${NEW.access_token}`);
  assert.deepEqual(tokens, [
    {
      accessToken: NEW.access_token,
      refreshToken: NEW.refresh_token,
      expiresIn: 3600,
      tokenType: 'Bearer',
      userId: 12345678,
    },
  ]);
});

test('a second 401 after a refresh is thrown', async () => {
  const { client, sent } = clientFor(accepting('never'), { accessToken: ACCESS, refreshToken: REFRESH });
  await assert.rejects(client.users.getMe(), AuthenticationError);
  assert.equal(sent.length, 3);
});

test('a 401 on a key-only operation does not refresh', async () => {
  const { client, sent } = clientFor(() => json({ error: 'invalid_key' }, 401), {
    accessToken: ACCESS,
    refreshToken: REFRESH,
  });
  await assert.rejects(client.listings.get(1), AuthenticationError);
  assert.equal(sent.length, 1);
});

test('without a refresh token a 401 is thrown', async () => {
  const { client, sent } = clientFor(accepting('never'), { accessToken: ACCESS });
  await assert.rejects(client.users.getMe(), AuthenticationError);
  assert.equal(sent.length, 1);
});

test('a failed refresh throws its own error, without the refresh token', async () => {
  const { client } = clientFor(
    (url) => (url.pathname === TOKEN_PATH ? json({ error: `invalid_grant ${REFRESH}` }, 400) : json({}, 401)),
    { accessToken: ACCESS, refreshToken: REFRESH },
  );
  const error = await client.users.getMe().catch((caught: unknown) => caught);
  assert.ok(error instanceof BadRequestError);
  assert.equal(error.detail, 'invalid_grant ***');
});

test('a 401 from the token endpoint is thrown without another refresh', async () => {
  const { client, sent } = clientFor(() => json({ error: 'invalid_client' }, 401), { refreshToken: REFRESH });
  await assert.rejects(client.oauth.refresh(), AuthenticationError);
  assert.equal(sent.length, 1);
});

test('a token response without tokens is a decode error', async () => {
  const { client } = clientFor(() => json({ access_token: ACCESS }), { refreshToken: REFRESH });
  await assert.rejects(client.oauth.refresh(), DecodeError);
});

test('refresh without a refresh token sends nothing', async () => {
  const { client, sent } = clientFor(tokenReply);
  await assert.rejects(client.oauth.refresh(), TypeError);
  assert.equal(sent.length, 0);
});

test('exchangeCode stores the token for later calls', async () => {
  const { client, sent, tokens } = clientFor(accepting(NEW.access_token));
  const token = await client.oauth.exchangeCode('synthetic-code', {
    codeVerifier: 'v'.repeat(43),
    redirectUri: 'https://example.com/callback',
  });
  assert.equal(token.userId, 12345678);
  assert.deepEqual(tokens, [token]);
  const fields = Object.fromEntries(new URLSearchParams(sent[0]?.body));
  assert.deepEqual(fields, {
    grant_type: 'authorization_code',
    client_id: KEY,
    redirect_uri: 'https://example.com/callback',
    code: 'synthetic-code',
    code_verifier: 'v'.repeat(43),
  });
  await client.users.getMe();
  assert.equal(sent[1]?.headers.get('authorization'), `Bearer ${NEW.access_token}`);
});

test('the client waits for onToken before retrying', async () => {
  const order: string[] = [];
  const { client } = clientFor(
    (url, init) => {
      order.push(url.pathname);
      return accepting(NEW.access_token)(url, init);
    },
    {
      accessToken: ACCESS,
      refreshToken: REFRESH,
      onToken: async () => {
        await new Promise((resolve) => setTimeout(resolve, 5));
        order.push('stored');
      },
    },
  );
  await client.users.getMe();
  assert.deepEqual(order, ['/v3/application/users/me', TOKEN_PATH, 'stored', '/v3/application/users/me']);
});

test('concurrent 401s share one refresh', async () => {
  const { client, sent } = clientFor(
    async (url, init) => {
      if (url.pathname === TOKEN_PATH) await new Promise((resolve) => setTimeout(resolve, 10));
      return accepting(NEW.access_token)(url, init);
    },
    { accessToken: ACCESS, refreshToken: REFRESH },
  );
  await Promise.all([1, 2, 3, 4].map(() => client.users.getMe()));
  assert.equal(sent.filter(({ url }) => url.pathname === TOKEN_PATH).length, 1);
});

test('an explicit refresh and a 401 share one token request', async () => {
  const { client, sent, tokens } = clientFor(
    async (url, init) => {
      if (url.pathname === TOKEN_PATH) await new Promise((resolve) => setTimeout(resolve, 10));
      return accepting(NEW.access_token)(url, init);
    },
    { accessToken: ACCESS, refreshToken: REFRESH },
  );
  const [token, me] = await Promise.all([client.oauth.refresh(), client.users.getMe()]);
  assert.equal(token.accessToken, NEW.access_token);
  assert.deepEqual(me, { user_id: 12345678, shop_id: 1 });
  const requests = sent.filter(({ url }) => url.pathname === TOKEN_PATH);
  assert.deepEqual(
    requests.map(({ body }) => new URLSearchParams(body).get('refresh_token')),
    [REFRESH],
  );
  assert.equal(tokens.length, 1);
});

test('credentials keep only recent values for redaction', () => {
  const credentials = new EtsyCredentials({ apiKey: KEY, sharedSecret: SHARED, accessToken: ACCESS });
  const values = Array.from({ length: 100 }, (_, index) => `synthetic-old-${index}`);
  credentials.remember(...values);
  const secrets = credentials.secrets();
  assert.ok(secrets.length < 20);
  assert.ok(secrets.includes(KEY) && secrets.includes(SHARED) && secrets.includes('synthetic-old-99'));
  assert.equal(secrets.includes(ACCESS), false);
  assert.equal('refresher' in credentials, false);
});

test('logs and errors never hold a secret', async () => {
  const code = 'synthetic-code';
  const verifier = 'w'.repeat(43);
  const echo: Handler = (url, init) => {
    const headers = new Headers(init.headers);
    const body = `${headers.get('x-api-key')} ${headers.get('authorization')} ${String(init.body)} ${url}`;
    return url.pathname === TOKEN_PATH ? tokenReply() : new Response(body, { status: 400 });
  };
  const { client, logs } = clientFor(echo, { accessToken: ACCESS, refreshToken: REFRESH });
  await client.oauth.exchangeCode(code, { codeVerifier: verifier, redirectUri: 'https://example.com/callback' });
  const error = await client.users.getMe().catch((caught: unknown) => caught);
  assert.ok(error instanceof BadRequestError);
  const output = `${error.message} ${error.rawBody} ${logs.join(' ')}`;
  for (const secret of [KEY, SHARED, ACCESS, REFRESH, NEW.access_token, NEW.refresh_token, code, verifier]) {
    assert.equal(output.includes(secret), false, secret);
  }
});

test('authorizationUrl uses PKCE S256 and a fresh state', async () => {
  const request = await authorizationUrl(KEY, 'https://example.com/callback', ['listings_r', 'shops_r']);
  const url = new URL(request.url);
  assert.equal(`${url.origin}${url.pathname}`, 'https://www.etsy.com/oauth/connect');
  const query = Object.fromEntries(url.searchParams);
  const challenge = createHash('sha256').update(request.codeVerifier).digest('base64url');
  assert.deepEqual(query, {
    response_type: 'code',
    client_id: KEY,
    redirect_uri: 'https://example.com/callback',
    scope: 'listings_r shops_r',
    state: request.state,
    code_challenge: challenge,
    code_challenge_method: 'S256',
  });
  assert.match(request.codeVerifier, /^[A-Za-z0-9_-]{43,128}$/);
  assert.ok(request.state.length >= 32);
  const other = await authorizationUrl(KEY, 'https://example.com/callback', ['shops_r']);
  assert.notEqual(other.state, request.state);
  assert.notEqual(other.codeVerifier, request.codeVerifier);
});

test('authorizationUrl keeps a given state and verifier, and rejects bad ones', async () => {
  const codeVerifier = 'dBjftJeZ4CVP-mJ92K9qYEvc4iBhsUKyIRmFh7mLjvbpFOD1yW_o2g';
  assert.equal(await codeChallenge(codeVerifier), createHash('sha256').update(codeVerifier).digest('base64url'));
  const { client } = clientFor(() => json({}));
  const request = await client.oauth.authorizationUrl('https://example.com/callback', ['shops_r'], {
    state: 'synthetic-state',
    codeVerifier,
  });
  assert.equal(request.state, 'synthetic-state');
  assert.equal(new URL(request.url).searchParams.get('client_id'), KEY);
  await assert.rejects(authorizationUrl(KEY, 'https://example.com/callback', []), TypeError);
  await assert.rejects(
    authorizationUrl(KEY, 'https://example.com/callback', ['shops_r'], { codeVerifier: 'short' }),
    TypeError,
  );
});

test('the key and shared secret are required', () => {
  assert.throws(() => new EtsyClient({ apiKey: '', sharedSecret: SHARED }), TypeError);
  assert.throws(() => new EtsyClient({ apiKey: KEY, sharedSecret: '' }), TypeError);
});
