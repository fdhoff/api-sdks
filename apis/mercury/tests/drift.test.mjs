import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';
import { checkUpstream, DOCS_PAGE, namedIds, registryId, specProblem } from '../spec/check-upstream.mjs';

const lock = JSON.parse(await readFile(new URL('../spec/upstream/lock.json', import.meta.url), 'utf8'));
const PINNED = registryId(lock.url);
const SPEC = JSON.stringify({ openapi: '3.0.0', info: { title: 'synthetic', version: '1' }, paths: {} });
const page = (id) => `<script>{"oasPublicUrl":"@mercurytechnologies/v1#${id}","other":1}</script>`;

// A fake fetch answering the registry URL and the docs page.
const answering = ({ spec = [200, SPEC], docs = [200, page(PINNED)] } = {}) => async (url) => {
  const [status, text] = url === DOCS_PAGE ? docs : spec;
  return { status, ok: status >= 200 && status < 300, text: async () => text };
};

test('the pin is current when the registry serves a spec and the docs name its ID', async () => {
  assert.deepEqual(await checkUpstream(lock, answering()), []);
});

test('a registry URL that fails, or answers empty or with something other than JSON, is reported', async () => {
  assert.equal(specProblem(404, ''), 'HTTP 404');
  assert.equal(specProblem(200, '  \n'), 'an empty body');
  assert.equal(specProblem(200, '<html></html>'), 'a body that is not JSON');
  assert.equal(specProblem(200, '{"error":"gone"}'), 'JSON that is not an OpenAPI document');
  assert.equal(specProblem(200, SPEC), null);
  const [problem] = await checkUpstream(lock, answering({ spec: [200, '<html></html>'] }));
  assert.match(problem, /answered with a body that is not JSON/);
});

test('docs that name another registry ID report the pin as stale', async () => {
  const problems = await checkUpstream(lock, answering({ docs: [200, page('newid123')] }));
  assert.equal(problems.length, 1);
  assert.match(problems[0], new RegExp(`names registry ID newid123, not the pinned ${PINNED}`));
});

test('docs that cannot be read or name no ID are reported, not taken as current', async () => {
  assert.match((await checkUpstream(lock, answering({ docs: [500, ''] })))[0], /HTTP 500/);
  assert.match((await checkUpstream(lock, answering({ docs: [200, '<html></html>'] })))[0], /names no registry ID/);
});

test('namedIds reads every distinct ID and registryId refuses another URL', () => {
  assert.deepEqual(namedIds(`${page('a1')}${page('a1')}${page('b2')}`), ['a1', 'b2']);
  assert.throws(() => registryId('https://example.com/spec.json'), /not a ReadMe registry URL/);
});

test('the spec drift workflow runs the check apart from the pin comparison', async () => {
  const workflow = parse(await readFile(new URL('../../../.github/workflows/spec-drift.yml', import.meta.url), 'utf8'));
  assert.match(workflow.jobs.apis.steps.at(-1).run, /checks=\$\(names apis\/\*\/spec\/check-upstream\.mjs\)/);
  const { upstream } = workflow.jobs;
  assert.deepEqual(upstream.permissions, { contents: 'read' });
  assert.equal(upstream.steps.at(-1).run, 'node "apis/$API/spec/check-upstream.mjs"');
});
