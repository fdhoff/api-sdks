import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const CSHARP = join(ROOT, 'apis/etsy/packages/csharp');
const AFFILIATION = /not affiliated with.*Etsy/i;
// Etsy's API terms require this notice wherever the app is described.
const TRADEMARK = "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.";

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

test('the C# package ships the Apache-2.0 licence and a notice for Etsy', async () => {
  assert.equal(await readFile(join(CSHARP, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(CSHARP, 'NOTICE'));
  assert.match(notice, AFFILIATION);
  assert.ok(notice.includes(TRADEMARK));
  assert.doesNotMatch(notice, /back ?market/i);
});

test('the C# manifest declares Apache-2.0, the approved name, and says it is unofficial', async () => {
  const manifest = await readFile(join(CSHARP, 'src/EtsySeller/EtsySeller.csproj'), 'utf8');
  assert.match(manifest, /<PackageLicenseExpression>Apache-2\.0<\/PackageLicenseExpression>/);
  assert.match(manifest, /<PackageId>EtsySeller<\/PackageId>/);
  assert.match(manifest, /<Version>0\.[^<]*<\/Version>/);
  assert.match(manifest.match(/<Description>.*<\/Description>/)[0], /Unofficial.*not affiliated with Etsy/i);
  for (const name of ['LICENSE', 'NOTICE', 'README.md']) assert.match(manifest, new RegExp(`\\.\\./\\.\\./${name.replace('.', '\\.')}`));
  assert.doesNotMatch(manifest, /back ?market/i);
});

test('the C# README says it is unofficial, carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(CSHARP, 'README.md'));
  assert.match(readme, AFFILIATION);
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /6 hours/);
  assert.match(readme, /scraping/);
  assert.match(readme, /train AI/);
});

test('generated C# carries no upstream prose', async () => {
  const ours = await readFile(join(CSHARP, 'operations.yaml'), 'utf8');
  const templates = join(ROOT, 'toolchain/generator/csharp');
  const corpus = [ours, ...(await Promise.all((await readdir(templates)).map((name) => readFile(join(templates, name), 'utf8'))))].join('\n');
  const offenders = [];
  for (const sub of ['Api', 'Models']) {
    const dir = join(CSHARP, 'src/EtsySeller', sub);
    for (const name of await readdir(dir)) {
      const text = await readFile(join(dir, name), 'utf8');
      const summaries = [...text.matchAll(/<summary>(.*?)<\/summary>/g)].map((match) => match[1]);
      const foreign = summaries.filter((summary) => !corpus.includes(summary) && !/^The \w+ operations\.$/.test(summary));
      if (/Etsy, Inc/i.test(text) || foreign.length > 0) offenders.push(`${sub}/${name}`);
    }
  }
  assert.deepEqual(offenders, []);
});
