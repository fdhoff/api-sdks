import assert from 'node:assert/strict';
import { access, readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PACKAGES = join(ROOT, 'apis/backmarket/packages');

test('the spec drift job regenerates every generated package', async () => {
  const workflow = await readFile(join(ROOT, '.github/workflows/spec-drift.yml'), 'utf8');
  const generated = [];
  for (const language of await readdir(PACKAGES)) {
    const hasConfig = await access(join(PACKAGES, language, 'generate.yaml')).then(
      () => true,
      () => false,
    );
    if (hasConfig) generated.push(language);
  }
  assert.ok(generated.length > 0);
  const missing = generated.filter((language) => !workflow.includes(`npm run generate:${language}\n`));
  assert.deepEqual(missing, []);
});
