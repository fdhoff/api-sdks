import assert from 'node:assert/strict';
import { test } from 'node:test';
import { applyOverlay } from './build-spec.mjs';
import { sha256, verifyPin } from './fetch-spec.mjs';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

const overlayWith = (actions) => ({ overlay: '1.0.0', info: { title: 't', version: '1' }, actions });

test('verifyPin accepts matching bytes and rejects anything else', () => {
  const bytes = Buffer.from('spec');
  assert.doesNotThrow(() => verifyPin(bytes, { sha256: sha256(bytes) }));
  assert.throws(() => verifyPin(Buffer.from('tampered'), { sha256: sha256(bytes) }), /does not match/);
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
  assert.equal(apiDirFromArgs(['node', 'x.mjs', '--verify', 'apis/example']), 'apis/example');
  assert.throws(() => apiDirFromArgs(['node', 'x.mjs', '--verify']), /Usage/);
});
