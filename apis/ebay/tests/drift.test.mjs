import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { lockSources, sourcePaths } from '../../../toolchain/pipeline/paths.mjs';
import { renderContracts } from '../../../toolchain/pipeline/spec-diff.mjs';

const API_DIR = fileURLToPath(new URL('..', import.meta.url));
const lock = JSON.parse(await readFile(new URL('../spec/upstream/lock.json', import.meta.url), 'utf8'));

test('drift reports a removed eBay operation by contract', async () => {
  const contracts = [];
  for (const source of lockSources(lock)) {
    const before = parse(await readFile(sourcePaths(API_DIR, source).spec, 'utf8'));
    const after = structuredClone(before);
    if (source.name === 'sell_negotiation') delete after.paths[Object.keys(after.paths)[0]];
    contracts.push({ name: source.name, before, after });
  }
  const report = renderContracts(contracts);
  assert.match(report, /^Changed contracts: `sell_negotiation`\./);
  assert.match(report, /\*\*Operations were removed\*\* from `sell_negotiation`/);
});
