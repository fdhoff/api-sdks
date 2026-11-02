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
const schemas = built.components.schemas;
const operations = Object.values(built.paths).flatMap((item) =>
  METHODS.filter((method) => item[method]).map((method) => item[method]),
);

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

test('every operation inherits the token scheme', () => {
  assert.deepEqual(built.security, [{ ApiKeyAuth: [] }]);
  assert.deepEqual(Object.keys(built.components.securitySchemes), ['ApiKeyAuth']);
  assert.ok(operations.every((operation) => operation.security === undefined));
});

test('every required property is declared', () => {
  const undeclared = Object.entries(schemas).flatMap(([name, schema]) =>
    schema.properties ? (schema.required ?? []).filter((key) => !(key in schema.properties)).map((key) => `${name}.${key}`) : [],
  );
  assert.deepEqual(undeclared, []);
});

test('paginated lists may end on either side', () => {
  const { next, previous } = schemas.getCareFolderListResponse.properties;
  assert.equal(next.nullable, true);
  assert.equal(previous.nullable, true);
});
