import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtemp, readdir, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const WORKFLOWS = join(ROOT, '.github/workflows');
const SPEC_ACTION = './.github/actions/upstream-spec';
const TARGET_ACTION = './.github/actions/release-target';
const RELEASES = { python: 'pypi', typescript: 'npm', csharp: 'nuget', rust: 'crates-io' };

async function workflows() {
  const names = (await readdir(WORKFLOWS)).filter((name) => name.endsWith('.yml'));
  return Promise.all(
    names.map(async (name) => ({ name, workflow: parse(await readFile(join(WORKFLOWS, name), 'utf8')) })),
  );
}

// Runs the release target action's script as a release workflow would, and returns its exit status and outputs.
async function releaseTarget(language, event, tag = '') {
  const action = parse(await readFile(join(ROOT, TARGET_ACTION, 'action.yml'), 'utf8'));
  const dir = await mkdtemp(join(tmpdir(), 'release-target-'));
  try {
    const output = join(dir, 'output');
    const { status } = spawnSync('bash', ['-c', action.runs.steps[0].run], {
      cwd: ROOT,
      env: { ...process.env, LANGUAGE: language, EVENT: event, TAG: tag, GITHUB_OUTPUT: output },
      stdio: 'ignore',
    });
    const lines = (await readFile(output, 'utf8').catch(() => '')).split('\n').filter(Boolean);
    return { status, outputs: Object.fromEntries(lines.map((line) => [line.slice(0, line.indexOf('=')), line.slice(line.indexOf('=') + 1)])) };
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
}

test('only the spec drift job reads the spec from upstream', async () => {
  const offenders = [];
  for (const { name, workflow } of await workflows()) {
    if (name === 'spec-drift.yml') continue;
    for (const [id, job] of Object.entries(workflow.jobs)) {
      const runs = (job.steps ?? []).map((step) => step.run ?? '');
      if (runs.some((run) => /spec:(fetch|pin)|bundled_openapi/.test(run))) offenders.push(`${name} ${id}`);
      const build = runs.findIndex((run) => run.includes('spec:build'));
      if (build === -1) continue;
      const restore = job.steps.findIndex((step) => step.uses === SPEC_ACTION);
      if (restore === -1 || restore > build) offenders.push(`${name} ${id}`);
    }
  }
  assert.deepEqual(offenders, []);
});

test('the spec cache is keyed by the pinned hashes', async () => {
  const action = parse(await readFile(join(ROOT, SPEC_ACTION, 'action.yml'), 'utf8'));
  const cache = 'node toolchain/pipeline/spec-cache.mjs "apis/$API" >> "$GITHUB_OUTPUT"';
  assert.equal(action.runs.steps.find((step) => step.id === 'key').run, cache);
  for (const step of action.runs.steps.filter((item) => item.uses?.startsWith('actions/cache/'))) {
    assert.deepEqual(step.with, { path: '${{ steps.key.outputs.path }}', key: '${{ steps.key.outputs.key }}' });
  }
  const drift = parse(await readFile(join(WORKFLOWS, 'spec-drift.yml'), 'utf8')).jobs.drift.steps;
  assert.equal(drift.find((step) => step.id === 'lock').run, cache);
  const save = drift.find((step) => step.uses?.startsWith('actions/cache/save@'));
  assert.deepEqual(save.with, { path: '${{ steps.lock.outputs.path }}', key: '${{ steps.pin.outputs.key }}' });
});

test('one job per workflow saves the spec cache after a miss', async () => {
  const savers = {};
  for (const { name, workflow } of await workflows()) {
    for (const [id, job] of Object.entries(workflow.jobs)) {
      for (const step of job.steps ?? []) {
        if (step.uses === SPEC_ACTION && step.with?.save === true) (savers[name] ??= []).push(id);
      }
    }
  }
  assert.deepEqual(savers, {
    'ci.yml': ['spec'],
    'release-csharp.yml': ['build'],
    'release-python.yml': ['build'],
    'release-rust.yml': ['build'],
    'release-typescript.yml': ['build'],
  });
});

test('CI runs each language job for every API that has the package', async () => {
  const { jobs } = parse(await readFile(join(WORKFLOWS, 'ci.yml'), 'utf8'));
  const packages = join(ROOT, 'apis/backmarket/packages');
  const languages = [];
  for (const entry of await readdir(packages, { withFileTypes: true })) {
    if (entry.isDirectory() && (await readdir(join(packages, entry.name))).includes('generate.yaml')) languages.push(entry.name);
  }
  assert.ok(languages.length > 0);
  assert.equal(jobs.spec.strategy.matrix.api, '${{ fromJSON(needs.apis.outputs.spec) }}');
  for (const language of languages) {
    assert.equal(jobs.apis.outputs[language], `\${{ steps.find.outputs.${language} }}`);
    assert.equal(jobs[language].strategy.matrix.api, `\${{ fromJSON(needs.apis.outputs.${language}) }}`);
    assert.equal(jobs[language].if, `needs.apis.outputs.${language} != '[]'`);
  }
});

test('crates.io publishes with trusted publishing only', async () => {
  const text = await readFile(join(WORKFLOWS, 'release-rust.yml'), 'utf8');
  assert.doesNotMatch(text, /secrets\.CARGO_REGISTRY_TOKEN/);
});

test('every publish step can be rerun after it succeeded', async () => {
  const publishing = Object.fromEntries(
    (await workflows())
      .filter(({ name }) => name.startsWith('release-'))
      .map(({ name, workflow }) => [name, workflow.jobs.publish.steps]),
  );
  const run = (name, pattern) => publishing[name].find((step) => pattern.test(step.run ?? ''));

  assert.match(run('release-csharp.yml', /dotnet nuget push/).run, /--skip-duplicate/);

  const pypi = publishing['release-python.yml'].find((step) => step.uses?.startsWith('pypa/gh-action-pypi-publish@'));
  assert.equal(pypi.with?.['skip-existing'], true);

  assert.match(run('release-typescript.yml', /npm publish/).run, /npm view [\s\S]*else\s+npm publish/);

  const cargo = run('release-rust.yml', /cargo publish/);
  assert.equal(cargo.if, "steps.published.outputs.skip != 'true'");
  assert.ok(publishing['release-rust.yml'].some((step) => step.id === 'published'));
});

test('each release workflow takes the API from its tag and builds every API on a pull request', async () => {
  for (const [language, environment] of Object.entries(RELEASES)) {
    const workflow = parse(await readFile(join(WORKFLOWS, `release-${language}.yml`), 'utf8'));
    assert.deepEqual(workflow.on.push.tags, [`*/${language}/v*`, `${language}/v*`]);
    assert.ok(workflow.on.pull_request.paths.includes(`apis/*/packages/${language}/CHANGELOG.md`), language);
    assert.ok(workflow.on.pull_request.paths.includes('.github/actions/release-target/**'), language);
    const { target, build, publish } = workflow.jobs;
    assert.deepEqual(target.steps.at(-1), { id: 'target', uses: TARGET_ACTION, with: { language } });
    assert.equal(build.strategy.matrix.include, '${{ fromJSON(needs.target.outputs.matrix) }}');
    assert.equal(publish.environment.name, environment);
    assert.equal(
      publish.if,
      `github.event_name == 'push' && vars.PUBLISH_${language.toUpperCase()} == 'true' && ` +
        "(needs.target.outputs.api == 'backmarket' || vars[needs.target.outputs.gate] == 'true')",
    );
  }
});

test('release tags from before tags named the API still release Back Market', async () => {
  assert.deepEqual((await releaseTarget('python', 'push', 'python/v0.1.0a2')).outputs, {
    api: 'backmarket',
    package: 'backmarket-seller',
    version: '0.1.0a2',
    gate: 'PUBLISH_BACKMARKET_PYTHON',
    matrix: JSON.stringify([{ api: 'backmarket', package: 'backmarket-seller' }]),
  });
  assert.equal((await releaseTarget('csharp', 'push', 'backmarket/csharp/v0.1.0-alpha.2')).outputs.package, 'BackMarketSeller');
});

test('a release tag must name an API that has the package', async () => {
  for (const tag of ['nowhere/python/v1.0.0', '../backmarket/python/v1.0.0', 'backmarket/rust/v1.0.0', 'python-v1.0.0']) {
    assert.notEqual((await releaseTarget('python', 'push', tag)).status, 0, tag);
  }
});

test('a pull request dry-runs every API that has the package', async () => {
  for (const language of Object.keys(RELEASES)) {
    const apis = [];
    for (const api of await readdir(join(ROOT, 'apis'))) {
      if ((await readdir(join(ROOT, 'apis', api, 'packages', language)).catch(() => [])).includes('generate.yaml')) apis.push(api);
    }
    const { status, outputs } = await releaseTarget(language, 'pull_request');
    assert.equal(status, 0);
    assert.deepEqual(JSON.parse(outputs.matrix).map(({ api }) => api).sort(), apis.sort());
    assert.equal(outputs.api, undefined);
  }
});

test('each release workflow smoke tests what it published, installed from the registry', async () => {
  for (const language of Object.keys(RELEASES)) {
    const { jobs } = parse(await readFile(join(WORKFLOWS, `release-${language}.yml`), 'utf8'));
    assert.deepEqual(jobs.published.needs, ['target', 'publish']);
    assert.equal(jobs.published.uses, './.github/workflows/published.yml');
    assert.deepEqual(jobs.published.with, {
      api: '${{ needs.target.outputs.api }}',
      language,
      version: '${{ needs.target.outputs.version }}',
    });
    assert.deepEqual(jobs.published.permissions, { contents: 'read', issues: 'write' });
  }
  const { on, jobs } = parse(await readFile(join(WORKFLOWS, 'published.yml'), 'utf8'));
  assert.deepEqual(Object.keys(on.workflow_call.inputs), ['api', 'language', 'version']);
  assert.deepEqual(on.push.tags, ['apis/*/packages/go/v*']);
  assert.equal(on.schedule.length, 1);
  assert.equal(jobs.smoke.steps.at(-1).if, "failure() && github.event_name != 'pull_request'");
});
