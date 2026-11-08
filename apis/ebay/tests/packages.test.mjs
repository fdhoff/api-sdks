import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PYTHON = join(ROOT, 'apis/ebay/packages/python');
const TRADEMARK = 'eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.';

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

test('the Python package ships the Apache-2.0 licence and a notice for eBay', async () => {
  assert.equal(await readFile(join(PYTHON, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(PYTHON, 'NOTICE'));
  assert.match(notice, /not affiliated with.*eBay/i);
  assert.doesNotMatch(notice, /back ?market|etsy/i);
});

test('the Python manifest declares Apache-2.0, its name and says it is unofficial', async () => {
  const manifest = await readFile(join(PYTHON, 'pyproject.toml'), 'utf8');
  assert.match(manifest, /^license = "Apache-2\.0"$/m);
  assert.match(manifest, /^license-files = \["LICENSE", "NOTICE"\]$/m);
  assert.match(manifest, /^name = "ebay-sell"$/m);
  assert.match(manifest.match(/^description = .*$/m)[0], /Unofficial.*not affiliated with.*eBay/i);
});

test('the Python README carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(PYTHON, 'README.md'));
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /Marketplace Account Deletion/);
  for (const section of ['§9.10', '§8.1', '§9.5', '§9.6']) assert.ok(readme.includes(section), section);
  assert.match(readme, /6 hours/);
  assert.match(readme, /24 hours/);
  assert.match(readme, /Restricted APIs/);
  assert.match(readme, /EU or UK/);
  assert.match(readme, /0\.x/);
});

test('generated Python carries no upstream prose', async () => {
  const dir = join(PYTHON, 'src/ebay_sell');
  const entries = await readdir(dir, { recursive: true, withFileTypes: true });
  const offenders = [];
  for (const entry of entries.filter((item) => item.isFile() && item.name.endsWith('.py'))) {
    const path = join(entry.parentPath, entry.name);
    if (path.includes('/api/') || path.includes('/models/')) {
      if (/Field\([^)]*description=|json_schema_extra|eBay Inc/i.test(await readFile(path, 'utf8'))) offenders.push(path);
    }
  }
  assert.deepEqual(offenders, []);
});
