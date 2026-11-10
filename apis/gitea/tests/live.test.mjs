import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createServer } from 'node:http';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { operationIds } from '../../../toolchain/conformance/cases.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';
import { checkScenario, checkStep, fill, loadScenarios, matches, runScenarios, startProxy } from '../conformance/live/run.mjs';

const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const lock = JSON.parse(await readFile(apiPaths(API_DIR).lock, 'utf8'));
const image = JSON.parse(await readFile(new URL('../conformance/live/image.json', import.meta.url), 'utf8'));

test('the container image is the pinned release, by digest', () => {
  assert.equal(image.image, 'gitea/gitea');
  assert.equal(`v${image.tag}`, lock.tag);
  assert.match(image.digest, /^sha256:[0-9a-f]{64}$/);
});

test('every live scenario is well formed and names operations in the built spec', async () => {
  const operations = operationIds(parse(await readFile(apiPaths(API_DIR).build, 'utf8')));
  const scenarios = await loadScenarios();
  assert.deepEqual(scenarios.map(({ scenario }) => scenario), ['auth', 'errors', 'files', 'pagination']);
  for (const scenario of scenarios) assert.deepEqual(checkScenario(scenario, operations), [], scenario.file);
});

test('a scenario with an unknown operation or key is rejected', () => {
  const problems = checkScenario(
    { scenario: 'bad', steps: [{ name: 'one', request: { operation: 'nope' }, expect: { error: {}, count: 1 }, extra: 1 }] },
    new Set(['known']),
  );
  assert.deepEqual(problems, ['one: unknown key extra', 'one: no operation nope', 'one: an expected error cannot also expect a result']);
});

test('a whole placeholder keeps its type, and an unknown one fails', () => {
  const vars = { admin: 'synthetic-admin', issue: { number: 3 }, i: 2 };
  assert.deepEqual(fill({ index: '{{issue.number}}', title: 'Issue {{i}} of {{admin}}' }, vars), { index: 3, title: 'Issue 2 of synthetic-admin' });
  assert.throws(() => fill('{{missing.field}}', vars), /has no value/);
});

test('results match as a subset, with regular expressions for strings', () => {
  assert.ok(matches({ a: { $regex: '^x' }, b: [1] }, { a: 'xyz', b: [1], c: 2 }));
  assert.ok(!matches({ a: { $regex: '^x' } }, { a: 'yx' }));
  assert.ok(!matches({ a: { $regex: '^x' } }, { a: 1 }));
  assert.ok(!matches([1], [1, 2]));
});

test('a step checks its item count, uniqueness, requests and wire', () => {
  const requests = [
    { path: '/api/v1/repos/a/b/issues', headers: { accept: 'application/json' } },
    { path: '/api/v1/repos/a/b/issues', headers: { accept: 'application/json' } },
  ];
  const outcome = { result: [{ number: 1 }, { number: 1 }] };
  assert.deepEqual(checkStep({ count: 2, requests: 2, wire: { path_match: '/issues$', headers_match: { Accept: '^application/json$' } } }, outcome, requests), []);
  assert.deepEqual(checkStep({ count: 3, unique: 'number', requests: 1 }, outcome, requests), [
    'got 2 items, expected 3',
    'number repeats: 1, 1',
    'sent 2 requests, expected 1: /api/v1/repos/a/b/issues, /api/v1/repos/a/b/issues',
  ]);
  assert.deepEqual(checkStep({ error: { kind: 'not_found' } }, { error: { kind: 'not_found', status: 404 } }, []), []);
  assert.deepEqual(checkStep({ result: { a: 1 } }, { error: { kind: 'server' } }, []), ['unexpected error {"kind":"server"}']);
});

test('the proxy refuses any instance that is not local', async () => {
  await assert.rejects(startProxy('https://gitea.com'), /only against a local container/);
  await assert.rejects(startProxy('https://gitea.example.com'), /only against a local container/);
});

test('the proxy forwards the exact path and returns every response header, and runs record each step', async () => {
  const upstream = createServer((request, response) => {
    response.writeHead(200, [
      'Content-Type', 'application/json',
      'Link', '<http://localhost:3000/api/v1/x?page=2&limit=2>; rel="next"',
      'Link', '<http://localhost:3000/api/v1/x?page=3&limit=2>; rel="last"',
    ]);
    response.end(JSON.stringify({ path: request.url, auth: request.headers.authorization }));
  });
  await new Promise((resolve) => upstream.listen(0, '127.0.0.1', resolve));
  const proxy = await startProxy(`http://127.0.0.1:${upstream.address().port}`);
  try {
    const response = await fetch(`${proxy.url}/api/v1/repos/a/b/contents/docs%2Fnotes.md?ref=main`, { headers: { authorization: 'token synthetic' } });
    assert.deepEqual(await response.json(), { path: '/api/v1/repos/a/b/contents/docs%2Fnotes.md?ref=main', auth: 'token synthetic' });
    assert.match(response.headers.get('link'), /rel="next".*rel="last"/);
    const [sent] = proxy.take();
    assert.equal(sent.path, '/api/v1/repos/a/b/contents/docs%2Fnotes.md');
    assert.deepEqual(sent.query, { ref: 'main' });
    assert.deepEqual(proxy.take(), []);

    const settings = { admin: 'synthetic-admin', admin_password: 'synthetic-admin-password', user: 'synthetic-user', user_password: 'synthetic-user-password', token: 'synthetic-token' };
    const calls = [];
    const driver = {
      async call(message) {
        calls.push(message);
        await fetch(`${message.client.base_url}/api/v1/user`);
        return message.request.operation === 'leaky' ? { result: { echoed: settings.token }, logs: [] } : { result: { number: 7 }, logs: [] };
      },
    };
    const scenarios = [
      {
        scenario: 'synthetic',
        steps: [
          { name: 'make', request: { operation: 'make' }, save: 'made', expect: { requests: 1 } },
          { name: 'use', repeat: 2, request: { operation: 'use', params: { index: '{{made.number}}', n: '{{i}}' } }, expect: { result: { number: 7 } } },
          { name: 'leak', request: { operation: 'leaky' }, expect: {} },
        ],
      },
    ];
    const { total, failed } = await runScenarios({ scenarios, settings, driver, proxy });
    assert.equal(total, 4);
    assert.deepEqual(failed, [{ name: 'synthetic: leak', failures: ['a credential leaked into the client output'] }]);
    assert.deepEqual(calls[1].request.params, { index: 7, n: 1 });
    assert.deepEqual(calls[2].request.params, { index: 7, n: 2 });
    assert.deepEqual(calls[0].client, { token: 'synthetic-token', base_url: proxy.url });
  } finally {
    await proxy.close();
    await new Promise((resolve) => upstream.close(resolve));
  }
});
