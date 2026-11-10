import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';

const API = new URL('../', import.meta.url);
const ROOT = new URL('../../../', import.meta.url);
const GO = new URL('packages/go/', API);
const AFFILIATION = 'Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.';
const unwrapped = async (url) => (await readFile(url, 'utf8')).replace(/\s+(\/\/ )?/g, ' ');
const sdk = parse(await readFile(new URL('sdk.yaml', API), 'utf8'));
const operations = parse(await readFile(new URL('operations.yaml', GO), 'utf8'));

// Go iterates pages of strings too, so it pages every operation sdk.yaml lists.
test('the Go package pages exactly as sdk.yaml says', () => {
  const iterated = Object.fromEntries(
    Object.entries(operations)
      .filter(([, entry]) => entry.iterator)
      .map(([id, entry]) => [id, { items: entry.paging?.items }]),
  );
  assert.deepEqual(iterated, Object.fromEntries(Object.entries(sdk.iterators).map(([id, { items }]) => [id, { items }])));
});

test("the Go package's summaries start with the method and end with the operationId", () => {
  const wrong = Object.entries(operations).filter(
    ([id, entry]) => !entry.summary?.startsWith(`${entry.method} `) || !entry.summary.endsWith(`(${id}).`),
  );
  assert.deepEqual(wrong.map(([id]) => id), []);
});

test('the Go package ships the Apache-2.0 licence and a notice that names Gitea', async () => {
  assert.equal(await readFile(new URL('LICENSE', GO), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  const notice = await unwrapped(new URL('NOTICE', GO));
  assert.match(notice, /not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited/);
  assert.match(notice, /grants no right to the Gitea name/);
});

test('the Go module, package docs and README say it is unofficial and not affiliated', async () => {
  const mod = await readFile(new URL('go.mod', GO), 'utf8');
  assert.match(mod, /^module github\.com\/fdhoff\/api-sdks\/apis\/gitea\/packages\/go$/m);
  assert.ok((await unwrapped(new URL('go.mod', GO))).includes(AFFILIATION));
  const doc = await unwrapped(new URL('gitearest/doc.go', GO));
  assert.match(doc, /Package gitearest is an unofficial client/);
  assert.ok(doc.includes(AFFILIATION));
  const readme = await unwrapped(new URL('README.md', GO));
  assert.match(readme, /^# gitearest Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /code\.gitea\.io\/sdk\/gitea/);
  assert.match(readme, /the client adds `\/api\/v1`/);
  assert.match(readme, /0\.x/);
});

test('the Go README names the pinned Gitea release', async () => {
  const { tag } = JSON.parse(await readFile(new URL('spec/upstream/lock.json', API), 'utf8'));
  assert.ok((await readFile(new URL('README.md', GO), 'utf8')).includes(`pinned Gitea release, ${tag},`));
});

test('the Go changelog leaves the first alpha unreleased, so no tag has been made for it', async () => {
  const changelog = await readFile(new URL('CHANGELOG.md', GO), 'utf8');
  assert.match(changelog, /^## 0\.1\.0-alpha\.1 \(unreleased\)$/m);
  assert.doesNotMatch(changelog, /^## \d+\.\d+\.\d+\S* \((?!unreleased)/m);
});
