import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const WORKFLOWS = join(ROOT, '.github/workflows');
const SPEC_ACTION = './.github/actions/upstream-spec';

async function workflows() {
  const names = (await readdir(WORKFLOWS)).filter((name) => name.endsWith('.yml'));
  return Promise.all(
    names.map(async (name) => ({ name, workflow: parse(await readFile(join(WORKFLOWS, name), 'utf8')) })),
  );
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

test('the spec cache is keyed by the pinned hash', async () => {
  const action = parse(await readFile(join(ROOT, SPEC_ACTION, 'action.yml'), 'utf8'));
  assert.match(action.runs.steps.find((step) => step.id === 'key').run, /jq -r \.sha256 .*lock\.json/);
  const drift = parse(await readFile(join(WORKFLOWS, 'spec-drift.yml'), 'utf8')).jobs.drift.steps;
  const save = drift.find((step) => step.uses?.startsWith('actions/cache/save@'));
  assert.equal(save.with.key, 'upstream-spec-${{ steps.pin.outputs.upstream }}');
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
