import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { access, chmod, mkdir, mkdtemp, readdir, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PACKAGES = join(ROOT, 'apis/backmarket/packages');

test('the spec drift job regenerates every generated package', async () => {
  const workflow = parse(await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8'));
  const regenerate = workflow.jobs.drift.steps.find((step) => step.name === 'Regenerate clients');
  assert.match(regenerate.run, /for config in "\$PACKAGES"\/\*\/generate\.yaml/);
  assert.match(regenerate.run, /npm run "generate:\$language"/);
  const { scripts } = JSON.parse(await readFile(join(ROOT, 'package.json'), 'utf8'));
  const generated = [];
  for (const language of await readdir(PACKAGES)) {
    const hasConfig = await access(join(PACKAGES, language, 'generate.yaml')).then(
      () => true,
      () => false,
    );
    if (hasConfig) generated.push(language);
  }
  assert.ok(generated.length > 0);
  const missing = generated.filter((language) => !scripts[`generate:${language}`]);
  assert.deepEqual(missing, []);
});

test('the spec drift job gives its write token only to the step that pushes', async () => {
  const workflow = parse(await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8'));
  const { drift } = workflow.jobs;
  assert.equal(drift.env?.GH_TOKEN, undefined);
  const checkout = drift.steps.find((step) => step.uses?.startsWith('actions/checkout@'));
  assert.equal(checkout.with['persist-credentials'], false);
  const holders = drift.steps.filter((step) => JSON.stringify(step).includes('secrets.SPEC_DRIFT_TOKEN'));
  assert.deepEqual(
    holders.map((step) => step.name),
    ['Open or update the pull request'],
  );
});

test('the spec drift job proposes the pin even when regeneration fails', async () => {
  const workflow = parse(await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8'));
  const last = workflow.jobs.drift.steps.at(-1);
  assert.equal(last.name, 'Open or update the pull request');
  assert.match(last.if, /!cancelled\(\)/);
});

// Runs a drift step as Actions would, with `gh`, `npm`, `node` and `python` replaced by stubs that record their calls.
async function runStep(name, cwd, env) {
  const workflow = parse(await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8'));
  const step = workflow.jobs.drift.steps.find((item) => item.name === name);
  const stubs = join(cwd, '..', 'stubs');
  const calls = join(cwd, '..', 'calls.log');
  await mkdir(stubs, { recursive: true });
  for (const command of ['gh', 'npm', 'node', 'python']) {
    await writeFile(join(stubs, command), '#!/bin/sh\necho "$(basename "$0") $*" >> "$CALLS"\n');
    await chmod(join(stubs, command), 0o755);
  }
  const script = join(cwd, '..', 'step.sh');
  await writeFile(script, step.run);
  execFileSync('bash', ['--noprofile', '--norc', '-eo', 'pipefail', script], {
    cwd,
    env: { ...process.env, ...env, PATH: `${stubs}:${process.env.PATH}`, CALLS: calls, GIT_CONFIG_GLOBAL: '/dev/null' },
    stdio: 'pipe',
  });
  return readFile(calls, 'utf8').catch(() => '');
}

test('the spec drift job proposes a pin for an API with no packages', async () => {
  const root = await mkdtemp(join(tmpdir(), 'drift-'));
  try {
    const git = (cwd, ...args) => execFileSync('git', args, { cwd, env: { ...process.env, GIT_CONFIG_GLOBAL: '/dev/null' } });
    const origin = join(root, 'origin.git');
    const work = join(root, 'work');
    git(root, 'init', '--quiet', '--bare', origin);
    git(root, 'clone', '--quiet', origin, work);
    const lock = 'apis/example/spec/upstream/lock.json';
    await mkdir(join(work, 'apis/example/spec/upstream'), { recursive: true });
    await writeFile(join(work, lock), '{"sha256": "old"}\n');
    git(work, 'add', '.');
    git(work, '-c', 'user.name=t', '-c', 'user.email=t@example.com', 'commit', '--quiet', '-m', 'pin');
    const base = git(work, 'rev-parse', 'HEAD').toString().trim();
    const env = {
      API: 'example',
      BRANCH: 'spec-drift-example',
      LOCK: lock,
      PACKAGES: 'apis/example/packages',
      UPSTREAM: 'abc',
      RUNNER_TEMP: root,
      OPEN_PR: '',
      HAS_TOKEN: 'true',
      RUN_URL: 'https://example.com/run',
    };

    assert.equal(await runStep('Regenerate clients', work, env), '');
    for (const outcome of ['success', 'failure']) {
      git(work, 'checkout', '--quiet', '--detach', base);
      await writeFile(join(work, lock), `{"sha256": "${outcome}"}\n`);
      await rm(join(root, 'calls.log'), { force: true });
      const calls = await runStep('Open or update the pull request', work, { ...env, BUILD: outcome, JOB: outcome });
      assert.match(calls, /^gh pr create --head spec-drift-example /m);
      const files = git(work, 'show', '--name-only', '--format=', 'origin/spec-drift-example').toString().trim();
      assert.equal(files, lock);
    }
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
