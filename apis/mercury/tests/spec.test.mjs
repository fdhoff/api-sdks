import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { verifyPin } from '../../../toolchain/pipeline/fetch-spec.mjs';
import { applyHosts, resolveIdempotency, resolvePaging } from '../../../toolchain/pipeline/generate.mjs';
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
const queryParams = (operation) =>
  [...(operation.item.parameters ?? []), ...(operation.parameters ?? [])].map(deref).filter((parameter) => parameter.in === 'query').map(({ name }) => name);
const successSchema = (operation) => deref(deref(operation.responses['200'])?.content?.['application/json']?.schema);
const DROPPED = ['getAccount', 'getInvest', 'getInvestActivity', 'submitOnboardingData'];

test('the cached spec matches its lock and is not tracked', async () => {
  assert.match(lock.url, /^https:\/\/dash\.readme\.com\/api\/v1\/api-registry\/[a-z0-9]+$/);
  verifyPin(await readFile(paths.spec), lock, paths.spec);
  assert.equal(execFileSync('git', ['ls-files', paths.spec], { encoding: 'utf8' }), '');
});

test('the build keeps the 87 public, documented operations', () => {
  const internal = operationsOf(upstream).filter((operation) => operation['x-internal'] !== undefined);
  assert.equal(operationsOf(upstream).length, 132);
  assert.equal(internal.length, 41);
  assert.equal(operations.length, 87);
  const kept = new Set(ids(operations));
  assert.deepEqual(ids(internal).filter((id) => kept.has(id)), []);
  assert.deepEqual(DROPPED.filter((id) => kept.has(id)), []);
  assert.equal(operations.length, 132 - internal.length - DROPPED.length);
  assert.ok(Object.values(built.paths).every((item) => METHODS.some((method) => item[method])));
});

test('every operation has a unique operationId and needs the bearer token', () => {
  assert.equal(byId.size, operations.length);
  assert.deepEqual(built.security, [{ bearerAuth: [] }]);
  assert.deepEqual(ids(operations.filter((operation) => operation.security !== undefined)), []);
  assert.equal(built.components.securitySchemes.bearerAuth.scheme, 'bearer');
});

test('no sample token from upstream reaches the build', () => {
  assert.doesNotMatch(JSON.stringify(built.components.securitySchemes), /secret-token:/);
});

test('every operation declares 401 and 429, with no error body', () => {
  const missing = operations.filter(
    (operation) => operation.responses['401']?.$ref !== '#/components/responses/Unauthorized' || operation.responses['429']?.$ref !== '#/components/responses/RateLimited',
  );
  assert.deepEqual(ids(missing), []);
  for (const name of ['Unauthorized', 'RateLimited']) assert.equal(built.components.responses[name].content, undefined);
  for (const id of ['listCredit', 'getOrganization', 'getSafeRequests']) {
    assert.ok(Object.keys(byId.get(id).responses).some((status) => status.startsWith('4')), id);
  }
});

test('the PDF downloads and attachment uploads are kept', () => {
  for (const id of ['getInvoicePdf', 'getStatementPdf', 'getSafeRequestDocument']) {
    const media = deref(byId.get(id).responses['200']).content['application/pdf'];
    assert.deepEqual(deref(media.schema), { type: 'string', format: 'binary' }, id);
  }
  for (const id of ['uploadRecipientAttachment', 'uploadTransactionAttachment']) {
    assert.deepEqual(Object.keys(deref(byId.get(id).requestBody).content), ['multipart/form-data'], id);
  }
});

test('every operation maps to a host key, and each environment names every key', () => {
  const routed = applyHosts(structuredClone(built), sdk.hosts);
  const keys = operationsOf(routed).map((operation) => operation['x-sdk-host']);
  assert.deepEqual([...new Set(keys)].sort(), ['api', 'vault']);
  assert.deepEqual(ids(operationsOf(routed).filter((operation) => operation['x-sdk-host'] === 'vault')), ['revealCardPan']);
  assert.deepEqual(Object.keys(sdk.environments), ['production', 'sandbox']);
  for (const hosts of Object.values(sdk.environments)) assert.deepEqual(Object.keys(hosts).sort(), ['api', 'vault']);
  assert.equal(sdk.environments.production.api, 'https://api.mercury.com/api/v1');
  assert.equal(sdk.environments.sandbox.api, 'https://api-sandbox.mercury.com/api/v1');
});

test('every list that takes start_after is iterated by cursor, and the two others by their own style', () => {
  const paged = operations.filter((operation) => queryParams(operation).some((name) => ['start_after', 'offset', 'cursor'].includes(name)));
  assert.deepEqual(ids(paged), Object.keys(sdk.iterators).sort());
  const byStyle = (style) => Object.keys(sdk.iterators).filter((id) => (sdk.iterators[id].paging?.style ?? sdk.paging.style) === style).sort();
  assert.equal(byStyle('cursor').length, 25);
  assert.deepEqual(byStyle('offset'), ['listAccountTransactions']);
  const startAfter = byStyle('cursor').filter((id) => !sdk.iterators[id].paging);
  assert.equal(startAfter.length, 24);
  assert.ok(startAfter.every((id) => queryParams(byId.get(id)).includes('start_after')));
});

test('each iterator resolves as the generator will, and names the list its pages hold', () => {
  for (const [id, { items, paging }] of Object.entries(sdk.iterators)) {
    const operation = byId.get(id);
    const resolved = resolvePaging(id, queryParams(operation), paging, sdk.paging);
    const schema = successSchema(operation);
    assert.equal(deref(schema.properties[items])?.type, 'array', id);
    assert.ok(schema.required.includes(items), id);
    if (resolved.cursor) {
      const [head, ...rest] = resolved.cursor.next.split('.');
      const next = rest.reduce((node, key) => deref(node)?.properties?.[key], schema.properties[head]);
      assert.ok(next, `${id}: no ${resolved.cursor.next}`);
    } else {
      assert.equal(deref(schema.properties[resolved.offset.total])?.type, 'integer', id);
    }
  }
});

test('the treasury cursor is an integer, sent back in the cursor parameter', () => {
  const operation = byId.get('getTreasuryTransactions');
  assert.equal(deref(deref(successSchema(operation).properties.cursor).allOf[0]).type, 'integer');
  assert.ok(queryParams(operation).includes('cursor'));
});

test('the four money-moving writes are retried by their required idempotencyKey', () => {
  assert.deepEqual(Object.keys(sdk.idempotency).sort(), ['createInternalTransfer', 'createTransaction', 'requestSendMoney', 'requestTransferMoney']);
  for (const [id, setting] of Object.entries(sdk.idempotency)) {
    const operation = byId.get(id);
    assert.equal(resolveIdempotency(built, operation, setting), 'idempotencyKey', id);
    assert.ok(deref(deref(operation.requestBody).content['application/json'].schema).required.includes('idempotencyKey'), id);
  }
});

test('webhooks are signed in the Mercury-Signature header', () => {
  assert.deepEqual(sdk.webhooks, { header: 'Mercury-Signature' });
});
