import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { verifyPin } from '../../../toolchain/pipeline/fetch-spec.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const paths = apiPaths(fileURLToPath(new URL('..', import.meta.url)));
const built = parse(await readFile(paths.build, 'utf8'));
const operations = Object.values(built.paths).flatMap((item) =>
  METHODS.filter((method) => item[method]).map((method) => item[method]),
);
const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], built)) : value);

test('cached spec matches its lock', async () => {
  const lock = JSON.parse(await readFile(paths.lock, 'utf8'));
  verifyPin(await readFile(paths.spec), lock, paths.spec);
});

test('the upstream spec is not tracked', () => {
  assert.equal(execFileSync('git', ['ls-files', paths.spec], { encoding: 'utf8' }), '');
});

test('every operation has a unique operationId', () => {
  const ids = operations.map((operation) => operation.operationId);
  assert.ok(ids.every(Boolean));
  assert.equal(new Set(ids).size, ids.length);
});

test('every operation needs the API key, and OAuth operations need it too', () => {
  assert.deepEqual(built.security, [{ api_key: [] }]);
  const odd = operations.filter(
    ({ security }) =>
      security !== undefined &&
      !(security.length === 1 && Object.keys(security[0]).sort().join() === 'api_key,oauth2'),
  );
  assert.deepEqual(odd.map((operation) => operation.operationId), []);
});

test('every operation declares the shared rate-limit response', () => {
  const missing = operations.filter((operation) => operation.responses['429']?.$ref !== '#/components/responses/RateLimited');
  assert.deepEqual(missing.map((operation) => operation.operationId), []);
  const headers = Object.keys(built.components.responses.RateLimited.headers).sort();
  assert.deepEqual(headers, ['retry-after', 'x-limit-per-day', 'x-limit-per-second', 'x-remaining-this-second', 'x-remaining-today']);
});

test('no schema defaults to null', () => {
  assert.doesNotMatch(JSON.stringify(built), /"default":null/);
});

test('every offset-paged operation takes a limit and answers count and results', () => {
  const paged = operations.filter((operation) => (operation.parameters ?? []).some((parameter) => parameter.name === 'offset'));
  assert.ok(paged.length > 0);
  const odd = paged.filter((operation) => {
    const schema = deref(operation.responses['200']?.content?.['application/json']?.schema);
    const limit = operation.parameters.some((parameter) => parameter.name === 'limit');
    return !(limit && schema?.properties?.count && schema?.properties?.results?.type === 'array');
  });
  assert.deepEqual(odd.map((operation) => operation.operationId), []);
});
