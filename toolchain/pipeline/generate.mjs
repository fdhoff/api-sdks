// Generates one language's client into <api-dir>/packages/<language>/ from the built spec.
// That directory's generate.yaml and operations.yaml hold everything specific to the API.
import { spawnSync } from 'node:child_process';
import { copyFile, cp, mkdir, mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse, stringify } from 'yaml';
import { sha256 } from './fetch-spec.mjs';
import { apiPaths } from './paths.mjs';

const TOOLCHAIN = fileURLToPath(new URL('..', import.meta.url));
const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
const PROSE = new Set(['description', 'summary', 'example', 'examples', 'externalDocs']);

// The upstream spec is not redistributed, so its prose and examples must not reach generated code.
// Only `properties` maps hold user-chosen keys that can collide with those names.
export function stripProse(node, keys = false) {
  if (Array.isArray(node)) return node.map((item) => stripProse(item));
  if (node === null || typeof node !== 'object') return node;
  const kept = Object.entries(node)
    .filter(([key]) => keys || !PROSE.has(key))
    .map(([key, value]) => [key, stripProse(value, !keys && key === 'properties')]);
  return Object.fromEntries(kept);
}

// Generators fold case and reserved words differently, so colliding schemas are renamed before they run.
export function renameSchemas(spec, names = {}) {
  const schemas = {};
  for (const [name, schema] of Object.entries(spec.components.schemas)) schemas[names[name] ?? name] = schema;
  spec.components.schemas = schemas;
  const missing = Object.keys(names).filter((name) => !(names[name] in schemas));
  if (missing.length > 0) throw new Error(`schema_names has unknown schemas: ${missing.join(', ')}`);
  const rewrite = (node) => {
    if (node === null || typeof node !== 'object') return;
    const ref = typeof node.$ref === 'string' ? node.$ref.match(/^#\/components\/schemas\/(.+)$/) : null;
    if (ref && names[ref[1]]) node.$ref = `#/components/schemas/${names[ref[1]]}`;
    Object.values(node).forEach(rewrite);
  };
  rewrite(spec);
  return spec;
}

function dereference(spec, node) {
  return node?.$ref ? dereference(spec, node.$ref.split('/').slice(1).reduce((parent, key) => parent[key], spec)) : node;
}

function requiredProperties(spec, node) {
  const schema = dereference(spec, node);
  return [...(schema?.required ?? []), ...(schema?.allOf ?? []).flatMap((part) => requiredProperties(spec, part))];
}

// True when a query or form parameter must be passed, for templates that gather those into one argument.
function paramsRequired(spec, parameters, operation) {
  const query = parameters.map((parameter) => dereference(spec, parameter));
  const form = dereference(spec, operation.requestBody)?.content?.['multipart/form-data']?.schema;
  return query.some((parameter) => parameter.in === 'query' && parameter.required) || requiredProperties(spec, form).length > 0;
}

export function applyOperations(spec, operations) {
  const unused = new Set(Object.keys(operations));
  for (const item of Object.values(spec.paths)) {
    const shared = item.parameters ?? [];
    for (const operation of METHODS.map((method) => item[method]).filter(Boolean)) {
      const names = operations[operation.operationId];
      if (!names) throw new Error(`operations.yaml does not name ${operation.operationId}`);
      unused.delete(operation.operationId);
      operation.tags = [names.resource];
      operation['x-sdk-method'] = names.method;
      operation['x-sdk-summary'] = names.summary;
      operation['x-sdk-resource'] = names.resource;
      operation['x-sdk-params-required'] = paramsRequired(spec, [...shared, ...(operation.parameters ?? [])], operation);
      if (names.iterator) {
        operation['x-sdk-iterator'] = names.iterator;
        operation['x-sdk-items'] = names.items;
      }
      for (const parameter of [...shared, ...(operation.parameters ?? [])]) {
        if (names.string_params?.includes(parameter.name)) parameter.schema = { type: 'string' };
      }
    }
  }
  if (unused.size > 0) throw new Error(`operations.yaml names unknown operations: ${[...unused].join(', ')}`);
  return spec;
}

async function exists(path) {
  return stat(path).then(
    () => true,
    () => false,
  );
}

async function ensureGenerator(cacheDir) {
  const lock = JSON.parse(await readFile(join(TOOLCHAIN, 'generator/lock.json'), 'utf8'));
  const jar = join(cacheDir, `openapi-generator-${lock.version}.jar`);
  if (await exists(jar)) {
    if (sha256(await readFile(jar)) === lock.sha256) return jar;
    await rm(jar);
  }
  const response = await fetch(lock.url);
  if (!response.ok) throw new Error(`GET ${lock.url}: HTTP ${response.status}`);
  const bytes = Buffer.from(await response.arrayBuffer());
  if (sha256(bytes) !== lock.sha256) throw new Error(`Generator from ${lock.url} does not match its lock`);
  await mkdir(cacheDir, { recursive: true });
  await writeFile(jar, bytes);
  return jar;
}

function run(command, args, options = {}) {
  const { status } = spawnSync(command, args, { stdio: 'inherit', ...options });
  if (status !== 0) throw new Error(`${command} exited with ${status}`);
}

const pairs = (mapping = {}) =>
  Object.entries(mapping)
    .map(([key, value]) => `${key}=${value}`)
    .join(',');

async function generate(apiDir, language) {
  const paths = apiPaths(apiDir);
  const packageDir = resolve(apiDir, 'packages', language);
  const config = parse(await readFile(join(packageDir, 'generate.yaml'), 'utf8'));
  const operations = parse(await readFile(join(packageDir, 'operations.yaml'), 'utf8'));
  const output = join(packageDir, config.output);
  const source = config.source ?? config.properties.packageName.replaceAll('.', '/');

  const built = stripProse(parse(await readFile(paths.build, 'utf8')));
  const spec = applyOperations(renameSchemas(built, config.schema_names), operations);
  const work = await mkdtemp(join(tmpdir(), 'generate-'));
  try {
    const input = join(work, 'openapi.yaml');
    const generatorConfig = join(work, 'config.json');
    await writeFile(input, stringify(spec, { lineWidth: 0, compat: 'yaml-1.1' }));
    await writeFile(
      generatorConfig,
      JSON.stringify({ files: { 'resources.mustache': { templateType: 'SupportingFiles', destinationFilename: join(source, config.resources) } } }),
    );
    run('java', [
      '-jar', await ensureGenerator(dirname(paths.build)),
      'generate', '--generator-name', config.generator, '--skip-validate-spec',
      '--input-spec', input,
      '--output', join(work, 'out'),
      '--config', generatorConfig,
      '--template-dir', join(TOOLCHAIN, 'generator', language),
      '--global-property', 'apiTests=false,modelTests=false,apiDocs=false,modelDocs=false',
      '--additional-properties', pairs(config.properties),
      '--inline-schema-name-mappings', pairs(config.inline_schema_names),
    ], { stdio: ['ignore', 'ignore', 'inherit'] });

    await mkdir(output, { recursive: true });
    for (const dir of config.generated) {
      await rm(join(output, dir), { recursive: true, force: true });
      await cp(join(work, 'out', source, dir), join(output, dir), { recursive: true });
    }
    await copyFile(join(work, 'out', source, config.resources), join(output, config.resources));
  } finally {
    await rm(work, { recursive: true, force: true });
  }
  await rm(join(output, config.runtime), { recursive: true, force: true });
  await cp(join(TOOLCHAIN, 'runtime', language), join(output, config.runtime), { recursive: true });
  run(config.format[0], [...config.format.slice(1), config.output], { cwd: packageDir });
  console.log(`Generated ${output}`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [apiDir, language] = process.argv.slice(2);
  if (!apiDir || !language) throw new Error('Usage: node generate.mjs <api-dir> <language>');
  await generate(apiDir, language);
}
