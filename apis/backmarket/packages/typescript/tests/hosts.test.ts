import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiError } from 'backmarket-seller';
import {
  Resource,
  selectHosts,
  Transport,
  type AuthRequest,
  type Credentials,
  type Operation,
  type Settings,
} from '../dist/esm/runtime/index.js';

const MAIN = 'http://main.invalid';
const FILES = 'http://files.invalid';
const TOKEN = 'synthetic-token';

const listItems: Operation = {
  id: 'list-items',
  method: 'GET',
  path: '/items',
  resource: 'items',
  name: 'list',
  params: [
    { wire: 'offset', name: 'offset', location: 'query' },
    { wire: 'X-Tenant', name: 'xTenant', location: 'header' },
  ],
  returnsJson: true,
  paging: { style: 'offset', items: 'results', total: 'count', offset: 'offset' },
  security: [[{ scheme: 'key', scopes: [] }]],
};

const listFiles: Operation = { ...listItems, id: 'list-files', path: '/files', host: 'files' };
const plain: Operation = { ...listItems, id: 'plain', params: [], host: 'main' };
const unknownHost: Operation = { ...listItems, id: 'unknown', host: 'media' };

class Recorder implements Credentials {
  readonly seen: AuthRequest[] = [];

  apply(request: AuthRequest): void {
    this.seen.push(request);
    request.headers.set('authorization', `Bearer ${TOKEN}`);
  }

  secrets(): readonly string[] {
    return [TOKEN];
  }
}

class Calls extends Resource {
  run(operation: Operation, params: Record<string, unknown> = {}): Promise<unknown> {
    return this.call(operation, undefined, params);
  }

  async all(operation: Operation, params: Record<string, unknown> = {}): Promise<unknown[]> {
    const items: unknown[] = [];
    for await (const item of this.paginate(operation, undefined, params)) items.push(item);
    return items;
  }
}

const json = (body: unknown): Response =>
  new Response(JSON.stringify(body), { status: 200, headers: { 'content-type': 'application/json' } });

function callsWith(settings: Partial<Settings>, replies: unknown[] = [{ count: 0, results: [] }]) {
  const credentials = new Recorder();
  const sent: { url: URL; headers: Headers }[] = [];
  const transport = new Transport({
    baseUrl: MAIN,
    hosts: { main: MAIN, files: FILES },
    credentials,
    headers: { 'User-Agent': 'test' },
    toError: (context) => new ApiError(`status ${context.status}`, { status: context.status }),
    fetch: async (input, init = {}) => {
      sent.push({ url: new URL(String(input)), headers: new Headers(init.headers) });
      return json(replies.shift() ?? { count: 0, results: [] });
    },
    timeoutMs: 1000,
    maxRetries: 0,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
    ...settings,
  });
  return { calls: new Calls(transport), sent, credentials };
}

test('an operation without a host key goes to the base URL, and one with a key to its host', async () => {
  const { calls, sent } = callsWith({});
  await calls.run(listItems);
  await calls.run(listFiles);
  await calls.run(plain);
  assert.deepEqual(
    sent.map(({ url }) => url.href),
    [`${MAIN}/items`, `${FILES}/files`, `${MAIN}/items`],
  );
  assert.equal(sent[1]?.headers.get('authorization'), `Bearer ${TOKEN}`);
});

test('an iterator reissues every page against the operation host', async () => {
  const pages = [
    { count: 3, results: [{ id: 'a' }, { id: 'b' }] },
    { count: 3, results: [{ id: 'c' }] },
  ];
  const { calls, sent } = callsWith({}, pages);
  assert.deepEqual(await calls.all(listFiles), [{ id: 'a' }, { id: 'b' }, { id: 'c' }]);
  assert.deepEqual(
    sent.map(({ url }) => url.href),
    [`${FILES}/files`, `${FILES}/files?offset=2`],
  );
});

test('a host key with no URL fails before credentials are applied or anything is sent', async () => {
  const { calls, sent, credentials } = callsWith({});
  await assert.rejects(calls.run(unknownHost), { message: 'No base URL for host "media"' });
  const { calls: bare, sent: bareSent } = callsWith({ hosts: undefined });
  await assert.rejects(bare.run(listFiles), /No base URL for host "files"/);
  assert.equal(credentials.seen.length, 0);
  assert.equal(sent.length + bareSent.length, 0);
});

const ENVIRONMENTS = {
  production: { main: 'https://main.example.test', files: 'https://files.example.test' },
  sandbox: { main: 'https://main.sandbox.example.test', files: 'https://files.sandbox.example.test' },
};

test('selectHosts picks a named environment', () => {
  const hosts = selectHosts(ENVIRONMENTS, 'sandbox');
  assert.deepEqual(hosts, ENVIRONMENTS.sandbox);
  assert.notEqual(hosts, ENVIRONMENTS.sandbox);
  assert.throws(() => selectHosts(ENVIRONMENTS, 'staging'), {
    message: 'Unknown environment "staging"; expected one of: production, sandbox',
  });
});

test('selectHosts takes a custom map that names exactly the environment keys', () => {
  const custom = { main: 'http://127.0.0.1:4010/', files: 'http://127.0.0.1:4010//' };
  assert.deepEqual(selectHosts(ENVIRONMENTS, 'production', custom), {
    main: 'http://127.0.0.1:4010',
    files: 'http://127.0.0.1:4010',
  });
  assert.deepEqual(selectHosts(ENVIRONMENTS, 'production', {}), ENVIRONMENTS.production);
  assert.throws(() => selectHosts(ENVIRONMENTS, 'production', { main: MAIN }), { message: 'hosts lacks: files' });
  assert.throws(() => selectHosts(ENVIRONMENTS, 'production', { main: MAIN, files: FILES, media: MAIN }), {
    message: 'hosts has unknown keys: media',
  });
});

test('a declared header takes the client default, and a value passed to the call replaces it', async () => {
  const { calls, sent, credentials } = callsWith({
    headers: { 'User-Agent': 'test', 'x-tenant': 'client-wide' },
    headerDefaults: { 'x-TENANT': 'acme' },
  });
  await calls.run(listItems);
  await calls.run(listItems, { xTenant: 'other' });
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('x-tenant')),
    ['acme', 'other'],
  );
  assert.equal(credentials.seen[0]?.headers.get('x-tenant'), 'acme');
});

test('a header default never reaches an operation that does not declare the header', async () => {
  const { calls, sent } = callsWith({ headerDefaults: { 'X-Tenant': 'acme' } });
  await calls.run(plain);
  assert.equal(sent[0]?.headers.has('x-tenant'), false);
});

test('a declared header is not sent without a default or a value', async () => {
  const { calls, sent } = callsWith({});
  await calls.run(listItems, { xTenant: undefined });
  await calls.run(listItems, { xTenant: null });
  assert.deepEqual(
    sent.map(({ headers }) => headers.has('x-tenant')),
    [false, false],
  );
});
