import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join, relative } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const TOOLCHAIN = fileURLToPath(new URL('../../../toolchain', import.meta.url));
const API_SPECIFIC = /back[\s_-]*market|\/ws\//i;

test('toolchain names neither this API nor its endpoints', async () => {
  const entries = await readdir(TOOLCHAIN, { recursive: true, withFileTypes: true });
  const files = entries.filter((entry) => entry.isFile()).map((entry) => join(entry.parentPath, entry.name));
  assert.ok(files.length > 0);
  const offenders = [];
  for (const file of files) {
    const name = relative(TOOLCHAIN, file);
    if (API_SPECIFIC.test(name) || API_SPECIFIC.test(await readFile(file, 'utf8'))) offenders.push(name);
  }
  assert.deepEqual(offenders, []);
});
