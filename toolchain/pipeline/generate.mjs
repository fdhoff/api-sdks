// Generates one language's client into <api-dir>/packages/<language>/ from the built spec.
// That directory's generate.yaml and operations.yaml hold everything specific to the API.
import { spawnSync } from 'node:child_process';
import { copyFile, cp, mkdir, mkdtemp, readdir, readFile, rm, stat, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse, stringify } from 'yaml';
import { sha256 } from './fetch-spec.mjs';
import { apiPaths } from './paths.mjs';

const TOOLCHAIN = fileURLToPath(new URL('..', import.meta.url));
const METHODS = ['get', 'put', 'post', 'delete', 'patch'];
// Optional maps in generate.yaml, and the generator flag each one sets.
const MAPPINGS = {
  type_mappings: '--type-mappings',
  name_mappings: '--name-mappings',
  parameter_name_mappings: '--parameter-name-mappings',
  enum_name_mappings: '--enum-name-mappings',
  schema_mappings: '--schema-mappings',
};
const UNIONS = ['anyOf', 'oneOf'];
const NAME_MAPS = ['schema_names', 'inline_schema_names'];
const PROSE = new Set(['description', 'summary', 'example', 'examples', 'externalDocs']);
// Runtimes in languages without relative imports write their package name as this.
const PACKAGE_PLACEHOLDER = 'PackageNamespace';
// How an iterator walks pages, and the defaults for each style. `next_link` reads the position out of a
// link in each page. `offset` advances an offset query parameter by the number of items received.
const PAGING = {
  next_link: { items: 'results', link: 'next', params: ['page', 'cursor'] },
  offset: { items: 'results', total: 'count', offset: 'offset' },
};

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

// application/json or a +json suffix such as application/problem+json. A wildcard or a stream such as
// application/x-ndjson is not one JSON document.
export function isJsonMediaType(type) {
  const essence = type.split(';')[0].trim().toLowerCase();
  return essence === 'application/json' || /^[a-z0-9.+-]+\/[a-z0-9.+-]+\+json$/.test(essence);
}

// True when a success response declares a JSON body, so an empty one cannot be a result.
export function returnsJson(spec, operation) {
  return Object.entries(operation.responses ?? {}).some(
    ([status, response]) => status.startsWith('2') && Object.keys(dereference(spec, response)?.content ?? {}).some(isJsonMediaType),
  );
}

// Every package shares one set of schema names, so a model has the same name in every language. A
// package may add names for schemas only it sees, but never rename a shared one.
export function packageNames(shared, config) {
  const names = {};
  for (const key of NAME_MAPS) {
    const own = config[key] ?? {};
    const renamed = Object.keys(own).filter((name) => name in (shared?.[key] ?? {}));
    if (renamed.length > 0) throw new Error(`${key} renames shared names: ${renamed.join(', ')}`);
    names[key] = { ...shared?.[key], ...own };
  }
  return names;
}

// An operation's `paging` in operations.yaml overrides the API's default, which overrides the style's.
export function resolvePaging(operationId, queryParams, override = {}, fallback = {}) {
  const style = override.style ?? fallback.style ?? 'next_link';
  const defaults = PAGING[style];
  if (!defaults) throw new Error(`${operationId}: unknown paging style ${style}`);
  const inherited = (fallback.style ?? 'next_link') === style ? fallback : {};
  const paging = { ...defaults, ...inherited, ...override };
  delete paging.style;
  const unknown = Object.keys(paging).filter((key) => !(key in defaults));
  if (unknown.length > 0) throw new Error(`${operationId}: unknown ${style} paging keys: ${unknown.join(', ')}`);
  const positions = style === 'offset' ? [paging.offset] : paging.params;
  if (!positions.some((name) => queryParams.includes(name))) {
    throw new Error(`${operationId}: no query parameter holds the ${style} paging position (${positions.join(', ')})`);
  }
  return { [style]: paging };
}

// The requirements an operation's request must meet: any one of them, each naming its schemes and their scopes.
// An operation without its own `security` inherits the spec's, and an empty list means none.
export function securityOf(spec, operation) {
  return (operation.security ?? spec.security ?? []).map((requirement) => ({
    schemes: Object.entries(requirement).map(([scheme, scopes]) => ({ scheme, scopes: scopes ?? [] })),
  }));
}

export function applyOperations(spec, operations, paging = {}) {
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
      operation['x-sdk-returns-json'] = returnsJson(spec, operation);
      operation['x-sdk-security'] = securityOf(spec, operation);
      if (names.iterator) {
        const parameters = [...shared, ...(operation.parameters ?? [])].map((parameter) => dereference(spec, parameter));
        const queryParams = parameters.filter((parameter) => parameter.in === 'query').map((parameter) => parameter.name);
        operation['x-sdk-iterator'] = names.iterator;
        operation['x-sdk-items'] = names.items;
        operation['x-sdk-paging'] = resolvePaging(operation.operationId, queryParams, names.paging, paging);
      } else if (names.paging) {
        throw new Error(`${operation.operationId}: paging is set but there is no iterator`);
      }
      for (const parameter of [...shared, ...(operation.parameters ?? [])]) {
        if (names.string_params?.includes(parameter.name)) parameter.schema = { type: 'string' };
      }
    }
  }
  if (unused.size > 0) throw new Error(`operations.yaml names unknown operations: ${[...unused].join(', ')}`);
  return spec;
}

const isNullMarker = (node) => node?.nullable === true && Object.keys(node).length === 1;

// For generators whose nullable types do not suit their templates. `properties` maps hold user-chosen keys.
// A union of null and one other schema collapses to that schema.
export function dropNullable(node, keys = false) {
  if (Array.isArray(node)) return node.map((item) => dropNullable(item));
  if (node === null || typeof node !== 'object') return node;
  const kept = {};
  for (const [key, value] of Object.entries(node)) {
    if (!keys && key === 'nullable') continue;
    if (!keys && key === 'enum') kept[key] = value.filter((item) => item !== null);
    else if (!keys && UNIONS.includes(key)) {
      const branches = dropNullable(value.filter((item) => !isNullMarker(item)));
      if (branches.length === 1) Object.assign(kept, branches[0]);
      else kept[key] = branches;
    } else kept[key] = dropNullable(value, !keys && key === 'properties');
  }
  return kept;
}

const isUnion = (node) => UNIONS.some((key) => Array.isArray(node[key]));

// For languages with no union types, where a value of several types is simplest left untyped.
export function dropUnions(spec) {
  const schemas = spec.components.schemas;
  const unions = new Set(Object.keys(schemas).filter((name) => isUnion(schemas[name])));
  const rewrite = (node) => {
    if (Array.isArray(node)) return node.map(rewrite);
    if (node === null || typeof node !== 'object') return node;
    const ref = typeof node.$ref === 'string' ? node.$ref.match(/^#\/components\/schemas\/(.+)$/)?.[1] : undefined;
    if (isUnion(node) || unions.has(ref)) return {};
    return Object.fromEntries(Object.entries(node).map(([key, value]) => [key, rewrite(value)]));
  };
  const rewritten = rewrite(spec);
  for (const name of unions) delete rewritten.components.schemas[name];
  return rewritten;
}

// A union of one schema, with nothing beside it, is that schema. Generators otherwise emit a wrapper or
// alias for it, and an alias that refers back to its own schema can lose its import.
export function collapseSingleUnions(node, keys = false) {
  if (Array.isArray(node)) return node.map((item) => collapseSingleUnions(item));
  if (node === null || typeof node !== 'object') return node;
  const entries = Object.entries(node);
  if (!keys && entries.length === 1 && UNIONS.includes(entries[0][0]) && entries[0][1].length === 1) {
    return collapseSingleUnions(entries[0][1][0]);
  }
  return Object.fromEntries(entries.map(([key, value]) => [key, collapseSingleUnions(value, !keys && key === 'properties')]));
}

// Null-plus-one and single-branch unions collapse first, so only real unions are left untyped.
export function relax(spec, config) {
  const single = config.collapse_single_unions ? collapseSingleUnions(spec) : spec;
  const collapsed = config.drop_nullable ? dropNullable(single) : single;
  return config.drop_unions ? dropUnions(collapsed) : collapsed;
}

export async function fillPackageName(dir, name) {
  for (const entry of await readdir(dir, { recursive: true, withFileTypes: true })) {
    if (!entry.isFile()) continue;
    const path = join(entry.parentPath, entry.name);
    await writeFile(path, (await readFile(path, 'utf8')).replaceAll(PACKAGE_PLACEHOLDER, name));
  }
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

const hasPrefix = (name, prefixes = []) => prefixes.some((prefix) => name.startsWith(prefix));

// The resources file, plus extra templates such as a test driver's dispatch table. Each extra is generated
// under supporting/ and then copied to its path relative to the package.
export function supportingFiles(config, source) {
  const files = { 'resources.mustache': { templateType: 'SupportingFiles', destinationFilename: join(source, config.resources) } };
  for (const template of Object.keys(config.supporting_files ?? {})) {
    files[template] = { templateType: 'SupportingFiles', destinationFilename: join('supporting', template) };
  }
  return files;
}

// Generator files the package does not use, as paths relative to the generator's output.
export const ignoreFile = (config) => (config.ignore ?? []).map((path) => `${path}\n`).join('');

const pairs = (mapping = {}) =>
  Object.entries(mapping)
    .map(([key, value]) => `${key}=${value}`)
    .join(',');

async function generate(apiDir, language) {
  const paths = apiPaths(apiDir);
  const packageDir = resolve(apiDir, 'packages', language);
  const config = parse(await readFile(join(packageDir, 'generate.yaml'), 'utf8'));
  const sharedNames = join(apiDir, 'packages', 'names.yaml');
  const shared = (await exists(sharedNames)) ? parse(await readFile(sharedNames, 'utf8')) : {};
  Object.assign(config, packageNames(shared, config));
  const operations = parse(await readFile(join(packageDir, 'operations.yaml'), 'utf8'));
  const sdk = (await exists(join(apiDir, 'sdk.yaml'))) ? parse(await readFile(join(apiDir, 'sdk.yaml'), 'utf8')) : {};
  const output = join(packageDir, config.output);
  const source = config.source ?? config.properties.packageName.replaceAll('.', '/');

  const built = stripProse(parse(await readFile(paths.build, 'utf8')));
  const spec = applyOperations(renameSchemas(relax(built, config), config.schema_names), operations, sdk?.paging);
  const work = await mkdtemp(join(tmpdir(), 'generate-'));
  try {
    const input = join(work, 'openapi.yaml');
    const generatorConfig = join(work, 'config.json');
    await writeFile(input, stringify(spec, { lineWidth: 0, compat: 'yaml-1.1' }));
    await writeFile(generatorConfig, JSON.stringify({ files: supportingFiles(config, source) }));
    await mkdir(join(work, 'out'));
    await writeFile(join(work, 'out', '.openapi-generator-ignore'), ignoreFile(config));
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
      ...Object.entries(MAPPINGS).flatMap(([key, flag]) => (config[key] ? [flag, pairs(config[key])] : [])),
    ], { stdio: ['ignore', 'ignore', 'inherit'] });

    await mkdir(output, { recursive: true });
    for (const dir of config.generated ?? []) {
      await rm(join(output, dir), { recursive: true, force: true });
      await cp(join(work, 'out', source, dir), join(output, dir), { recursive: true });
    }
    const prefixed = async (dir) => (await readdir(dir)).filter((name) => hasPrefix(name, config.generated_prefixes));
    for (const name of await prefixed(output)) await rm(join(output, name));
    for (const name of await prefixed(join(work, 'out', source))) await copyFile(join(work, 'out', source, name), join(output, name));
    await copyFile(join(work, 'out', source, config.resources), join(output, config.resources));
    for (const [template, target] of Object.entries(config.supporting_files ?? {})) await copyFile(join(work, 'out', 'supporting', template), join(packageDir, target));
  } finally {
    await rm(work, { recursive: true, force: true });
  }
  await rm(join(output, config.runtime), { recursive: true, force: true });
  await cp(join(TOOLCHAIN, 'runtime', language), join(output, config.runtime), { recursive: true });
  if (config.runtime_package) await fillPackageName(join(output, config.runtime), config.runtime_package);
  run(config.format[0], [...config.format.slice(1), config.output], { cwd: packageDir });
  console.log(`Generated ${output}`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [apiDir, language] = process.argv.slice(2);
  if (!apiDir || !language) throw new Error('Usage: node generate.mjs <api-dir> <language>');
  await generate(apiDir, language);
}
