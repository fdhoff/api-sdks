import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { loadCases, operationIds } from '../../../toolchain/conformance/cases.mjs';
import { runSuite } from '../../../toolchain/conformance/run.mjs';
import { apiPaths } from '../../../toolchain/pipeline/paths.mjs';

const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const DRIVER = fileURLToPath(new URL('../conformance/reference-driver.mjs', import.meta.url));

test('the reference driver passes every case', { timeout: 120_000 }, async () => {
  const { total, failed } = await runSuite({ apiDir: API_DIR, driverCommand: `node ${DRIVER}` });
  assert.ok(total > 0);
  assert.deepEqual(failed, []);
});

test('every operation has a case', async () => {
  const spec = parse(await readFile(apiPaths(API_DIR).build, 'utf8'));
  const cases = await loadCases(join(API_DIR, 'conformance/cases'), operationIds(spec));
  const covered = new Set(cases.map((item) => item.request.operation));
  assert.deepEqual([...operationIds(spec)].filter((id) => !covered.has(id)), []);
});
