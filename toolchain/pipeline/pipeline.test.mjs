import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { applyOverlay } from './build-spec.mjs';
import { ensureSpec, sha256, verifyPin } from './fetch-spec.mjs';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

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
