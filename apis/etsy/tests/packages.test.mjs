import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PYTHON = join(ROOT, 'apis/etsy/packages/python');
const AFFILIATION = /not affiliated with.*Etsy/i;
// Etsy's API terms require this notice wherever the app is described.
const TRADEMARK = "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.";

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

test('the Python package ships the Apache-2.0 licence and a notice for Etsy', async () => {
  assert.equal(await readFile(join(PYTHON, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(PYTHON, 'NOTICE'));
  assert.match(notice, AFFILIATION);
  assert.ok(notice.includes(TRADEMARK));
  assert.doesNotMatch(notice, /back ?market/i);
});

test('the Python manifest declares Apache-2.0, the approved name and says it is unofficial', async () => {
  const manifest = await readFile(join(PYTHON, 'pyproject.toml'), 'utf8');
  assert.match(manifest, /^license = "Apache-2\.0"$/m);
  assert.match(manifest, /^license-files = \["LICENSE", "NOTICE"\]$/m);
  assert.match(manifest, /^name = "etsy-seller"$/m);
  assert.match(manifest.match(/^description = .*$/m)[0], /Unofficial.*not affiliated with Etsy/i);
});

test('the Python README says it is unofficial, carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(PYTHON, 'README.md'));
  assert.match(readme, AFFILIATION);
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /6 hours/);
  assert.match(readme, /scraping/);
  assert.match(readme, /train AI/);
});

test('generated Python carries no upstream prose', async () => {
  const dir = join(PYTHON, 'src/etsy_seller');
  const entries = await readdir(dir, { recursive: true, withFileTypes: true });
  const offenders = [];
  for (const entry of entries.filter((item) => item.isFile() && item.name.endsWith('.py'))) {
    const path = join(entry.parentPath, entry.name);
    if (path.includes('/api/') || path.includes('/models/')) {
      if (/Field\([^)]*description=|json_schema_extra|Etsy, Inc/i.test(await readFile(path, 'utf8'))) offenders.push(path);
    }
  }
  assert.deepEqual(offenders, []);
});
