import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';

const API = new URL('../', import.meta.url);
const sdk = parse(await readFile(new URL('sdk.yaml', API), 'utf8'));
const packages = [];
for (const entry of await readdir(new URL('packages/', API), { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const text = await readFile(new URL(`packages/${entry.name}/operations.yaml`, API), 'utf8').catch(() => null);
  if (text) packages.push({ name: entry.name, operations: parse(text) });
}

// Until generate.mjs reads `iterators` and `idempotency` from sdk.yaml, each package repeats them.
test('each package pages and retries exactly as sdk.yaml says', () => {
  assert.ok(packages.length > 0);
  for (const { name, operations } of packages) {
    const iterated = Object.fromEntries(
      Object.entries(operations)
        .filter(([, entry]) => entry.iterator)
        .map(([id, entry]) => {
          const { style, ...rest } = entry.paging ?? {};
          return [id, style ? { items: rest.items, paging: { style, ...rest, items: undefined } } : { items: rest.items }];
        }),
    );
    const expected = Object.fromEntries(
      Object.entries(sdk.iterators).map(([id, { items, paging }]) => [id, paging ? { items, paging: { ...paging, items: undefined } } : { items }]),
    );
    assert.deepEqual(iterated, expected, name);
    const idempotent = Object.fromEntries(Object.entries(operations).filter(([, entry]) => entry.idempotency).map(([id, entry]) => [id, entry.idempotency]));
    assert.deepEqual(idempotent, sdk.idempotency, name);
  }
});

const ROOT = new URL('../../../', import.meta.url);
const GO = new URL('packages/go/', API);
const AFFILIATION = 'Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc.';
const unwrapped = async (url) => (await readFile(url, 'utf8')).replace(/\s+/g, ' ');

test('the Go module ships the Apache-2.0 licence and the Python notice', async () => {
  assert.equal(await readFile(new URL('LICENSE', GO), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  assert.equal(await readFile(new URL('NOTICE', GO), 'utf8'), await readFile(new URL('packages/python/NOTICE', API), 'utf8'));
});

test('the Go manifest, package doc and README say it is unofficial and not affiliated', async () => {
  const manifest = await readFile(new URL('go.mod', GO), 'utf8');
  assert.match(manifest, /^\/\/ SPDX-License-Identifier: Apache-2\.0$/m);
  assert.ok(manifest.includes(`// Unofficial client for the Mercury API. ${AFFILIATION}`));
  assert.match(manifest, /^module github\.com\/fdhoff\/api-sdks\/apis\/mercury\/packages\/go$/m);
  const doc = (await unwrapped(new URL('mercurybanking/doc.go', GO))).replaceAll(' // ', ' ');
  assert.match(doc, /^\/\/ Package mercurybanking is an unofficial client/);
  const readme = await unwrapped(new URL('README.md', GO));
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /not a bank/);
  assert.match(readme, /How this differs from Mercury's Go SDK/);
  assert.match(readme, /0\.x/);
});

const CSHARP = new URL('packages/csharp/', API);

test('the C# package ships the Apache-2.0 licence and the Python notice', async () => {
  assert.equal(await readFile(new URL('LICENSE', CSHARP), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  assert.equal(await readFile(new URL('NOTICE', CSHARP), 'utf8'), await readFile(new URL('packages/python/NOTICE', API), 'utf8'));
});

test('the C# project declares Apache-2.0 and MercuryBanking, and its description starts with Unofficial', async () => {
  const project = await readFile(new URL('src/MercuryBanking/MercuryBanking.csproj', CSHARP), 'utf8');
  assert.match(project, /<PackageLicenseExpression>Apache-2\.0<\/PackageLicenseExpression>/);
  assert.match(project, /<PackageId>MercuryBanking<\/PackageId>/);
  assert.ok(project.includes(`<Description>Unofficial client for the Mercury API. ${AFFILIATION}</Description>`));
});

test('the C# README says it is unofficial, not affiliated and that Mercury is not a bank', async () => {
  const readme = await unwrapped(new URL('README.md', CSHARP));
  assert.match(readme, /^# MercuryBanking Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /not a bank/);
  assert.match(readme, /0\.x/);
});

const TYPESCRIPT = new URL('packages/typescript/', API);

test('the TypeScript package ships the Apache-2.0 licence and the Python notice', async () => {
  assert.equal(await readFile(new URL('LICENSE', TYPESCRIPT), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  assert.equal(await readFile(new URL('NOTICE', TYPESCRIPT), 'utf8'), await readFile(new URL('packages/python/NOTICE', API), 'utf8'));
});

test('the TypeScript package and README say it is unofficial and not affiliated', async () => {
  const manifest = JSON.parse(await readFile(new URL('package.json', TYPESCRIPT), 'utf8'));
  assert.equal(manifest.name, 'mercury-banking');
  assert.equal(manifest.license, 'Apache-2.0');
  assert.match(manifest.description, /^Unofficial /);
  assert.ok(manifest.description.includes(AFFILIATION));
  assert.match(manifest.version, /^0\./);
  const index = await unwrapped(new URL('src/index.ts', TYPESCRIPT));
  assert.ok(index.replaceAll(' * ', ' ').includes(AFFILIATION));
  const readme = await unwrapped(new URL('README.md', TYPESCRIPT));
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /not a bank/);
  assert.match(readme, /0\.x/);
});
