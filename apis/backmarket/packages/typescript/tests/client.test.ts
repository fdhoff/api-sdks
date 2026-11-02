import assert from 'node:assert/strict';
import { once } from 'node:events';
import { createServer, type RequestListener } from 'node:http';
import { test, type TestContext } from 'node:test';
import { inspect } from 'node:util';
import {
  ApiConnectionError,
  ApiError,
  ApiTimeoutError,
  BackMarketClient,
  DecodeError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  WafBlockedError,
  type ClientOptions,
  type Environment,
  type Order,
  type OrderPage,
  type Region,
} from 'backmarket-seller';
import { OPERATIONS } from '../dist/esm/resources.js';

const TOKEN = 'synthetic-token';
const BASE = 'http://mock.invalid';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;
type Sent = { url: URL; init: RequestInit };

const json = (body: unknown, init: ResponseInit = {}): Response =>
  new Response(JSON.stringify(body), { headers: { 'content-type': 'application/json' }, ...init });

const required = { userAgent: 'BM-Example-Test;test@example.com', locale: 'en-us' };

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const client = new BackMarketClient({
    token: TOKEN,
    baseUrl: BASE,
    ...required,
    retryBaseDelayMs: 1,
    fetch: async (input, init = {}) => {
      const url = new URL(String(input));
      sent.push({ url, init });
      return handler(url, init);
    },
    ...options,
  });
  return { client, sent };
}

async function collect<T>(items: AsyncIterable<T>): Promise<T[]> {
  const all: T[] = [];
  for await (const item of items) all.push(item);
  return all;
}

async function serve(t: TestContext, listener: RequestListener): Promise<string> {
  const server = createServer(listener).listen(0, '127.0.0.1');
  await once(server, 'listening');
  t.after(() => {
    server.close();
    server.closeAllConnections();
  });
  const address = server.address();
  assert.ok(address !== null && typeof address === 'object');
  return `http://127.0.0.1:${address.port}`;
}

test('every operation has a public method', () => {
  const { client } = clientFor(() => new Response());
  assert.equal(OPERATIONS.size, 40);
  for (const operation of OPERATIONS.values()) {
    const resource = client[operation.resource as keyof BackMarketClient] as unknown as Record<string, unknown>;
    assert.equal(typeof resource[operation.name], 'function', operation.id);
    if (operation.iterator) assert.equal(typeof resource[operation.iterator], 'function', operation.id);
  }
});

for (const [region, environment, host] of [
  ['eu', 'production', 'www.backmarket.fr'],
  ['na', 'preprod', 'preprod.backmarket.com'],
  ['ap', 'production', 'www.backmarket.co.jp'],
] as [Region, Environment, string][]) {
  test(`${region} ${environment} selects ${host}`, async () => {
    const { client, sent } = clientFor(() => json({}), { baseUrl: undefined, region, environment });
    await client.orders.get(1);
    assert.equal(sent[0]?.url.host, host);
  });
}

test('a server choice is required and exclusive', () => {
  const options = { token: TOKEN, ...required };
  assert.throws(() => new BackMarketClient(options), /exactly one/);
  assert.throws(() => new BackMarketClient({ ...options, region: 'eu', baseUrl: BASE }), /exactly one/);
  assert.throws(() => new BackMarketClient({ ...options, region: 'mars' as Region }), /Unknown server/);
});

test('the token and user agent are required', () => {
  assert.throws(() => new BackMarketClient({ ...required, token: '', region: 'eu' }), /token/);
  assert.throws(() => new BackMarketClient({ ...required, token: TOKEN, userAgent: '', region: 'eu' }), /userAgent/);
});

test('headers carry the token verbatim', async () => {
  const { client, sent } = clientFor(() => json({}));
  await client.orders.get(1);
  const headers = new Headers(sent[0]?.init.headers);
  assert.equal(headers.get('authorization'), `Basic ${TOKEN}`);
  assert.equal(headers.get('accept-language'), 'en-us');
  assert.equal(headers.get('user-agent'), required.userAgent);
});

test('parameters use camelCase here and wire names on the wire', async () => {
  const { client, sent } = clientFor(() => json({ count: 0, next: null, previous: null, results: [] }));
  await client.orders.list({ pageSize: 50, countryCode: 'fr-fr' as never });
  assert.equal(sent[0]?.url.pathname, '/ws/orders');
  assert.deepEqual(Object.fromEntries(sent[0]?.url.searchParams ?? []), { 'page-size': '50', country_code: 'fr-fr' });
});

test('path values are encoded and required at runtime', async () => {
  const { client, sent } = clientFor(() => json({}));
  await client.listings.get('a/b c');
  assert.equal(sent[0]?.url.pathname, '/ws/listings/a%2Fb%20c');
  await assert.rejects(() => client.orders.get(undefined as never), /orderId is required/);
});

test('bodies are sent as given, under wire names', async () => {
  const { client, sent } = clientFor(() => json({}));
  await client.orders.update(1, { order_id: 1, new_state: undefined } as never);
  assert.equal(sent[0]?.init.body, '{"order_id":1}');
  assert.equal(new Headers(sent[0]?.init.headers).get('content-type'), 'application/json');
});

test('responses are not checked against their types', async () => {
  const { client } = clientFor(() => json({ order_id: 'not-a-number', unknown_field: true }));
  const order: Order = await client.orders.get(1);
  assert.deepEqual(order, { order_id: 'not-a-number', unknown_field: true });
});

test('a non-object response comes back as decoded', async () => {
  const { client } = clientFor(() => json(['raw']));
  assert.deepEqual(await client.orders.get(1), ['raw']);
});

test('an empty success reads as undefined', async () => {
  const { client } = clientFor(() => new Response(null, { status: 204 }));
  assert.equal(await client.orders.uploadInvoice(1), undefined);
});

test('a success with broken JSON is a decode error', async () => {
  const { client } = clientFor(() => new Response('{', { headers: { 'content-type': 'application/json' } }));
  await assert.rejects(() => client.orders.get(1), DecodeError);
});

test('list returns the page and iter walks them all', async () => {
  const pages: Record<string, unknown> = {
    '1': { count: 2, next: `https://elsewhere.invalid/ws/orders?page=2`, previous: null, results: [{ order_id: 1 }] },
    '2': { count: 2, next: null, previous: null, results: [{ order_id: 2 }] },
  };
  const { client, sent } = clientFor((url) => json(pages[url.searchParams.get('page') ?? '1']));
  const page: OrderPage = await client.orders.list();
  assert.equal(page.count, 2);
  sent.length = 0;
  const orders = await collect(client.orders.iter());
  assert.deepEqual(
    orders.map((order) => order.order_id),
    [1, 2],
  );
  assert.deepEqual(
    sent.map(({ url }) => url.host),
    ['mock.invalid', 'mock.invalid'],
  );
});

test('iter rejects a next link that does not advance', async () => {
  const { client } = clientFor(() => json({ next: `${BASE}/ws/orders?page=1`, results: [] }));
  await assert.rejects(() => collect(client.orders.iter({ page: 1 })), DecodeError);
});

test('iter rejects a next link with no position', async () => {
  const { client } = clientFor(() => json({ next: `${BASE}/ws/orders`, results: [] }));
  await assert.rejects(() => collect(client.orders.iter()), DecodeError);
});

test('iter rejects a next link that is not a URL', async () => {
  const { client } = clientFor(() => json({ next: 'http://[', results: [] }));
  await assert.rejects(() => collect(client.orders.iter()), DecodeError);
});

test('redirects are not followed', async () => {
  const { client, sent } = clientFor(
    () => new Response(null, { status: 302, headers: { location: 'https://elsewhere.invalid/' } }),
  );
  await assert.rejects(() => client.orders.get(1), { kind: 'api', status: 302 });
  assert.equal(sent.length, 1);
  assert.equal(sent[0]?.init.redirect, 'manual');
});

test('a 404 is typed and carries what the body has', async () => {
  const { client } = clientFor(() => json({ error: { code: 'gone' }, requestId: 'r-1' }, { status: 404 }));
  const error = await client.orders.get(1).catch((caught: unknown) => caught);
  assert.ok(error instanceof NotFoundError);
  assert.ok(error instanceof ApiError);
  assert.equal(error.name, 'NotFoundError');
  assert.equal(error.code, 'gone');
  assert.equal(error.requestId, 'r-1');
});

test('a WAF block is a permission error and keeps cf-ray', async () => {
  const { client } = clientFor(
    () => new Response('<html>blocked</html>', { status: 403, headers: { 'cf-ray': 'ray-1' } }),
  );
  const error = await client.orders.get(1).catch((caught: unknown) => caught);
  assert.ok(error instanceof WafBlockedError);
  assert.ok(error instanceof PermissionDeniedError);
  assert.equal(error.cfRay, 'ray-1');
});

test('a connection failure on GET is retried, then thrown', async () => {
  const failure = () => Promise.reject(new TypeError('fetch failed', { cause: { code: 'ECONNRESET' } }));
  const { client, sent } = clientFor(failure, { maxRetries: 1 });
  await assert.rejects(() => client.orders.get(1), ApiConnectionError);
  assert.equal(sent.length, 2);
});

test('a connection failure on POST is not retried', async () => {
  const { client, sent } = clientFor(() => Promise.reject(new TypeError('fetch failed')));
  await assert.rejects(() => client.orders.update(1, { order_id: 1, new_state: 2 }), ApiConnectionError);
  assert.equal(sent.length, 1);
});

test('the token is neither logged nor shown by inspection', async () => {
  const logs: string[] = [];
  const log = (message: string) => void logs.push(message);
  const { client } = clientFor(() => json({ message: `bad ${TOKEN}` }, { status: 400 }), {
    logger: { debug: log, info: log },
  });
  const error = await client.listings.get(TOKEN).catch((caught: unknown) => caught);
  assert.ok(error instanceof ApiError);
  assert.ok(logs.length > 0);
  for (const text of [...logs, error.rawBody ?? '', inspect(client, { depth: null, showHidden: true })]) {
    assert.ok(!text.includes(TOKEN), text);
  }
});

for (const [name, value] of [
  ['seconds', '0'],
  ['an HTTP date', 'FUTURE'],
] as const) {
  test(`a 429 honours Retry-After as ${name}`, async () => {
    const header = value === 'FUTURE' ? new Date(Date.now() + 1500).toUTCString() : value;
    const replies = [new Response(null, { status: 429, headers: { 'retry-after': header } }), json({ ok: true })];
    const { client, sent } = clientFor(() => replies.shift() as Response, { rateLimitWaitMs: 60_000 });
    assert.deepEqual(await client.orders.get(1), { ok: true });
    assert.equal(sent.length, 2);
  });
}

for (const value of ['soon', 'foo 1', 'Thu, 01 Jan 2015 00:00:00 GMT']) {
  test(`a 429 with Retry-After "${value}" waits the default`, async () => {
    const replies = [new Response(null, { status: 429, headers: { 'retry-after': value } }), json({ ok: true })];
    const logs: string[] = [];
    const log = (message: string) => void logs.push(message);
    const { client } = clientFor(() => replies.shift() as Response, {
      rateLimitWaitMs: 5,
      logger: { debug: log, info: log },
    });
    await client.orders.get(1);
    assert.ok(logs.some((line) => line.includes('retrying after 5ms')));
  });
}

test('a Retry-After over the maximum is thrown at once, with its value', async () => {
  const { client, sent } = clientFor(() => new Response(null, { status: 429, headers: { 'retry-after': '2' } }), {
    maxRetryWaitMs: 1000,
  });
  await assert.rejects(() => client.orders.get(1), { kind: 'rate_limited', retryAfter: '2' });
  assert.equal(sent.length, 1);
});

test('a Retry-After over the default maximum of 60 seconds is thrown at once', async () => {
  const { client, sent } = clientFor(() => new Response(null, { status: 429, headers: { 'retry-after': '61' } }));
  await assert.rejects(() => client.orders.get(1), RateLimitedError);
  assert.equal(sent.length, 1);
});

test('the maximum does not apply to the rate-limit wait', async () => {
  const replies = [new Response(null, { status: 429 }), json({ ok: true })];
  const { client, sent } = clientFor(() => replies.shift() as Response, { rateLimitWaitMs: 5, maxRetryWaitMs: 1 });
  assert.deepEqual(await client.orders.get(1), { ok: true });
  assert.equal(sent.length, 2);
});

for (const [name, options, headers] of [
  ['Retry-After', { maxRetryWaitMs: Infinity }, { 'retry-after': '99999999999999999999' }],
  ['rate-limit wait', { rateLimitWaitMs: 2 ** 31 }, {}],
] as const) {
  test(`a ${name} too long for a timer gives up instead of firing early`, async () => {
    const { client, sent } = clientFor(() => new Response(null, { status: 429, headers }), options);
    await assert.rejects(() => client.orders.get(1), RateLimitedError);
    assert.equal(sent.length, 1);
  });
}

test('POST is retried on 429 and never on 500', async () => {
  const replies = [
    new Response(null, { status: 429, headers: { 'retry-after': '0' } }),
    new Response(null, { status: 500 }),
  ];
  const { client, sent } = clientFor(() => replies.shift() as Response);
  await assert.rejects(() => client.orders.update(1, { order_id: 1, new_state: 2 }), { kind: 'server', status: 500 });
  assert.equal(sent.length, 2);
});

test('uploads are multipart, with no JSON content type', async () => {
  const { client, sent } = clientFor(() => new Response(null, { status: 204 }));
  await client.orders.uploadInvoice(1, {
    invoice: [
      new Uint8Array([1, 2]),
      { filename: 'named.pdf', content: new Uint8Array([3]) },
      new File([new Uint8Array([4])], 'file.pdf'),
    ],
  });
  const { init } = sent[0] as Sent;
  assert.equal(new Headers(init.headers).get('content-type'), null);
  const parts = (init.body as FormData).getAll('invoice') as File[];
  assert.deepEqual(
    parts.map((part) => part.name),
    ['invoice', 'named.pdf', 'file.pdf'],
  );
});

test('form fields are text, one part per list item', async () => {
  const { client, sent } = clientFor(() => new Response(null, { status: 204 }));
  await client.buyback.counterOffer('EXAMPLE-1', { price: 10, reasons: ['a', 'b'], files: [] });
  const form = sent[0]?.init.body as FormData;
  assert.equal(form.get('price'), '10');
  assert.deepEqual(form.getAll('reasons'), ['a', 'b']);
});

test('a corrupt compressed success is a decode error', async (t) => {
  const baseUrl = await serve(t, (_request, response) => {
    response.writeHead(200, { 'content-type': 'application/json', 'content-encoding': 'gzip' });
    response.end('not gzip');
  });
  const client = new BackMarketClient({ token: TOKEN, baseUrl, ...required, maxRetries: 0 });
  await assert.rejects(() => client.orders.get(1), DecodeError);
});

test('the client asks for an uncompressed body, because fetch accepts a gzip body cut short', async (t) => {
  let accepted: string | undefined;
  const baseUrl = await serve(t, (request, response) => {
    accepted = request.headers['accept-encoding'];
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end('{"order_id":1}');
  });
  const client = new BackMarketClient({ token: TOKEN, baseUrl, ...required });
  assert.deepEqual(await client.orders.get(1), { order_id: 1 });
  assert.equal(accepted, 'identity');
});

test('a corrupt compressed failure keeps its status, with no body', async (t) => {
  const baseUrl = await serve(t, (_request, response) => {
    response.writeHead(502, { 'content-type': 'application/json', 'content-encoding': 'gzip' });
    response.end('not gzip');
  });
  const client = new BackMarketClient({ token: TOKEN, baseUrl, ...required, maxRetries: 0 });
  await assert.rejects(() => client.orders.get(1), { kind: 'server', status: 502, rawBody: '' });
});

test('a corrupt compressed 429 is still retried', async (t) => {
  let requests = 0;
  const baseUrl = await serve(t, (_request, response) => {
    requests += 1;
    if (requests === 1) {
      response.writeHead(429, { 'content-encoding': 'gzip', 'retry-after': '0' });
      response.end('not gzip');
    } else {
      response.writeHead(200, { 'content-type': 'application/json' });
      response.end('{"ok":true}');
    }
  });
  const client = new BackMarketClient({ token: TOKEN, baseUrl, ...required });
  assert.deepEqual(await client.orders.get(1), { ok: true });
  assert.equal(requests, 2);
});

test('the timeout covers a body that keeps trickling', async (t) => {
  const baseUrl = await serve(t, (_request, response) => {
    response.writeHead(200, { 'content-type': 'application/json' });
    const timer = setInterval(() => response.write(' '), 20);
    response.on('close', () => clearInterval(timer));
  });
  const client = new BackMarketClient({ token: TOKEN, baseUrl, ...required, timeoutMs: 100, maxRetries: 0 });
  await assert.rejects(() => client.orders.get(1), ApiTimeoutError);
});

test('the types reject what the API does not take', () => {
  const { client } = clientFor(() => json({}));
  const unused = () => {
    // @ts-expect-error orderId is a number
    void client.orders.get('1');
    // @ts-expect-error pageSize is camelCase
    void client.orders.list({ 'page-size': 1 });
    // @ts-expect-error message is required
    void client.care.sendMessage(1, {});
    // @ts-expect-error unknown region
    void new BackMarketClient({ ...required, token: TOKEN, region: 'mars' });
  };
  assert.equal(typeof unused, 'function');
});
