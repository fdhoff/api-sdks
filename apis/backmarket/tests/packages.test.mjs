import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PYTHON = join(ROOT, 'apis/backmarket/packages/python');
const TYPESCRIPT = join(ROOT, 'apis/backmarket/packages/typescript');
const AFFILIATION = /not affiliated with.*Back Market/i;

test('the Python package ships the root licence and notice', async () => {
  for (const name of ['LICENSE', 'NOTICE']) {
    assert.equal(await readFile(join(PYTHON, name), 'utf8'), await readFile(join(ROOT, name), 'utf8'));
  }
});

test('the Python manifest declares Apache-2.0 and says it is unofficial', async () => {
  const manifest = await readFile(join(PYTHON, 'pyproject.toml'), 'utf8');
  assert.match(manifest, /^license = "Apache-2\.0"$/m);
  assert.match(manifest, /^license-files = \["LICENSE", "NOTICE"\]$/m);
  assert.match(manifest, /^name = "backmarket-seller"$/m);
  assert.match(manifest.match(/^description = .*$/m)[0], /Unofficial.*not affiliated with Back Market/i);
  assert.match(await readFile(join(PYTHON, 'README.md'), 'utf8'), AFFILIATION);
});

test('generated Python carries no upstream prose', async () => {
  const dir = join(PYTHON, 'src/backmarket_seller');
  const entries = await readdir(dir, { recursive: true, withFileTypes: true });
  const offenders = [];
  for (const entry of entries.filter((item) => item.isFile() && item.name.endsWith('.py'))) {
    const path = join(entry.parentPath, entry.name);
    if (path.includes('/api/') || path.includes('/models/')) {
      if (/Field\([^)]*description=|json_schema_extra|back market/i.test(await readFile(path, 'utf8'))) offenders.push(path);
    }
  }
  assert.deepEqual(offenders, []);
});

test('the TypeScript package ships the root licence and notice', async () => {
  for (const name of ['LICENSE', 'NOTICE']) {
    assert.equal(await readFile(join(TYPESCRIPT, name), 'utf8'), await readFile(join(ROOT, name), 'utf8'));
  }
});

test('the TypeScript manifest declares Apache-2.0, says it is unofficial and cannot be published by accident', async () => {
  const manifest = JSON.parse(await readFile(join(TYPESCRIPT, 'package.json'), 'utf8'));
  assert.equal(manifest.name, 'backmarket-seller');
  assert.equal(manifest.license, 'Apache-2.0');
  assert.equal(manifest.private, true);
  assert.deepEqual(manifest.dependencies, undefined);
  for (const name of ['LICENSE', 'NOTICE']) assert.ok(manifest.files.includes(name));
  assert.match(manifest.description, /Unofficial.*not affiliated with Back Market/i);
  assert.match(await readFile(join(TYPESCRIPT, 'README.md'), 'utf8'), AFFILIATION);
});

test('the TypeScript manifest exports ESM and CommonJS builds', async () => {
  const { exports } = JSON.parse(await readFile(join(TYPESCRIPT, 'package.json'), 'utf8'));
  assert.equal(exports['.'].import.default, './dist/esm/index.js');
  assert.equal(exports['.'].require.default, './dist/cjs/index.js');
});

test('generated TypeScript carries no upstream prose', async () => {
  const ours = /^\/\*\* (Iterate every item across all pages\.|[A-Z][^.]*\.( Never retried on failure\.)?) \*\/$/;
  const offenders = [];
  for (const dir of ['src/apis', 'src/models']) {
    for (const name of await readdir(join(TYPESCRIPT, dir))) {
      const text = await readFile(join(TYPESCRIPT, dir, name), 'utf8');
      const comments = text.match(/\/\*\*.*?\*\//gs) ?? [];
      if (/back market/i.test(text) || comments.some((comment) => !ours.test(comment))) offenders.push(name);
    }
  }
  assert.deepEqual(offenders, []);
});
