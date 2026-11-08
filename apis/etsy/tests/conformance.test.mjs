import assert from 'node:assert/strict';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { runSuite } from '../../../toolchain/conformance/run.mjs';

const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const DRIVER = fileURLToPath(new URL('../conformance/reference-driver.mjs', import.meta.url));

test('the reference driver passes every case', { timeout: 120_000 }, async () => {
  const { total, failed } = await runSuite({ apiDir: API_DIR, driverCommand: `node ${DRIVER}` });
  assert.ok(total > 0);
  assert.deepEqual(failed, []);
});
