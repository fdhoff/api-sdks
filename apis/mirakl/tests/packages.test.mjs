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

// Until generate.mjs reads `iterators` from sdk.yaml, each package repeats them.
test('each package pages exactly as sdk.yaml says', () => {
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
  }
});

test("each package names a wait on every job's status operation, and nowhere else", () => {
  const statuses = Object.values(sdk.jobs).map(({ status }) => status).sort();
  for (const { name, operations } of packages) {
    assert.deepEqual(Object.keys(operations).filter((id) => operations[id].wait).sort(), statuses, name);
  }
});

test("each package's summaries end with the operation's API code", () => {
  for (const { name, operations } of packages) {
    const missing = Object.entries(operations).filter(([id, entry]) => !entry.summary?.endsWith(`(${id}).`));
    assert.deepEqual(missing.map(([id]) => id), [], name);
  }
});

const ROOT = new URL('../../../', import.meta.url);
const AFFILIATION = 'Not affiliated with, endorsed by or sponsored by Mirakl SAS.';
const TYPESCRIPT = new URL('packages/typescript/', API);
const unwrapped = async (url) => (await readFile(url, 'utf8')).replace(/\s+/g, ' ');

test('the TypeScript package ships the Apache-2.0 licence and a notice that names Mirakl', async () => {
  assert.equal(await readFile(new URL('LICENSE', TYPESCRIPT), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  const notice = await unwrapped(new URL('NOTICE', TYPESCRIPT));
  assert.match(notice, /not affiliated with, endorsed by or sponsored by Mirakl SAS/);
  assert.match(notice, /grants no right to the Mirakl name/);
});

test('the TypeScript package and README say it is unofficial and not affiliated', async () => {
  const manifest = JSON.parse(await readFile(new URL('package.json', TYPESCRIPT), 'utf8'));
  assert.equal(manifest.name, 'mirakl-seller');
  assert.equal(manifest.license, 'Apache-2.0');
  assert.match(manifest.description, /^Unofficial /);
  assert.ok(manifest.description.includes(AFFILIATION));
  assert.match(manifest.version, /^0\./);
  const index = await unwrapped(new URL('src/index.ts', TYPESCRIPT));
  assert.ok(index.replaceAll(' * ', ' ').includes(AFFILIATION));
  const readme = await unwrapped(new URL('README.md', TYPESCRIPT));
  assert.match(readme, /^# mirakl-seller Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /no public sandbox/);
  assert.match(readme, /Best Buy/);
  assert.match(readme, /0\.x/);
});

test('the TypeScript changelog leaves the first alpha unreleased, so no tag can publish it', async () => {
  const manifest = JSON.parse(await readFile(new URL('package.json', TYPESCRIPT), 'utf8'));
  const changelog = await readFile(new URL('CHANGELOG.md', TYPESCRIPT), 'utf8');
  assert.ok(changelog.includes(`## ${manifest.version} (unreleased)`));
});

const PYTHON = new URL('packages/python/', API);

test('the Python package ships the Apache-2.0 licence and the same notice', async () => {
  assert.equal(await readFile(new URL('LICENSE', PYTHON), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  assert.equal(await readFile(new URL('NOTICE', PYTHON), 'utf8'), await readFile(new URL('NOTICE', TYPESCRIPT), 'utf8'));
});

test('the Python metadata and README say it is unofficial and not affiliated', async () => {
  const manifest = await readFile(new URL('pyproject.toml', PYTHON), 'utf8');
  assert.match(manifest, /^name = "mirakl-seller"$/m);
  const description = manifest.match(/^description = "(.*)"$/m)?.[1];
  assert.match(description, /^Unofficial /);
  assert.ok(description.includes(AFFILIATION));
  const init = await unwrapped(new URL('src/mirakl_seller/__init__.py', PYTHON));
  assert.ok(init.includes(AFFILIATION));
  const readme = await unwrapped(new URL('README.md', PYTHON));
  assert.match(readme, /^# mirakl-seller Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /no public sandbox/);
  assert.match(readme, /Best Buy/);
  assert.match(readme, /mirakl\/sdk-php-shop/);
  assert.match(readme, /0\.x/);
});

test('the Python changelog leaves the first alpha unreleased, so no tag can publish it', async () => {
  const version = (await readFile(new URL('src/mirakl_seller/__init__.py', PYTHON), 'utf8')).match(/^__version__ = "(.*)"$/m)?.[1];
  assert.match(version, /^0\./);
  const changelog = await readFile(new URL('CHANGELOG.md', PYTHON), 'utf8');
  assert.ok(changelog.includes(`## ${version} (unreleased)`));
});

const CSHARP = new URL('packages/csharp/', API);

test('the C# package ships the Apache-2.0 licence and the same notice', async () => {
  assert.equal(await readFile(new URL('LICENSE', CSHARP), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  assert.equal(await readFile(new URL('NOTICE', CSHARP), 'utf8'), await readFile(new URL('NOTICE', TYPESCRIPT), 'utf8'));
});

test('the C# project declares Apache-2.0 and MiraklSeller, and its description starts with Unofficial', async () => {
  const project = await readFile(new URL('src/MiraklSeller/MiraklSeller.csproj', CSHARP), 'utf8');
  assert.match(project, /<PackageLicenseExpression>Apache-2\.0<\/PackageLicenseExpression>/);
  assert.match(project, /<PackageId>MiraklSeller<\/PackageId>/);
  assert.match(project, /<Version>0\./);
  assert.ok(project.includes(`<Description>Unofficial client for the Mirakl seller API. ${AFFILIATION}</Description>`));
  const client = await unwrapped(new URL('src/MiraklSeller/MiraklClient.cs', CSHARP));
  assert.ok(client.replaceAll(' /// ', ' ').includes(AFFILIATION));
});

test('the C# README says it is unofficial and not affiliated', async () => {
  const readme = await unwrapped(new URL('README.md', CSHARP));
  assert.match(readme, /^# MiraklSeller Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /no public sandbox/);
  assert.match(readme, /Best Buy/);
  assert.match(readme, /mirakl\/sdk-php-shop/);
  assert.match(readme, /0\.x/);
});

test('the C# changelog leaves the first alpha unreleased, so no tag can publish it', async () => {
  const project = await readFile(new URL('src/MiraklSeller/MiraklSeller.csproj', CSHARP), 'utf8');
  const version = project.match(/<Version>(.*)<\/Version>/)?.[1];
  const changelog = await readFile(new URL('CHANGELOG.md', CSHARP), 'utf8');
  assert.ok(changelog.includes(`## ${version} (unreleased)`));
});
