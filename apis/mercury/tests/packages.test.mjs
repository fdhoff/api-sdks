import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { parse } from 'yaml';

const API = new URL('../', import.meta.url);
const sdk = parse(await readFile(new URL('sdk.yaml', API), 'utf8'));
const packages = [];
for (const entry of await readdir(new URL('packages/', API), { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const text = await readFile(new URL(`packages/${entry.name}/operations.yaml`, API), 'utf8').catch(() => null);
  if (text) packages.push({ name: entry.name, operations: parse(text) });
}

// Until generate.mjs reads `iterators` and `idempotency` from sdk.yaml, each package repeats them.
test('each package pages and retries exactly as sdk.yaml says', () => {
  assert.ok(packages.length > 0);
  for (const { name, operations } of packages) {
    const iterated = Object.fromEntries(
      Object.entries(operations)
        .filter(([, entry]) => entry.iterator)
        .map(([id, entry]) => {
          const { style, ...rest } = entry.paging ?? {};
          return [id, style ? { items: rest.items, paging: { style, ...rest, items: undefined } } : { items: rest.items }];
        }),
    );
    const expected = Object.fromEntries(
      Object.entries(sdk.iterators).map(([id, { items, paging }]) => [id, paging ? { items, paging: { ...paging, items: undefined } } : { items }]),
    );
    assert.deepEqual(iterated, expected, name);
    const idempotent = Object.fromEntries(Object.entries(operations).filter(([, entry]) => entry.idempotency).map(([id, entry]) => [id, entry.idempotency]));
    assert.deepEqual(idempotent, sdk.idempotency, name);
  }
});
