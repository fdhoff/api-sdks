import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';

const API = new URL('../', import.meta.url);
const ROOT = new URL('../../../', import.meta.url);
const CSHARP = new URL('packages/csharp/', API);
const AFFILIATION = 'Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.';
const unwrapped = async (url) => (await readFile(url, 'utf8')).replace(/\s+(\/\/\/ )?/g, ' ');
const sdk = parse(await readFile(new URL('sdk.yaml', API), 'utf8'));
const operations = parse(await readFile(new URL('operations.yaml', CSHARP), 'utf8'));
const project = await readFile(new URL('src/GiteaRest/GiteaRest.csproj', CSHARP), 'utf8');

// C# iterates pages of strings too, so it pages every operation sdk.yaml lists.
test('the C# package pages exactly as sdk.yaml says', () => {
  const iterated = Object.fromEntries(
    Object.entries(operations)
      .filter(([, entry]) => entry.iterator)
      .map(([id, entry]) => [id, { items: entry.paging?.items }]),
  );
  assert.deepEqual(iterated, Object.fromEntries(Object.entries(sdk.iterators).map(([id, { items }]) => [id, { items }])));
});

test("the C# package's methods are async and its iterators list or search all", () => {
  const wrong = Object.entries(operations).filter(
    ([, entry]) => !/^[A-Z][A-Za-z0-9]*Async$/.test(entry.method) || (entry.iterator && !/^(ListAll|SearchAll)[A-Za-z0-9]*Async$/.test(entry.iterator)),
  );
  assert.deepEqual(wrong.map(([id]) => id), []);
});

test('the C# package ships the Apache-2.0 licence and a notice that names Gitea', async () => {
  assert.equal(await readFile(new URL('LICENSE', CSHARP), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  const notice = await unwrapped(new URL('NOTICE', CSHARP));
  assert.match(notice, /not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited/);
  assert.match(notice, /grants no right to the Gitea name/);
});

test('the C# project declares Apache-2.0 and GiteaRest, and its description starts with Unofficial', async () => {
  assert.match(project, /<PackageLicenseExpression>Apache-2\.0<\/PackageLicenseExpression>/);
  assert.match(project, /<PackageId>GiteaRest<\/PackageId>/);
  assert.match(project, /<Version>0\./);
  assert.ok(project.includes(`<Description>Unofficial client for the Gitea API. ${AFFILIATION}</Description>`));
  assert.ok((await unwrapped(new URL('src/GiteaRest/GiteaClient.cs', CSHARP))).includes(AFFILIATION));
});

test('the C# README says it is unofficial and not affiliated, and what it adds', async () => {
  const readme = await unwrapped(new URL('README.md', CSHARP));
  assert.match(readme, /^# GiteaRest Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /Gitea\.Net\.API/);
  assert.match(readme, /code\.gitea\.io\/sdk\/gitea/);
  assert.match(readme, /The client adds `\/api\/v1`/);
  assert.match(readme, /0\.x/);
});

test('the C# README names the pinned Gitea release', async () => {
  const { tag } = JSON.parse(await readFile(new URL('spec/upstream/lock.json', API), 'utf8'));
  assert.ok((await readFile(new URL('README.md', CSHARP), 'utf8')).includes(`pinned Gitea release, ${tag},`));
});

test('the C# changelog leaves the first alpha unreleased, so no tag can publish it', async () => {
  const version = project.match(/<Version>(.*)<\/Version>/)?.[1];
  const changelog = await readFile(new URL('CHANGELOG.md', CSHARP), 'utf8');
  assert.ok(changelog.includes(`## ${version} (unreleased)`));
  assert.doesNotMatch(changelog, /^## \d+\.\d+\.\d+\S* \((?!unreleased)/m);
});
