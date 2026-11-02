import assert from 'node:assert/strict';
import { after, before, test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { validateCase } from './cases.mjs';
import { checkCase, fill, matches } from './check.mjs';
import { startHarness } from './harness.mjs';
import { runCases, startDriver } from './run.mjs';

const FIXTURE = fileURLToPath(new URL('./fixtures/driver.mjs', import.meta.url));
const operations = new Set(['list-items']);

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
    [{ wire: [] }, /wire must be a non-empty list/],
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
  assert.deepEqual(checkCase(baseCase(), [sent()], { result: { id: 1, extra: 2 }, logs: [] }, 't0ken'), []);
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
    assert.match(checkCase(item, requests, { result: { id: 1 } }, 't0ken').join('\n'), pattern);
  }
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
  const failures = checkCase(item, requests, { result: { id: 1 } }, 't0ken').join('\n');
  assert.match(failures, /content-type is undefined/);
  assert.match(failures, /Authorization must be absent/);
  assert.match(failures, /body is \{"a":2\}/);
  assert.match(failures, /sent after 50ms/);
});

test('checkCase compares outcomes', () => {
  const item = baseCase();
  assert.match(checkCase(item, [sent()], { error: { kind: 'server' } }, 't0ken').join(), /unexpected error/);
  assert.match(checkCase(item, [sent()], { result: { id: 2 } }, 't0ken').join(), /outcome is/);

  item.expect = { error: { kind: 'server', status: 500 } };
  assert.deepEqual(checkCase(item, [sent()], { error: { kind: 'server', status: 500 } }, 't0ken'), []);
  assert.match(checkCase(item, [sent()], { result: {} }, 't0ken').join(), /outcome is/);

  item.expect = { result_keys: ['id'] };
  assert.deepEqual(checkCase(item, [sent()], { result: [{ id: 1 }] }, 't0ken'), []);
  assert.match(checkCase(item, [sent()], { result: { other: 1 } }, 't0ken').join(), /result lacks id/);

  item.expect = { result: { id: 1 }, logs_required: true };
  assert.match(checkCase(item, [sent()], { result: { id: 1 }, logs: [] }, 't0ken').join(), /logged nothing/);
});

test('checkCase fails any output containing the token', () => {
  const leaks = [
    { result: { id: 1 }, logs: ['Authorization: Basic t0ken'] },
    { result: { id: 1, echoed: 't0ken' } },
    { error: { kind: 'server', raw_body: 't0ken' } },
  ];
  for (const outcome of leaks) {
    assert.match(checkCase(baseCase(), [sent()], outcome, 't0ken').join(), /token leaked/);
  }
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

test('harness replays a new script from a clean record', async () => {
  harness.play({ responses: [{ status: 200 }] });
  await fetch(`${harness.url}/one`);
  harness.play({ responses: [{ status: 200 }] });
  await fetch(`${harness.url}/two`);
  assert.deepEqual(harness.requests().map((request) => request.path), ['/two']);
});

test('harness forwards unscripted requests and reports a dead mock', async () => {
  harness.play({ prism: {} });
  const response = await fetch(`${harness.url}/items`);
  assert.equal(response.status, 500);
  assert.match(await response.text(), /prism forward failed/);
});

async function runWith(mode) {
  const driver = startDriver(`node ${FIXTURE} ${mode}`);
  try {
    return await runCases({ cases: [baseCase()], defaults: {}, driver, harness });
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
