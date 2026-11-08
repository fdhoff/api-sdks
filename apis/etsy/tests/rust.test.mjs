import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const RUST = join(ROOT, 'apis/etsy/packages/rust');
const AFFILIATION = /not affiliated with.*Etsy/i;
// Etsy's API terms require this notice wherever the app is described.
const TRADEMARK = "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.";

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

test('the Rust crate ships the Apache-2.0 licence and a notice for Etsy', async () => {
  assert.equal(await readFile(join(RUST, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(RUST, 'NOTICE'));
  assert.match(notice, AFFILIATION);
  assert.ok(notice.includes(TRADEMARK));
  assert.doesNotMatch(notice, /back ?market/i);
});

test('the Rust manifest declares Apache-2.0, the approved name, a 0.x version and says it is unofficial', async () => {
  const manifest = await readFile(join(RUST, 'Cargo.toml'), 'utf8');
  assert.match(manifest, /^name = "etsy-seller"$/m);
  assert.match(manifest, /^version = "0\./m);
  assert.match(manifest, /^license = "Apache-2\.0"$/m);
  assert.match(manifest.match(/^description = .*$/m)[0], /Unofficial.*not affiliated with.*Etsy/i);
  assert.match(manifest, /^include = .*"\/LICENSE", "\/NOTICE"\]$/m);
});

test('the Rust README says it is unofficial, carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(RUST, 'README.md'));
  assert.match(readme, AFFILIATION);
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /6 hours/);
  assert.match(readme, /scraping/);
  assert.match(readme, /train AI/);
});

test('generated Rust carries no upstream prose', async () => {
  const operations = parse(await readFile(join(RUST, 'operations.yaml'), 'utf8'));
  const summaries = new Set(Object.values(operations).map((names) => `/// ${names.summary}`));
  const ours = [
    /^\/\/\/ The [a-z ]+ of \[`\w+::\w+`\]\. Set only what you need\.$/,
    /^\/\/\/ The `\w+` operations, from \[`Client::\w+`\]\(crate::Client::\w+\)\.$/,
    /^\/\/\/ Iterates every item across all pages\. The stream ends after yielding an error\.$/,
    /^\/\/\/ \w+ is an API object\. `extra` holds unknown fields, nulls, and any value that did not fit its field\.$/,
    /^\/\/\/ \w+ is an enumerated value\. A value this version does not list is kept in `Unlisted`\.$/,
  ];
  const offenders = [];
  for (const dir of ['src/apis', 'src/models']) {
    for (const name of await readdir(join(RUST, dir))) {
      const text = await readFile(join(RUST, dir, name), 'utf8');
      const comments = text.split('\n').map((line) => line.trim()).filter((line) => line.startsWith('///'));
      const foreign = comments.filter((line) => !summaries.has(line) && !ours.some((pattern) => pattern.test(line)));
      if (/Etsy, Inc/i.test(text) || foreign.length > 0) offenders.push(`${name}: ${foreign[0] ?? 'Etsy, Inc'}`);
    }
  }
  assert.deepEqual(offenders, []);
});

test('the conformance driver can call every operation and iterator', async () => {
  const operations = parse(await readFile(join(RUST, 'operations.yaml'), 'utf8'));
  const dispatch = await readFile(join(RUST, 'conformance/dispatch.rs'), 'utf8');
  const arms = [...dispatch.matchAll(/^\s*\("(\w+)", (true|false)\) =>/gm)].map((match) => `${match[1]} ${match[2]}`);
  const expected = Object.entries(operations).flatMap(([id, names]) => [`${id} false`, ...(names.iterator ? [`${id} true`] : [])]);
  assert.equal(Object.keys(operations).length, 107);
  assert.equal(expected.length, 107 + 16);
  assert.deepEqual(arms.sort(), expected.sort());
});
