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

// Pages of strings, which the templates cannot iterate yet.
const STRING_PAGES = ['adminUnadoptedList', 'repoListTopics'];

// Until generate.mjs reads `iterators` from sdk.yaml, each package repeats them.
test('each package pages exactly as sdk.yaml says', () => {
  assert.ok(packages.length > 0);
  const expected = Object.fromEntries(Object.entries(sdk.iterators).filter(([id]) => !STRING_PAGES.includes(id)));
  for (const { name, operations } of packages) {
    const iterated = Object.fromEntries(
      Object.entries(operations)
        .filter(([, entry]) => entry.iterator)
        .map(([id, entry]) => [id, { items: entry.paging?.items }]),
    );
    assert.deepEqual(iterated, expected, name);
  }
});

test("each package's summaries end with the operationId", () => {
  for (const { name, operations } of packages) {
    const missing = Object.entries(operations).filter(([id, entry]) => !entry.summary?.endsWith(`(${id}).`));
    assert.deepEqual(missing.map(([id]) => id), [], name);
  }
});

const ROOT = new URL('../../../', import.meta.url);
const AFFILIATION = 'Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited.';
const PYTHON = new URL('packages/python/', API);
const unwrapped = async (url) => (await readFile(url, 'utf8')).replace(/\s+/g, ' ');

test('the Python package ships the Apache-2.0 licence and a notice that names Gitea', async () => {
  assert.equal(await readFile(new URL('LICENSE', PYTHON), 'utf8'), await readFile(new URL('LICENSE', ROOT), 'utf8'));
  const notice = await unwrapped(new URL('NOTICE', PYTHON));
  assert.match(notice, /not affiliated with, endorsed by or sponsored by the Gitea project or Gitea Limited/);
  assert.match(notice, /grants no right to the Gitea name/);
});

test('the Python metadata and README say it is unofficial and not affiliated', async () => {
  const manifest = await readFile(new URL('pyproject.toml', PYTHON), 'utf8');
  assert.match(manifest, /^name = "gitea-rest"$/m);
  const description = manifest.match(/^description = "(.*)"$/m)?.[1];
  assert.match(description, /^Unofficial /);
  assert.ok(description.includes(AFFILIATION));
  const init = await unwrapped(new URL('src/gitea_rest/__init__.py', PYTHON));
  assert.ok(init.includes(AFFILIATION));
  const readme = await unwrapped(new URL('README.md', PYTHON));
  assert.match(readme, /^# gitea-rest Unofficial /);
  assert.ok(readme.includes(AFFILIATION));
  assert.match(readme, /code\.gitea\.io\/sdk\/gitea/);
  assert.match(readme, /giteapy/);
  assert.match(readme, /v28\.3\.0/);
  assert.match(readme, /0\.x/);
});

test('the Python README names the pinned Gitea release', async () => {
  const { tag } = JSON.parse(await readFile(new URL('spec/upstream/lock.json', API), 'utf8'));
  assert.ok((await readFile(new URL('README.md', PYTHON), 'utf8')).includes(`pinned Gitea release, ${tag},`));
});

test('the Python changelog leaves the first alpha unreleased, so no tag can publish it', async () => {
  const version = (await readFile(new URL('src/gitea_rest/__init__.py', PYTHON), 'utf8')).match(/^__version__ = "(.*)"$/m)?.[1];
  assert.match(version, /^0\./);
  const changelog = await readFile(new URL('CHANGELOG.md', PYTHON), 'utf8');
  assert.ok(changelog.includes(`## ${version} (unreleased)`));
});
