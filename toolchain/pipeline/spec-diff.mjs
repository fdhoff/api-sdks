// Summarises which operations and schemas differ between two specs, by name only, without quoting either.
import { readFile } from 'node:fs/promises';
import { isDeepStrictEqual } from 'node:util';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { stripProse } from './generate.mjs';

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

function section(title, result) {
  const lines = [`### ${title}`, ''];
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

export function renderDiff(diff) {
  const [before, after] = diff.version;
  const version = before === after ? `\`info.version\` is unchanged at \`${after}\`.` : `\`info.version\` moved from \`${before}\` to \`${after}\`.`;
  return [version, '', ...section('Operations', diff.operations), ...section('Schemas', diff.schemas)].join('\n');
}

async function readSpec(path) {
  try {
    return parse(await readFile(path, 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [beforePath, afterPath] = process.argv.slice(2);
  if (!beforePath || !afterPath) throw new Error('Usage: node spec-diff.mjs <before.yaml> <after.yaml>');
  const before = await readSpec(beforePath);
  const after = parse(await readFile(afterPath, 'utf8'));
  console.log(before ? renderDiff(diffSpecs(before, after)) : 'No copy of the previously pinned spec was cached, so no comparison was possible.');
}
