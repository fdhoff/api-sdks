import assert from 'node:assert/strict';
import { after, before, test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { get } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { loadCases, validateCase } from './cases.mjs';
import { checkCase, fill, matches } from './check.mjs';
import { startHarness, unhost } from './harness.mjs';
import { runCases, startDriver } from './run.mjs';

const FIXTURE = fileURLToPath(new URL('./fixtures/driver.mjs', import.meta.url));
const SIGNING_CASES = fileURLToPath(new URL('./fixtures/signing', import.meta.url));
const fixtureCases = (style) => fileURLToPath(new URL(`./fixtures/cases/${style}`, import.meta.url));
const operations = new Set(['list-items', 'create-item', 'create-transfer', 'list-files', 'download-file', 'upload-file', 'get-report']);

const baseCase = () => ({
  name: 'lists-items',
  request: { operation: 'list-items' },
  mock: { responses: [{ status: 200, body: { id: 1 } }] },
  wire: [{ method: 'GET', path: '/items', headers: { authorization: 'Basic {{token}}' } }],
  expect: { result: { id: 1 } },
});

const sent = (overrides = {}) => ({
  method: 'GET',
  path: '/items',
  query: {},
  headers: { authorization: 'Basic t0ken' },
  body: '',
  at: 0,
  ...overrides,
});

test('validateCase accepts a well-formed case', () => {
  assert.deepEqual(validateCase(baseCase(), operations), []);
});

test('validateCase accepts a dropped connection in place of a status', () => {
  const item = { ...baseCase(), mock: { responses: [{ drop: true }] } };
  assert.deepEqual(validateCase(item, operations), []);
});

test('validateCase reports each malformed part', () => {
  const invalid = [
    [{ name: 'Not Kebab' }, /kebab-case/],
    [{ extra: true }, /unknown key case\.extra/],
    [{ request: { operation: 'missing' } }, /unknown operation missing/],
    [{ mock: {} }, /exactly one of prism or responses/],
    [{ mock: { prism: {}, responses: [{ status: 200 }] } }, /exactly one of prism or responses/],
    [{ mock: { responses: [{ status: 200 }, { status: 200 }] } }, /2 scripted responses but 1 wire/],
    [{ mock: { responses: [{ body: 'no status' }] } }, /status must be an integer/],
    [{ mock: { responses: [{ drop: false }] } }, /drop must be true and alone/],
    [{ mock: { responses: [{ drop: true, status: 200 }] } }, /drop must be true and alone/],
    [{ mock: { responses: [{ status: 200, gzip: 'yes' }] } }, /gzip must be true/],
    [{ mock: { responses: [{ status: 200, cut: 1.5 }] } }, /cut must be an integer/],
    [{ wire: [] }, /wire must be a non-empty list/],
    [{ wire: [{ method: 'GET', path: '/items', body: {}, parts: {} }] }, /at most one of body, body_base64 or parts/],
    [{ wire: [{ method: 'GET', path: '/items', body: {}, body_base64: '' }] }, /at most one of body, body_base64 or parts/],
    [{ request: { operation: 'upload-file', body: {}, raw_body_base64: '' } }, /at most one of body, multipart or raw_body_base64/],
    [{ mock: { responses: [{ status: 200, body: 'a', body_base64: 'YQ==' }] } }, /at most one of body or body_base64/],
    [{ expect: {} }, /exactly one of result/],
    [{ expect: { error: { status: 500 } } }, /needs a kind/],
  ];
  for (const [override, pattern] of invalid) {
    assert.match(validateCase({ ...baseCase(), ...override }, operations).join('\n'), pattern);
  }
});

test('matches treats objects as subsets and lists as exact in length', () => {
  assert.ok(matches({ a: 1 }, { a: 1, b: 2 }));
  assert.ok(!matches({ a: 1 }, { a: 2 }));
  assert.ok(matches([{ a: 1 }], [{ a: 1, b: 2 }]));
  assert.ok(!matches([{ a: 1 }], [{ a: 1 }, { a: 2 }]));
  assert.ok(matches(null, null));
  assert.ok(!matches({ a: 1 }, null));
});

test('fill expands the token at any depth', () => {
  assert.deepEqual(fill({ a: ['Basic {{token}}'], b: 1 }, { token: 't' }), { a: ['Basic t'], b: 1 });
});

test('checkCase passes a matching exchange', () => {
  assert.deepEqual(checkCase(baseCase(), [sent()], { result: { id: 1, extra: 2 }, logs: [] }, { token: 't0ken' }), []);
});

test('checkCase reports a wire mismatch', () => {
  const item = baseCase();
  const cases = [
    [[], /sent 0 requests/],
    [[sent(), sent()], /sent 2 requests/],
    [[sent({ method: 'POST' })], /method is POST/],
    [[sent({ path: '/other' })], /path is \/other/],
    [[sent({ query: { page: '2' } })], /query is/],
    [[sent({ headers: {} })], /header authorization is undefined/],
  ];
  for (const [requests, pattern] of cases) {
    assert.match(checkCase(item, requests, { result: { id: 1 } }, { token: 't0ken' }).join('\n'), pattern);
  }
});

test('checkCase compares the host only where the wire names one', () => {
  const item = { ...baseCase(), wire: [{ ...baseCase().wire[0], host: 'files' }] };
  assert.deepEqual(checkCase(item, [sent({ host: 'files' })], { result: { id: 1 }, logs: [] }, { token: 't0ken' }), []);
  assert.match(checkCase(item, [sent({ host: 'main' })], { result: { id: 1 }, logs: [] }, { token: 't0ken' }).join(), /host is main/);
  assert.match(checkCase(item, [sent()], { result: { id: 1 }, logs: [] }, { token: 't0ken' }).join(), /host is undefined/);
  assert.deepEqual(checkCase(baseCase(), [sent({ host: 'files' })], { result: { id: 1 }, logs: [] }, { token: 't0ken' }), []);
});

test('checkCase enforces header patterns, absent headers, bodies and delays', () => {
  const item = baseCase();
  item.wire = [
    { method: 'GET', path: '/items' },
    {
      method: 'GET',
      path: '/items',
      headers_match: { 'content-type': '^multipart/' },
      headers_absent: ['Authorization'],
      body: { a: 1 },
      min_delay_ms: 100,
    },
  ];
  const requests = [sent({ at: 0 }), sent({ at: 50, body: '{"a":2}', headers: { authorization: 'x' } })];
  const failures = checkCase(item, requests, { result: { id: 1 } }, { token: 't0ken' }).join('\n');
  assert.match(failures, /content-type is undefined/);
  assert.match(failures, /Authorization must be absent/);
  assert.match(failures, /body is \{"a":2\}/);
  assert.match(failures, /sent after 50ms/);
});

test('validateCase accepts only true for content_digest', () => {
  const item = baseCase();
  item.wire[0].content_digest = false;
  assert.deepEqual(validateCase(item, operations), ['wire[].content_digest can only be true']);
});

test('checkCase compares Content-Digest with the body bytes', () => {
  const item = baseCase();
  item.wire = [
    { method: 'POST', path: '/items', content_digest: true },
    { method: 'POST', path: '/items', content_digest: true },
  ];
  const sha256 = 'RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=';
  const requests = [
    sent({ method: 'POST', sha256, headers: { 'content-digest': `sha-256=:${sha256}:` } }),
    sent({ method: 'POST', sha256, headers: {} }),
  ];
  const failures = checkCase(item, requests, { result: { id: 1 } }, { token: 't0ken' });
  assert.deepEqual(failures, [`wire[1]: Content-Digest is undefined, expected sha-256=:${sha256}:`]);
});

test('checkCase compares multipart parts by name, including repeated parts', () => {
  const item = baseCase();
  item.wire = [{ method: 'POST', path: '/items', parts: { note: ['hi'], files: ['a', 'b'] } }];
  const body = [
    '--xyz',
    'Content-Disposition: form-data; name="files"; filename="files"',
    'Content-Type: application/octet-stream',
    '',
    'a',
    '--xyz',
    'content-disposition: form-data; name=note',
    '',
    'hi',
    '--xyz',
    'Content-Disposition: form-data; name="files"; filename="files"',
    '',
    'b',
    '--xyz--',
    '',
  ].join('\r\n');
  const request = (text, type = 'multipart/form-data; boundary="xyz"') =>
    sent({ method: 'POST', body: text, headers: { 'content-type': type } });
  const check = (...args) => checkCase(item, [request(...args)], { result: { id: 1 } }, { token: 't0ken' }).join('\n');
  assert.equal(check(body), '');
  assert.match(check(body.replace('\r\nb\r\n', '\r\nc\r\n')), /parts are .*"files":\["a","c"\]/);
  const single = ['--xyz', 'Content-Disposition: form-data; name="files"', '', 'a', '--xyz--', ''].join('\r\n');
  assert.match(check(single), /parts are \{"files":\["a"\]\}/);
  assert.match(check('{}', 'application/json'), /body is not multipart/);
});

test('checkCase compares outcomes', () => {
  const item = baseCase();
  assert.match(checkCase(item, [sent()], { error: { kind: 'server' } }, { token: 't0ken' }).join(), /unexpected error/);
  assert.match(checkCase(item, [sent()], { result: { id: 2 } }, { token: 't0ken' }).join(), /outcome is/);

  item.expect = { error: { kind: 'server', status: 500 } };
  assert.deepEqual(checkCase(item, [sent()], { error: { kind: 'server', status: 500 } }, { token: 't0ken' }), []);
  assert.match(checkCase(item, [sent()], { result: {} }, { token: 't0ken' }).join(), /outcome is/);

  item.expect = { result_keys: ['id'] };
  assert.deepEqual(checkCase(item, [sent()], { result: [{ id: 1 }] }, { token: 't0ken' }), []);
  assert.match(checkCase(item, [sent()], { result: { other: 1 } }, { token: 't0ken' }).join(), /result lacks id/);

  item.expect = { result: { id: 1 }, logs_required: true };
  assert.match(checkCase(item, [sent()], { result: { id: 1 }, logs: [] }, { token: 't0ken' }).join(), /logged nothing/);
});

test('checkCase fails any output containing the token', () => {
  const leaks = [
    { result: { id: 1 }, logs: ['Authorization: Basic t0ken'] },
    { result: { id: 1, echoed: 't0ken' } },
    { error: { kind: 'server', raw_body: 't0ken' } },
  ];
  for (const outcome of leaks) {
    assert.match(checkCase(baseCase(), [sent()], outcome, { token: 't0ken' }).join(), /token leaked/);
  }
});

test('fill expands every named secret and leaves unknown placeholders', () => {
  const vars = { token: 't', api_key: 'k' };
  assert.equal(fill('{{api_key}}:{{token}} {{other}} {{http_date+2s}}', vars), 'k:t {{other}} {{http_date+2s}}');
});

test('checkCase fails output containing any secret, by name', () => {
  const secrets = { token: 't0ken', api_key: 'k3y', shared_secret: 's3cret' };
  const outcome = { result: { id: 1 }, logs: ['x-api-key: k3y:s3cret'] };
  const failures = checkCase(baseCase(), [sent()], outcome, secrets);
  assert.deepEqual(failures, ['api_key leaked into the client output', 'shared_secret leaked into the client output']);
});

let harness;
before(async () => {
  harness = await startHarness('http://127.0.0.1:1');
});
after(() => harness.close());

test('harness records requests and plays responses in order', async () => {
  harness.play({ responses: [{ status: 429, headers: { 'retry-after': '1' } }, { status: 200, body: { ok: true } }] });
  const first = await fetch(`${harness.url}/items?page=2`, { method: 'POST', body: 'hello' });
  assert.equal(first.status, 429);
  assert.equal(first.headers.get('retry-after'), '1');
  const second = await fetch(`${harness.url}/items`);
  assert.equal(second.headers.get('content-type'), 'application/json');
  assert.deepEqual(await second.json(), { ok: true });

  const [recorded] = harness.requests();
  assert.equal(recorded.method, 'POST');
  assert.equal(recorded.path, '/items');
  assert.deepEqual(recorded.query, { page: '2' });
  assert.equal(recorded.body, 'hello');
  assert.equal(recorded.sha256, 'LPJNul+wow4m6DsqxbninhsWHlwfp0JecwQzYpOLmCQ=');
});

test('harness sends string bodies verbatim and delays responses', async () => {
  harness.play({ responses: [{ status: 503, body: '<html>', delay_ms: 60 }] });
  const started = performance.now();
  const response = await fetch(`${harness.url}/items`);
  assert.equal(await response.text(), '<html>');
  assert.ok(performance.now() - started >= 50);
});

test('harness records a request and then drops its connection', async () => {
  harness.play({ responses: [{ drop: true }, { status: 200 }] });
  await assert.rejects(fetch(`${harness.url}/items`, { method: 'POST', body: 'hello' }), TypeError);
  assert.equal((await fetch(`${harness.url}/items`)).status, 200);

  const [dropped] = harness.requests();
  assert.equal(dropped.method, 'POST');
  assert.equal(dropped.body, 'hello');
});

test('harness closes every connection after its response', async () => {
  harness.play({ responses: [{ status: 200 }] });
  const response = await fetch(`${harness.url}/items`);
  assert.equal(response.headers.get('connection'), 'close');
});

test('harness expands a relative HTTP date when it responds', async () => {
  harness.play({ responses: [{ status: 429, headers: { 'retry-after': '{{http_date+60s}}' } }] });
  const started = Date.now();
  const response = await fetch(`${harness.url}/items`);
  const value = response.headers.get('retry-after');
  assert.match(value, /^\w{3}, \d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} GMT$/);
  const wait = Date.parse(value) - started;
  assert.ok(wait > 58_000 && wait <= 61_000, `date is ${wait}ms away`);
});

test('harness trickles a body one byte at a time', async () => {
  harness.play({ responses: [{ status: 200, body: 'abc', trickle_ms: 30 }] });
  const started = performance.now();
  const response = await fetch(harness.url);
  assert.equal(await response.text(), 'abc');
  assert.ok(performance.now() - started >= 60);
});

function rawGet(url, accept) {
  return new Promise((resolve, reject) => {
    get(url, { headers: { 'accept-encoding': accept } }, async (response) => {
      const chunks = [];
      for await (const chunk of response) chunks.push(chunk);
      resolve({ headers: response.headers, body: Buffer.concat(chunks) });
    }).on('error', reject);
  });
}

test('harness compresses a body for a client that accepts gzip, and can cut it short', async () => {
  const body = { id: 1, name: 'synthetic' };
  harness.play({ responses: [{ status: 200, body, gzip: true }, { status: 200, body, gzip: true, cut: -8 }] });

  const whole = await rawGet(harness.url, 'gzip, deflate');
  assert.equal(whole.headers['content-encoding'], 'gzip');
  assert.deepEqual(JSON.parse(gunzipSync(whole.body)), body);

  const cut = await rawGet(harness.url, 'gzip');
  assert.deepEqual(cut.body, whole.body.subarray(0, -8));
  assert.throws(() => gunzipSync(cut.body), /unexpected end of file/);
});

test('harness sends identity to a client that does not accept gzip', async () => {
  for (const accept of ['identity', 'gzip;q=0', 'br']) {
    harness.play({ responses: [{ status: 200, body: { id: 1 }, gzip: true, cut: 4 }] });
    const { headers, body } = await rawGet(harness.url, accept);
    assert.equal(headers['content-encoding'], undefined);
    assert.equal(body.toString(), '{"id');
  }
});

test('harness replays a new script from a clean record', async () => {
  harness.play({ responses: [{ status: 200 }] });
  await fetch(`${harness.url}/one`);
  harness.play({ responses: [{ status: 200 }] });
  await fetch(`${harness.url}/two`);
  assert.deepEqual(harness.requests().map((request) => request.path), ['/two']);
});

test('unhost reads the host key out of a path and leaves other paths alone', () => {
  assert.deepEqual(unhost('/_host/files/items/1'), { host: 'files', path: '/items/1' });
  assert.deepEqual(unhost('/_host/files'), { host: 'files', path: '/' });
  assert.deepEqual(unhost('/items/_host/files'), { path: '/items/_host/files' });
});

test('harness records the host key and strips it from the path', async () => {
  harness.play({ responses: [{ status: 200 }, { status: 200 }] });
  await fetch(`${harness.url}/_host/files/items?limit=1`);
  await fetch(`${harness.url}/items`);
  const [hosted, plain] = harness.requests();
  assert.deepEqual([hosted.host, hosted.path, hosted.query], ['files', '/items', { limit: '1' }]);
  assert.equal('host' in plain, false);
});

test('harness forwards unscripted requests and reports a dead mock', async () => {
  harness.play({ prism: {} });
  const response = await fetch(`${harness.url}/items`);
  assert.equal(response.status, 500);
  assert.match(await response.text(), /prism forward failed/);
});

async function runWith(mode, cases = [baseCase()]) {
  const driver = startDriver(`node ${FIXTURE} ${mode}`);
  try {
    return await runCases({ cases, defaults: {}, driver, harness });
  } finally {
    driver.stop();
  }
}

test('runCases passes a conforming driver', async () => {
  assert.deepEqual(await runWith('good'), []);
});

test('runCases fails a driver that skips the wire', async () => {
  const [{ failures }] = await runWith('silent');
  assert.match(failures.join(), /sent 0 requests/);
});

test('runCases fails a driver that logs the token', async () => {
  const [{ failures }] = await runWith('leaky');
  assert.match(failures.join(), /token leaked/);
});

test('offset paging cases hold for a driver that walks offsets', async () => {
  const cases = await loadCases(fixtureCases('offset'), operations);
  assert.ok(cases.length > 0);
  assert.deepEqual(await runWith('offset', cases), []);
});

test('offset paging cases fail a driver that reads only the first page', async () => {
  const cases = await loadCases(fixtureCases('offset'), operations);
  const failed = await runWith('good', cases);
  assert.ok(failed.length > 0);
});

test('signing cases hold for a driver that signs each attempt', async () => {
  const cases = await loadCases(SIGNING_CASES, operations);
  assert.ok(cases.length > 0);
  assert.deepEqual(await runWith('signed', cases), []);
});

test('signing cases fail a driver whose digest is not of the bytes sent', async () => {
  const cases = await loadCases(SIGNING_CASES, operations);
  const failed = await runWith('wrong-digest', cases);
  assert.ok(failed.some(({ failures }) => failures.some((failure) => /Content-Digest is/.test(failure))));
});

for (const style of ['hosts', 'headers']) {
  test(`${style} cases hold for a driver that routes by host and sends declared headers`, async () => {
    const cases = await loadCases(fixtureCases(style), operations);
    assert.ok(cases.length > 0);
    assert.deepEqual(await runWith('routed', cases), []);
  });
}

test('signing cases fail a driver that sends a valid digest but no signature', async () => {
  const cases = await loadCases(SIGNING_CASES, operations);
  const failed = await runWith('unsigned', cases);
  assert.equal(failed.length, cases.length);
  for (const { failures } of failed) {
    assert.ok(failures.some((failure) => /header signature is undefined/.test(failure)));
    assert.ok(!failures.some((failure) => /Content-Digest is/.test(failure)));
  }
});

test('hosts cases fail only on the host for a driver that sends every request to the base URL', async () => {
  const cases = await loadCases(fixtureCases('hosts'), operations);
  const failed = await runWith('unhosted', cases);
  assert.equal(failed.length, cases.length);
  assert.ok(failed.every(({ failures }) => failures.length > 0 && failures.every((failure) => /: host is undefined$/.test(failure))));
});

test('headers cases fail only on the header for a driver that ignores the client defaults', async () => {
  const cases = await loadCases(fixtureCases('headers'), operations);
  const failed = await runWith('undefaulted', cases);
  assert.deepEqual(
    failed.map(({ failures }) => failures),
    [['wire[0]: header x-tenant is undefined, expected acme']],
  );
});

test('checkCase compares the exact body bytes as base64', () => {
  const item = { ...baseCase(), wire: [{ method: 'GET', path: '/items', body_base64: 'AP8=' }] };
  assert.deepEqual(checkCase(item, [sent({ base64: 'AP8=' })], { result: { id: 1 } }, { token: 't0ken' }), []);
  assert.match(checkCase(item, [sent({ base64: '77+9' })], { result: { id: 1 } }, { token: 't0ken' }).join(), /body is base64 77\+9/);
});

test('harness sends a base64 body as its bytes and records request bytes as base64', async () => {
  harness.play({ responses: [{ status: 200, headers: { 'content-type': 'application/pdf' }, body_base64: 'AP/+' }] });
  const response = await fetch(`${harness.url}/download`, { method: 'POST', body: Buffer.of(0x00, 0xff) });
  assert.equal(response.headers.get('content-type'), 'application/pdf');
  assert.deepEqual(Buffer.from(await response.arrayBuffer()), Buffer.of(0x00, 0xff, 0xfe));
  assert.equal(harness.requests()[0].base64, 'AP8=');
});

test('binary cases hold for a driver that keeps bytes as bytes', async () => {
  const cases = await loadCases(fixtureCases('binary'), operations);
  assert.ok(cases.length > 0);
  assert.deepEqual(await runWith('binary', cases), []);
});

test('binary cases fail a driver that decodes bodies as text', async () => {
  const cases = await loadCases(fixtureCases('binary'), operations);
  const failed = (await runWith('binary-as-text', cases)).map(({ name }) => name);
  assert.deepEqual(failed, ['binary-download-returns-the-exact-bytes', 'binary-upload-sends-the-bytes-unchanged']);
});

test('idempotency cases hold for a driver that retries a write only when its key is set', async () => {
  const cases = await loadCases(fixtureCases('idempotency'), operations);
  assert.ok(cases.length > 0);
  assert.deepEqual(await runWith('idempotent', cases), []);
});

test('idempotency cases fail a driver that retries every write, and one that retries none', async () => {
  const cases = await loadCases(fixtureCases('idempotency'), operations);
  const names = async (mode) => (await runWith(mode, cases)).map(({ name }) => name);
  assert.deepEqual(await names('retry-writes'), [
    'unmarked-write-is-not-retried-on-a-server-error',
    'idempotent-write-with-an-empty-key-is-not-retried',
    'idempotent-write-without-a-key-is-not-retried',
  ]);
  assert.deepEqual(await names('unretried'), [
    'idempotent-write-retries-a-server-error-with-the-same-body',
    'idempotent-write-retries-a-dropped-connection-with-the-same-body',
  ]);
});
