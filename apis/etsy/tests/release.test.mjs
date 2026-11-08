import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));

// Runs the release target action's script as a release workflow would, and returns its exit status and outputs.
async function releaseTarget(language, event, tag = '') {
  const action = parse(await readFile(join(ROOT, '.github/actions/release-target/action.yml'), 'utf8'));
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

const PACKAGES = { python: 'etsy-seller', typescript: 'etsy-seller', csharp: 'EtsySeller', rust: 'etsy-seller' };

test('an etsy/<language>/v<version> tag releases the Etsy package behind its own variable', async () => {
  for (const [language, pkg] of Object.entries(PACKAGES)) {
    const { status, outputs } = await releaseTarget(language, 'push', `etsy/${language}/v0.1.0-alpha.1`);
    assert.equal(status, 0, language);
    assert.deepEqual(outputs, {
      api: 'etsy',
      package: pkg,
      version: '0.1.0-alpha.1',
      gate: `PUBLISH_ETSY_${language.toUpperCase()}`,
      matrix: JSON.stringify([{ api: 'etsy', package: pkg }]),
    });
  }
});

test('pull requests dry-run the Etsy packages', async () => {
  for (const [language, pkg] of Object.entries(PACKAGES)) {
    const { outputs } = await releaseTarget(language, 'pull_request');
    assert.ok(JSON.parse(outputs.matrix).some((entry) => entry.api === 'etsy' && entry.package === pkg), language);
  }
});
