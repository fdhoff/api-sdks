import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import {
  AuthenticationError,
  BadRequestError,
  ConflictError,
  DecodeError,
  GiteaClient,
  HttpError,
  NotFoundError,
  PermissionDeniedError,
  RateLimitedError,
  ServerError,
  UnprocessableError,
  type ClientOptions,
  type Credentials,
} from 'gitea-rest';
import { OPERATIONS } from '../dist/esm/resources.js';

const TOKEN = 'synthetic-unit-access-token';
const PASSWORD = 'synthetic-unit-password';
const OTP = '482913';
const BASE = 'https://gitea.example.test';
const OTHER = 'https://root-url.example.test';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;
type Sent = { url: URL; headers: Headers; body: RequestInit['body'] };

const json = (body: unknown, status = 200, headers: Record<string, string> = {}): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json', ...headers } });

function clientFor(handler: Handler, options: Partial<ClientOptions> = {}) {
  const sent: Sent[] = [];
  const logs: string[] = [];
  const client = new GiteaClient({
    baseUrl: BASE,
    token: TOKEN,
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

/** Answers each request with the next response, in order. */
const sequence =
  (...responses: Response[]): Handler =>
  () =>
    responses.shift() ?? new Response(null, { status: 500 });

function page(body: unknown, next?: string, extra: Record<string, string> = {}): Response {
  const links = Object.entries(extra).map(([rel, query]) => `<${OTHER}/api/v1/user/repos?${query}>; rel="${rel}"`);
  if (next !== undefined) links.unshift(`<${OTHER}/api/v1/user/repos?${next}>; rel="next"`);
  return json(body, 200, links.length > 0 ? { link: links.join(', ') } : {});
}

test('every operation has a public method whose comment names its operationId', async () => {
  const { client } = clientFor(() => json({}));
  assert.equal(OPERATIONS.size, 533);
  const sources = new Map<string, string>();
  for (const operation of OPERATIONS.values()) {
    const resource = (client as unknown as Record<string, Record<string, unknown>>)[operation.resource];
    assert.equal(typeof resource?.[operation.name], 'function', operation.id);
    if (operation.iterator) assert.equal(typeof resource?.[operation.iterator], 'function', operation.id);
    const file = `${operation.resource[0]!.toUpperCase()}${operation.resource.slice(1)}Api.ts`;
    if (!sources.has(file)) sources.set(file, await readFile(new URL(`../src/apis/${file}`, import.meta.url), 'utf8'));
    assert.match(
      sources.get(file)!,
      new RegExp(`\\(${operation.id}\\)\\. \\*/\\n\\s+${operation.name}\\(`),
      operation.id,
    );
  }
  assert.equal([...OPERATIONS.values()].filter((operation) => operation.iterator).length, 110);
});

for (const [baseUrl, url] of [
  [BASE, `${BASE}/api/v1/version`],
  [`${BASE}/`, `${BASE}/api/v1/version`],
  ['https://example.test/git', 'https://example.test/git/api/v1/version'],
  ['http://localhost:3000', 'http://localhost:3000/api/v1/version'],
] as const) {
  test(`the client adds /api/v1 to ${baseUrl}`, async () => {
    const { client, sent } = clientFor(() => json({ version: '0.0.0-synthetic' }), { baseUrl });
    assert.equal((await client.misc.getVersion()).version, '0.0.0-synthetic');
    assert.equal(sent[0]!.url.href, url);
  });
}

test('the base URL is an http URL, required, and leaves out /api/v1', () => {
  for (const baseUrl of ['', 'gitea.example.test', 'ftp://gitea.example.test', 'https://'])
    assert.throws(() => new GiteaClient({ baseUrl, token: TOKEN }), /baseUrl/, baseUrl);
  for (const baseUrl of [`${BASE}/api/v1`, `${BASE}/api/v1/`])
    assert.throws(() => new GiteaClient({ baseUrl, token: TOKEN }), /\/api\/v1/, baseUrl);
});

test('a token goes with the token scheme', async () => {
  const { client, sent } = clientFor(() => json({ id: 1, login: 'synthetic-user' }));
  assert.equal((await client.currentUser.get()).login, 'synthetic-user');
  assert.equal(sent[0]!.headers.get('authorization'), `token ${TOKEN}`);
  assert.equal(sent[0]!.headers.has('x-gitea-otp'), false);
  assert.equal(sent[0]!.headers.has('sudo'), false);
});

test('Basic sends the one-time password and sudo', async () => {
  const basic = { token: undefined, password: PASSWORD };
  const { client: plain, sent: first } = clientFor(() => json({}), { ...basic, username: 'synthetic-user' });
  await plain.currentUser.get();
  const { client: admin, sent: second } = clientFor(() => json({}), {
    ...basic,
    username: 'synthetic-admin',
    otp: OTP,
    sudo: 'other',
  });
  await admin.misc.getVersion();
  const encoded = (username: string) => Buffer.from(`${username}:${PASSWORD}`).toString('base64');
  assert.equal(first[0]!.headers.get('authorization'), `Basic ${encoded('synthetic-user')}`);
  assert.equal(first[0]!.headers.has('x-gitea-otp'), false);
  assert.equal(second[0]!.headers.get('authorization'), `Basic ${encoded('synthetic-admin')}`);
  assert.equal(second[0]!.headers.get('x-gitea-otp'), OTP);
  assert.equal(second[0]!.headers.get('sudo'), 'other');
});

test('sudo goes with a token', async () => {
  const { client, sent } = clientFor(() => json({}), { sudo: 'synthetic-other-user' });
  await client.currentUser.get();
  assert.equal(sent[0]!.headers.get('sudo'), 'synthetic-other-user');
});

const custom: Credentials = {
  apply: ({ headers }) => headers.set('Authorization', 'Bearer synthetic-oauth2-token'),
  secrets: () => ['synthetic-oauth2-token'],
};

for (const [options, match] of [
  [{}, /exactly one/],
  [{ token: TOKEN, username: 'u', password: PASSWORD }, /exactly one/],
  [{ token: TOKEN, credentials: custom }, /exactly one/],
  [{ username: 'u' }, /both/],
  [{ password: PASSWORD }, /both/],
  [{ token: TOKEN, otp: OTP }, /otp/],
  [{ credentials: custom, sudo: 'other' }, /credentials provider/],
  [{ token: '' }, /token must not be empty/],
  [{ username: 'u', password: '' }, /password must not be empty/],
  [{ token: TOKEN, sudo: '' }, /sudo must not be empty/],
] as const) {
  test(`credentials are checked: ${JSON.stringify(options)}`, () => {
    assert.throws(() => new GiteaClient({ baseUrl: BASE, ...options }), match);
  });
}

test('a custom credentials provider replaces the others', async () => {
  const { client, sent } = clientFor(() => json({}), { token: undefined, credentials: custom });
  await client.currentUser.get();
  assert.equal(sent[0]!.headers.get('authorization'), 'Bearer synthetic-oauth2-token');
});

for (const [status, type] of [
  [400, BadRequestError],
  [401, AuthenticationError],
  [403, PermissionDeniedError],
  [404, NotFoundError],
  [405, HttpError],
  [409, ConflictError],
  [422, UnprocessableError],
  [429, RateLimitedError],
  [500, ServerError],
] as const) {
  test(`HTTP ${status} carries the status, Gitea's message and the raw body`, async () => {
    const body = { message: 'synthetic refusal', url: `${BASE}/api/swagger` };
    const { client } = clientFor(() => json(body, status), { maxRetries: 0 });
    const error = (await client.repos
      .get('synthetic-owner', 'synthetic-repo')
      .catch((caught: unknown) => caught)) as HttpError;
    assert.equal(error.constructor, type);
    assert.equal(error.status, status);
    assert.equal(error.detail, 'synthetic refusal');
    assert.match(error.message, /synthetic refusal/);
    assert.ok(error.rawBody?.includes('"synthetic refusal"'));
  });
}

test('an error that is not JSON has no detail', async () => {
  const { client } = clientFor(() => new Response('forbidden', { status: 403 }), { maxRetries: 0 });
  const error = (await client.currentUser.get().catch((caught: unknown) => caught)) as PermissionDeniedError;
  assert.ok(error instanceof PermissionDeniedError);
  assert.equal(error.detail, undefined);
  assert.equal(error.rawBody, 'forbidden');
});

const ENCODED = Buffer.from(`synthetic-user:${PASSWORD}`).toString('base64');

for (const [options, secrets] of [
  [{ token: TOKEN }, [TOKEN]],
  [{ token: undefined, username: 'synthetic-user', password: PASSWORD, otp: OTP }, [PASSWORD, OTP, ENCODED]],
] as const) {
  test(`no credential reaches an error or the logs: ${secrets.length} secrets`, async () => {
    const echo = ['refused', ...secrets].join(' ');
    const { client, logs } = clientFor(() => json({ message: echo }, 401), { maxRetries: 0, ...options });
    const error = (await client.currentUser.get().catch((caught: unknown) => caught)) as AuthenticationError;
    assert.ok(error instanceof AuthenticationError);
    assert.equal(error.detail, ['refused', ...secrets.map(() => '***')].join(' '));
    assert.notEqual(logs.length, 0);
    for (const secret of secrets) {
      assert.ok(!error.message.includes(secret));
      assert.ok(!(error.rawBody ?? '').includes(secret));
      assert.ok(!logs.join('\n').includes(secret));
    }
  });
}

test('a file path is one encoded segment', async () => {
  const { client, sent } = clientFor(() => json({ type: 'file', path: 'docs/guide/intro.md' }));
  await client.contents.get('synthetic-owner', 'synthetic-repo', 'docs/guide/intro.md', { ref: 'main' });
  assert.equal(
    sent[0]!.url.href,
    `${BASE}/api/v1/repos/synthetic-owner/synthetic-repo/contents/docs%2Fguide%2Fintro.md?ref=main`,
  );
});

test('iterators follow the next link without fetching it', async () => {
  const { client, sent } = clientFor(
    sequence(
      page([{ id: 1 }, { id: 2 }], 'limit=2&page=2', { last: 'limit=2&page=3' }),
      page([{ id: 3 }, { id: 4 }], 'limit=2&page=3', { prev: 'limit=2&page=1' }),
      page([{ id: 5 }], undefined, { prev: 'limit=2&page=2', first: 'limit=2&page=1' }),
    ),
  );
  const ids: number[] = [];
  for await (const repo of client.currentUser.iterRepos({ limit: 2 })) ids.push(repo.id!);
  assert.deepEqual(ids, [1, 2, 3, 4, 5]);
  assert.deepEqual(
    sent.map(({ url }) => url.href),
    [
      `${BASE}/api/v1/user/repos?limit=2`,
      `${BASE}/api/v1/user/repos?limit=2&page=2`,
      `${BASE}/api/v1/user/repos?limit=2&page=3`,
    ],
  );
});

test('an object page reads its field', async () => {
  const { client, sent } = clientFor(
    sequence(
      json({ ok: true, data: [{ id: 1 }] }, 200, { link: `<${OTHER}/x?page=2>; rel="next"` }),
      json({ ok: true, data: [{ id: 2 }] }),
    ),
  );
  const ids: number[] = [];
  for await (const repo of client.repos.iterSearch({ q: 'synthetic' })) ids.push(repo.id!);
  assert.deepEqual(ids, [1, 2]);
  assert.deepEqual(
    sent.map(({ url }) => Object.fromEntries(url.searchParams)),
    [{ q: 'synthetic' }, { q: 'synthetic', page: '2' }],
  );
});

test('a next link back to a page already sent is a decode error', async () => {
  const { client, sent } = clientFor(sequence(page([{ id: 1 }], 'page=2'), page([{ id: 2 }], 'page=1')));
  const iterate = async () => {
    for await (const _ of client.currentUser.iterRepos({ page: 1 }));
  };
  await assert.rejects(iterate(), DecodeError);
  assert.equal(sent.length, 2);
});

test('an attachment goes as one multipart part, with its name in the query', async () => {
  const { client, sent } = clientFor(() => json({ id: 41, name: 'notes.txt' }, 201));
  const attachment = await client.issues.uploadAttachment('synthetic-owner', 'synthetic-repo', 1, {
    name: 'notes.txt',
    attachment: { filename: 'notes.txt', content: new TextEncoder().encode('synthetic attachment') },
  });
  assert.equal(attachment.id, 41);
  const { url, headers, body } = sent[0]!;
  assert.equal(url.searchParams.get('name'), 'notes.txt');
  const form = await new Response(body, { headers }).formData();
  assert.deepEqual([...form.keys()], ['attachment']);
  assert.equal(await (form.get('attachment') as File).text(), 'synthetic attachment');
});

test('a raw file keeps every byte, and a diff is text', async () => {
  const raw = new Uint8Array([0x73, 0x79, 0x6e, 0xff, 0x00]);
  const { client } = clientFor(
    sequence(
      new Response(raw, { headers: { 'content-type': 'application/octet-stream' } }),
      new Response('diff --git a/x b/x\n', { headers: { 'content-type': 'text/plain; charset=utf-8' } }),
    ),
  );
  const file = await client.contents.downloadRaw('synthetic-owner', 'synthetic-repo', 'assets/logo.bin');
  assert.deepEqual(await file.bytes(), raw);
  const diff = await client.commits.getDiff('synthetic-owner', 'synthetic-repo', '0123abcd', 'diff');
  assert.equal(diff, 'diff --git a/x b/x\n');
});
