import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiConnectionError, ServerError } from 'backmarket-seller';
import { toError } from '../dist/esm/errors.js';
import { Resource, Transport, type Credentials, type Operation } from '../dist/esm/runtime/index.js';

const transfer: Operation = {
  id: 'create-transfer',
  method: 'POST',
  path: '/transfers',
  resource: 'transfers',
  name: 'create',
  params: [],
  hasBody: true,
  returnsJson: true,
  idempotencyKey: 'idempotency_key',
};

const item: Operation = {
  id: 'create-item',
  method: 'POST',
  path: '/items',
  resource: 'items',
  name: 'create',
  params: [],
  hasBody: true,
  returnsJson: true,
};

const anonymous: Credentials = { apply: () => {}, secrets: () => [] };

class Calls extends Resource {
  run<T>(operation: Operation, body: unknown): Promise<T> {
    return this.call<T>(operation, body, {});
  }
}

type Reply = () => Response;

function callsWith(replies: Reply[]) {
  const sent: string[] = [];
  const transport = new Transport({
    baseUrl: 'http://idempotency.invalid',
    credentials: anonymous,
    headers: {},
    toError,
    fetch: async (_input, init = {}) => {
      sent.push(await new Response(init.body).text());
      const reply = replies.shift();
      if (reply === undefined) throw new Error('no reply scripted');
      return reply();
    },
    timeoutMs: 1000,
    maxRetries: 2,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
  });
  return { calls: new Calls(transport), sent };
}

const status =
  (code: number): Reply =>
  () =>
    new Response(null, { status: code });
const ok =
  (body: unknown): Reply =>
  () =>
    Response.json(body);
const dropped: Reply = () => {
  throw new TypeError('fetch failed');
};

test('a keyed write is retried on a server error with the same body', async () => {
  const body = { idempotency_key: 'k-1', amount: 5 };
  const { calls, sent } = callsWith([status(503), ok({ id: 't-1' })]);
  assert.deepEqual(await calls.run(transfer, body), { id: 't-1' });
  assert.equal(sent.length, 2);
  assert.equal(sent[0], sent[1]);
  assert.deepEqual(JSON.parse(sent[0]!), body);
});

test('a keyed write is retried after a dropped connection', async () => {
  const { calls, sent } = callsWith([dropped, ok({ id: 't-2' })]);
  assert.deepEqual(await calls.run(transfer, { idempotency_key: 'k-2' }), { id: 't-2' });
  assert.equal(sent[0], sent[1]);
});

const unkeyed: [string, Operation, Record<string, unknown>][] = [
  ['an unmarked write', item, { idempotency_key: 'k-3', name: 'widget' }],
  ['an empty key', transfer, { idempotency_key: '', amount: 5 }],
  ['a null key', transfer, { idempotency_key: null, amount: 5 }],
  ['a missing key', transfer, { amount: 5 }],
];

for (const [label, operation, body] of unkeyed) {
  test(`${label} is not retried on a server error or a dropped connection`, async () => {
    const server = callsWith([status(503), ok({})]);
    await assert.rejects(server.calls.run(operation, body), ServerError);
    assert.equal(server.sent.length, 1);
    const connection = callsWith([dropped, ok({})]);
    await assert.rejects(connection.calls.run(operation, body), ApiConnectionError);
    assert.equal(connection.sent.length, 1);
  });
}

test('a write without a key is still retried on a rate limit', async () => {
  const { calls, sent } = callsWith([status(429), ok({ id: 't-3' })]);
  assert.deepEqual(await calls.run(transfer, { amount: 5 }), { id: 't-3' });
  assert.equal(sent.length, 2);
});
