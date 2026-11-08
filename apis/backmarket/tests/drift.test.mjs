import assert from 'node:assert/strict';
import { access, readdir, readFile } from 'node:fs/promises';
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
