// Applies an API's overlay to its pinned spec, producing <api-dir>/build/openapi.yaml. An API built from
// several contracts gets each one built on its own under build/contracts/, and a merged copy for the mock.
import { mkdir, readFile, stat, writeFile } from 'node:fs/promises';
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import openapiFormat from 'openapi-format';
import { parse, stringify } from 'yaml';
import { ensureSpecs } from './fetch-spec.mjs';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

const METHODS = ['get', 'put', 'post', 'delete', 'patch', 'head', 'options', 'trace'];
const SECTIONS = ['schemas', 'responses', 'parameters', 'examples', 'requestBodies', 'headers', 'securitySchemes', 'links', 'callbacks'];

export async function applyOverlay(spec, overlay) {
  const { data, resultData } = await openapiFormat.openapiOverlay(spec, { overlaySet: overlay });
  if (resultData.totalActions === 0) throw new Error('Overlay has no actions');
  if (resultData.unusedActions.length > 0) {
    const targets = resultData.unusedActions.map((action) => action.target).join(', ');
    throw new Error(`Overlay actions matched nothing: ${targets}`);
  }
  return data;
}

const operationsOf = (item) => METHODS.map((method) => item[method]).filter(Boolean);

// Splits a server URL at the first `/` after its scheme into an origin, which keeps its variables, and a
// path, whose variables take their defaults. A variable whose default holds that `/` mid-way is refused.
function splitServer(server) {
  const value = (name) => {
    const fallback = server.variables?.[name]?.default;
    if (fallback === undefined) throw new Error(`Server ${server.url} has no default for {${name}}`);
    return String(fallback);
  };
  const pieces = server.url.split(/(\{[^}]+\})/).filter(Boolean).map((piece) => {
    const name = /^\{(.+)\}$/.exec(piece)?.[1];
    return { piece, name, text: name ? value(name) : piece };
  });
  const filled = pieces.map(({ text }) => text).join('');
  const scheme = /^[a-z][a-z0-9+.-]*:\/\//i.exec(filled)?.[0].length ?? 0;
  let origin = '';
  let path = '';
  let length = 0;
  for (const { piece, name, text } of pieces) {
    const slash = text.indexOf('/', Math.max(0, scheme - length));
    if (path) path += text;
    else if (slash < 0) origin += piece;
    else if (!name) [origin, path] = [origin + text.slice(0, slash), text.slice(slash)];
    else if (slash === 0) path = text;
    else throw new Error(`Server ${server.url} has {${name}} spanning its host and path`);
    length += text.length;
  }
  const variables = Object.fromEntries(Object.entries(server.variables ?? {}).filter(([name]) => origin.includes(`{${name}}`)));
  const { variables: _, ...rest } = server;
  return {
    prefix: path.replace(/\/+$/, ''),
    server: { ...rest, url: origin || '/', ...(Object.keys(variables).length > 0 ? { variables } : {}) },
  };
}

// Moves the path every server shares into the paths, leaving each server its origin, so contracts that
// share a host can share one client and one mock. Servers that disagree on the path are refused.
export function inlineServerPath(spec) {
  const holders = [spec, ...Object.values(spec.paths ?? {}).flatMap((item) => [item, ...operationsOf(item)])].filter((node) => node.servers);
  const prefixes = new Set();
  for (const holder of holders) {
    holder.servers = holder.servers.map((server) => {
      const split = splitServer(server);
      prefixes.add(split.prefix);
      return split.server;
    });
  }
  if (prefixes.size > 1) throw new Error(`Servers disagree on their path: ${[...prefixes].join(', ')}`);
  const [prefix = ''] = prefixes;
  spec.paths = Object.fromEntries(Object.entries(spec.paths ?? {}).map(([path, item]) => [`${prefix}${path}`, item]));
  return spec;
}

const REF = /^#\/components\/([^/]+)\/(.+)$/;

function prefixRefs(node, prefix) {
  if (Array.isArray(node)) return node.map((item) => prefixRefs(item, prefix));
  if (node === null || typeof node !== 'object') return node;
  const rename = (ref) => ref.replace(REF, (whole, section, key) => (SECTIONS.includes(section) ? `#/components/${section}/${prefix}${key}` : whole));
  return Object.fromEntries(
    Object.entries(node).map(([key, value]) => {
      if (key === '$ref' && typeof value === 'string') return [key, rename(value)];
      if (key === 'discriminator' && value?.mapping) {
        const mapping = Object.fromEntries(Object.entries(value.mapping).map(([name, ref]) => [name, rename(ref)]));
        return [key, { ...value, mapping }];
      }
      return [key, prefixRefs(value, prefix)];
    }),
  );
}

const prefixSecurity = (security, prefix) =>
  security.map((requirement) => Object.fromEntries(Object.entries(requirement).map(([scheme, scopes]) => [`${prefix}${scheme}`, scopes])));

// One document for Prism and Spectral. Each contract's component names and operation IDs get its name and a
// dot as a prefix, because contracts reuse schema names. Paths must already be disjoint.
export function mergeContracts(contracts) {
  const merged = {
    openapi: contracts[0].spec.openapi,
    info: {
      title: contracts.map(({ name }) => name).join(', '),
      version: contracts.map(({ name, spec }) => `${name}@${spec.info?.version}`).join(' '),
    },
    servers: [],
    tags: [],
    paths: {},
    components: {},
  };
  const owners = {};
  for (const { name, spec: original } of contracts) {
    const prefix = `${name}.`;
    const spec = prefixRefs(original, prefix);
    for (const section of SECTIONS) {
      for (const [key, value] of Object.entries(spec.components?.[section] ?? {})) {
        (merged.components[section] ??= {})[`${prefix}${key}`] = value;
      }
    }
    for (const server of spec.servers ?? []) {
      if (!merged.servers.some((known) => known.url === server.url)) merged.servers.push(server);
    }
    for (const tag of spec.tags ?? []) {
      if (!merged.tags.some((known) => known.name === tag.name)) merged.tags.push(tag);
    }
    for (const [path, item] of Object.entries(spec.paths ?? {})) {
      if (owners[path]) throw new Error(`Contracts ${owners[path]} and ${name} both declare ${path}`);
      owners[path] = name;
      if (!item.servers && spec.servers) item.servers = spec.servers;
      for (const operation of operationsOf(item)) {
        if (operation.operationId) operation.operationId = `${prefix}${operation.operationId}`;
        const security = operation.security ?? spec.security;
        if (security) operation.security = prefixSecurity(security, prefix);
      }
      merged.paths[path] = item;
    }
  }
  for (const key of ['servers', 'tags']) if (merged[key].length === 0) delete merged[key];
  return merged;
}

const exists = (path) =>
  stat(path).then(
    () => true,
    () => false,
  );

async function writeSpec(path, spec) {
  await mkdir(dirname(path), { recursive: true });
  await writeFile(path, stringify(spec, { lineWidth: 0, compat: 'yaml-1.1' }));
  console.log(`Built ${path}`);
}

// A contract's overlay is optional; an API with one spec must have one.
async function correct(bytes, overlayPath, required) {
  const spec = parse(bytes.toString('utf8'));
  if (!required && !(await exists(overlayPath))) return spec;
  return applyOverlay(spec, parse(await readFile(overlayPath, 'utf8')));
}

export async function buildSpec(apiDir) {
  const specs = await ensureSpecs(apiDir);
  if (specs[0].source.name === null) {
    await writeSpec(specs[0].paths.build, await correct(specs[0].bytes, specs[0].paths.overlay, true));
    return;
  }
  const contracts = [];
  for (const { source, paths, bytes } of specs) {
    const spec = inlineServerPath(await correct(bytes, paths.overlay, false));
    await writeSpec(paths.build, spec);
    contracts.push({ name: source.name, spec });
  }
  await writeSpec(apiPaths(apiDir).build, mergeContracts(contracts));
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  await buildSpec(apiDirFromArgs(process.argv));
}
