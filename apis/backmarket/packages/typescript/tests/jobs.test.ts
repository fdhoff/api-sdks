import assert from 'node:assert/strict';
import { test } from 'node:test';
import { toError } from '../dist/esm/errors.js';
import {
  DecodeError,
  JobTimeoutError,
  Resource,
  StaticCredentials,
  Transport,
  type Operation,
  type WaitOptions,
} from '../dist/esm/runtime/index.js';

const SECRET = 'synthetic-secret';
const BASE = 'https://api.example.test';
const CSV = 'id;error\n1;none\n';

// A synthetic start and status pair. Only the status operation is polled.
const startImport: Operation = {
  id: 'startImport',
  method: 'POST',
  path: '/imports',
  resource: 'imports',
  name: 'start',
  params: [],
  returnsJson: true,
};

const getImport: Operation = {
  id: 'getImport',
  method: 'GET',
  path: '/imports/{import_id}',
  resource: 'imports',
  name: 'get',
  params: [{ wire: 'import_id', name: 'importId', location: 'path' }],
  returnsJson: true,
  job: { state: 'progress.state', done: ['COMPLETE'], failed: ['FAILED'] },
  security: [[{ scheme: 'key', scopes: [] }]],
};

interface ImportStatus {
  import_id: number;
  progress: { state: string };
}

class Imports extends Resource {
  wait(options?: WaitOptions, operation = getImport): Promise<ImportStatus> {
    return this.pollJob(operation, { importId: 7 }, options);
  }
}

interface Sent {
  url: string;
  headers: Headers;
  redirect: RequestInit['redirect'];
}

type Reply = (url: URL) => Response;

function client(reply: Reply) {
  const sent: Sent[] = [];
  const logs: string[] = [];
  const transport = new Transport({
    baseUrl: BASE,
    credentials: new StaticCredentials({ Authorization: SECRET }, [SECRET]),
    headers: { 'User-Agent': 'test' },
    toError,
    fetch: async (input, init = {}) => {
      sent.push({ url: String(input), headers: new Headers(init.headers), redirect: init.redirect });
      return reply(new URL(String(input)));
    },
    logger: { debug: (message) => logs.push(message), info: (message) => logs.push(message) },
    timeoutMs: 1000,
    maxRetries: 2,
    retryBaseDelayMs: 0,
    rateLimitWaitMs: 0,
    maxRetryWaitMs: 1000,
  });
  return { transport, imports: new Imports(transport), sent, logs };
}

const status = (state: unknown): Response =>
  new Response(JSON.stringify({ import_id: 7, progress: { state } }), {
    status: 200,
    headers: { 'content-type': 'application/json' },
  });

const replies =
  (...responses: Response[]): Reply =>
  () =>
    responses.shift() ?? assert.fail('no reply scripted');

const csv = (): Response => new Response(CSV, { status: 200, headers: { 'content-type': 'text/csv' } });
const redirect = (location: string): Response => new Response(null, { status: 302, headers: { location } });
const text = async (download: { bytes(): Promise<Uint8Array> }): Promise<string> =>
  new TextDecoder().decode(await download.bytes());

test('wait polls until the job is done and returns its last status', async () => {
  const { imports, sent } = client(replies(status('WAITING'), status('RUNNING'), status('COMPLETE')));
  const result = await imports.wait({ intervalMs: 0, timeoutMs: 5000 });
  assert.equal(result.progress.state, 'COMPLETE');
  assert.deepEqual(
    sent.map(({ url }) => url),
    Array(3).fill(`${BASE}/imports/7`),
  );
});

test('a failed job returns its status rather than throwing', async () => {
  const { imports, sent } = client(replies(status('RUNNING'), status('FAILED')));
  assert.equal((await imports.wait({ intervalMs: 0, timeoutMs: 5000 })).progress.state, 'FAILED');
  assert.equal(sent.length, 2);
});

test('a job that outlasts the deadline is a typed timeout with its last status', async () => {
  const { imports, sent } = client(() => status('RUNNING'));
  await assert.rejects(imports.wait({ intervalMs: 20, timeoutMs: 50 }), (error: unknown) => {
    assert.ok(error instanceof JobTimeoutError);
    assert.equal(error.kind, 'job_timeout');
    assert.equal((error.result as ImportStatus).progress.state, 'RUNNING');
    return true;
  });
  assert.ok(sent.length >= 2);
});

test('a rate limit while polling is retried after its Retry-After', async () => {
  const limited = new Response('', { status: 429, headers: { 'retry-after': '0' } });
  const { imports, sent } = client(replies(status('RUNNING'), limited, status('COMPLETE')));
  assert.equal((await imports.wait({ intervalMs: 0, timeoutMs: 5000 })).progress.state, 'COMPLETE');
  assert.equal(sent.length, 3);
});

test('a state that is not a string is a decode error', async () => {
  const { imports } = client(() => status(3));
  await assert.rejects(imports.wait({ intervalMs: 0, timeoutMs: 5000 }), (error: unknown) => {
    assert.ok(error instanceof DecodeError);
    assert.match(error.message, /progress\.state/);
    return true;
  });
});

test('wait refuses a negative interval or timeout and an operation without a job', async () => {
  const { imports, sent } = client(() => status('COMPLETE'));
  await assert.rejects(imports.wait({ intervalMs: -1, timeoutMs: 5000 }), { name: 'RangeError', message: /interval/ });
  await assert.rejects(imports.wait({ intervalMs: 0, timeoutMs: -1 }), { name: 'RangeError', message: /timeout/ });
  await assert.rejects(imports.wait({ intervalMs: 0, timeoutMs: 5000 }, startImport), {
    name: 'TypeError',
    message: /does not report a job/,
  });
  assert.deepEqual(sent, []);
});

test('aborting the signal stops the wait between polls with its reason', async () => {
  const controller = new AbortController();
  const reason = new Error('stopped');
  const { imports, sent } = client(() => {
    setTimeout(() => controller.abort(reason), 10);
    return status('RUNNING');
  });
  const started = performance.now();
  await assert.rejects(imports.wait({ intervalMs: 60_000, timeoutMs: 600_000, signal: controller.signal }), reason);
  assert.ok(performance.now() - started < 5000);
  assert.equal(sent.length, 1);
});

test('a download URL on the base origin sends credentials, and logs no query', async () => {
  const { transport, sent, logs } = client(csv);
  const download = await transport.downloadUrl(`${BASE}/files/report.csv?sig=abc`);
  assert.equal(download.contentType, 'text/csv');
  assert.equal(await text(download), CSV);
  assert.equal(sent[0]?.headers.get('authorization'), SECRET);
  assert.equal(sent[0]?.headers.get('accept-encoding'), 'identity');
  assert.equal(sent[0]?.redirect, 'manual');
  assert.ok(logs.some((line) => line.includes(`${BASE}/files/report.csv`)));
  assert.ok(!logs.some((line) => line.includes('sig=abc')));
});

for (const url of [
  'https://files.example.test/report.csv',
  'http://api.example.test/report.csv',
  'https://api.example.test:8443/report.csv',
]) {
  test(`a download URL on another scheme, host or port sends no credentials: ${url}`, async () => {
    const { transport, sent } = client(csv);
    assert.equal(await text(await transport.downloadUrl(url)), CSV);
    assert.equal(sent[0]?.headers.get('authorization'), null);
    assert.equal(sent[0]?.headers.get('user-agent'), 'test');
  });
}

test('a redirect to another origin drops credentials for the rest of the chain', async () => {
  const { transport, sent } = client((url) => {
    if (url.host === 'api.example.test' && url.pathname === '/files/1')
      return redirect('https://files.example.test/signed/1');
    if (url.host === 'files.example.test') return redirect(`${BASE}/files/final`);
    return csv();
  });
  assert.equal(await text(await transport.downloadUrl(`${BASE}/files/1`)), CSV);
  assert.deepEqual(
    sent.map(({ url }) => url),
    [`${BASE}/files/1`, 'https://files.example.test/signed/1', `${BASE}/files/final`],
  );
  assert.deepEqual(
    sent.map(({ headers }) => headers.get('authorization')),
    [SECRET, null, null],
  );
});

test('a relative redirect on the base origin keeps credentials', async () => {
  const { transport, sent } = client((url) => (url.pathname === '/files/1' ? redirect('/files/2') : csv()));
  await (await transport.downloadUrl(`${BASE}/files/1`)).bytes();
  assert.deepEqual(
    sent.map(({ url, headers }) => [url, headers.get('authorization')]),
    [
      [`${BASE}/files/1`, SECRET],
      [`${BASE}/files/2`, SECRET],
    ],
  );
});

test('a download URL refuses a relative URL and endless redirects', async () => {
  const { transport, sent } = client((url) => redirect(url.href));
  await assert.rejects(transport.downloadUrl('/files/1'), { name: 'TypeError', message: /absolute/ });
  await assert.rejects(transport.downloadUrl('ftp://api.example.test/files/1'), {
    name: 'TypeError',
    message: /absolute/,
  });
  assert.deepEqual(sent, []);
  await assert.rejects(transport.downloadUrl(`${BASE}/files/1`), (error: unknown) => {
    assert.ok(error instanceof DecodeError);
    assert.match(error.message, /redirects/);
    return true;
  });
  assert.equal(sent.length, 6);
});

test('a redirect without a usable Location is a decode error', async () => {
  for (const reply of [new Response(null, { status: 307 }), redirect('ftp://files.example.test/1')]) {
    const { transport } = client(() => reply);
    await assert.rejects(transport.downloadUrl(`${BASE}/files/1`), DecodeError);
  }
});
