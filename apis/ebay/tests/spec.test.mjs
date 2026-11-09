import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { verifyPin } from '../../../toolchain/pipeline/fetch-spec.mjs';
import { apiPaths, CONTRACT_CACHE, lockSources, sourcePaths } from '../../../toolchain/pipeline/paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const paths = apiPaths(API_DIR);
const lock = JSON.parse(await readFile(paths.lock, 'utf8'));
const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));
const built = parse(await readFile(paths.build, 'utf8'));
const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], built)) : value);
const operations = Object.entries(built.paths).flatMap(([path, item]) =>
  METHODS.filter((method) => item[method]).map((method) => ({ path, method, item, ...item[method] })),
);
const byId = new Map(operations.map((operation) => [operation.operationId, operation]));
const contractOf = (operation) => operation.operationId.split('.')[0];
const parameters = (operation) => [...(operation.item.parameters ?? []), ...(operation.parameters ?? [])].map(deref);
const ids = (list) => list.map((operation) => operation.operationId).sort();
const postOrder = operations.filter((operation) => contractOf(operation) === 'sell_post_order');
// developer.ebay.com publishes every contract but Post-Order, which eBay's own SDKs carry, pinned to a commit.
const CONTRACT_URL =
  /^https:\/\/(developer\.ebay\.com\/api-docs\/master\/[a-z0-9/-]+\/openapi\/3\/[a-z0-9_]+_oas3|raw\.githubusercontent\.com\/eBay\/[a-z-]+-sdk\/[0-9a-f]{40}\/specs\/openapi\/[a-z-]+)\.json$/;

test('every cached contract matches its lock and none is tracked', async () => {
  for (const source of lockSources(lock)) {
    assert.match(source.url, CONTRACT_URL);
    verifyPin(await readFile(sourcePaths(API_DIR, source).spec), source, source.name);
  }
  assert.equal(execFileSync('git', ['ls-files', CONTRACT_CACHE], { cwd: API_DIR, encoding: 'utf8' }), '');
});

test('the build holds the Sell, Commerce and Developer contracts, 346 operations', () => {
  const groups = lockSources(lock).map(({ name }) => name.split('_')[0]);
  assert.deepEqual([...new Set(groups)], ['sell', 'commerce', 'developer']);
  assert.equal(operations.length, 346);
});

test('every operation has a unique operationId', () => {
  assert.ok(operations.every((operation) => operation.operationId));
  assert.equal(byId.size, operations.length);
});

test('every operation declares its contract’s rate-limit response', () => {
  const missing = operations.filter((operation) => operation.responses['429']?.$ref !== `#/components/responses/${contractOf(operation)}.RateLimited`);
  assert.deepEqual(ids(missing), []);
});

test('no operation takes Content-Type as a parameter', () => {
  const odd = operations.filter((operation) => parameters(operation).some((parameter) => parameter.name.toLowerCase() === 'content-type'));
  assert.deepEqual(ids(odd), []);
});

test('every scope an operation needs is declared by a flow of its scheme', () => {
  const undeclared = [];
  for (const operation of operations) {
    for (const requirement of operation.security ?? []) {
      for (const [scheme, scopes] of Object.entries(requirement)) {
        const flows = Object.values(built.components.securitySchemes[scheme]?.flows ?? {});
        const declared = new Set(flows.flatMap((flow) => Object.keys(flow.scopes ?? {})));
        for (const scope of scopes) if (!declared.has(scope)) undeclared.push(`${operation.operationId} ${scope}`);
      }
    }
  }
  assert.deepEqual(undeclared, []);
});

test('the operations EU and UK sellers must sign are every Finances call, issueRefund and five Post-Order calls', () => {
  const signed = operations.filter((operation) => operation['x-ebay-signature-required'] === true);
  const postOrderSigned = ['createCancellationRequest', 'approveCancellation', 'issueInquiryRefund', 'processReturnRequest', 'issueReturnRefund'].map((id) => `sell_post_order.${id}`);
  const expected = operations.filter(
    (operation) => contractOf(operation) === 'sell_finances' || operation.operationId === 'sell_fulfillment.issueRefund' || postOrderSigned.includes(operation.operationId),
  );
  assert.equal(signed.length, 17);
  assert.deepEqual(ids(signed), ids(expected));
});

test('no success response declares the error object as its body', () => {
  const odd = operations.filter((operation) =>
    Object.entries(operation.responses).some(
      ([status, response]) => ['202', '204'].includes(status) && Object.keys(deref(response).content ?? {}).length > 0,
    ),
  );
  assert.deepEqual(ids(odd), []);
});

test('every upload declares its request body', () => {
  const bodies = Object.fromEntries(
    ['sell_feed.uploadFile', 'sell_fulfillment.uploadEvidenceFile', 'commerce_media.createImageFromFile', 'commerce_media.uploadDocument', 'commerce_media.uploadPostOrderDocument', 'commerce_media.uploadVideo'].map((id) => [
      id,
      Object.keys(deref(byId.get(id).requestBody)?.content ?? {}),
    ]),
  );
  assert.deepEqual(bodies, {
    'sell_feed.uploadFile': ['multipart/form-data'],
    'sell_fulfillment.uploadEvidenceFile': ['multipart/form-data'],
    'commerce_media.createImageFromFile': ['multipart/form-data'],
    'commerce_media.uploadDocument': ['multipart/form-data'],
    'commerce_media.uploadPostOrderDocument': ['multipart/form-data'],
    'commerce_media.uploadVideo': ['application/octet-stream'],
  });
});

test('the evidence upload requires its file part', () => {
  const body = deref(byId.get('sell_fulfillment.uploadEvidenceFile').requestBody);
  assert.equal(body.required, true);
  assert.deepEqual(deref(body.content['multipart/form-data'].schema).required, ['file']);
});

test('every non-JSON success body is a string, and every binary one is binary', () => {
  const odd = [];
  for (const operation of operations) {
    for (const [status, response] of Object.entries(operation.responses)) {
      if (!status.startsWith('2')) continue;
      for (const [type, { schema }] of Object.entries(deref(response).content ?? {})) {
        if (type.startsWith('application/json')) continue;
        const resolved = deref(schema);
        const binary = !type.startsWith('text/');
        if (resolved?.type !== 'string' || (binary && resolved.format !== 'binary')) odd.push(`${operation.operationId} ${type}`);
      }
    }
  }
  assert.deepEqual(odd, []);
});

test('sdk.yaml names an iterator for every operation that pages with a next link, and its items list', () => {
  const positions = new Set(sdk.paging.params);
  const paged = operations.filter((operation) => {
    const query = parameters(operation).filter((parameter) => parameter.in === 'query').map((parameter) => parameter.name);
    const success = Object.values(deref(operation.responses['200'])?.content ?? {})[0];
    return query.some((name) => positions.has(name) && name !== 'limit') && deref(success?.schema)?.properties?.[sdk.paging.link];
  });
  assert.deepEqual(Object.keys(sdk.iterators).sort(), ids(paged));
  const odd = Object.entries(sdk.iterators).filter(([id, items]) => {
    const success = Object.values(deref(byId.get(id).responses['200']).content)[0];
    return deref(deref(success.schema).properties[items])?.type !== 'array';
  });
  assert.deepEqual(odd, []);
});

test('every server has a host key, and every environment maps exactly those keys', () => {
  const origins = new Set(operations.flatMap((operation) => (operation.servers ?? operation.item.servers ?? built.servers).map((server) => server.url)));
  assert.deepEqual([...origins].filter((url) => !sdk.hosts[url]), []);
  const keys = [...new Set(Object.values(sdk.hosts))].sort();
  for (const [name, hosts] of Object.entries(sdk.environments)) assert.deepEqual(Object.keys(hosts).sort(), keys, name);
  assert.deepEqual(Object.fromEntries(Object.entries(sdk.hosts).map(([url, key]) => [key, url])), sdk.environments.production);
});

test('every header default names a header some operation declares', () => {
  const declared = new Set(operations.flatMap((operation) => parameters(operation).filter((parameter) => parameter.in === 'header').map((parameter) => parameter.name.toLowerCase())));
  assert.deepEqual(sdk.header_defaults.filter((name) => !declared.has(name.toLowerCase())), []);
});

test('Post-Order keeps the 29 operations eBay still serves, under one base path', () => {
  assert.equal(postOrder.length, 29);
  const decommissioned = ['confirm', 'closeCase', 'issueCaseRefund', 'provideCaseShipmentInfo', 'provideCaseReturnAddress', 'createInquiry', 'closeInquiry', 'confirmInquiryRefund', 'provideInquiryRefundInfo'];
  assert.deepEqual(decommissioned.filter((id) => byId.has(`sell_post_order.${id}`)), []);
  assert.deepEqual(postOrder.filter((operation) => !operation.path.startsWith('/post-order/v2/') || operation.path.includes('/post-order/v2/post-order/')).map((operation) => operation.path), []);
  assert.deepEqual([...new Set(postOrder.flatMap((operation) => (operation.servers ?? operation.item.servers).map((server) => server.url)))], ['https://api.ebay.com']);
});

test('every Post-Order call takes the user token and requires the marketplace header', () => {
  assert.deepEqual(postOrder.filter((operation) => JSON.stringify(operation.security) !== '[{"sell_post_order.api_auth":[]}]').map((operation) => operation.operationId), []);
  assert.deepEqual(Object.keys(built.components.securitySchemes['sell_post_order.api_auth'].flows), ['authorizationCode']);
  const missing = postOrder.filter((operation) => !parameters(operation).some((parameter) => parameter.in === 'header' && parameter.name === 'X-EBAY-C-MARKETPLACE-ID' && parameter.required));
  assert.deepEqual(ids(missing), []);
});

test('every path parameter is required', () => {
  const optional = operations.filter((operation) => parameters(operation).some((parameter) => parameter.in === 'path' && parameter.required !== true));
  assert.deepEqual(ids(optional), []);
});

test('Post-Order bodies are JSON, and every schema they refer to is defined', () => {
  const xml = postOrder.filter((operation) => JSON.stringify([operation.requestBody, operation.responses]).includes('xml'));
  assert.deepEqual(ids(xml), []);
  const refs = [...JSON.stringify(built).matchAll(/#\/components\/schemas\/(sell_post_order\.[A-Za-z0-9_]+)/g)].map((match) => match[1]);
  assert.deepEqual([...new Set(refs)].filter((name) => !built.components.schemas[name]), []);
  const objectEnums = Object.entries(built.components.schemas).filter(([name, schema]) => name.startsWith('sell_post_order.') && schema.enum && schema.type !== 'string');
  assert.deepEqual(objectEnums.map(([name]) => name), []);
});

test('Post-Order requires the bodies its calls cannot do without, and uploads a base64 file as JSON', () => {
  const optional = postOrder.filter((operation) => operation.requestBody && deref(operation.requestBody).required !== true);
  assert.deepEqual(ids(optional), ['appealCaseDecision', 'issueInquiryRefund', 'markItemReceived', 'rejectCancellation'].map((id) => `sell_post_order.${id}`));
  const upload = deref(byId.get('sell_post_order.uploadReturnFile').requestBody);
  assert.deepEqual(Object.keys(upload.content), ['application/json']);
  assert.deepEqual(deref(upload.content['application/json'].schema).required, ['data', 'filePurpose']);
});
