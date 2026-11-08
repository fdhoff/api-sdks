import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const TYPESCRIPT = join(ROOT, 'apis/etsy/packages/typescript');
const AFFILIATION = /not affiliated with.*Etsy/i;
// Etsy's API terms require this notice wherever the app is described.
const TRADEMARK = "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.";

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

test('the TypeScript package ships the Apache-2.0 licence and a notice for Etsy', async () => {
  assert.equal(await readFile(join(TYPESCRIPT, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(TYPESCRIPT, 'NOTICE'));
  assert.match(notice, AFFILIATION);
  assert.ok(notice.includes(TRADEMARK));
  assert.doesNotMatch(notice, /back ?market/i);
});

test('the TypeScript manifest declares Apache-2.0, the approved name, and says it is unofficial', async () => {
  const manifest = JSON.parse(await readFile(join(TYPESCRIPT, 'package.json'), 'utf8'));
  assert.equal(manifest.name, 'etsy-seller');
  assert.match(manifest.version, /^0\./);
  assert.equal(manifest.license, 'Apache-2.0');
  assert.deepEqual(manifest.dependencies, undefined);
  for (const name of ['LICENSE', 'NOTICE']) assert.ok(manifest.files.includes(name));
  assert.match(manifest.description, /Unofficial.*not affiliated with Etsy/i);
  assert.equal(manifest.exports['.'].import.default, './dist/esm/index.js');
  assert.equal(manifest.exports['.'].require.default, './dist/cjs/index.js');
});

test('the TypeScript README says it is unofficial, carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(TYPESCRIPT, 'README.md'));
  assert.match(readme, AFFILIATION);
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /6 hours/);
  assert.match(readme, /scraping/);
  assert.match(readme, /train AI/);
});

test('generated TypeScript carries no upstream prose', async () => {
  const ours = /^\/\*\* (Iterate every item across all pages\.|[A-Z][^.]*\.) \*\/$/;
  const offenders = [];
  for (const dir of ['src/apis', 'src/models']) {
    for (const name of await readdir(join(TYPESCRIPT, dir))) {
      const text = await readFile(join(TYPESCRIPT, dir, name), 'utf8');
      const comments = text.match(/\/\*\*.*?\*\//gs) ?? [];
      if (/Etsy, Inc/i.test(text) || comments.some((comment) => !ours.test(comment))) offenders.push(name);
    }
  }
  assert.deepEqual(offenders, []);
});
