import assert from 'node:assert/strict';
import { mkdir, mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { applyOverlay } from './build-spec.mjs';
import { ensureSpec, sha256, verifyPin } from './fetch-spec.mjs';
import { applyBinary, applyHeaders, applyHosts, applyOperations, checkHeaderDefaults, collapseSingleUnions, omitOperations, dropNullable, securityOf, dropUnions, fillPackageName, ignoreFile, isJsonMediaType, packageNames, relax, renameSchemas, resolveIdempotency, resolvePaging, stripProse, supportingFiles } from './generate.mjs';
import { apiDirFromArgs, apiPaths } from './paths.mjs';
import { diffSpecs, renderDiff } from './spec-diff.mjs';

const overlayWith = (actions) => ({ overlay: '1.0.0', info: { title: 't', version: '1' }, actions });

test('verifyPin accepts matching bytes and rejects anything else', () => {
  const bytes = Buffer.from('spec');
  assert.doesNotThrow(() => verifyPin(bytes, { sha256: sha256(bytes) }, 'Spec'));
  assert.throws(() => verifyPin(Buffer.from('tampered'), { sha256: sha256(bytes) }, 'Spec'), /Spec does not match the lock/);
});

const SPEC = Buffer.from('spec');
const SPEC_URL = 'https://spec.invalid/openapi.yaml';

async function emptyCache(t) {
  const dir = await mkdtemp(join(tmpdir(), 'spec-cache-'));
  t.after(() => rm(dir, { recursive: true, force: true }));
  const paths = { spec: join(dir, 'openapi.yaml'), lock: join(dir, 'lock.json') };
  await writeFile(paths.lock, JSON.stringify({ url: SPEC_URL, sha256: sha256(SPEC) }));
  return paths;
}

const offline = (t) =>
  t.mock.method(globalThis, 'fetch', async () => {
    throw new Error('network used');
  });

test('ensureSpec downloads the pinned spec into an empty cache', async (t) => {
  const paths = await emptyCache(t);
  const fetchSpec = t.mock.method(globalThis, 'fetch', async () => new Response(SPEC));
  assert.deepEqual(await ensureSpec(paths), SPEC);
  assert.equal(fetchSpec.mock.calls[0].arguments[0], SPEC_URL);
  assert.deepEqual(await readFile(paths.spec), SPEC);
});

test('ensureSpec serves a valid cache without the network', async (t) => {
  const paths = await emptyCache(t);
  await writeFile(paths.spec, SPEC);
  const fetchSpec = offline(t);
  assert.deepEqual(await ensureSpec(paths), SPEC);
  assert.equal(fetchSpec.mock.callCount(), 0);
});

test('ensureSpec rejects a mismatched download and caches nothing', async (t) => {
  const paths = await emptyCache(t);
  t.mock.method(globalThis, 'fetch', async () => new Response('changed upstream'));
  await assert.rejects(ensureSpec(paths), /does not match the lock.*spec:pin/);
  await assert.rejects(stat(paths.spec), { code: 'ENOENT' });
});

test('ensureSpec rejects a cache that does not match the lock', async (t) => {
  const paths = await emptyCache(t);
  await writeFile(paths.spec, 'stale');
  const fetchSpec = offline(t);
  await assert.rejects(ensureSpec(paths), /Cached spec .* does not match the lock/);
  assert.equal(fetchSpec.mock.callCount(), 0);
});

test('ensureSpec reports a failed download', async (t) => {
  const paths = await emptyCache(t);
  t.mock.method(globalThis, 'fetch', async () => new Response('', { status: 503 }));
  await assert.rejects(ensureSpec(paths), /HTTP 503/);
});

test('applyOverlay applies an action that matches', async () => {
  const result = await applyOverlay({ info: {} }, overlayWith([{ target: '$.info', update: { title: 'x' } }]));
  assert.equal(result.info.title, 'x');
});

test('applyOverlay rejects an action that matches nothing', async () => {
  const overlay = overlayWith([{ target: '$.paths.missing', update: { a: 1 } }]);
  await assert.rejects(applyOverlay({ paths: {} }, overlay), /matched nothing: \$\.paths\.missing/);
});

test('applyOverlay rejects an overlay with no actions', async () => {
  await assert.rejects(applyOverlay({}, overlayWith([])), /no actions/);
});

test('apiPaths resolves every artefact under the API directory', () => {
  const paths = apiPaths('/repo/apis/example');
  assert.equal(paths.spec, '/repo/apis/example/spec/upstream/openapi.yaml');
  assert.equal(paths.build, '/repo/apis/example/build/openapi.yaml');
});

test('apiDirFromArgs skips flags and requires a directory', () => {
  assert.equal(apiDirFromArgs(['node', 'x.mjs', '--pin', 'apis/example']), 'apis/example');
  assert.throws(() => apiDirFromArgs(['node', 'x.mjs', '--verify']), /Usage/);
});

test('stripProse removes prose but keeps fields that share its names', () => {
  const spec = {
    info: { title: 'T', description: 'prose' },
    components: {
      schemas: {
        Thing: {
          description: 'prose',
          example: { description: 'x' },
          properties: { description: { type: 'string', description: 'prose' } },
        },
      },
    },
  };
  assert.deepEqual(stripProse(spec), {
    info: { title: 'T' },
    components: { schemas: { Thing: { properties: { description: { type: 'string' } } } } },
  });
});

test('renameSchemas moves a schema and every reference to it', () => {
  const spec = {
    components: { schemas: { a: { type: 'string' }, B: { properties: { x: { $ref: '#/components/schemas/a' } } } } },
  };
  const renamed = renameSchemas(spec, { a: 'Renamed' });
  assert.deepEqual(Object.keys(renamed.components.schemas), ['Renamed', 'B']);
  assert.equal(renamed.components.schemas.B.properties.x.$ref, '#/components/schemas/Renamed');
  assert.throws(() => renameSchemas(spec, { missing: 'Other' }), /unknown schemas: missing/);
});

test('packageNames adds a package\'s own names to the shared ones but refuses a rename', () => {
  const shared = { schema_names: { a: 'A' }, inline_schema_names: { x_response: 'X' } };
  assert.deepEqual(packageNames(shared, { inline_schema_names: { y_response: 'Y' } }), {
    schema_names: { a: 'A' },
    inline_schema_names: { x_response: 'X', y_response: 'Y' },
  });
  assert.deepEqual(packageNames({}, {}), { schema_names: {}, inline_schema_names: {} });
  assert.throws(() => packageNames(shared, { inline_schema_names: { x_response: 'Other' } }), /renames shared names: x_response/);
});

test('applyOperations marks operations whose query or form parameters must be passed', () => {
  const op = (operationId, extra) => ({ '/x': { get: { operationId, ...extra } } });
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const required = (paths, components) =>
    applyOperations({ paths, components }, names).paths['/x'].get['x-sdk-params-required'];

  assert.equal(required(op('a', {})), false);
  assert.equal(required(op('a', { parameters: [{ name: 'q', in: 'query' }] })), false);
  assert.equal(required(op('a', { parameters: [{ name: 'q', in: 'query', required: true }] })), true);
  assert.equal(required(op('a', { parameters: [{ name: 'id', in: 'path', required: true }] })), false);
  assert.equal(
    required(op('a', { parameters: [{ $ref: '#/components/parameters/Q' }] }), {
      parameters: { Q: { name: 'q', in: 'query', required: true } },
    }),
    true,
  );
  const form = { requestBody: { content: { 'multipart/form-data': { schema: { $ref: '#/components/schemas/F' } } } } };
  const allOf = { allOf: [{ required: ['file'] }] };
  assert.equal(required(op('a', form), { schemas: { F: {} } }), false);
  assert.equal(required(op('a', form), { schemas: { F: allOf } }), true);
  const urlencoded = { requestBody: { content: { 'application/x-www-form-urlencoded': { schema: { required: ['title'] } } } } };
  assert.equal(required(op('a', urlencoded)), true);
});

test('applyOperations marks operations that take query or form parameters', () => {
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const has = (extra) => applyOperations({ paths: { '/x': { get: { operationId: 'a', ...extra } } } }, names).paths['/x'].get['x-sdk-has-params'];
  const body = (type) => ({ requestBody: { content: { [type]: { schema: {} } } } });

  assert.equal(has({}), false);
  assert.equal(has({ parameters: [{ name: 'id', in: 'path', required: true }] }), false);
  assert.equal(has(body('application/json')), false);
  assert.equal(has({ parameters: [{ name: 'q', in: 'query' }] }), true);
  assert.equal(has(body('multipart/form-data')), true);
  assert.equal(has({ parameters: [{ name: 'q', in: 'query' }], ...body('application/x-www-form-urlencoded') }), true);
});

test('applyHosts gives each operation the host key of its first server, unless the overlay set one', () => {
  const spec = () => ({
    servers: [{ url: 'https://main.example.test/' }],
    paths: {
      '/a': { get: { operationId: 'a' } },
      '/b': { servers: [{ url: 'https://{host}.example.test', variables: { host: { default: 'files' } } }], get: { operationId: 'b' } },
      '/c': { get: { operationId: 'c', servers: [{ url: 'https://files.example.test' }, { url: 'https://main.example.test' }] } },
      '/d': { get: { operationId: 'd', 'x-sdk-host': 'main' } },
    },
  });
  const servers = { 'https://main.example.test': 'main', 'https://files.example.test/': 'files' };
  const { paths } = applyHosts(spec(), servers);
  assert.deepEqual(
    Object.values(paths).map((item) => item.get['x-sdk-host']),
    ['main', 'files', 'files', 'main'],
  );
  const unrouted = spec();
  delete unrouted.paths['/d'];
  assert.equal(applyHosts(unrouted, undefined).paths['/a'].get['x-sdk-host'], undefined);
  assert.throws(() => applyHosts(spec(), undefined), /d: x-sdk-host main is set, but sdk.yaml has no hosts/);
  assert.throws(() => applyHosts(spec(), { 'https://main.example.test': 'main' }), /b: no host key for server/);
  const typo = spec();
  typo.paths['/d'].get['x-sdk-host'] = 'mian';
  assert.throws(() => applyHosts(typo, servers), /d: x-sdk-host mian is not a host key; expected one of: files, main/);
});

test('applyHeaders flags default-able headers as optional and drops headers the runtime sets', () => {
  const spec = () => ({
    paths: {
      '/x': {
        parameters: [{ name: 'Content-Type', in: 'header', required: true }],
        get: {
          operationId: 'a',
          parameters: [
            { $ref: '#/components/parameters/Tenant' },
            { name: 'accept', in: 'header' },
            { name: 'X-Other', in: 'header' },
            { name: 'x-tenant', in: 'query' },
          ],
        },
      },
    },
    components: { parameters: { Tenant: { name: 'X-Tenant', in: 'header', required: true } } },
  });
  const built = applyHeaders(spec(), ['x-TENANT']);
  const item = built.paths['/x'];
  assert.deepEqual(item.parameters, []);
  assert.deepEqual(item.get.parameters.slice(1), [{ name: 'X-Other', in: 'header' }, { name: 'x-tenant', in: 'query' }]);
  assert.deepEqual(built.components.parameters.Tenant, { name: 'X-Tenant', in: 'header', required: false, 'x-sdk-header-default': true });
  assert.equal(applyHeaders(spec()).components.parameters.Tenant['x-sdk-header-default'], undefined);
  assert.throws(() => applyHeaders(spec(), ['Content-Type']), /runtime sets: content-type/);
  assert.throws(() => applyHeaders(spec(), ['X-Tenant', 'X-Tenat']), /names no header parameter: x-tenat$/);

  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const { get } = applyOperations(built, names).paths['/x'];
  assert.equal(get['x-sdk-has-headers'], true);
  assert.equal(get['x-sdk-has-params'], true);
  assert.equal(get['x-sdk-params-required'], false);
  assert.equal(applyOperations(applyHeaders(spec()), names).paths['/x'].get['x-sdk-has-headers'], false);
});

test('header defaults need only be declared by one of an API\'s contracts', () => {
  const contract = (header) => ({ paths: { '/x': { get: { operationId: 'a', parameters: [{ name: header, in: 'header' }] } } } });
  const used = new Set();
  const defaults = ['X-Tenant', 'Content-Language'];
  applyHeaders(contract('X-Tenant'), defaults, used);
  const second = applyHeaders(contract('Content-Language'), defaults, used);
  assert.equal(second.paths['/x'].get.parameters[0]['x-sdk-header-default'], true);
  checkHeaderDefaults(defaults, used);
  assert.throws(() => checkHeaderDefaults([...defaults, 'X-Tenat'], used), /names no header parameter: x-tenat$/);
});

test('applyOperations marks operations whose success response declares a JSON body, beside a 204 or not', () => {
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const json = (responses, components) =>
    applyOperations({ paths: { '/x': { get: { operationId: 'a', responses } } }, components }, names).paths['/x'].get[
      'x-sdk-returns-json'
    ];
  const body = (type) => ({ content: { [type]: { schema: {} } } });

  assert.equal(json(undefined), false);
  assert.equal(json({ 204: { description: 'None.' } }), false);
  assert.equal(json({ 200: body('text/plain') }), false);
  assert.equal(json({ 400: body('application/json'), 204: {} }), false);
  assert.equal(json({ 200: body('application/json') }), true);
  assert.equal(json({ 200: body('application/json'), 204: { description: 'None.' } }), true);
  assert.equal(json({ 202: { $ref: '#/components/responses/R' } }, { responses: { R: body('application/json') } }), true);
  assert.equal(json({ 200: body('application/problem+json') }), true);
  assert.equal(json({ 200: body('*/*') }), false);
  assert.equal(json({ 200: body('application/x-ndjson') }), false);
});

test('applyBinary marks binary responses and raw request bodies, and drops what generators would type', () => {
  const file = { type: 'string', format: 'binary' };
  const spec = () => ({
    paths: {
      '/download': {
        get: {
          operationId: 'download',
          responses: {
            200: { content: { 'application/pdf': { schema: file } } },
            206: { $ref: '#/components/responses/Partial' },
            404: { content: { 'application/json': { schema: {} } } },
          },
        },
      },
      '/upload': { post: { operationId: 'upload', requestBody: { content: { 'application/octet-stream': { schema: { $ref: '#/components/schemas/File' } } } } } },
      '/form': { post: { operationId: 'form', requestBody: { content: { 'multipart/form-data': { schema: { properties: { file } } } } } } },
      '/text': { get: { operationId: 'text', responses: { 200: { content: { 'text/plain': { schema: { type: 'string' } } } } } } },
    },
    components: { schemas: { File: file }, responses: { Partial: { content: { 'application/octet-stream': { schema: file } } } } },
  });
  const { paths, components } = applyBinary(spec());
  const download = paths['/download'].get;
  assert.equal(download['x-sdk-binary-response'], true);
  assert.equal(download['x-sdk-accept'], 'application/pdf, application/octet-stream');
  assert.deepEqual(download.responses[200], { description: '' });
  assert.deepEqual(download.responses[206], { description: '' });
  assert.deepEqual(Object.keys(download.responses[404].content), ['application/json']);
  assert.ok(components.responses.Partial.content);
  const upload = paths['/upload'].post;
  assert.equal(upload['x-sdk-raw-body'], 'application/octet-stream');
  assert.equal(upload.requestBody, undefined);
  assert.deepEqual(applyBinary(spec()).paths['/form'], spec().paths['/form']);
  assert.deepEqual(applyBinary(spec()).paths['/text'], spec().paths['/text']);

  const names = { download: { resource: 'r', method: 'download', summary: 'D.' } };
  const only = { paths: { '/download': spec().paths['/download'] }, components: spec().components };
  assert.equal(applyOperations(applyBinary(only), names).paths['/download'].get['x-sdk-returns-json'], false);

  const mixed = spec();
  mixed.paths['/download'].get.responses[201] = { content: { 'application/json': { schema: {} } } };
  assert.throws(() => applyBinary(mixed), /download: a success response mixes binary and other bodies/);
  const offered = spec();
  offered.paths['/upload'].post.requestBody.content['application/json'] = { schema: {} };
  assert.throws(() => applyBinary(offered), /upload: a request body offers binary and other media types/);
});

test('applyOperations marks operations that declare a 204 beside a JSON success', () => {
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const empty = (responses) =>
    applyOperations({ paths: { '/x': { put: { operationId: 'a', responses } } } }, names).paths['/x'].put['x-sdk-no-content'];
  const json = { content: { 'application/json': { schema: {} } } };

  assert.equal(empty({ 200: json, 204: { description: 'None.' } }), true);
  assert.equal(empty({ 200: json }), false);
  assert.equal(empty({ 204: { description: 'None.' } }), false);
  assert.equal(empty({ 202: { description: 'None.' }, 200: json }), false);
});

test('applyOperations passes each operation its security requirements, inherited or its own', () => {
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' } };
  const security = (spec, own) =>
    applyOperations({ ...spec, paths: { '/x': { get: { operationId: 'a', ...own } } } }, names).paths['/x'].get['x-sdk-security'];

  assert.deepEqual(security({}, {}), []);
  assert.deepEqual(security({ security: [{ key: [] }] }, {}), [{ schemes: [{ scheme: 'key', scopes: [] }] }]);
  assert.deepEqual(security({ security: [{ key: [] }] }, { security: [] }), []);
  assert.deepEqual(security({ security: [{ key: [] }] }, { security: [{ key: [], oauth: ['read', 'write'] }, { app: ['read'] }] }), [
    { schemes: [{ scheme: 'key', scopes: [] }, { scheme: 'oauth', scopes: ['read', 'write'] }] },
    { schemes: [{ scheme: 'app', scopes: ['read'] }] },
  ]);
  assert.deepEqual(securityOf({}, { security: [{ key: null }] }), [{ schemes: [{ scheme: 'key', scopes: [] }] }]);
});

test('omitOperations removes the operations operations.yaml omits, and their empty paths', () => {
  const names = { a: { resource: 'r', method: 'a', summary: 'A.' }, b: { omit: 'Needs binary bodies.' }, c: { omit: 'Same.' } };
  const spec = { paths: { '/x': { get: { operationId: 'a' }, post: { operationId: 'b' } }, '/y': { get: { operationId: 'c' } } } };
  const omitted = applyOperations(omitOperations(spec, names), names);
  assert.deepEqual(Object.keys(omitted.paths), ['/x']);
  assert.deepEqual(Object.keys(omitted.paths['/x']), ['get']);
  assert.throws(() => omitOperations({ paths: {} }, { z: { omit: 'Gone.' } }), /omits unknown operations: z/);
});

test('isJsonMediaType accepts application/json and +json suffixes only', () => {
  for (const type of ['application/json', 'Application/JSON', 'application/json; charset=utf-8', 'application/problem+json', 'application/vnd.api+json']) {
    assert.equal(isJsonMediaType(type), true, type);
  }
  for (const type of ['*/*', 'application/*', 'application/x-ndjson', 'application/jsonl', 'text/json-seq', 'text/plain']) {
    assert.equal(isJsonMediaType(type), false, type);
  }
});

test('dropNullable removes nullability but keeps properties that use its name', () => {
  const spec = {
    a: { type: 'string', nullable: true, enum: ['x', null] },
    b: { anyOf: [{ nullable: true }, { type: 'string', nullable: true }] },
    c: { anyOf: [{ type: 'string' }, { type: 'integer' }] },
    d: { properties: { nullable: { type: 'boolean', nullable: true } } },
  };
  assert.deepEqual(dropNullable(spec), {
    a: { type: 'string', enum: ['x'] },
    b: { type: 'string' },
    c: { anyOf: [{ type: 'string' }, { type: 'integer' }] },
    d: { properties: { nullable: { type: 'boolean' } } },
  });
});

test('collapseSingleUnions replaces a lone single-branch union with its branch', () => {
  const ref = { $ref: '#/components/schemas/Node' };
  const spec = {
    lone: { items: { oneOf: [ref] } },
    nested: { anyOf: [{ oneOf: [ref] }] },
    beside: { oneOf: [ref], nullable: true },
    real: { oneOf: [ref, { type: 'string' }] },
    properties: { oneOf: { type: 'array', items: { oneOf: [ref] } } },
  };
  assert.deepEqual(collapseSingleUnions(spec), {
    lone: { items: ref },
    nested: ref,
    beside: { oneOf: [ref], nullable: true },
    real: { oneOf: [ref, { type: 'string' }] },
    properties: { oneOf: { type: 'array', items: ref } },
  });
});

test('dropUnions leaves unions and references to them untyped', () => {
  const spec = {
    components: {
      schemas: {
        Either: { oneOf: [{ type: 'string' }, { type: 'integer' }] },
        Item: { properties: { either: { $ref: '#/components/schemas/Either' }, inline: { anyOf: [{ type: 'string' }] } } },
      },
    },
  };
  assert.deepEqual(dropUnions(spec), { components: { schemas: { Item: { properties: { either: {}, inline: {} } } } } });
});

test('relax types single-branch and null-plus-one unions before leaving real unions untyped', () => {
  const ref = { $ref: '#/components/schemas/Amount' };
  const spec = {
    components: {
      schemas: {
        Amount: { type: 'string' },
        Item: {
          properties: {
            single: { anyOf: [ref], nullable: true },
            optional: { oneOf: [{ nullable: true }, { type: 'string' }] },
            either: { anyOf: [ref, { type: 'integer' }] },
          },
        },
      },
    },
  };
  const { properties } = relax(spec, { drop_nullable: true, drop_unions: true }).components.schemas.Item;
  assert.deepEqual(properties, { single: ref, optional: { type: 'string' }, either: {} });
  assert.deepEqual(relax(spec, {}), spec);
});

test('applyOperations names every operation and refuses gaps', () => {
  const spec = () => ({
    paths: {
      '/items/{id}': {
        parameters: [{ name: 'id', schema: { oneOf: [{ type: 'string' }] } }],
        get: { operationId: 'get-item', parameters: [{ name: 'page', in: 'query' }] },
      },
    },
  });
  const names = {
    'get-item': { resource: 'items', method: 'get', summary: 'Get.', iterator: 'iter', items: 'Item', string_params: ['id'] },
  };
  const { paths } = applyOperations(spec(), names);
  const item = paths['/items/{id}'];
  assert.deepEqual(item.get.tags, ['items']);
  assert.equal(item.get['x-sdk-method'], 'get');
  assert.equal(item.get['x-sdk-items'], 'Item');
  assert.deepEqual(item.parameters[0].schema, { type: 'string' });
  assert.throws(() => applyOperations(spec(), {}), /does not name get-item/);
  assert.throws(() => applyOperations(spec(), { ...names, other: {} }), /unknown operations: other/);
});

test('applyOperations gives every iterator its paging, and refuses paging without one', () => {
  const spec = () => ({
    paths: {
      '/items': {
        parameters: [{ name: 'limit', in: 'query' }],
        get: { operationId: 'list-items', parameters: [{ name: 'offset', in: 'query' }] },
      },
    },
  });
  const list = { resource: 'items', method: 'list', summary: 'List.', iterator: 'iter', items: 'Item' };
  const offset = { style: 'offset' };
  const { get } = applyOperations(spec(), { 'list-items': list }, offset).paths['/items'];
  assert.deepEqual(get['x-sdk-paging'], { offset: { items: 'results', total: 'count', offset: 'offset' } });
  const unpaged = { ...list, iterator: undefined, paging: offset };
  assert.throws(() => applyOperations(spec(), { 'list-items': unpaged }), /paging is set but there is no iterator/);
  assert.throws(() => applyOperations(spec(), { 'list-items': list }), /no query parameter holds the next_link paging position/);
});

test('resolvePaging layers the operation over the API default over the style default', () => {
  assert.deepEqual(resolvePaging('op', ['page']), { next_link: { items: 'results', link: 'next', params: ['page', 'cursor'] } });
  assert.deepEqual(resolvePaging('op', ['token'], { params: ['token'] }, { style: 'next_link', link: 'more' }), {
    next_link: { items: 'results', link: 'more', params: ['token'] },
  });
  assert.deepEqual(resolvePaging('op', ['start'], { total: 'total', offset: 'start' }, { style: 'offset', items: 'data' }), {
    offset: { items: 'data', total: 'total', offset: 'start' },
  });
  assert.deepEqual(resolvePaging('op', ['offset'], { style: 'offset' }, { style: 'next_link', link: 'more' }), {
    offset: { items: 'results', total: 'count', offset: 'offset' },
  });
  assert.throws(() => resolvePaging('op', ['page'], { style: 'keyset' }), /op: unknown paging style keyset/);
  assert.throws(() => resolvePaging('op', ['offset'], { style: 'offset', link: 'next' }), /unknown offset paging keys: link/);
  assert.throws(() => resolvePaging('op', ['page'], { style: 'offset' }), /no query parameter holds the offset paging position \(offset\)/);
});

test('applyOperations marks a write as idempotent only when its JSON body has the named key', () => {
  const spec = () => ({
    paths: {
      '/payments': {
        post: {
          operationId: 'create-payment',
          requestBody: { content: { 'application/json': { schema: { $ref: '#/components/schemas/Payment' } } } },
        },
      },
    },
    components: {
      schemas: {
        Base: { type: 'object', properties: { idempotencyKey: { type: 'string' } } },
        Payment: { allOf: [{ $ref: '#/components/schemas/Base' }, { type: 'object', properties: { amount: { type: 'number' } } }] },
      },
    },
  });
  const create = { resource: 'payments', method: 'create', summary: 'Create.' };
  const marked = applyOperations(spec(), { 'create-payment': { ...create, idempotency: { body: 'idempotencyKey' } } });
  assert.equal(marked.paths['/payments'].post['x-sdk-idempotency-key'], 'idempotencyKey');
  const unmarked = applyOperations(spec(), { 'create-payment': create });
  assert.equal(unmarked.paths['/payments'].post['x-sdk-idempotency-key'], undefined);
  assert.throws(
    () => applyOperations(spec(), { 'create-payment': { ...create, idempotency: { body: 'requestId' } } }),
    /create-payment: idempotency field requestId is not in the JSON request body/,
  );
});

test('resolveIdempotency refuses unknown keys, a missing field and an operation without a JSON body', () => {
  const operation = { operationId: 'op', requestBody: { content: { 'application/json': { schema: { properties: { key: {} } } } } } };
  assert.equal(resolveIdempotency({}, operation, { body: 'key' }), 'key');
  assert.throws(() => resolveIdempotency({}, operation, { body: 'key', header: 'Idempotency-Key' }), /op: unknown idempotency keys: header/);
  assert.throws(() => resolveIdempotency({}, operation, {}), /op: idempotency needs a body field/);
  assert.throws(() => resolveIdempotency({}, { operationId: 'op' }, { body: 'key' }), /idempotency field key is not in the JSON request body/);
  const form = { operationId: 'op', requestBody: { content: { 'multipart/form-data': { schema: { properties: { key: {} } } } } } };
  assert.throws(() => resolveIdempotency({}, form, { body: 'key' }), /idempotency field key is not in the JSON request body/);
});

test('resolvePaging reads a cursor style that sends a value from each page back as a query parameter', () => {
  assert.deepEqual(resolvePaging('op', ['cursor'], { style: 'cursor' }), { cursor: { items: 'results', next: 'cursor', param: 'cursor' } });
  assert.deepEqual(resolvePaging('op', ['limit', 'start_after'], { items: 'gadgets', next: 'page.next_page', param: 'start_after' }, { style: 'cursor' }), {
    cursor: { items: 'gadgets', next: 'page.next_page', param: 'start_after' },
  });
  assert.throws(() => resolvePaging('op', ['cursor'], { style: 'cursor', link: 'next' }), /unknown cursor paging keys: link/);
  assert.throws(() => resolvePaging('op', ['limit'], { style: 'cursor', param: 'start_after' }), /no query parameter holds the cursor paging position \(start_after\)/);
  assert.throws(() => resolvePaging('op', ['cursor'], { style: 'cursor', next: 'page..next' }), /cursor paging next is not a dotted path: page\.\.next/);
});

const driftSpec = (version, paths, schemas) => ({ info: { version }, paths, components: { schemas } });

test('diffSpecs sorts operations and schemas into added, removed, changed and prose-only', () => {
  const before = driftSpec(
    '1',
    {
      '/a': { get: { responses: { 200: { description: 'old' } } } },
      '/b': { parameters: [{ name: 'x', in: 'query' }], get: {} },
      '/c': { delete: {} },
    },
    { Kept: { type: 'string', description: 'old' }, Gone: { type: 'string' }, Moved: { type: 'string' } },
  );
  const after = driftSpec(
    '2',
    {
      '/a': { get: { responses: { 200: { description: 'new' } } } },
      '/b': { parameters: [{ name: 'x', in: 'path' }], get: {} },
      '/d': { post: {} },
    },
    { Kept: { type: 'string', description: 'new' }, Moved: { type: 'integer' }, New: { type: 'object' } },
  );
  assert.deepEqual(diffSpecs(before, after), {
    version: ['1', '2'],
    operations: { added: ['POST /d'], removed: ['DELETE /c'], changed: ['GET /b'], prose: ['GET /a'] },
    schemas: { added: ['New'], removed: ['Gone'], changed: ['Moved'], prose: ['Kept'] },
  });
});

test('renderDiff names what changed without quoting either spec', () => {
  const before = driftSpec('1', { '/a': { get: { summary: 'secret prose' } } }, { S: { type: 'string' } });
  const after = driftSpec('1', { '/a': { get: { summary: 'other prose' } } }, { S: { type: 'string' }, T: { type: 'string' } });
  const text = renderDiff(diffSpecs(before, after));
  assert.match(text, /`info\.version` is unchanged at `1`/);
  assert.match(text, /### Operations\n\nDescriptions or examples only: 1/);
  assert.match(text, /### Schemas\n\nAdded:\n\n\* `T`/);
  assert.doesNotMatch(text, /prose/);
  assert.match(renderDiff(diffSpecs(after, after)), /### Operations\n\nNo changes\./);
});

test('fillPackageName writes the package name into every runtime file', async (t) => {
  const dir = await mkdtemp(join(tmpdir(), 'runtime-'));
  t.after(() => rm(dir, { recursive: true, force: true }));
  await mkdir(join(dir, 'nested'));
  await writeFile(join(dir, 'a.cs'), 'namespace PackageNamespace;');
  await writeFile(join(dir, 'nested/b.cs'), 'using PackageNamespace.Runtime;');
  await fillPackageName(dir, 'Example');
  assert.equal(await readFile(join(dir, 'a.cs'), 'utf8'), 'namespace Example;');
  assert.equal(await readFile(join(dir, 'nested/b.cs'), 'utf8'), 'using Example.Runtime;');
});

test('supportingFiles generates extra templates apart from the package source', () => {
  const files = supportingFiles({ resources: 'resources.rs', supporting_files: { 'dispatch.mustache': 'driver/dispatch.rs' } }, 'src');
  assert.deepEqual(files, {
    'resources.mustache': { templateType: 'SupportingFiles', destinationFilename: join('src', 'resources.rs') },
    'dispatch.mustache': { templateType: 'SupportingFiles', destinationFilename: join('supporting', 'dispatch.mustache') },
  });
  assert.deepEqual(Object.keys(supportingFiles({ resources: 'resources.py' }, 'pkg')), ['resources.mustache']);
});

test('ignoreFile lists one path per line, and nothing by default', () => {
  assert.equal(ignoreFile({ ignore: ['src/a.rs', 'src/b.rs'] }), 'src/a.rs\nsrc/b.rs\n');
  assert.equal(ignoreFile({}), '');
});
