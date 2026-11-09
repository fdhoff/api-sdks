import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';
import { checkUpstream, specProblem } from '../spec/check-upstream.mjs';

const lock = JSON.parse(await readFile(new URL('../spec/upstream/lock.json', import.meta.url), 'utf8'));
const SPEC = JSON.stringify({ openapi: '3.1.0', info: { title: 'synthetic', version: '' }, paths: { '/items': { get: { operationId: 'X01' } } } });
const answering = (status, text) => async () => ({ status, ok: status >= 200 && status < 300, text: async () => text });

test('the pin is current when the URL serves an OpenAPI document', async () => {
  assert.deepEqual(await checkUpstream(lock, answering(200, SPEC)), []);
});

test('a URL that fails, or answers empty, with something other than JSON or with no operations, is reported', async () => {
  assert.equal(specProblem(404, ''), 'HTTP 404');
  assert.equal(specProblem(200, '  \n'), 'an empty body');
  assert.equal(specProblem(200, '<html></html>'), 'a body that is not JSON');
  assert.equal(specProblem(200, '{"error":"gone"}'), 'JSON that is not an OpenAPI document');
  assert.equal(specProblem(200, JSON.stringify({ openapi: '3.1.0', paths: { '/items': {} } })), 'an OpenAPI document with no operations');
  assert.equal(specProblem(200, SPEC), null);
  const [problem] = await checkUpstream(lock, answering(200, '<html></html>'));
  assert.match(problem, /answered with a body that is not JSON/);
});

test('a URL that cannot be reached is reported', async () => {
  const problems = await checkUpstream(lock, async () => {
    throw new Error('getaddrinfo ENOTFOUND');
  });
  assert.equal(problems.length, 1);
  assert.match(problems[0], /could not be fetched: getaddrinfo ENOTFOUND/);
});

test('the spec drift workflow runs the check, compares content and fails on removed operations', async () => {
  const workflow = parse(await readFile(new URL('../../../.github/workflows/spec-drift.yml', import.meta.url), 'utf8'));
  assert.match(workflow.jobs.apis.steps.at(-1).run, /checks=\$\(names apis\/\*\/spec\/check-upstream\.mjs\)/);
  assert.equal(workflow.jobs.upstream.steps.at(-1).run, 'node "apis/$API/spec/check-upstream.mjs"');
  const steps = workflow.jobs.drift.steps;
  assert.match(steps.find((step) => step.id === 'pin').run, /spec-cache\.mjs/);
  assert.match(steps.find((step) => step.name === 'Open or update the pull request').run, /Operations were removed[\s\S]*exit 1/);
});
