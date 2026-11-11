import assert from 'node:assert/strict';
import { test } from 'node:test';
import {
  AuthenticationError,
  BadRequestError,
  HttpError,
  JobTimeoutError,
  MiraklClient,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
  type ClientOptions,
  type Credentials,
} from 'mirakl-seller';
import { OPERATIONS } from '../dist/esm/resources.js';

const KEY = 'synthetic-unit-shop-key';
const BASE = 'http://operator.mock.invalid';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;
type Sent = { url: URL; headers: Headers; body: RequestInit['body'] };

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const logs: string[] = [];
  const client = new MiraklClient({
    baseUrl: BASE,
    apiKey: KEY,
    retryBaseDelayMs: 0,
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    fetch: async (input, init = {}) => {
      const url = new URL(String(input));
      sent.push({ url, headers: new Headers(init.headers), body: init.body });
      return handler(url, init);
    },
    ...options,
  });
  return { client, sent, logs };
}

test('every operation has a public method', () => {
  const { client } = clientFor(() => json({}));
  assert.equal(OPERATIONS.size, 117);
  for (const operation of OPERATIONS.values()) {
    const resource = (client as unknown as Record<string, Record<string, unknown>>)[operation.resource];
    assert.equal(typeof resource?.[operation.name], 'function', operation.id);
    if (operation.iterator) assert.equal(typeof resource?.[operation.iterator], 'function', operation.id);
  }
  const ids = (filter: (operation: { iterator?: string; job?: unknown }) => unknown) =>
    [...OPERATIONS.values()].filter(filter).map((operation) => operation.id);
  assert.equal(ids((operation) => operation.iterator).length, 21);
  assert.deepEqual(ids((operation) => operation.job).sort(), ['OF02', 'OF53', 'OR14', 'P42', 'STO02', 'TL04']);
});

test('the key is the whole Authorization header, with no scheme', async () => {
  const { client, sent } = clientFor(() => json({ shop_id: 1 }));
  await client.shop.get();
  assert.equal(sent[0]!.headers.get('authorization'), KEY);
  assert.equal(sent[0]!.url.href, `${BASE}/api/account`);
});

test('the base URL is required, and its trailing slash is dropped', async () => {
  assert.throws(() => new MiraklClient({ baseUrl: '', apiKey: KEY }), /baseUrl is required/);
  assert.throws(() => new MiraklClient({ baseUrl: 'operator.mock.invalid', apiKey: KEY }), /http or https/);
  const { client, sent } = clientFor(() => json({}), { baseUrl: `${BASE}/` });
  await client.platform.healthCheck();
  assert.equal(sent[0]!.url.href, `${BASE}/api/version`);
});

test('exactly one of apiKey and credentials is taken', async () => {
  assert.throws(() => new MiraklClient({ baseUrl: BASE }), /exactly one/);
  const credentials: Credentials = {
    apply: ({ headers }) => headers.set('Authorization', 'custom'),
    secrets: () => ['custom'],
  };
  assert.throws(() => new MiraklClient({ baseUrl: BASE, apiKey: KEY, credentials }), /exactly one/);
  assert.throws(() => new MiraklClient({ baseUrl: BASE, apiKey: '' }), /apiKey/);
  const { client, sent } = clientFor(() => json({}), { apiKey: undefined, credentials });
  await client.shop.get();
  assert.equal(sent[0]!.headers.get('authorization'), 'custom');
});

test('the client shop is sent unless a call names its own', async () => {
  const { client, sent } = clientFor(() => json({}), { shopId: 2001 });
  await client.shop.get();
  await client.shop.get({ shopId: 2002 });
  assert.deepEqual(
    sent.map(({ url }) => url.searchParams.get('shop_id')),
    ['2001', '2002'],
  );
  const { client: none, sent: unset } = clientFor(() => json({}));
  await none.shop.get();
  assert.equal(unset[0]!.url.searchParams.has('shop_id'), false);
});

for (const [status, type] of [
  [400, BadRequestError],
  [401, AuthenticationError],
  [403, PermissionDeniedError],
  [404, NotFoundError],
  [429, RateLimitedError],
  [503, ServerError],
  [409, HttpError],
] as const) {
  test(`HTTP ${status} keeps the status and raw body`, async () => {
    const { client } = clientFor(() => new Response('synthetic failure', { status }), { maxRetries: 0 });
    const error = await client.shop.get().catch((caught: unknown) => caught);
    assert.equal((error as object).constructor, type);
    assert.equal((error as HttpError).status, status);
    assert.equal((error as HttpError).rawBody, 'synthetic failure');
  });
}

test('the key never reaches errors or logs', async () => {
  const { client, logs } = clientFor(() => new Response(`unknown key ${KEY}`, { status: 401 }));
  const error = (await client.shop.get().catch((caught: unknown) => caught)) as AuthenticationError;
  assert.ok(error instanceof AuthenticationError);
  assert.equal(error.rawBody, 'unknown key ***');
  assert.notEqual(logs.length, 0);
  assert.ok(!logs.join('\n').includes(KEY));
});

test('offset iterators advance by the items received, up to the total', async () => {
  const { client, sent } = clientFor((url) => {
    const offset = Number(url.searchParams.get('offset') ?? 0);
    return json({ orders: offset < 2 ? [{ order_id: `order-${offset}` }] : [], total_count: 2 });
  });
  const ids: string[] = [];
  for await (const order of client.orders.iter({ max: 1 })) ids.push(order.order_id);
  assert.deepEqual(ids, ['order-0', 'order-1']);
  assert.deepEqual(
    sent.map(({ url }) => url.searchParams.get('offset')),
    [null, '1'],
  );
});

test('seek iterators send each next page token back', async () => {
  const { client, sent } = clientFor((url) =>
    json(
      url.searchParams.get('page_token') === 'token-2'
        ? { data: [{ id: 'shipment-2' }] }
        : { data: [{ id: 'shipment-1' }], next_page_token: 'token-2' },
    ),
  );
  const ids: string[] = [];
  for await (const shipment of client.shipments.iter({ limit: 1 })) ids.push(shipment.id);
  assert.deepEqual(ids, ['shipment-1', 'shipment-2']);
  assert.deepEqual(
    sent.map(({ url }) => url.searchParams.get('page_token')),
    [null, 'token-2'],
  );
});

test('a wait polls until the job ends and returns a failed status as it is', async () => {
  const states = ['QUEUED', 'RUNNING', 'FAILED'];
  const { client, sent } = clientFor(() => json({ import_id: 41, status: states.shift(), has_error_report: true }));
  const status = await client.offers.waitForImport(41, { intervalMs: 0 });
  assert.equal(status.status, 'FAILED');
  assert.equal(sent.length, 3);
  assert.ok(sent.every(({ url }) => url.pathname === '/api/offers/imports/41'));
});

test('a wait throws JobTimeoutError at its deadline, with the last status', async () => {
  const { client } = clientFor(() => json({ status: 'PENDING' }));
  const error = await client.orders.waitForExport('tracking-1', { timeoutMs: 0 }).catch((caught: unknown) => caught);
  assert.ok(error instanceof JobTimeoutError);
  assert.deepEqual(error.result, { status: 'PENDING' });
});

test('a wait stops when its signal aborts', async () => {
  const controller = new AbortController();
  const { client } = clientFor(() => {
    controller.abort(new Error('synthetic stop'));
    return json({ status: 'PENDING' });
  });
  await assert.rejects(
    client.accounting.waitForTransactionExport('tracking-1', { signal: controller.signal }),
    /synthetic stop/,
  );
});

test('downloadUrl sends the key to the base origin only', async () => {
  const { client, sent } = clientFor(() => new Response('[]', { headers: { 'content-type': 'application/json' } }));
  const own = await client.downloadUrl(`${BASE}/exports/offers-1.json`);
  assert.equal(new TextDecoder().decode(await own.bytes()), '[]');
  await client.downloadUrl('http://files.mock.invalid/exports/offers-1.json?signature=synthetic');
  await client.downloadUrl('http://operator.mock.invalid:8080/exports/offers-1.json');
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('authorization')),
    [KEY, null, null],
  );
});

test('downloadUrl drops the key once a redirect leaves the base origin', async () => {
  const { client, sent, logs } = clientFor((url) =>
    url.origin === BASE
      ? new Response(null, {
          status: 302,
          headers: { location: 'http://files.mock.invalid/stored.json?signature=synthetic' },
        })
      : new Response('[]', { headers: { 'content-type': 'application/json' } }),
  );
  await client.downloadUrl(`${BASE}/exports/offers-2.json`);
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('authorization')),
    [KEY, null],
  );
  assert.ok(!logs.join('\n').includes('signature=synthetic'));
});

test('an import sends one multipart file part and its options', async () => {
  const { client, sent } = clientFor(() => json({ import_id: 41 }, 201));
  const started = await client.offers.import({
    file: { filename: 'offers.csv', content: new TextEncoder().encode('sku;price') },
    importMode: 'NORMAL',
  });
  assert.equal(started.import_id, 41);
  const { headers, body } = sent[0]!;
  const form = await new Response(body, { headers }).formData();
  assert.deepEqual([...form.keys()].sort(), ['file', 'import_mode']);
  assert.equal((form.get('file') as File).name, 'offers.csv');
  assert.equal(form.get('import_mode'), 'NORMAL');
});

test('an error report keeps every byte and asks for its media type', async () => {
  const csv = new Uint8Array([0x73, 0x6b, 0x75, 0x3b, 0xff, 0x00]);
  const { client, sent } = clientFor(() => new Response(csv, { headers: { 'content-type': 'text/csv' } }));
  const report = await client.offers.downloadStockImportErrorReport('stock-import-1');
  assert.deepEqual(await report.bytes(), csv);
  assert.match(sent[0]!.headers.get('accept') ?? '', /text\/csv/);
});
