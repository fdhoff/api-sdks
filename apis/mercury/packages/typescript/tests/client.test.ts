import assert from 'node:assert/strict';
import { test } from 'node:test';
import {
  AuthenticationError,
  BadRequestError,
  ConflictError,
  HttpError,
  MercuryClient,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
  UnprocessableError,
  type ClientOptions,
  type PostTransactionAPIRequest,
} from 'mercury-banking';
import { OPERATIONS } from '../dist/esm/resources.js';

const TOKEN = 'secret-token:synthetic-unit-token';
const HOSTS = { api: 'http://api.mock.invalid/api/v1', vault: 'http://vault.mock.invalid/api/v1' };
const ACCOUNT = '00000000-0000-4000-8000-acc000000001';
const CARD = '00000000-0000-4000-8000-ca4d00000001';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;
type Sent = { url: URL; headers: Headers; body: RequestInit['body'] };

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const logs: string[] = [];
  const client = new MercuryClient({
    token: TOKEN,
    hosts: HOSTS,
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

const text = (body: RequestInit['body']): string =>
  typeof body === 'string' ? body : new TextDecoder().decode(body as Uint8Array);

test('every operation has a public method', () => {
  const { client } = clientFor(() => json({}));
  assert.equal(OPERATIONS.size, 87);
  for (const operation of OPERATIONS.values()) {
    const resource = (client as unknown as Record<string, Record<string, unknown>>)[operation.resource];
    assert.equal(typeof resource?.[operation.name], 'function', operation.id);
    if (operation.iterator) assert.equal(typeof resource?.[operation.iterator], 'function', operation.id);
  }
  assert.equal([...OPERATIONS.values()].filter((operation) => operation.iterator).length, 26);
});

test('only the money-moving writes are idempotent', () => {
  const marked = [...OPERATIONS.values()].filter((operation) => operation.idempotencyKey);
  assert.deepEqual(marked.map((operation) => operation.id).sort(), [
    'createInternalTransfer',
    'createTransaction',
    'requestSendMoney',
    'requestTransferMoney',
  ]);
  assert.deepEqual([...new Set(marked.map((operation) => operation.idempotencyKey))], ['idempotencyKey']);
});

test('the token is sent verbatim as a bearer token', async () => {
  const { client, sent } = clientFor(() => json({ accounts: [], page: {} }));
  await client.accounts.list();
  assert.equal(sent[0]!.headers.get('authorization'), `Bearer ${TOKEN}`);
  assert.equal(sent[0]!.url.href, 'http://api.mock.invalid/api/v1/accounts');
});

for (const [environment, api, vault] of [
  ['production', 'https://api.mercury.com/api/v1', 'https://vault-api.mercury.com/api/v1'],
  ['sandbox', 'https://api-sandbox.mercury.com/api/v1', 'https://api-sandbox.mercury.com/api/v1'],
] as const) {
  test(`the ${environment} environment has its own hosts`, async () => {
    const { client, sent } = clientFor(() => json({}), { environment, hosts: undefined });
    await client.organization.get();
    await client.cards.reveal(CARD);
    assert.deepEqual(
      sent.map(({ url }) => url.href),
      [`${api}/organization`, `${vault}/cards/${CARD}/reveal`],
    );
  });
}

test('the token and environment are checked', () => {
  assert.throws(() => new MercuryClient({ token: '' }), /token/);
  assert.throws(() => new MercuryClient({ token: TOKEN, environment: 'staging' as 'sandbox' }), /environment/);
  assert.throws(
    () => new MercuryClient({ token: TOKEN, hosts: { api: 'http://api.mock.invalid' } as typeof HOSTS }),
    /vault/,
  );
});

for (const [status, type] of [
  [400, BadRequestError],
  [401, AuthenticationError],
  [403, PermissionDeniedError],
  [404, NotFoundError],
  [409, ConflictError],
  [422, UnprocessableError],
  [429, RateLimitedError],
  [503, ServerError],
  [413, HttpError],
] as const) {
  test(`HTTP ${status} keeps the status and raw body`, async () => {
    const { client } = clientFor(() => new Response('synthetic failure', { status }), { maxRetries: 0 });
    const error = await client.organization.get().catch((caught: unknown) => caught);
    assert.equal((error as object).constructor, type);
    assert.equal((error as HttpError).status, status);
    assert.equal((error as HttpError).rawBody, 'synthetic failure');
  });
}

test('the token never reaches errors or logs', async () => {
  const { client, logs } = clientFor(() => new Response(`bad token ${TOKEN}`, { status: 401 }));
  const error = (await client.users.list().catch((caught: unknown) => caught)) as AuthenticationError;
  assert.ok(error instanceof AuthenticationError);
  assert.equal(error.rawBody, 'bad token ***');
  assert.notEqual(logs.length, 0);
  assert.ok(!logs.join('\n').includes(TOKEN));
  assert.ok(!error.message.includes(TOKEN));
});

test('revealed card details never reach the logs', async () => {
  const { client, logs } = clientFor(() => json({ cardNumber: '0000111122223333', cvc: '0417' }));
  const card = await client.cards.reveal(CARD);
  assert.equal(card.cardNumber, '0000111122223333');
  assert.notEqual(logs.length, 0);
  assert.ok(!logs.join('\n').includes('0000111122223333'));
  assert.ok(!logs.join('\n').includes('0417'));
});

const payment = (idempotencyKey: string): PostTransactionAPIRequest => ({
  recipientId: '00000000-0000-4000-8000-4ec100000001',
  amount: 1,
  paymentMethod: 'ach',
  idempotencyKey,
});

test('a keyed payment is retried with the same body', async () => {
  let calls = 0;
  const { client, sent } = clientFor(() =>
    ++calls < 3 ? new Response(null, { status: 503 }) : json({ id: 'txn', status: 'pending' }),
  );
  const result = await client.accounts.sendMoney(ACCOUNT, payment('synthetic-key-1'));
  assert.equal(result.status, 'pending');
  assert.equal(sent.length, 3);
  assert.equal(new Set(sent.map(({ body }) => text(body))).size, 1);
  assert.equal(JSON.parse(text(sent[0]!.body)).idempotencyKey, 'synthetic-key-1');
});

test('a payment without a key is not retried', async () => {
  const { client, sent } = clientFor(() => new Response(null, { status: 503 }));
  await assert.rejects(client.accounts.sendMoney(ACCOUNT, payment('')), ServerError);
  assert.equal(sent.length, 1);
  assert.equal(JSON.parse(text(sent[0]!.body)).idempotencyKey, '');
});

test('a download asks for a PDF and keeps every byte', async () => {
  const pdf = new Uint8Array([0x25, 0x50, 0x44, 0x46, 0xff, 0x00]);
  const { client, sent } = clientFor((url) =>
    url.pathname.endsWith('/pdf') ? new Response(pdf, { headers: { 'content-type': 'application/pdf' } }) : json({}),
  );
  const download = await client.invoices.downloadPdf('00000000-0000-4000-8000-1a4000000001');
  assert.equal(download.contentType, 'application/pdf');
  assert.deepEqual(await download.bytes(), pdf);
  await client.organization.get();
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('accept')),
    ['application/pdf', 'application/json'],
  );
});

test('an upload sends one multipart file part and returns the attachment', async () => {
  const { client, sent } = clientFor(() =>
    json({ attachmentId: 'att-1', downloadUrl: 'https://files.mock.invalid/att-1' }),
  );
  const attachment = await client.transactions.uploadAttachment('00000000-0000-4000-8000-7a4000000001', {
    file: { filename: 'receipt.txt', content: new TextEncoder().encode('synthetic receipt') },
  });
  assert.equal(attachment.attachmentId, 'att-1');
  const form = sent[0]!.body as FormData;
  assert.ok(form instanceof FormData);
  const file = form.get('file') as File;
  assert.equal(file.name, 'receipt.txt');
  assert.equal(await file.text(), 'synthetic receipt');
});

test('iterators follow the start_after cursor', async () => {
  const NEXT = '00000000-0000-4000-8000-05e400000001';
  const pages: Record<string, unknown> = {
    '': { users: [{ userId: 'u1' }], page: { nextPage: NEXT } },
    [NEXT]: { users: [{ userId: 'u2' }], page: { nextPage: null } },
  };
  const { client } = clientFor((url) => json(pages[url.searchParams.get('start_after') ?? '']));
  const ids: string[] = [];
  for await (const user of client.users.iter({ limit: 1 })) ids.push(user.userId);
  assert.deepEqual(ids, ['u1', 'u2']);
});
