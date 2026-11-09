import assert from 'node:assert/strict';
import { generateKeyPairSync } from 'node:crypto';
import { test } from 'node:test';
import {
  API_SCOPE,
  authorizationUrl,
  AuthenticationError,
  BadRequestError,
  DecodeError,
  EbayClient,
  HttpError,
  NotFoundError,
  ServerError,
  SigningKey,
  type ClientOptions,
  type Token,
} from 'ebay-sell';
import { OrdersApi, type Order } from 'ebay-sell/fulfillment';
import type { BaseCategoryTree } from 'ebay-sell/taxonomy';

const BASE = 'http://mock.invalid';
const HOSTS = { api: `${BASE}/api`, apiz: `${BASE}/apiz`, apim: `${BASE}/apim` };
const CLIENT_ID = 'synthetic-app-id';
const CLIENT_SECRET = 'synthetic-cert-id';
const BASIC = `Basic ${btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)}`;
const APP = 'synthetic-app-token';
const USER = 'synthetic-user-token';
const REFRESH = 'synthetic-refresh-token';
const TOKEN_PATH = '/api/identity/v1/oauth2/token';
const ORDERS_PATH = '/api/sell/fulfillment/v1/order';

type Handler = (url: URL, sent: Sent) => Response | Promise<Response>;
type Sent = { url: URL; headers: Headers; body: string };

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const tokens: Token[] = [];
  const logs: string[] = [];
  const client = new EbayClient({
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    hosts: HOSTS,
    retryBaseDelayMs: 1,
    onToken: (token) => void tokens.push(token),
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    fetch: async (input, init = {}) => {
      const url = new URL(String(input));
      const { body } = init;
      const text =
        typeof body === 'string'
          ? body
          : body instanceof URLSearchParams
            ? String(body)
            : body
              ? new TextDecoder().decode(body as Uint8Array)
              : '';
      const request = { url, headers: new Headers(init.headers), body: text };
      sent.push(request);
      return handler(url, request);
    },
    ...options,
  });
  return { client, sent, tokens, logs };
}

const form = (sent: Sent): Record<string, string> => Object.fromEntries(new URLSearchParams(sent.body));
const toTokenEndpoint = (sent: Sent[]): Sent[] => sent.filter(({ url }) => url.pathname === TOKEN_PATH);
const orders = (...ids: string[]) => ({ total: ids.length, orders: ids.map((orderId) => ({ orderId })) });

test('every operation has a public method', async () => {
  const { client } = clientFor(() => json({}));
  const contracts = Object.entries(client).filter(([name]) => name !== 'oauth');
  assert.equal(contracts.length, 20);
  let count = 0;
  for (const [name, resources] of contracts) {
    const dir = name.replace(/[A-Z]/g, (letter) => `-${letter.toLowerCase()}`);
    const { OPERATIONS } = await import(`../dist/esm/${dir}/resources.js`);
    for (const operation of OPERATIONS.values()) {
      const resource = (resources as Record<string, Record<string, unknown>>)[operation.resource];
      assert.equal(typeof resource?.[operation.name], 'function', operation.id);
      if (operation.iterator) assert.equal(typeof resource?.[operation.iterator], 'function', operation.id);
      count += 1;
    }
  }
  assert.equal(count, 310);
});

test('each API is a subpath export with its own classes', () => {
  const { client } = clientFor(() => json({}));
  assert.ok(client.fulfillment.orders instanceof OrdersApi);
});

test('an application token is minted with Basic authentication and reused while fresh', async () => {
  const { client, sent } = clientFor((url) =>
    url.pathname === TOKEN_PATH
      ? json({ access_token: APP, expires_in: 7200, token_type: 'Application Access Token' })
      : json({ categoryTreeId: '0' }),
  );
  const first: BaseCategoryTree | undefined = await client.taxonomy.categoryTrees.getDefaultId({
    marketplaceId: 'EBAY_US',
  });
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_GB' });
  assert.deepEqual(first, { categoryTreeId: '0' });
  const [mint, ...calls] = sent;
  assert.equal(mint?.url.pathname, TOKEN_PATH);
  assert.equal(mint?.headers.get('authorization'), BASIC);
  assert.match(mint?.headers.get('content-type') ?? '', /^application\/x-www-form-urlencoded/);
  assert.deepEqual(form(mint!), { grant_type: 'client_credentials', scope: API_SCOPE });
  assert.equal(calls.length, 2);
  for (const call of calls) assert.equal(call.headers.get('authorization'), `Bearer ${APP}`);
});

test('an application token about to expire is minted again', async () => {
  const { client, sent } = clientFor((url) =>
    url.pathname === TOKEN_PATH ? json({ access_token: APP, expires_in: 30 }) : json({ categoryTreeId: '0' }),
  );
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
  assert.equal(toTokenEndpoint(sent).length, 2);
});

test('concurrent calls share one mint', async () => {
  const { client, sent } = clientFor((url) =>
    url.pathname === TOKEN_PATH ? json({ access_token: APP, expires_in: 7200 }) : json({ categoryTreeId: '0' }),
  );
  await Promise.all([1, 2, 3].map(() => client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' })));
  assert.equal(toTokenEndpoint(sent).length, 1);
});

test('operations that act for a seller get the user token, and the others the application token', async () => {
  const { client, sent } = clientFor(() => json(orders()), { appToken: APP, userToken: USER });
  await client.fulfillment.orders.list();
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('authorization')),
    [`Bearer ${USER}`, `Bearer ${APP}`],
  );
});

test('without an application token or a way to mint one, the user token is sent', async () => {
  const { client, sent } = clientFor(() => json({}), {
    clientId: undefined,
    clientSecret: undefined,
    userToken: USER,
  });
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
  assert.equal(sent[0]?.headers.get('authorization'), `Bearer ${USER}`);
});

test('a call that needs a missing user token sends nothing', async () => {
  const { client, sent } = clientFor(() => json({}));
  await assert.rejects(client.fulfillment.orders.list(), /needs a user token/);
  assert.equal(sent.length, 0);
});

test('credentials are checked', () => {
  assert.throws(() => new EbayClient({ clientId: CLIENT_ID }), /together/);
  assert.throws(() => new EbayClient({}), /or a token/);
  assert.throws(() => new EbayClient({ userToken: USER, environment: 'staging' as 'sandbox' }), /Unknown environment/);
  assert.throws(
    () => new EbayClient({ userToken: USER, hosts: { api: BASE } as typeof HOSTS }),
    /lacks keys: apim, apiz/,
  );
});

test('a 401 refreshes the user token once, keeps the refresh token and retries', async () => {
  const fresh = 'synthetic-new-user-token';
  const { client, sent, tokens } = clientFor(
    (url, request) => {
      if (url.pathname === TOKEN_PATH) {
        return json({ access_token: fresh, expires_in: 7200, token_type: 'User Access Token' });
      }
      return request.headers.get('authorization') === `Bearer ${fresh}` ? json(orders('1')) : json({}, 401);
    },
    { userToken: USER, refreshToken: REFRESH, userScopes: ['https://api.ebay.com/oauth/api_scope/sell.fulfillment'] },
  );
  const page = await client.fulfillment.orders.list();
  assert.equal(page.orders?.[0]?.orderId, '1');
  const [refresh] = toTokenEndpoint(sent);
  assert.equal(refresh?.headers.get('authorization'), BASIC);
  assert.deepEqual(form(refresh!), {
    grant_type: 'refresh_token',
    refresh_token: REFRESH,
    scope: 'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
  });
  assert.equal(tokens.length, 1);
  assert.equal(tokens[0]?.accessToken, 'synthetic-new-user-token');
  assert.equal(tokens[0]?.refreshToken, REFRESH);
  assert.equal(sent.length, 3);
});

test('concurrent 401s share one refresh', async () => {
  const fresh = 'synthetic-new-user-token';
  const { client, sent } = clientFor(
    async (url, request) => {
      if (url.pathname === TOKEN_PATH) {
        await new Promise((resolve) => setTimeout(resolve, 5));
        return json({ access_token: fresh });
      }
      return request.headers.get('authorization') === `Bearer ${fresh}` ? json(orders()) : json({}, 401);
    },
    { userToken: USER, refreshToken: REFRESH },
  );
  await Promise.all([1, 2, 3].map(() => client.fulfillment.orders.list()));
  assert.equal(toTokenEndpoint(sent).length, 1);
});

test('a 401 on an application call mints a new application token', async () => {
  const { client, sent } = clientFor(
    (url, request) => {
      if (url.pathname === TOKEN_PATH) {
        return json({ access_token: APP, expires_in: 7200 });
      }
      return request.headers.get('authorization') === `Bearer ${APP}` ? json({}) : json({}, 401);
    },
    { appToken: 'synthetic-stale-app-token' },
  );
  await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
  assert.deepEqual(form(toTokenEndpoint(sent)[0]!), { grant_type: 'client_credentials', scope: API_SCOPE });
});

test('a failed refresh throws its own error, not the 401', async () => {
  const { client } = clientFor(
    (url) => (url.pathname === TOKEN_PATH ? json({ error: 'invalid_grant' }, 400) : json({}, 401)),
    { userToken: USER, refreshToken: REFRESH },
  );
  await assert.rejects(client.fulfillment.orders.list(), BadRequestError);
});

test('a 401 with no way to refresh is an AuthenticationError', async () => {
  const { client, sent } = clientFor(() => json({}, 401), { userToken: USER });
  await assert.rejects(client.fulfillment.orders.list(), AuthenticationError);
  assert.equal(sent.length, 1);
});

test('the authorization URL carries the RuName, scopes and a fresh state', () => {
  const { client } = clientFor(() => json({}), { ruName: 'synthetic-ru-name' });
  const scope = 'https://api.ebay.com/oauth/api_scope/sell.fulfillment';
  const first = client.oauth.authorizationUrl([scope], { prompt: 'login' });
  const url = new URL(first.url);
  assert.equal(url.origin + url.pathname, 'https://auth.ebay.com/oauth2/authorize');
  assert.deepEqual(Object.fromEntries(url.searchParams), {
    client_id: CLIENT_ID,
    redirect_uri: 'synthetic-ru-name',
    response_type: 'code',
    scope,
    state: first.state,
    prompt: 'login',
  });
  assert.ok(first.state.length >= 32);
  assert.notEqual(client.oauth.authorizationUrl([scope]).state, first.state);
  const sandbox = authorizationUrl(CLIENT_ID, 'synthetic-ru-name', [scope], { state: 's', environment: 'sandbox' });
  assert.match(sandbox.url, /^https:\/\/auth\.sandbox\.ebay\.com\/oauth2\/authorize\?.*state=s/);
  assert.throws(() => authorizationUrl(CLIENT_ID, 'synthetic-ru-name', []), /at least one scope/);
  assert.throws(() => clientFor(() => json({})).client.oauth.authorizationUrl([scope]), /ruName/);
});

test('exchanging a code stores the user token and redacts the code', async () => {
  const code = 'synthetic-authorization-code';
  const reply = { access_token: 'synthetic-exchanged-token', refresh_token: REFRESH, expires_in: 7200 };
  const { client, sent, tokens, logs } = clientFor(
    (url) => (url.pathname === TOKEN_PATH ? json({ ...reply, refresh_token_expires_in: 47304000 }) : json(orders())),
    { ruName: 'synthetic-ru-name' },
  );
  const token = await client.oauth.exchangeCode(code);
  assert.equal(token.refreshTokenExpiresIn, 47304000);
  assert.deepEqual(form(sent[0]!), { grant_type: 'authorization_code', code, redirect_uri: 'synthetic-ru-name' });
  await client.fulfillment.orders.list();
  assert.equal(sent[1]?.headers.get('authorization'), 'Bearer synthetic-exchanged-token');
  assert.equal(tokens.length, 1);
  assert.ok(!logs.join('\n').includes(code));
});

test('a token response without an access token is a DecodeError', async () => {
  const { client } = clientFor(() => json({ token_type: 'Bearer' }));
  await assert.rejects(client.oauth.appToken(), DecodeError);
});

test('each operation goes to its own host, in the chosen environment', async () => {
  const { client, sent } = clientFor(() => json({ total: 0, payouts: [] }), { userToken: USER });
  await client.finances.payouts.list();
  await client.fulfillment.orders.list();
  assert.deepEqual(
    sent.map(({ url }) => url.pathname.split('/')[1]),
    ['apiz', 'api'],
  );
  const sandbox = clientFor(() => json({}), { userToken: USER, environment: 'sandbox', hosts: undefined });
  await sandbox.client.finances.sellerFunds.getSummary();
  assert.equal(sandbox.sent[0]?.url.origin, 'https://apiz.sandbox.ebay.com');
});

test('the marketplace default is sent on operations that take it, unless a call passes its own', async () => {
  const { client, sent } = clientFor(() => json({}), { userToken: USER, marketplaceId: 'EBAY_US' });
  await client.finances.sellerFunds.getSummary();
  await client.finances.sellerFunds.getSummary({ marketplaceId: 'EBAY_GB' });
  await client.fulfillment.orders.list();
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('x-ebay-c-marketplace-id')),
    ['EBAY_US', 'EBAY_GB', null],
  );
});

test('a signing key signs every request and stays out of logs and errors', async () => {
  const pem = String(generateKeyPairSync('ed25519').privateKey.export({ type: 'pkcs8', format: 'pem' }));
  const raw = pem.split('\n').slice(1, -2).join('');
  const signingKey = await SigningKey.create({ privateKey: raw, jwe: 'synthetic-jwe' });
  const { client, sent, logs } = clientFor(() => json({ errors: [{ message: raw }] }, 400), {
    userToken: USER,
    signingKey,
    maxRetries: 0,
  });
  const error = await client.fulfillment.orders.issueRefund('1', { reasonForRefund: 'BUYER_CANCEL' }).catch((e) => e);
  assert.ok(error instanceof BadRequestError);
  const [request] = sent;
  assert.equal(request?.headers.get('x-ebay-signature-key'), 'synthetic-jwe');
  assert.match(request?.headers.get('content-digest') ?? '', /^sha-256=:[A-Za-z0-9+/]+=*:$/);
  assert.match(
    request?.headers.get('signature-input') ?? '',
    /^sig1=\("content-digest" "x-ebay-signature-key" "@method" "@path" "@authority"\);created=\d+$/,
  );
  assert.match(request?.headers.get('signature') ?? '', /^sig1=:[A-Za-z0-9+/]+=*:$/);
  assert.ok(!JSON.stringify([error.rawBody, error.detail, error.message, logs]).includes(raw));
  await assert.rejects(SigningKey.create({ privateKey: 'not a key', jwe: 'synthetic-jwe' }), TypeError);
});

test('error responses map to typed errors with the eBay errors list', async () => {
  const body = {
    errors: [
      {
        errorId: 32100,
        domain: 'API_FULFILLMENT',
        category: 'REQUEST',
        message: 'Synthetic order not found',
        longMessage: 'Synthetic long message',
        parameters: [{ name: 'orderId', value: '1' }],
      },
    ],
  };
  const { client } = clientFor(() => json(body, 404), { userToken: USER });
  const error = await client.fulfillment.orders.get('1').catch((caught) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof HttpError);
  assert.equal(error.kind, 'not_found');
  assert.equal(error.status, 404);
  assert.equal(error.code, 32100);
  assert.equal(error.detail, 'Synthetic order not found');
  assert.equal(error.message, 'HTTP 404 (not_found): Synthetic order not found');
  assert.deepEqual(error.errors[0]?.parameters, [{ name: 'orderId', value: '1' }]);
  assert.equal(error.errors[0]?.subdomain, undefined);

  const server = clientFor(() => new Response('oops', { status: 503 }), { userToken: USER, maxRetries: 0 });
  const failed = await server.client.fulfillment.orders.get('1').catch((caught) => caught);
  assert.ok(failed instanceof ServerError);
  assert.deepEqual(failed.errors, []);
  assert.equal(failed.message, 'HTTP 503 (server)');
});

test('credentials never reach an error body or the logs', async () => {
  const { client, logs } = clientFor(() => json({ errors: [{ message: `bad ${USER} ${CLIENT_SECRET}` }] }, 400), {
    userToken: USER,
  });
  const error = await client.fulfillment.orders.get('1').catch((caught) => caught);
  const output = JSON.stringify([error.rawBody, error.detail, error.message, logs]);
  assert.ok(!output.includes(USER));
  assert.ok(!output.includes(CLIENT_SECRET));
});

test('the iterator follows next links and stays on its own host', async () => {
  const { client, sent } = clientFor(
    (url) =>
      url.searchParams.get('offset') === '1'
        ? json(orders('2'))
        : json({ ...orders('1'), next: 'https://elsewhere.invalid/sell/fulfillment/v1/order?limit=1&offset=1' }),
    { userToken: USER },
  );
  const seen: Order[] = [];
  for await (const order of client.fulfillment.orders.iter({ limit: '1' })) seen.push(order);
  assert.deepEqual(
    seen.map(({ orderId }) => orderId),
    ['1', '2'],
  );
  assert.deepEqual(
    sent.map(({ url }) => `${url.origin}${url.pathname}?${url.searchParams}`),
    [`${BASE}${ORDERS_PATH}?limit=1`, `${BASE}${ORDERS_PATH}?limit=1&offset=1`],
  );
});

test('an empty 204 page ends the iteration, and a page without its items is a DecodeError', async () => {
  const pages = [
    json({ ...orders('1'), next: '/sell/fulfillment/v1/order?offset=1' }),
    new Response(null, { status: 204 }),
  ];
  const ended = clientFor(() => pages.shift()!, { userToken: USER });
  const seen: Order[] = [];
  for await (const order of ended.client.fulfillment.orders.iter()) seen.push(order);
  assert.equal(seen.length, 1);

  const broken = clientFor(() => json({ total: 1, next: '/sell/fulfillment/v1/order?offset=1' }), { userToken: USER });
  const iterate = async () => {
    for await (const order of broken.client.fulfillment.orders.iter()) void order;
  };
  await assert.rejects(iterate(), DecodeError);
});

test('an empty 204 resolves to undefined', async () => {
  const { client } = clientFor(() => new Response(null, { status: 204 }), { appToken: APP });
  assert.equal(await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' }), undefined);
});
