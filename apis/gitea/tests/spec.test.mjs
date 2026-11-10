import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { verifyPin } from '../../../toolchain/pipeline/fetch-spec.mjs';
import { checkPageItems, resolvePaging } from '../../../toolchain/pipeline/generate.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';
import { specUrl } from '../spec/check-upstream.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const paths = apiPaths(API_DIR);
const lock = JSON.parse(await readFile(paths.lock, 'utf8'));
const sdk = parse(await readFile(new URL('../sdk.yaml', import.meta.url), 'utf8'));
const names = parse(await readFile(new URL('../packages/names.yaml', import.meta.url), 'utf8'));
const upstream = parse(await readFile(paths.spec, 'utf8'));
const built = parse(await readFile(paths.build, 'utf8'));
const deref = (value) => (value?.$ref ? deref(value.$ref.split('/').slice(1).reduce((node, key) => node[key], built)) : value);
const operationsOf = (spec) =>
  Object.entries(spec.paths).flatMap(([path, item]) => METHODS.filter((method) => item[method]).map((method) => ({ path, method, item, ...item[method] })));
const operations = operationsOf(built);
const byId = new Map(operations.map((operation) => [operation.operationId, operation]));
const ids = (list) => list.map((operation) => operation.operationId).sort();
const queryParams = (operation) =>
  [...(operation.item.parameters ?? []), ...(operation.parameters ?? [])]
    .map(deref)
    .filter((parameter) => parameter.in === 'query')
    .map(({ name }) => name);

const DEPRECATED = ['createOrgRepoDeprecated', 'issueDeleteCommentDeprecated', 'issueEditCommentDeprecated', 'userTrackedTimes'];
const ERRORS = ['error', 'forbidden', 'unauthorized', 'validationError', 'repoArchivedError', 'invalidTopicsError', 'notFound', 'conflict'];
const UPSTREAM_ERRORS = ['400', '401', '403', '404', '405', '409', '412', '413', '422', '423', '500'];

test('the cached spec matches its lock at the tag it names, and is not tracked', async () => {
  assert.equal(lock.tag, 'v28.3.0');
  assert.equal(lock.url, specUrl(lock.tag));
  verifyPin(await readFile(paths.spec), lock, paths.spec);
  assert.equal(execFileSync('git', ['ls-files', paths.spec], { encoding: 'utf8' }), '');
});

test('the build stays OpenAPI 3.0.3 and keeps 533 operations, none deprecated', () => {
  assert.equal(built.openapi, '3.0.3');
  assert.equal(operationsOf(upstream).length, 537);
  assert.equal(operations.length, 533);
  assert.equal(byId.size, operations.length);
  assert.deepEqual(DEPRECATED.filter((id) => byId.has(id)), []);
  assert.ok(operations.every((operation) => !operation.deprecated));
  assert.ok(Object.values(built.paths).every((item) => METHODS.some((method) => item[method])));
});

test('the server is a placeholder instance URL with the API prefix', () => {
  assert.deepEqual(built.servers, [{ url: 'https://gitea.example.com/api/v1' }]);
});

test('credentials go in headers only, with the one-time password on Basic and Sudo on either', () => {
  const schemes = built.components.securitySchemes;
  assert.deepEqual(Object.keys(schemes).sort(), ['AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'TOTPHeader']);
  assert.deepEqual(Object.values(schemes).filter((scheme) => scheme.in === 'query'), []);
  assert.deepEqual([schemes.SudoHeader.name, schemes.TOTPHeader.name], ['Sudo', 'X-GITEA-OTP']);
  const requirements = built.security.map((requirement) => Object.keys(requirement).sort().join('+'));
  assert.deepEqual(requirements.sort(), [
    'AuthorizationHeaderToken',
    'AuthorizationHeaderToken+SudoHeader',
    'BasicAuth',
    'BasicAuth+SudoHeader',
    'BasicAuth+SudoHeader+TOTPHeader',
    'BasicAuth+TOTPHeader',
  ]);
  assert.ok(operations.every((operation) => operation.security === undefined));
});

test('error responses carry the APIError body, not headers', () => {
  assert.deepEqual(Object.keys(built.components.schemas.APIError.properties).sort(), ['message', 'url']);
  for (const name of ERRORS) {
    const response = built.components.responses[name];
    assert.deepEqual(response.content, { 'application/json': { schema: { $ref: '#/components/schemas/APIError' } } }, name);
    assert.equal(response.headers, undefined, name);
  }
});

test('every operation that declared no error response now declares the common ones', () => {
  const bare = operationsOf(upstream).filter((operation) => !UPSTREAM_ERRORS.some((status) => operation.responses[status]));
  assert.equal(bare.length, 55);
  const expected = { 400: 'error', 401: 'unauthorized', 403: 'forbidden', 404: 'notFound', 422: 'validationError', '5XX': 'error' };
  for (const { operationId } of bare) {
    const { responses } = byId.get(operationId);
    for (const [status, name] of Object.entries(expected)) assert.equal(responses[status]?.$ref, `#/components/responses/${name}`, `${operationId} ${status}`);
  }
});

test('diffs are text, an archive is binary, and uploads are multipart', () => {
  for (const id of ['repoDownloadCommitDiffOrPatch', 'repoDownloadPullDiffOrPatch']) {
    assert.deepEqual(byId.get(id).responses['200'].content, { 'text/plain': { schema: { type: 'string' } } }, id);
  }
  assert.deepEqual(byId.get('repoGetArchive').responses['200'].content, { 'application/octet-stream': { schema: { type: 'string', format: 'binary' } } });
  for (const id of ['repoGetRawFile', 'repoGetRawFileOrLFS']) {
    assert.ok(Object.values(deref(byId.get(id).responses['200']).content).some((media) => media.schema?.format === 'binary'), id);
  }
  for (const id of ['issueCreateIssueAttachment', 'issueCreateIssueCommentAttachment', 'repoCreateReleaseAttachment']) {
    const content = deref(byId.get(id).requestBody).content;
    assert.deepEqual(Object.keys(content), ['multipart/form-data'], id);
    assert.equal(deref(content['multipart/form-data'].schema).properties.attachment.format, 'binary', id);
  }
});

test('every operation paged by page and limit has an iterator that reads its list', () => {
  const paged = operations.filter((operation) => ['page', 'limit'].every((name) => queryParams(operation).includes(name)));
  assert.equal(paged.length, 112);
  assert.deepEqual(Object.keys(sdk.iterators).sort(), ids(paged));
  for (const [id, iterator] of Object.entries(sdk.iterators)) {
    const operation = byId.get(id);
    const paging = resolvePaging(id, queryParams(operation), iterator, sdk.paging).link_header;
    assert.deepEqual([paging.rel, paging.params], ['next', ['page', 'limit']], id);
    checkPageItems(built, operation, paging.items);
  }
  assert.equal(Object.values(sdk.iterators).filter((iterator) => iterator.items === '$').length, 94);
});

test('every inline name in names.yaml is an inline body of the operation it names', () => {
  const inline = {
    issueCreateIssueCommentAttachment_request: deref(byId.get('issueCreateIssueCommentAttachment').requestBody).content['multipart/form-data'].schema,
    repoCreateReleaseAttachment_request: deref(byId.get('repoCreateReleaseAttachment').requestBody).content['multipart/form-data'].schema,
    teamSearch_200_response: deref(byId.get('teamSearch').responses['200']).content['application/json'].schema,
    userSearch_200_response: deref(byId.get('userSearch').responses['200']).content['application/json'].schema,
  };
  assert.deepEqual(Object.keys(names.inline_schema_names).sort(), Object.keys(inline).sort());
  for (const [name, schema] of Object.entries(inline)) assert.equal(schema.$ref, undefined, name);
});

test('no spec content is tracked under this API', () => {
  const tracked = execFileSync('git', ['ls-files', API_DIR], { encoding: 'utf8' }).split('\n').filter(Boolean);
  assert.deepEqual(tracked.filter((file) => /openapi|upstream\/(?!lock\.json$)|\/build\//.test(file)), []);
});
