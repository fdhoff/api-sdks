// Pins an API's upstream spec. `--verify` checks the pin offline; no flag re-fetches from the lock's URL.
import { createHash } from 'node:crypto';
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { apiDirFromArgs, apiPaths } from './paths.mjs';

export const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

export function verifyPin(specBytes, lock) {
  const actual = sha256(specBytes);
  if (actual !== lock.sha256) {
    throw new Error(`Pinned spec does not match lock: got ${actual}, expected ${lock.sha256}`);
  }
}

async function fetchPin(paths) {
  const { url } = JSON.parse(await readFile(paths.lock, 'utf8'));
  const response = await fetch(url);
  if (!response.ok) throw new Error(`GET ${url}: HTTP ${response.status}`);
  const bytes = Buffer.from(await response.arrayBuffer());
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
  const lock = JSON.parse(await readFile(paths.lock, 'utf8'));
  verifyPin(await readFile(paths.spec), lock);
  console.log(`Pin verified: ${lock.sha256}`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const paths = apiPaths(apiDirFromArgs(process.argv));
  await (process.argv.includes('--verify') ? verify(paths) : fetchPin(paths));
}
