// Keeps an API's pinned upstream spec in a local, gitignored cache.
// No flag fetches it from the lock's URL if absent; `--verify` checks the cache offline; `--pin` re-pins.
import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

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

const readLock = async (paths) => JSON.parse(await readFile(paths.lock, 'utf8'));

async function readCache(paths) {
  try {
    return await readFile(paths.spec);
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

async function download(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`GET ${url}: HTTP ${response.status}`);
  return { response, bytes: Buffer.from(await response.arrayBuffer()) };
}

export async function ensureSpec(paths) {
  const lock = await readLock(paths);
  const cached = await readCache(paths);
  if (cached) {
    verifyPin(cached, lock, `Cached spec ${paths.spec}`);
    return cached;
  }
  const { bytes } = await download(lock.url);
  verifyPin(bytes, lock, `Spec from ${lock.url}`);
  await writeFile(paths.spec, bytes);
  return bytes;
}

async function pin(paths) {
  const { url } = await readLock(paths);
  const { response, bytes } = await download(url);
  const lock = {
    url,
    sha256: sha256(bytes),
    infoVersion: parse(bytes.toString('utf8')).info.version,
    lastModified: response.headers.get('last-modified'),
    retrievedOn: new Date().toISOString().slice(0, 10),
  };
  await writeFile(paths.spec, bytes);
  await writeFile(paths.lock, `${JSON.stringify(lock, null, 2)}\n`);
  console.log(`Pinned ${lock.sha256}`);
}

async function verify(paths) {
  const lock = await readLock(paths);
  const cached = await readCache(paths);
  if (!cached) throw new Error(`No cached spec at ${paths.spec}. Run \`npm run spec:fetch\`.`);
  verifyPin(cached, lock, `Cached spec ${paths.spec}`);
  console.log(`Pin verified: ${lock.sha256}`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const paths = apiPaths(apiDirFromArgs(process.argv));
  if (process.argv.includes('--pin')) await pin(paths);
  else if (process.argv.includes('--verify')) await verify(paths);
  else {
    await ensureSpec(paths);
    console.log(`Spec ready: ${paths.spec}`);
  }
}
