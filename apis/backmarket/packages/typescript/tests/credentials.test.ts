import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiError } from 'backmarket-seller';
import {
  Resource,
  StaticCredentials,
  Transport,
  type AuthRequest,
  type Credentials,
  type Operation,
} from '../dist/esm/runtime/index.js';

const BASE = 'http://mock.invalid';
const KEY = 'synthetic-key';
const SHARED = 'synthetic-shared-secret';

type Handler = (url: URL, init: RequestInit) => Response | Promise<Response>;

const getItem: Operation = {
  id: 'get-item',
  method: 'GET',
  path: '/items/{id}',
  resource: 'items',
  name: 'get',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsJson: true,
  security: [
    [
      { scheme: 'key', scopes: [] },
      { scheme: 'user', scopes: ['items_r'] },
    ],
  ],
};

const upload: Operation = {
  id: 'upload',
  method: 'POST',
  path: '/files',
  resource: 'files',
  name: 'upload',
  params: [{ wire: 'file', name: 'file', location: 'form' }],
  security: [[{ scheme: 'key', scopes: [] }]],
};

/** A synthetic bearer token that changes on each refresh, beside a fixed key. */
class Tokens implements Credentials {
  version = 1;
  refreshes = 0;
  readonly seen: AuthRequest[] = [];

  get token(): string {
    return `synthetic-access-${this.version}`;
  }

  apply(request: AuthRequest): void {
    this.seen.push(request);
    request.headers.set('x-api-key', `${KEY}:${SHARED}`);
    const user = request.operation.security?.some((requirement) => requirement.some(({ scheme }) => scheme === 'user'));
    if (user) request.headers.set('authorization', `Bearer ${this.token}`);
  }

  secrets(): readonly string[] {
    return [KEY, SHARED, this.token, 'synthetic-refresh'];
  }

  async refresh(): Promise<boolean> {
    this.refreshes += 1;
    await new Promise((resolve) => setTimeout(resolve, 10));
    this.version += 1;
    return true;
  }
}

class Calls extends Resource {
  run(operation: Operation, params: Record<string, unknown>): Promise<unknown> {
    return this.call(operation, undefined, params);
  }
}

function callsFor(credentials: Credentials, handler: Handler, logs: string[] = []) {
  const sent: { url: URL; init: RequestInit }[] = [];
  const transport = new Transport({
    baseUrl: BASE,
    credentials,
    headers: { 'User-Agent': 'test' },
    toError: (context) =>
      new ApiError(`status ${context.status}: ${context.text}`, { status: context.status, rawBody: context.text }),
    fetch: async (input, init = {}) => {
      const url = new URL(String(input));
      sent.push({ url, init });
      return handler(url, init);
    },
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    timeoutMs: 1000,
    maxRetries: 1,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
  });
  return { calls: new Calls(transport), sent };
}

const json = (body: unknown, status = 200): Response =>
  new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });

const accepts =
  (token: string): Handler =>
  (_url, init) =>
    new Headers(init.headers).get('authorization') === `Bearer ${token}`
      ? json({ id: 1 })
      : json({ error: 'expired' }, 401);

test('apply sees the final request on every attempt', async () => {
  const credentials = new Tokens();
  const replies = [new Response(null, { status: 503 }), json({ id: 1 })];
  const { calls, sent } = callsFor(credentials, () => replies.shift() as Response);
  assert.deepEqual(await calls.run(getItem, { id: 'a b' }), { id: 1 });
  assert.equal(credentials.seen.length, 2);
  const [first] = credentials.seen;
  assert.equal(first?.method, 'GET');
  assert.equal(first?.url, `${BASE}/items/a%20b`);
  assert.equal(first?.body.length, 0);
  assert.equal(first?.headers.get('user-agent'), 'test');
  assert.equal(first?.operation, getItem);
  for (const { init } of sent) {
    const headers = new Headers(init.headers);
    assert.equal(headers.get('authorization'), 'Bearer synthetic-access-1');
    assert.equal(headers.get('x-api-key'), `${KEY}:${SHARED}`);
  }
});

test('apply gets the multipart bytes that are sent', async () => {
  const credentials = new Tokens();
  const { calls, sent } = callsFor(credentials, () => json({}));
  await calls.run(upload, { file: { filename: 'a.txt', content: new TextEncoder().encode('hello') } });
  const [seen] = credentials.seen;
  const { init } = sent[0] ?? { init: {} as RequestInit };
  assert.deepEqual(new Uint8Array(init.body as Uint8Array), seen?.body);
  assert.match(new TextDecoder().decode(seen?.body), /hello/);
  assert.equal(new Headers(init.headers).get('content-type'), seen?.headers.get('content-type'));
  assert.equal(new Headers(init.headers).get('authorization'), null);
});

test('a 401 refreshes once and retries once', async () => {
  const credentials = new Tokens();
  assert.deepEqual(await callsFor(credentials, accepts('synthetic-access-2')).calls.run(getItem, { id: 1 }), { id: 1 });
  assert.equal(credentials.refreshes, 1);

  const stale = new Tokens();
  await assert.rejects(() => callsFor(stale, accepts('never')).calls.run(getItem, { id: 1 }), { status: 401 });
  assert.equal(stale.refreshes, 1);
  assert.equal(stale.seen.length, 2);
});

test('a 401 is final when the credentials cannot refresh', async () => {
  const { calls, sent } = callsFor(new StaticCredentials({ Authorization: 'Basic synthetic' }, ['synthetic']), () =>
    json({}, 401),
  );
  await assert.rejects(() => calls.run(getItem, { id: 1 }), { status: 401 });
  assert.equal(sent.length, 1);
});

test('concurrent calls share one refresh', async () => {
  const credentials = new Tokens();
  const { calls } = callsFor(credentials, accepts('synthetic-access-2'));
  const results = await Promise.all([1, 2, 3, 4].map((id) => calls.run(getItem, { id })));
  assert.deepEqual(results, [{ id: 1 }, { id: 1 }, { id: 1 }, { id: 1 }]);
  assert.equal(credentials.refreshes, 1);
});

test('every secret is kept out of errors and logs', async () => {
  const credentials = new Tokens();
  const logs: string[] = [];
  const body = `bad ${KEY}:${SHARED} and synthetic-access-1 and synthetic-refresh`;
  const { calls } = callsFor(credentials, () => new Response(body, { status: 400 }), logs);
  const error = (await calls.run(getItem, { id: SHARED }).catch((caught: unknown) => caught)) as ApiError;
  assert.equal(error.rawBody, 'bad ***:*** and *** and ***');
  const output = `${error.message} ${error.rawBody} ${logs.join(' ')}`;
  for (const secret of credentials.secrets()) assert.equal(output.includes(secret), false, secret);
});
