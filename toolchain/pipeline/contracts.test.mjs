// An API built from several upstream contracts, with synthetic fixtures only.
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdir, mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse, stringify } from 'yaml';
import { buildSpec, inlineServerPath, mergeContracts } from './build-spec.mjs';
import { download, ensureSpec, ensureSpecs, pin, sha256, verify } from './fetch-spec.mjs';
import { contractConfigs, mergeConfig, outermost } from './generate.mjs';
import { contractPaths, lockSources, sourcePaths } from './paths.mjs';
import { specCache } from './spec-cache.mjs';
import { renderContracts } from './spec-diff.mjs';

const HOST = 'https://api.example.test';

// Both contracts declare `Error` and `Money`, as real contracts from one vendor do, and share a host.
const contract = (base, resource) => ({
  openapi: '3.0.3',
  info: { title: resource, version: '1.0.0' },
  servers: [{ url: `${HOST}{basePath}`, variables: { basePath: { default: base } } }],
  security: [{ auth: ['scope'] }],
  paths: {
    [`/${resource}`]: {
      get: {
        operationId: 'list',
        responses: {
          200: { description: 'OK', content: { 'application/json': { schema: { $ref: '#/components/schemas/Money' } } } },
          400: { description: 'Bad', content: { 'application/json': { schema: { $ref: '#/components/schemas/Error' } } } },
        },
      },
    },
  },
  components: {
    schemas: { Error: { type: 'object', properties: { code: { type: 'string' } } }, Money: { type: 'object', properties: { value: { type: 'string' } } } },
    securitySchemes: { auth: { type: 'oauth2', flows: { clientCredentials: { tokenUrl: `${HOST}/token`, scopes: { scope: 'Scope.' } } } } },
  },
});

const ALPHA = Buffer.from(JSON.stringify(contract('/alpha/v1', 'items')));
const BETA = Buffer.from(JSON.stringify(contract('/beta/v2', 'orders')));
const URLS = { alpha: `${HOST}/alpha.json`, beta: `${HOST}/beta.json` };

const twoSourceLock = () => ({
  sources: [
    { name: 'alpha', url: URLS.alpha, sha256: sha256(ALPHA) },
    { name: 'beta', url: URLS.beta, sha256: sha256(BETA) },
  ],
});

async function apiDir(t, lock = twoSourceLock()) {
  const dir = await mkdtemp(join(tmpdir(), 'contracts-'));
  t.after(() => rm(dir, { recursive: true, force: true }));
  await mkdir(join(dir, 'spec/upstream'), { recursive: true });
  await writeFile(join(dir, 'spec/upstream/lock.json'), JSON.stringify(lock));
  return dir;
}

const serve = (t, bodies) =>
  t.mock.method(globalThis, 'fetch', async (url) => new Response(bodies[url] ?? '', { headers: { 'last-modified': 'Mon, 02 Nov 2026 00:00:00 GMT' } }));

test('lockSources reads a single pin or a named list, and refuses bad names', () => {
  assert.deepEqual(lockSources({ url: 'u', sha256: 'h' }), [{ url: 'u', sha256: 'h', name: null }]);
  assert.deepEqual(lockSources(twoSourceLock()).map(({ name }) => name), ['alpha', 'beta']);
  assert.throws(() => lockSources({ sources: [] }), /at least one source/);
  assert.throws(() => lockSources({ sources: [{ name: 'Alpha' }] }), /source name "Alpha" must match/);
  assert.throws(() => lockSources({ sources: [{ name: 'a' }, { name: 'a' }] }), /names source a twice/);
});

test('sourcePaths keeps a single spec where it was and gives each contract its own files', () => {
  assert.equal(sourcePaths('/api', { name: null }).overlay, '/api/spec/overlay.yaml');
  assert.deepEqual(contractPaths('/api', 'alpha'), {
    spec: '/api/spec/upstream/contracts/alpha.yaml',
    overlay: '/api/spec/overlay/alpha.yaml',
    build: '/api/build/contracts/alpha.yaml',
  });
});

test('download rejects a 200 with an empty body before any hash is compared', async (t) => {
  for (const body of ['', ' \n']) {
    t.mock.method(globalThis, 'fetch', async () => new Response(body));
    await assert.rejects(download(URLS.alpha), /HTTP 200 with an empty body, so there is no spec at this URL/);
  }
});

test('ensureSpec reports an empty download as missing, not as changed upstream', async (t) => {
  const dir = await apiDir(t, { url: URLS.alpha, sha256: sha256(ALPHA) });
  t.mock.method(globalThis, 'fetch', async () => new Response(''));
  const paths = { spec: join(dir, 'spec/upstream/openapi.yaml'), lock: join(dir, 'spec/upstream/lock.json') };
  await assert.rejects(ensureSpec(paths), (error) => /empty body/.test(error.message) && !/does not match/.test(error.message));
});

test('ensureSpecs fetches and verifies every contract into its own cache file', async (t) => {
  const dir = await apiDir(t);
  const fetchSpec = serve(t, { [URLS.alpha]: ALPHA, [URLS.beta]: BETA });
  const specs = await ensureSpecs(dir);
  assert.deepEqual(specs.map(({ source }) => source.name), ['alpha', 'beta']);
  assert.deepEqual(await readFile(contractPaths(dir, 'beta').spec), BETA);
  assert.equal(fetchSpec.mock.callCount(), 2);
  await ensureSpecs(dir);
  assert.equal(fetchSpec.mock.callCount(), 2);
  await writeFile(contractPaths(dir, 'alpha').spec, 'stale');
  await assert.rejects(ensureSpecs(dir), /Cached spec .*alpha\.yaml does not match the lock/);
});

test('pin re-pins every contract, and changes nothing when one of them is missing', async (t) => {
  const dir = await apiDir(t, { sources: twoSourceLock().sources.map(({ name, url }) => ({ name, url, sha256: 'old' })) });
  const lockPath = join(dir, 'spec/upstream/lock.json');
  const before = await readFile(lockPath, 'utf8');
  serve(t, { [URLS.alpha]: ALPHA });
  await assert.rejects(pin(dir), /beta\.json: HTTP 200 with an empty body/);
  assert.equal(await readFile(lockPath, 'utf8'), before);
  await assert.rejects(stat(contractPaths(dir, 'alpha').spec), { code: 'ENOENT' });

  t.mock.restoreAll();
  serve(t, { [URLS.alpha]: ALPHA, [URLS.beta]: BETA });
  t.mock.method(console, 'log', () => {});
  await pin(dir);
  const { sources } = JSON.parse(await readFile(lockPath, 'utf8'));
  assert.deepEqual(
    sources.map(({ name, sha256: hash, infoVersion, lastModified }) => ({ name, hash, infoVersion, lastModified })),
    [
      { name: 'alpha', hash: sha256(ALPHA), infoVersion: '1.0.0', lastModified: 'Mon, 02 Nov 2026 00:00:00 GMT' },
      { name: 'beta', hash: sha256(BETA), infoVersion: '1.0.0', lastModified: 'Mon, 02 Nov 2026 00:00:00 GMT' },
    ],
  );
  await verify(dir);
  await rm(contractPaths(dir, 'beta').spec);
  await assert.rejects(verify(dir), /No cached spec at .*beta\.yaml/);
});

test('pin keeps a single-source lock in its single form', async (t) => {
  const dir = await apiDir(t, { url: URLS.alpha, sha256: 'old' });
  serve(t, { [URLS.alpha]: ALPHA });
  t.mock.method(console, 'log', () => {});
  await pin(dir);
  const lock = JSON.parse(await readFile(join(dir, 'spec/upstream/lock.json'), 'utf8'));
  assert.deepEqual(Object.keys(lock), ['url', 'sha256', 'infoVersion', 'lastModified', 'retrievedOn']);
  assert.deepEqual(await readFile(join(dir, 'spec/upstream/openapi.yaml')), ALPHA);
});

test('inlineServerPath moves the server path into every path and keeps each server its host', () => {
  const spec = contract('/alpha/v1', 'items');
  spec.paths['/items'].get.servers = [{ url: 'https://files.example.test{basePath}', variables: { basePath: { default: '/alpha/v1/' } } }];
  spec.servers.push({ url: 'https://{region}.example.test/alpha/v1', variables: { region: { default: 'eu' } } });
  const inlined = inlineServerPath(spec);
  assert.deepEqual(Object.keys(inlined.paths), ['/alpha/v1/items']);
  assert.deepEqual(inlined.servers, [{ url: HOST }, { url: 'https://{region}.example.test', variables: { region: { default: 'eu' } } }]);
  assert.deepEqual(inlined.paths['/alpha/v1/items'].get.servers, [{ url: 'https://files.example.test' }]);

  assert.deepEqual(Object.keys(inlineServerPath({ paths: { '/x': {} } }).paths), ['/x']);
  const disagree = contract('/alpha/v1', 'items');
  disagree.paths['/items'].servers = [{ url: `${HOST}/other` }];
  assert.throws(() => inlineServerPath(disagree), /Servers disagree on their path: \/alpha\/v1, \/other/);
  assert.throws(() => inlineServerPath({ servers: [{ url: `${HOST}{basePath}` }], paths: {} }), /no default for \{basePath\}/);
  const spanning = { servers: [{ url: 'https://{host}', variables: { host: { default: 'api.example.test/v1' } } }], paths: {} };
  assert.throws(() => inlineServerPath(spanning), /\{host\} spanning its host and path/);
  const templated = inlineServerPath({
    servers: [{ url: '{scheme}://api.example.test/v1', variables: { scheme: { default: 'https' } } }],
    paths: { '/x': {} },
  });
  assert.deepEqual(
    [templated.servers, Object.keys(templated.paths)],
    [[{ url: '{scheme}://api.example.test', variables: { scheme: { default: 'https' } } }], ['/v1/x']],
  );
  const whole = inlineServerPath({ servers: [{ url: '{origin}/v1', variables: { origin: { default: 'https://api.example.test' } } }], paths: { '/x': {} } });
  assert.deepEqual(Object.keys(whole.paths), ['/v1/x']);
  const relative = inlineServerPath({ servers: [{ url: '/v{major}', variables: { major: { default: '2' } } }], paths: { '/x': {} } });
  assert.deepEqual([relative.servers, Object.keys(relative.paths)], [[{ url: '/' }], ['/v2/x']]);
});

test('inlineServerPath counts an operation with no server anywhere as served from /', () => {
  const served = { servers: [{ url: `${HOST}/v1` }], get: {} };
  assert.deepEqual(Object.keys(inlineServerPath({ paths: { '/a': structuredClone(served), '/b': { get: { servers: served.servers } } } }).paths), ['/v1/a', '/v1/b']);
  assert.throws(() => inlineServerPath({ paths: { '/a': structuredClone(served), '/b': { get: {} } } }), /Servers disagree on their path: \/v1, \/$/);
  assert.throws(() => inlineServerPath({ paths: { '/a': { get: { servers: served.servers }, post: {} } } }), /Servers disagree on their path: \/v1, \/$/);
});

test('mergeContracts keeps colliding schema names apart and every reference pointing at its own', () => {
  const merged = mergeContracts([
    { name: 'alpha', spec: inlineServerPath(contract('/alpha/v1', 'items')) },
    { name: 'beta', spec: inlineServerPath(contract('/beta/v2', 'orders')) },
  ]);
  assert.deepEqual(Object.keys(merged.components.schemas), ['alpha.Error', 'alpha.Money', 'beta.Error', 'beta.Money']);
  assert.deepEqual(Object.keys(merged.components.securitySchemes), ['alpha.auth', 'beta.auth']);
  const orders = merged.paths['/beta/v2/orders'].get;
  assert.equal(orders.operationId, 'beta.list');
  assert.equal(orders.responses[400].content['application/json'].schema.$ref, '#/components/schemas/beta.Error');
  assert.deepEqual(orders.security, [{ 'beta.auth': ['scope'] }]);
  assert.equal(merged.paths['/alpha/v1/items'].get.operationId, 'alpha.list');
  assert.deepEqual(merged.servers, [{ url: HOST }]);
  assert.equal(merged.security, undefined);
});

test('mergeContracts rewrites discriminator mappings and refuses a path two contracts share', () => {
  const pets = () => ({
    paths: { '/pets': {} },
    components: { schemas: { Pet: { discriminator: { propertyName: 'kind', mapping: { cat: '#/components/schemas/Cat' } } }, Cat: {} } },
  });
  const merged = mergeContracts([{ name: 'alpha', spec: pets() }]);
  assert.deepEqual(merged.components.schemas['alpha.Pet'].discriminator.mapping, { cat: '#/components/schemas/alpha.Cat' });
  assert.throws(() => mergeContracts([{ name: 'alpha', spec: pets() }, { name: 'beta', spec: pets() }]), /Contracts alpha and beta both declare \/pets/);
});

test('mergeContracts spells out bare and implicit discriminator mappings before renaming the schemas', () => {
  const ref = (name) => ({ $ref: `#/components/schemas/${name}` });
  const original = {
    paths: {
      '/pets': {
        get: { responses: { 200: { description: 'OK', content: { 'application/json': { schema: { oneOf: [ref('Cat')], discriminator: { propertyName: 'kind' } } } } } } },
      },
    },
    components: {
      schemas: {
        Pet: { discriminator: { propertyName: 'kind', mapping: { cat: 'Cat' } } },
        Cat: { allOf: [ref('Pet')] },
        Dog: { allOf: [ref('Pet')] },
        Pick: { oneOf: [ref('Cat'), ref('Dog')], discriminator: { propertyName: 'kind', mapping: { dog: '#/components/schemas/Dog' } } },
        Plain: { discriminator: { propertyName: 'kind' } },
      },
    },
  };
  const before = structuredClone(original);
  const merged = mergeContracts([{ name: 'alpha', spec: original }]);
  const schemas = merged.components.schemas;
  const to = (name) => `#/components/schemas/alpha.${name}`;
  assert.deepEqual(schemas['alpha.Pet'].discriminator.mapping, { cat: to('Cat'), Cat: to('Cat'), Dog: to('Dog') });
  assert.deepEqual(schemas['alpha.Pick'].discriminator.mapping, { dog: to('Dog'), Cat: to('Cat'), Dog: to('Dog') });
  assert.equal(schemas['alpha.Plain'].discriminator.mapping, undefined);
  const inline = merged.paths['/pets'].get.responses[200].content['application/json'].schema;
  assert.deepEqual(inline.discriminator.mapping, { Cat: to('Cat') });
  assert.deepEqual(original, before);
});

test('buildSpec builds each contract on its own, then one merged document for the mock', async (t) => {
  const dir = await apiDir(t);
  serve(t, { [URLS.alpha]: ALPHA, [URLS.beta]: BETA });
  t.mock.method(console, 'log', () => {});
  const overlay = { overlay: '1.0.0', info: { title: 't', version: '1' }, actions: [{ target: '$.components.schemas.Error', update: { required: ['code'] } }] };
  await mkdir(join(dir, 'spec/overlay'));
  await writeFile(join(dir, 'spec/overlay/beta.yaml'), stringify(overlay));
  await buildSpec(dir);

  const alpha = parse(await readFile(contractPaths(dir, 'alpha').build, 'utf8'));
  const beta = parse(await readFile(contractPaths(dir, 'beta').build, 'utf8'));
  assert.deepEqual(Object.keys(alpha.paths), ['/alpha/v1/items']);
  assert.deepEqual(Object.keys(alpha.components.schemas), ['Error', 'Money']);
  assert.equal(alpha.components.schemas.Error.required, undefined);
  assert.deepEqual(beta.components.schemas.Error.required, ['code']);
  const merged = parse(await readFile(join(dir, 'build/openapi.yaml'), 'utf8'));
  assert.deepEqual(Object.keys(merged.paths), ['/alpha/v1/items', '/beta/v2/orders']);
  assert.deepEqual(merged.components.schemas['beta.Error'].required, ['code']);

  await writeFile(join(dir, 'spec/overlay/alpha.yaml'), stringify({ ...overlay, actions: [{ target: '$.paths.missing', update: {} }] }));
  await assert.rejects(buildSpec(dir), /matched nothing: \$\.paths\.missing/);
});

test('specCache keeps the single-spec key and gives several one key over all their pins', () => {
  assert.deepEqual(specCache('apis/one', { url: 'u', sha256: 'abc' }), { key: 'upstream-spec-abc', path: 'apis/one/spec/upstream/openapi.yaml' });
  const lock = twoSourceLock();
  const { key, path } = specCache('apis/two', lock);
  assert.match(key, /^upstream-spec-[0-9a-f]{64}$/);
  assert.equal(path, 'apis/two/spec/upstream/contracts');
  assert.equal(specCache('apis/two', twoSourceLock()).key, key);
  lock.sources[1].sha256 = 'changed';
  assert.notEqual(specCache('apis/two', lock).key, key);
});

test('renderContracts names the contracts that changed and warns when operations were removed', () => {
  const alpha = contract('/alpha/v1', 'items');
  const beta = contract('/beta/v2', 'orders');
  const shrunk = { ...beta, paths: {} };
  const text = renderContracts([
    { name: 'alpha', before: alpha, after: alpha },
    { name: 'beta', before: beta, after: shrunk },
    { name: 'gamma', before: null, after: alpha },
  ]);
  assert.match(text, /^Changed contracts: `beta`, `gamma`\./);
  assert.match(text, /\*\*Operations were removed\*\* from `beta`\./);
  assert.match(text, /### Contract `beta`\n\n.*\n\n#### Operations\n\nRemoved:\n\n\* `GET \/orders`/);
  assert.match(text, /### Contract `gamma`\n\nNo copy of the previously pinned spec was cached/);
  assert.doesNotMatch(text, /Contract `alpha`/);
  assert.equal(renderContracts([{ name: 'alpha', before: alpha, after: alpha }]), 'No contract changed.');
  assert.doesNotMatch(renderContracts([{ name: 'alpha', before: alpha, after: { ...alpha, info: { version: '2' } } }]), /removed/);
});

test('the spec-diff command compares a single cached spec or each contract with its old copy', async (t) => {
  const script = fileURLToPath(new URL('./spec-diff.mjs', import.meta.url));
  const specDiff = (dir, pinned) => execFileSync(process.execPath, [script, dir, pinned], { encoding: 'utf8' });
  const alpha = contract('/alpha/v1', 'items');
  const shrunk = { ...alpha, info: { version: '2.0.0' }, paths: {} };

  const single = await apiDir(t, { url: URLS.alpha, sha256: 'unused' });
  await writeFile(join(single, 'spec/upstream/openapi.yaml'), stringify(shrunk));
  await writeFile(join(single, 'pinned.yaml'), stringify(alpha));
  const text = specDiff(single, join(single, 'pinned.yaml'));
  assert.match(text, /^`info\.version` moved from `1\.0\.0` to `2\.0\.0`\.\n\n### Operations\n\nRemoved:\n\n\* `GET \/items`/);
  assert.doesNotMatch(text, /Contract/);
  assert.match(specDiff(single, join(single, 'missing.yaml')), /^No copy of the previously pinned spec was cached/);

  const several = await apiDir(t);
  await mkdir(join(several, 'pinned'));
  for (const [name, spec] of [['alpha', alpha], ['beta', contract('/beta/v2', 'orders')]]) {
    await mkdir(dirname(contractPaths(several, name).spec), { recursive: true });
    await writeFile(contractPaths(several, name).spec, stringify(name === 'alpha' ? shrunk : spec));
    await writeFile(join(several, 'pinned', `${name}.yaml`), stringify(spec));
  }
  assert.match(specDiff(several, join(several, 'pinned')), /^Changed contracts: `alpha`\./);
});

test('contractConfigs gives each contract its own sub-module settings over the package defaults', () => {
  const config = { output: 'src/pkg', runtime: '_runtime', properties: { packageName: 'pkg', flag: true } };
  assert.deepEqual(contractConfigs(config, [null]), [{ name: null, config }]);
  const contracts = {
    alpha: { output: 'src/pkg/alpha', properties: { packageName: 'pkg.alpha' } },
    beta: { output: 'src/pkg/beta', operations: 'operations/beta.yaml', properties: { packageName: 'pkg.beta' } },
  };
  const [alpha, beta] = contractConfigs({ ...config, contracts }, ['alpha', 'beta']);
  assert.deepEqual(alpha.config, { output: 'src/pkg/alpha', runtime: '_runtime', properties: { packageName: 'pkg.alpha', flag: true } });
  assert.equal(beta.config.operations, 'operations/beta.yaml');
  assert.equal('contracts' in beta.config, false);
  assert.throws(() => contractConfigs({ ...config, contracts }, [null]), /lock pins a single spec/);
  assert.throws(() => contractConfigs({ ...config, contracts: { alpha: {} } }, ['alpha', 'beta']), /no sub-module for contracts: beta/);
  assert.throws(() => contractConfigs({ ...config, contracts }, ['alpha']), /unknown contracts: beta/);
  assert.throws(() => contractConfigs(config, ['alpha']), /no sub-module for contracts: alpha/);
});

test('mergeConfig merges nested maps and replaces lists', () => {
  assert.deepEqual(mergeConfig({ a: { b: 1, c: 2 }, list: [1] }, { a: { c: 3 }, list: [2] }), { a: { b: 1, c: 3 }, list: [2] });
});

test('outermost formats a sub-module with the package that holds it', () => {
  assert.deepEqual(outermost(['/p/src/pkg', '/p/src/pkg/alpha', '/p/src/pkg', '/p/src/other']), ['/p/src/pkg', '/p/src/other']);
});
