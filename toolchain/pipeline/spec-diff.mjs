// Summarises which operations and schemas differ between two specs, by name only, without quoting either.
// It compares every source in an API's lock with its old copy: the cached spec file for a single source, or
// a directory of `<name>.yaml` for several.
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { isDeepStrictEqual } from 'node:util';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { stripProse } from './generate.mjs';
import { lockSources, sourcePaths } from './paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch', 'head', 'options', 'trace'];

function operations(spec) {
  const found = new Map();
  for (const [path, item] of Object.entries(spec.paths ?? {})) {
    for (const method of METHODS) {
      if (item[method]) found.set(`${method.toUpperCase()} ${path}`, { parameters: item.parameters, operation: item[method] });
    }
  }
  return found;
}

const schemas = (spec) => new Map(Object.entries(spec.components?.schemas ?? {}));

function compare(before, after) {
  const result = { added: [], removed: [], changed: [], prose: [] };
  for (const name of after.keys()) if (!before.has(name)) result.added.push(name);
  for (const [name, old] of before) {
    if (!after.has(name)) result.removed.push(name);
    else if (!isDeepStrictEqual(stripProse(old), stripProse(after.get(name)))) result.changed.push(name);
    else if (!isDeepStrictEqual(old, after.get(name))) result.prose.push(name);
  }
  for (const list of Object.values(result)) list.sort();
  return result;
}

export function diffSpecs(before, after) {
  return {
    version: [before.info?.version, after.info?.version],
    operations: compare(operations(before), operations(after)),
    schemas: compare(schemas(before), schemas(after)),
  };
}

function section(title, result, depth) {
  const lines = [`${'#'.repeat(depth)} ${title}`, ''];
  const groups = [
    ['Added', result.added],
    ['Removed', result.removed],
    ['Changed', result.changed],
  ];
  for (const [label, names] of groups) {
    if (names.length > 0) lines.push(`${label}:`, '', ...names.map((name) => `* \`${name}\``), '');
  }
  if (result.prose.length > 0) lines.push(`Descriptions or examples only: ${result.prose.length}`, '');
  if (lines.length === 2) lines.push('No changes.', '');
  return lines;
}

export function renderDiff(diff, depth = 3) {
  const [before, after] = diff.version;
  const version = before === after ? `\`info.version\` is unchanged at \`${after}\`.` : `\`info.version\` moved from \`${before}\` to \`${after}\`.`;
  return [version, '', ...section('Operations', diff.operations, depth), ...section('Schemas', diff.schemas, depth)].join('\n');
}

const NO_COPY = 'No copy of the previously pinned spec was cached, so no comparison was possible.';

// One section per contract that changed, after a summary naming them and any that lost operations, since
// removing an operation breaks its callers. `before` is null for a contract with no cached old copy.
export function renderContracts(contracts) {
  const changed = contracts.filter(({ before, after }) => before === null || !isDeepStrictEqual(before, after));
  if (changed.length === 0) return 'No contract changed.';
  const diffs = changed.map((contract) => ({ ...contract, diff: contract.before && diffSpecs(contract.before, contract.after) }));
  const names = (list) => list.map(({ name }) => `\`${name}\``).join(', ');
  const lines = [`Changed contracts: ${names(diffs)}.`, ''];
  const removing = diffs.filter(({ diff }) => diff?.operations.removed.length > 0);
  if (removing.length > 0) lines.push(`**Operations were removed** from ${names(removing)}. Their callers break; check each one before merging.`, '');
  for (const { name, diff } of diffs) lines.push(`### Contract \`${name}\``, '', diff ? renderDiff(diff, 4) : NO_COPY, '');
  return lines.join('\n').trimEnd();
}

async function readSpec(path) {
  try {
    return parse(await readFile(path, 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

async function renderApi(apiDir, pinnedCopy) {
  const sources = lockSources(JSON.parse(await readFile(join(apiDir, 'spec/upstream/lock.json'), 'utf8')));
  const after = async (source) => parse(await readFile(sourcePaths(apiDir, source).spec, 'utf8'));
  if (sources[0].name === null) {
    const before = await readSpec(pinnedCopy);
    return before ? renderDiff(diffSpecs(before, await after(sources[0]))) : NO_COPY;
  }
  const contracts = [];
  for (const source of sources) {
    contracts.push({ name: source.name, before: await readSpec(join(pinnedCopy, `${source.name}.yaml`)), after: await after(source) });
  }
  return renderContracts(contracts);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [apiDir, pinnedCopy] = process.argv.slice(2);
  if (!apiDir || !pinnedCopy) throw new Error('Usage: node spec-diff.mjs <api-dir> <pinned-copy>');
  console.log(await renderApi(apiDir, pinnedCopy));
}
