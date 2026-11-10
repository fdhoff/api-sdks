// Keeps an API's pinned upstream specs in a local, gitignored cache.
// No flag fetches each from its lock URL if absent; `--verify` checks the cache offline; `--pin` re-pins.
// `--pin --url <url> [--tag <tag>]` moves a single-source lock to another URL, and records the upstream release
// tag it names, for upstreams that publish each release at its own URL.
import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { apiDirFromArgs, apiPaths, lockSources, sourcePaths } from './paths.mjs';

export const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

export function verifyPin(specBytes, lock, source) {
  const actual = sha256(specBytes);
  if (actual !== lock.sha256) {
    throw new Error(
      `${source} does not match the lock: got ${actual}, expected ${lock.sha256}. ` +
        'If upstream changed, review it and run `npm run spec:pin`. ' +
        'If the cached copy is stale, delete it and run `npm run spec:fetch`.',
    );
  }
}

export const readLock = async (apiDir) => JSON.parse(await readFile(apiPaths(apiDir).lock, 'utf8'));

async function readCache(path) {
  try {
    return await readFile(path);
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

// Some servers answer a missing file with 200 and no body, which must not read as a changed spec.
export async function download(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`GET ${url}: HTTP ${response.status}`);
  const bytes = Buffer.from(await response.arrayBuffer());
  if (bytes.toString('utf8').trim() === '') throw new Error(`GET ${url}: HTTP ${response.status} with an empty body, so there is no spec at this URL`);
  return { response, bytes };
}

async function ensureSource(specPath, source) {
  const cached = await readCache(specPath);
  if (cached) {
    verifyPin(cached, source, `Cached spec ${specPath}`);
    return cached;
  }
  const { bytes } = await download(source.url);
  verifyPin(bytes, source, `Spec from ${source.url}`);
  await mkdir(dirname(specPath), { recursive: true });
  await writeFile(specPath, bytes);
  return bytes;
}

export async function ensureSpec(paths) {
  return ensureSource(paths.spec, JSON.parse(await readFile(paths.lock, 'utf8')));
}

// Every source in the lock, each with its cached bytes and its paths.
export async function ensureSpecs(apiDir) {
  const specs = [];
  for (const source of lockSources(await readLock(apiDir))) {
    const paths = sourcePaths(apiDir, source);
    specs.push({ source, paths, bytes: await ensureSource(paths.spec, source) });
  }
  return specs;
}

// Downloads every source before writing anything, so one failure leaves the old pins and caches in place. A lock
// keeps its `tag` unless `tag` replaces it.
export async function pin(apiDir, { url, tag } = {}) {
  const lock = await readLock(apiDir);
  const retrievedOn = new Date().toISOString().slice(0, 10);
  const sources = lockSources(lock);
  if ((url !== undefined || tag !== undefined) && sources[0].name !== null) throw new Error('--url and --tag move a single-source lock only');
  if (tag !== undefined && url === undefined) throw new Error('--tag needs --url');
  const pinned = [];
  for (const original of sources) {
    const source = url === undefined ? original : { ...original, url, tag };
    const { response, bytes } = await download(source.url);
    const entry = {
      ...(source.name === null ? {} : { name: source.name }),
      url: source.url,
      ...(source.tag ? { tag: source.tag } : {}),
      sha256: sha256(bytes),
      infoVersion: parse(bytes.toString('utf8')).info.version,
      lastModified: response.headers.get('last-modified'),
      retrievedOn,
    };
    pinned.push({ entry, bytes, path: sourcePaths(apiDir, source).spec });
  }
  for (const { bytes, path } of pinned) {
    await mkdir(dirname(path), { recursive: true });
    await writeFile(path, bytes);
  }
  const entries = pinned.map(({ entry }) => entry);
  const updated = 'sources' in lock ? { sources: entries } : entries[0];
  await writeFile(apiPaths(apiDir).lock, `${JSON.stringify(updated, null, 2)}\n`);
  for (const { entry } of pinned) console.log(`Pinned ${entry.name ? `${entry.name} ` : ''}${entry.sha256}`);
}

export async function verify(apiDir) {
  for (const source of lockSources(await readLock(apiDir))) {
    const { spec } = sourcePaths(apiDir, source);
    const cached = await readCache(spec);
    if (!cached) throw new Error(`No cached spec at ${spec}. Run \`npm run spec:fetch\`.`);
    verifyPin(cached, source, `Cached spec ${spec}`);
    console.log(`Pin verified: ${source.name ? `${source.name} ` : ''}${source.sha256}`);
  }
}

// The value after `--<name>`, if the flag is given.
function option(argv, name) {
  const index = argv.indexOf(`--${name}`);
  if (index === -1) return undefined;
  const value = argv[index + 1];
  if (value === undefined || value.startsWith('--') || value === '') throw new Error(`--${name} needs a value`);
  return value;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const apiDir = apiDirFromArgs(process.argv);
  if (process.argv.includes('--pin')) await pin(apiDir, { url: option(process.argv, 'url'), tag: option(process.argv, 'tag') });
  else if (process.argv.includes('--verify')) await verify(apiDir);
  else {
    for (const { paths } of await ensureSpecs(apiDir)) console.log(`Spec ready: ${paths.spec}`);
  }
}
