import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { chmod, mkdir, mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { checkUpstream, compareTags, newestRelease, newestStable, specUrl, stableTags } from '../spec/check-upstream.mjs';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const lock = JSON.parse(await readFile(new URL('../spec/upstream/lock.json', import.meta.url), 'utf8'));
const listing = (...tags) => async () => tags.map((tag, index) => `${String(index).padStart(40, '0')}\trefs/tags/${tag}`).join('\n');

test('the lock pins a stable tag at its spec URL', () => {
  assert.match(lock.tag, /^v\d+\.\d+\.\d+$/);
  assert.equal(lock.url, specUrl(lock.tag));
  assert.equal(lock.url, 'https://raw.githubusercontent.com/go-gitea/gitea/v28.3.0/templates/swagger/v1-openapi3.generated.json');
});

test('only stable vN.N.N tags count, and the newest is by version, not by order', () => {
  const tags = stableTags(
    ['a\trefs/tags/v1.24.7', 'b\trefs/tags/v28.3.0', 'c\trefs/tags/v28.10.0-rc1', 'd\trefs/tags/v28.10.0', 'e\trefs/tags/v28.9.1^{}', 'f\trefs/tags/1.0.0', ''].join('\n'),
  );
  assert.deepEqual(tags, ['v1.24.7', 'v28.3.0', 'v28.10.0', 'v28.9.1']);
  assert.equal(newestStable(tags), 'v28.10.0');
  assert.equal(newestStable([]), null);
  assert.ok(compareTags('v28.3.0', 'v28.3.1') < 0);
  assert.ok(compareTags('v29.0.0', 'v28.99.99') > 0);
});

test('the newest release gives its spec URL, and no stable tag is an error', async () => {
  assert.deepEqual(await newestRelease(listing('v28.3.0', 'v28.4.0-rc0', 'v28.4.0')), { tag: 'v28.4.0', url: specUrl('v28.4.0') });
  await assert.rejects(newestRelease(listing('v28.4.0-rc0')), /lists no stable vN\.N\.N release tag/);
});

test('the pin is current until a newer stable release exists', async () => {
  assert.deepEqual(await checkUpstream(lock, listing('v1.24.7', lock.tag, 'v99.0.0-rc1')), []);
  const [problem] = await checkUpstream(lock, listing(lock.tag, 'v99.0.0'));
  assert.match(problem, /Gitea v99\.0\.0 is newer than the pinned v28\.3\.0/);
});

test('a lock whose URL or tag disagree, or tags that cannot be listed, are reported', async () => {
  assert.match((await checkUpstream({ ...lock, tag: 'v28.3.0-rc1' }, listing()))[0], /not a stable vN\.N\.N release tag/);
  assert.match((await checkUpstream({ ...lock, tag: 'v28.2.0' }, listing()))[0], /is not the spec URL of tag v28\.2\.0/);
  const problems = await checkUpstream(lock, async () => {
    throw new Error('could not resolve host');
  });
  assert.match(problems[0], /could not be listed: could not resolve host/);
});

const workflow = parse(await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8'));
const compare = workflow.jobs.drift.steps.find((step) => step.id === 'pin');

// Runs the drift job's pin step as Actions would, with `node` answering the upstream URL script and the cache key,
// and `npm` recording its calls.
async function runCompare(t, { script }) {
  const root = await mkdtemp(join(tmpdir(), 'gitea-drift-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  const work = join(root, 'work');
  const stubs = join(root, 'stubs');
  await mkdir(join(work, 'apis/example/spec'), { recursive: true });
  await mkdir(stubs);
  if (script) await writeFile(join(work, 'apis/example/spec/upstream-url.mjs'), '');
  const node = [
    '#!/bin/sh',
    'echo "node $*" >> "$CALLS"',
    'case "$1" in',
    '  */upstream-url.mjs) printf "url=https://spec.invalid/v2.0.0/openapi.json\\ntag=v2.0.0\\n" ;;',
    '  */spec-cache.mjs) echo "key=upstream-spec-new" ;;',
    'esac',
  ].join('\n');
  await writeFile(join(stubs, 'node'), `${node}\n`);
  await writeFile(join(stubs, 'npm'), '#!/bin/sh\necho "npm $*" >> "$CALLS"\n');
  await chmod(join(stubs, 'node'), 0o755);
  await chmod(join(stubs, 'npm'), 0o755);
  await writeFile(join(root, 'step.sh'), compare.run);
  const calls = join(root, 'calls.log');
  execFileSync('bash', ['--noprofile', '--norc', '-eo', 'pipefail', join(root, 'step.sh')], {
    cwd: work,
    env: {
      ...process.env,
      PATH: `${stubs}:${process.env.PATH}`,
      CALLS: calls,
      API: 'example',
      BRANCH: 'spec-drift-example',
      LOCK: 'apis/example/spec/upstream/lock.json',
      OPEN_PR: '',
      PINNED: 'upstream-spec-old',
      CACHED: join(work, 'missing'),
      RUNNER_TEMP: root,
      GITHUB_OUTPUT: join(root, 'output'),
    },
    stdio: 'pipe',
  });
  return { calls: (await readFile(calls, 'utf8')).split('\n').filter(Boolean), output: await readFile(join(root, 'output'), 'utf8') };
}

test("the drift job pins the URL and tag an API's upstream-url.mjs prints", async (t) => {
  const { calls, output } = await runCompare(t, { script: true });
  assert.ok(calls.includes('node apis/example/spec/upstream-url.mjs'));
  assert.ok(calls.includes('npm run spec:pin -- --url https://spec.invalid/v2.0.0/openapi.json --tag v2.0.0'));
  assert.match(output, /^changed=true$/m);
});

test('the drift job re-pins the locked URL for an API without upstream-url.mjs', async (t) => {
  const { calls } = await runCompare(t, { script: false });
  assert.ok(calls.includes('npm run spec:pin'));
  assert.ok(!calls.some((call) => call.includes('upstream-url.mjs') || call.includes('--url')));
});

test('the spec drift workflow runs the upstream check', () => {
  assert.match(workflow.jobs.apis.steps.at(-1).run, /checks=\$\(names apis\/\*\/spec\/check-upstream\.mjs\)/);
  assert.equal(workflow.jobs.upstream.steps.at(-1).run, 'node "apis/$API/spec/check-upstream.mjs"');
});
