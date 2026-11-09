import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { LANGUAGES, latestVersion, packages, PROGRAMS, registryUrl, releaseTags, targets } from './targets.mjs';

const ROOT = fileURLToPath(new URL('../../', import.meta.url));
const NO_PROGRAM = () => null;

test('PyPI: the version uploaded last, ignoring yanked files and empty releases', () => {
  const file = (time, yanked = false) => ({ upload_time_iso_8601: time, yanked });
  const body = JSON.stringify({
    releases: {
      '0.1.0a1': [file('2026-01-01T00:00:00Z')],
      '0.1.0a3': [file('2026-03-01T00:00:00Z', true)],
      '0.1.0a2': [file('2026-02-01T00:00:00Z'), file('2026-02-02T00:00:00Z')],
      '0.2.0a1': [],
    },
  });
  assert.equal(latestVersion('python', body), '0.1.0a2');
  assert.equal(latestVersion('python', JSON.stringify({ releases: {} })), null);
});

test('npm: the version published last, whatever its dist-tag', () => {
  const body = JSON.stringify({
    versions: { '0.1.0-alpha.1': {}, '0.1.0-alpha.2': {} },
    time: { created: '2026-01-01T00:00:00Z', modified: '2026-03-01T00:00:00Z', '0.1.0-alpha.2': '2026-02-01T00:00:00Z', '0.1.0-alpha.1': '2026-01-01T00:00:00Z' },
    'dist-tags': { latest: '0.1.0-alpha.1', alpha: '0.1.0-alpha.2' },
  });
  assert.equal(latestVersion('typescript', body), '0.1.0-alpha.2');
});

test('Go: a tagged version, and none for an untagged module', () => {
  assert.equal(latestVersion('go', JSON.stringify({ Version: 'v0.1.0-alpha.1' })), '0.1.0-alpha.1');
  assert.equal(latestVersion('go', JSON.stringify({ Version: 'v0.0.0-20261101000000-0123456789ab' })), null);
});

test('NuGet and crates.io: the last version listed, skipping yanked crates', () => {
  assert.equal(latestVersion('csharp', JSON.stringify({ versions: ['0.1.0-alpha.1', '0.1.0-alpha.2'] })), '0.1.0-alpha.2');
  const index = ['0.1.0-alpha.1', '0.1.0-alpha.2'].map((vers, i) => JSON.stringify({ name: 'example-sdk', vers, yanked: i === 1 }));
  assert.equal(latestVersion('rust', `${index.join('\n')}\n`), '0.1.0-alpha.1');
});

test('registry URLs follow each registry layout', () => {
  assert.equal(registryUrl('rust', 'example-sdk'), 'https://index.crates.io/ex/am/example-sdk');
  assert.equal(registryUrl('rust', 'abc'), 'https://index.crates.io/3/a/abc');
  assert.equal(registryUrl('csharp', 'ExampleSdk'), 'https://api.nuget.org/v3-flatcontainer/examplesdk/index.json');
  assert.equal(registryUrl('go', 'github.com/Example/sdk'), 'https://proxy.golang.org/github.com/!example/sdk/@latest');
});

test('a release names one package at its version, without asking the registry', async () => {
  const [{ api, language }] = await packages(ROOT);
  const never = () => assert.fail('looked up the registry');
  const matrix = await targets(ROOT, { api, language, version: '9.9.9' }, never, () => `${api}/${language}/v9.9.9`);
  assert.equal(matrix.length, 1);
  assert.equal(matrix[0].version, '9.9.9');
  assert.ok(matrix[0].package);
  assert.equal(matrix[0].ref, `${api}/${language}/v9.9.9`);
  assert.equal(matrix[0].best_effort, false);
});

test('a Go module tag names that module', async () => {
  const go = (await packages(ROOT)).find((item) => item.language === 'go');
  const tag = `apis/${go.api}/packages/go/v0.1.0-alpha.3`;
  const matrix = await targets(ROOT, { tag }, () => assert.fail(), () => tag);
  assert.deepEqual(matrix, [
    { api: go.api, language: 'go', package: `github.com/fdhoff/api-sdks/apis/${go.api}/packages/go`, version: '0.1.0-alpha.3', ref: tag, best_effort: false },
  ]);
});

test('otherwise every package at its latest version, leaving out those never published', async () => {
  const all = await packages(ROOT);
  const matrix = await targets(ROOT, {}, async (language) => (language === 'rust' ? null : '1.0.0'), NO_PROGRAM);
  assert.equal(matrix.length, all.filter(({ language }) => language !== 'rust').length);
  const python = await targets(ROOT, { language: 'python' }, async () => '1.0.0', NO_PROGRAM);
  assert.deepEqual(python.map(({ api }) => api), all.filter(({ language }) => language === 'python').map(({ api }) => api));
});

test('a version released before it had a smoke program is checked best effort with this one', async () => {
  const [{ api, language }] = await packages(ROOT);
  const [entry] = await targets(ROOT, { api, language, version: '0.0.1' }, () => assert.fail(), NO_PROGRAM);
  assert.equal(entry.ref, '');
  assert.equal(entry.best_effort, true);
});

test('release tags name the API, except Go modules and tags from before tags did', () => {
  assert.deepEqual(releaseTags('example', 'python', '1.0.0'), ['example/python/v1.0.0', 'python/v1.0.0']);
  assert.deepEqual(releaseTags('example', 'go', '1.0.0'), ['apis/example/packages/go/v1.0.0']);
});

test('a version needs an API that has the package', async () => {
  await assert.rejects(targets(ROOT, { language: 'python', version: '1.0.0' }));
  await assert.rejects(targets(ROOT, { api: 'nowhere', language: 'python', version: '1.0.0' }));
  await assert.rejects(targets(ROOT, { api: 'nowhere', language: 'cobol' }));
});

test('every package has the smoke program smoke.sh runs', async () => {
  const script = await readFile(join(ROOT, 'toolchain/published/smoke.sh'), 'utf8');
  assert.deepEqual(Object.keys(PROGRAMS), LANGUAGES);
  for (const program of Object.values(PROGRAMS)) assert.ok(script.includes(`"$program/${program}"`), program);
  for (const { api, language } of await packages(ROOT)) {
    await access(join(ROOT, 'apis', api, 'packages', language, 'published', PROGRAMS[language]));
  }
});
