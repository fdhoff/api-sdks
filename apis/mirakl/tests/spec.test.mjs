import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { verifyPin } from '../../../toolchain/pipeline/fetch-spec.mjs';
import { applyJobs, applyQueryDefaults, resolvePaging } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const paths = apiPaths(API_DIR);
const lock = JSON.parse(await readFile(paths.lock, 'utf8'));
const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));
const upstream = parse(await readFile(paths.spec, 'utf8'));
const built = parse(await readFile(paths.build, 'utf8'));
const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], built)) : value);
const operationsOf = (spec) =>
  Object.entries(spec.paths).flatMap(([path, item]) => METHODS.filter((method) => item[method]).map((method) => ({ path, method, item, ...item[method] })));
const operations = operationsOf(built);
const byId = new Map(operations.map((operation) => [operation.operationId, operation]));
const ids = (list) => list.map((operation) => operation.operationId).sort();
const parameters = (operation) => [...(operation.item.parameters ?? []), ...(operation.parameters ?? [])].map(deref);
const queryParams = (operation) => parameters(operation).filter((parameter) => parameter.in === 'query').map(({ name }) => name);
const successContent = (operation) => {
  const [, response] = Object.entries(operation.responses).find(([status]) => status.startsWith('2'));
  return deref(response).content ?? {};
};

const DEPRECATED = ['M01', 'OF26', 'OF51', 'OR12', 'OR26', 'OR41', 'OR42', 'RE02', 'RE11', 'RE12', 'RE14'];
const DYNAMIC = ['OF54', 'OR15', 'TL05'];
const OFFSET = ['IV01', 'OF21', 'OR11', 'P11', 'P51', 'PR01'];
const SEEK = ['DR11', 'DR12', 'M11', 'OF04', 'PL11', 'PRI02', 'RT11', 'RT12', 'RT52', 'SBC11', 'ST11', 'ST12', 'ST42', 'ST52', 'TL02'];
const BINARY = ['DR73', 'IV02', 'M13', 'OF03', 'OR73', 'P44', 'P45', 'P46', 'P47', 'PRI03', 'S31', 'STO03'];
const MULTIPART = ['DR74', 'M12', 'M14', 'OF01', 'OR43', 'OR74', 'P41', 'PRI01', 'S32', 'STO01'];

test('the cached spec matches its lock and is not tracked', async () => {
  assert.equal(lock.url, 'https://developer.mirakl.com/_spec/content/product/mmp/rest/seller/openapi3.json');
  verifyPin(await readFile(paths.spec), lock, paths.spec);
  assert.equal(execFileSync('git', ['ls-files', paths.spec], { encoding: 'utf8' }), '');
});

test('the build stays OpenAPI 3.1 and keeps 116 operations', () => {
  assert.match(built.openapi, /^3\.1\./);
  assert.equal(operationsOf(upstream).length, 130);
  assert.equal(operations.length, 116);
  assert.equal(byId.size, operations.length);
  const kept = new Set(ids(operations));
  assert.deepEqual([...DEPRECATED, ...DYNAMIC].filter((id) => kept.has(id)), []);
  assert.ok(operations.every((operation) => !operation.deprecated), 'no deprecated operation is left');
  assert.ok(operations.every((operation) => !operation.path.includes('dynamic-url')));
  assert.ok(Object.values(built.paths).every((item) => METHODS.some((method) => item[method])));
});

test('every operation needs the shop API key, except the health check', () => {
  const scheme = Object.entries(built.components.securitySchemes);
  assert.equal(scheme.length, 1);
  const [name, { type, in: where, name: header }] = scheme[0];
  assert.deepEqual([type, where, header], ['apiKey', 'header', 'Authorization']);
  const open = operations.filter((operation) => !operation.security?.some((requirement) => name in requirement));
  assert.deepEqual(ids(open), ['V01']);
});

test('every operation declares 400, 401, 403, 404, 429 and 5XX, with no error body', () => {
  const statuses = ['400', '401', '403', '404', '429', '5XX'];
  const missing = operations.filter((operation) => !statuses.every((status) => operation.responses[status]));
  assert.deepEqual(ids(missing), []);
  for (const name of ['BadRequest', 'Unauthorized', 'Forbidden', 'NotFound', 'RateLimited', 'ServerError']) {
    assert.equal(built.components.responses[name].content, undefined, name);
  }
  assert.deepEqual(built.components.responses.RateLimited.headers['Retry-After'].schema, { type: 'integer' });
});

test('no request or response example is left', () => {
  const media = operations.flatMap((operation) => [
    ...Object.values(deref(operation.requestBody)?.content ?? {}),
    ...Object.values(operation.responses).flatMap((response) => Object.values(deref(response).content ?? {})),
  ]);
  assert.ok(media.length > 0);
  assert.deepEqual(media.filter((type) => type.examples !== undefined || type.example !== undefined), []);
});

test('offset lists take max, offset, sort and order, and seek lists take limit and page_token', () => {
  for (const id of OFFSET) assert.deepEqual(['max', 'offset', 'sort', 'order'].filter((name) => !queryParams(byId.get(id)).includes(name)), [], id);
  for (const id of SEEK) assert.deepEqual(['limit', 'page_token'].filter((name) => !queryParams(byId.get(id)).includes(name)), [], id);
  const limit = (id) => parameters(byId.get(id)).find((parameter) => parameter.name === 'limit').schema.maximum;
  assert.deepEqual([limit('ST11'), limit('SBC11'), limit('TL02')], [100, 1000, 2000]);
  assert.ok(!queryParams(byId.get('M11')).includes('sort'));
});

test('every iterator pages the way its response says', () => {
  assert.deepEqual(Object.keys(sdk.iterators).sort(), [...OFFSET, ...SEEK].sort());
  for (const [id, iterator] of Object.entries(sdk.iterators)) {
    const operation = byId.get(id);
    const paging = resolvePaging(id, queryParams(operation), iterator.paging, sdk.paging);
    const schema = deref(successContent(operation)['application/json'].schema);
    assert.equal(deref(schema.properties[iterator.items]).type, 'array', id);
    if (OFFSET.includes(id)) {
      assert.ok(paging.offset, id);
      if (id !== 'P11') assert.ok(schema.properties.total_count, id);
    } else {
      assert.deepEqual([paging.cursor?.next, paging.cursor?.param], ['next_page_token', 'page_token'], id);
      assert.ok(schema.properties.next_page_token, id);
    }
  }
});

test('shop_id is a client-level default on every operation', () => {
  const spec = applyQueryDefaults(structuredClone(built), sdk.query_defaults);
  const shopIds = operationsOf(spec).map((operation) => (operation.parameters ?? []).find((parameter) => parameter.name === 'shop_id'));
  assert.equal(shopIds.length, 116);
  assert.ok(shopIds.every((parameter) => parameter?.in === 'query' && parameter['x-sdk-query-default'] === true && parameter.required === false));
});

test('every job polls a GET by its ID until a final state', () => {
  const operationsYaml = Object.fromEntries(operations.map(({ operationId }) => [operationId, { method: operationId.toLowerCase(), wait: Object.values(sdk.jobs).some((job) => job.status === operationId) ? 'wait' : undefined }]));
  const spec = applyJobs(structuredClone(built), sdk.jobs, operationsYaml);
  const waited = operationsOf(spec).filter((operation) => operation['x-sdk-job']);
  assert.deepEqual(ids(waited), ['OF02', 'OF53', 'OR14', 'P42', 'STO02', 'TL04']);
  assert.equal(sdk.jobs.PRI01, undefined);
});

test('binary downloads and multipart uploads are kept', () => {
  for (const id of BINARY) {
    const binary = Object.values(successContent(byId.get(id))).filter((media) => deref(media.schema)?.format === 'binary');
    assert.ok(binary.length > 0, id);
  }
  assert.deepEqual(Object.keys(successContent(byId.get('PM11'))), ['application/json', 'text/csv']);
  for (const id of MULTIPART) assert.ok(Object.keys(deref(byId.get(id).requestBody).content).includes('multipart/form-data'), id);
});

test('no spec content is tracked under this API', () => {
  const tracked = execFileSync('git', ['ls-files', API_DIR], { encoding: 'utf8' }).split('\n').filter(Boolean);
  assert.deepEqual(tracked.filter((file) => /openapi|upstream\/(?!lock\.json$)|\/build\//.test(file)), []);
});
