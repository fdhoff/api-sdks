import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const RUST = join(ROOT, 'apis/ebay/packages/rust');
const TRADEMARK = 'eBay is a trademark of eBay Inc. This project is not affiliated with, endorsed by or sponsored by eBay Inc.';

const unwrapped = async (path) => (await readFile(path, 'utf8')).replace(/\s+/g, ' ');

const contracts = async () => {
  const config = parse(await readFile(join(RUST, 'generate.yaml'), 'utf8'));
  return Promise.all(
    Object.values(config.contracts).filter((contract) => !contract.omit).map(async (contract) => ({
      module: contract.properties.sdkModule,
      operations: Object.fromEntries(
        Object.entries(parse(await readFile(join(RUST, contract.operations), 'utf8'))).filter(([, names]) => !names.omit),
      ),
    })),
  );
};

test('the Rust crate ships the Apache-2.0 licence and a notice for eBay', async () => {
  assert.equal(await readFile(join(RUST, 'LICENSE'), 'utf8'), await readFile(join(ROOT, 'LICENSE'), 'utf8'));
  const notice = await unwrapped(join(RUST, 'NOTICE'));
  assert.match(notice, /not affiliated with.*eBay/i);
  assert.doesNotMatch(notice, /back ?market|etsy/i);
});

test('the Rust manifest declares Apache-2.0, the approved name, a 0.x version and says it is unofficial', async () => {
  const manifest = await readFile(join(RUST, 'Cargo.toml'), 'utf8');
  assert.match(manifest, /^name = "ebay-sell"$/m);
  assert.match(manifest, /^version = "0\./m);
  assert.match(manifest, /^license = "Apache-2\.0"$/m);
  assert.match(manifest.match(/^description = .*$/m)[0], /Unofficial.*not affiliated with.*eBay/i);
  assert.match(manifest, /^include = .*"\/LICENSE", "\/NOTICE"\]$/m);
});

test('the Rust README carries the trademark notice and the terms users must follow', async () => {
  const readme = await unwrapped(join(RUST, 'README.md'));
  assert.ok(readme.includes(TRADEMARK));
  assert.match(readme, /Marketplace Account Deletion/);
  for (const section of ['§9.10', '§8.1', '§9.5', '§9.6']) assert.ok(readme.includes(section), section);
  assert.match(readme, /6 hours/);
  assert.match(readme, /24 hours/);
  assert.match(readme, /Restricted APIs/);
  assert.match(readme, /EU or UK/);
  assert.match(readme, /0\.x/);
});

test('generated Rust carries no upstream prose', async () => {
  const summaries = new Set();
  for (const { operations } of await contracts()) {
    for (const names of Object.values(operations)) summaries.add(`/// ${names.summary}`);
  }
  const ours = [
    /^\/\/\/$/,
    /^\/\/\/ `None` when the API answers 204 with no body\.$/,
    /^\/\/\/ The [a-z ]+ of \[`\w+::\w+`\]\. Set only what you need\.$/,
    /^\/\/\/ The `[\w-]+` header\. `None` sends the client's default, if it has one\.$/,
    /^\/\/\/ The `\w+` operations, from \[`Resources::\w+`\]\(crate::\w+::Resources::\w+\)\.$/,
    /^\/\/\/ Iterates every item across all pages\. The stream ends after yielding an error\.$/,
    /^\/\/\/ \w+ is an API object\. `extra` holds unknown fields, nulls, and any value that did not fit its field\.$/,
    /^\/\/\/ \w+ is an enumerated value\. A value this version does not list is kept in `Unlisted`\.$/,
  ];
  const offenders = [];
  for (const { module } of await contracts()) {
    for (const dir of ['apis', 'models']) {
      for (const name of await readdir(join(RUST, 'src', module, dir))) {
        const text = await readFile(join(RUST, 'src', module, dir, name), 'utf8');
        const comments = text.split('\n').map((line) => line.trim()).filter((line) => line.startsWith('///'));
        const foreign = comments.filter((line) => !summaries.has(line) && !ours.some((pattern) => pattern.test(line)));
        if (/eBay Inc/i.test(text) || foreign.length > 0) offenders.push(`${module}/${name}: ${foreign[0] ?? 'eBay Inc'}`);
      }
    }
  }
  assert.deepEqual(offenders, []);
});

test('the conformance driver can call every operation and iterator', async () => {
  let operations = 0;
  let iterators = 0;
  for (const contract of await contracts()) {
    const dispatch = await readFile(join(RUST, 'conformance/dispatch', `${contract.module}.rs`), 'utf8');
    const arms = [...dispatch.matchAll(/^\s*\("(\w+)", (true|false)\) =>/gm)].map((match) => `${match[1]} ${match[2]}`);
    const expected = Object.entries(contract.operations).flatMap(([id, names]) => [
      `${id} false`,
      ...(names.iterator ? [`${id} true`] : []),
    ]);
    assert.deepEqual(arms.sort(), expected.sort(), contract.module);
    operations += Object.keys(contract.operations).length;
    iterators += expected.length - Object.keys(contract.operations).length;
  }
  assert.equal(operations, 339);
  assert.equal(iterators, 35);
});
