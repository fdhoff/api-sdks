import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiTimeoutError, NotFoundError, RateLimitedError } from 'backmarket-seller';
import { toError } from '../dist/esm/errors.js';
import {
  Resource,
  Transport,
  type AuthRequest,
  type Credentials,
  type Download,
  type Operation,
  type RawBody,
  type Settings,
} from '../dist/esm/runtime/index.js';

const BASE = 'http://binary.invalid';
const TOKEN = 'synthetic-token';
const PDF = Uint8Array.of(0x25, 0x50, 0x44, 0x46, 0x00, 0xff, 0xfe, 0x80, 0x0a, 0xc3, 0x28);

const download: Operation = {
  id: 'download-file',
  method: 'GET',
  path: '/files/{id}',
  resource: 'files',
  name: 'download',
  params: [{ wire: 'id', name: 'id', location: 'path' }],
  returnsBinary: true,
  security: [[{ scheme: 'key', scopes: [] }]],
};

const upload: Operation = {
  id: 'upload-file',
  method: 'POST',
  path: '/files',
  resource: 'files',
  name: 'upload',
  params: [],
  rawBody: 'application/octet-stream',
  returnsJson: true,
  security: [[{ scheme: 'key', scopes: [] }]],
};

const report: Operation = {
  id: 'get-report',
  method: 'GET',
  path: '/report',
  resource: 'reports',
  name: 'get',
  params: [],
  returnsText: true,
  security: [[{ scheme: 'key', scopes: [] }]],
};

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
  run<T>(operation: Operation, body?: RawBody, params: Record<string, unknown> = {}): Promise<T> {
    return this.call<T>(operation, body, params);
  }
}

interface Sent {
  url: string;
  headers: Headers;
  body: Uint8Array;
}

type Reply = (signal: AbortSignal | undefined) => Response;

function callsWith(replies: Reply[], settings: Partial<Settings> = {}) {
  const credentials = new Recorder();
  const sent: Sent[] = [];
  const logs: string[] = [];
  const transport = new Transport({
    baseUrl: BASE,
    credentials,
    headers: { 'User-Agent': 'test' },
    toError,
    fetch: async (input, init = {}) => {
      const body =
        init.body === undefined ? new Uint8Array() : new Uint8Array(await new Response(init.body).arrayBuffer());
      sent.push({ url: String(input), headers: new Headers(init.headers), body });
      const reply = replies.shift();
      if (reply === undefined) throw new Error('no reply scripted');
      return reply(init.signal ?? undefined);
    },
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    timeoutMs: 1000,
    maxRetries: 1,
    retryBaseDelayMs: 1,
    rateLimitWaitMs: 1,
    maxRetryWaitMs: 1,
    ...settings,
  });
  return { calls: new Calls(transport), sent, credentials, logs };
}

const bytes =
  (body: Uint8Array, type = 'application/pdf'): Reply =>
  () =>
    new Response(body, { status: 200, headers: { 'content-type': type } });

test('a binary response returns the exact bytes and content type, as a stream', async () => {
  const { calls, sent, logs } = callsWith([bytes(PDF)]);
  const result = await calls.run<Download>(download, undefined, { id: 7 });
  assert.equal(result.contentType, 'application/pdf');
  assert.ok(result.body instanceof ReadableStream);
  assert.deepEqual(await result.bytes(), PDF);
  assert.equal(sent[0]?.url, `${BASE}/files/7`);
  assert.equal(sent[0]?.headers.get('accept-encoding'), 'identity');
  assert.ok(logs.some((line) => line.includes('(streamed)')));
});

test('an empty binary response is an empty download, and a missing content type is empty', async () => {
  const { calls } = callsWith([() => new Response(null, { status: 200 })]);
  const result = await calls.run<Download>(download, undefined, { id: 1 });
  assert.equal(result.contentType, '');
  assert.deepEqual(await result.bytes(), new Uint8Array());
});

test('the deadline keeps running while the download is read', async () => {
  // As fetch does, an abort errors a body still arriving with the signal's reason. The timeout's timer does
  // not keep Node running, so a timer stands in for the open socket a real fetch holds.
  const slow: Reply = (signal) =>
    new Response(
      new ReadableStream<Uint8Array>({
        start(controller) {
          controller.enqueue(Uint8Array.of(1));
          const socket = setTimeout(() => controller.close(), 5000);
          signal?.addEventListener(
            'abort',
            () => {
              clearTimeout(socket);
              controller.error(signal.reason);
            },
            { once: true },
          );
        },
      }),
      { status: 200, headers: { 'content-type': 'application/octet-stream' } },
    );
  const { calls } = callsWith([slow], { timeoutMs: 50 });
  const result = await calls.run<Download>(download, undefined, { id: 1 });
  await assert.rejects(result.bytes(), ApiTimeoutError);
});

test('a failed binary call is a typed error with its text redacted', async () => {
  const missing: Reply = () =>
    new Response(JSON.stringify({ message: `no file for ${TOKEN}` }), {
      status: 404,
      headers: { 'content-type': 'application/json' },
    });
  const { calls } = callsWith([missing]);
  await assert.rejects(calls.run<Download>(download, undefined, { id: 1 }), (error: unknown) => {
    assert.ok(error instanceof NotFoundError);
    assert.equal(error.status, 404);
    assert.ok(!(error.rawBody ?? '').includes(TOKEN));
    return true;
  });
});

const rateLimited: Reply = () => new Response('', { status: 429 });
const created: Reply = () =>
  new Response(JSON.stringify({ id: 1 }), { status: 200, headers: { 'content-type': 'application/json' } });

test('raw bytes are sent unchanged with the declared content type, seen by credentials and retried', async () => {
  const { calls, sent, credentials } = callsWith([rateLimited, created]);
  assert.deepEqual(await calls.run(upload, PDF), { id: 1 });
  assert.equal(sent.length, 2);
  for (const request of sent) {
    assert.deepEqual(request.body, PDF);
    assert.equal(request.headers.get('content-type'), 'application/octet-stream');
  }
  assert.deepEqual(credentials.seen[0]?.body, PDF);
});

test('a Blob is sent as its bytes, with the declared content type', async () => {
  const { calls, sent } = callsWith([created]);
  await calls.run(upload, new Blob([PDF], { type: 'text/plain' }));
  assert.deepEqual(sent[0]?.body, PDF);
  assert.equal(sent[0]?.headers.get('content-type'), 'application/octet-stream');
});

test('a streamed upload is sent once, and a failure that would resend it is raised', async () => {
  const { calls, sent, credentials } = callsWith([rateLimited, created]);
  const stream = new ReadableStream<Uint8Array>({
    start(controller) {
      controller.enqueue(PDF);
      controller.close();
    },
  });
  await assert.rejects(calls.run(upload, stream), RateLimitedError);
  assert.equal(sent.length, 1);
  assert.deepEqual(sent[0]?.body, PDF);
  assert.deepEqual(credentials.seen[0]?.body, new Uint8Array());
});

test('a text response that is not JSON is returned as text', async () => {
  const table = 'id\tname\n1\tsynthetic\n';
  const { calls } = callsWith([
    () => new Response(table, { status: 200, headers: { 'content-type': 'text/tab-separated-values' } }),
  ]);
  assert.equal(await calls.run<string>(report), table);
});
