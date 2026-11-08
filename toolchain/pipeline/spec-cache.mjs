// Prints the Actions cache key and path for an API's pinned specs, as `key=` and `path=` lines for
// $GITHUB_OUTPUT. Uses only Node's own modules, so it runs before `npm ci`.
// A single spec keeps the key `upstream-spec-<sha256>`; several share one key over every name and hash.
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { apiPaths, CONTRACT_CACHE, lockSources } from './paths.mjs';

export function specCache(apiDir, lock) {
  const sources = lockSources(lock);
  if (sources[0].name === null) return { key: `upstream-spec-${lock.sha256}`, path: join(apiDir, 'spec/upstream/openapi.yaml') };
  const pins = sources.map(({ name, sha256 }) => `${name}=${sha256}`).join('\n');
  return { key: `upstream-spec-${createHash('sha256').update(pins).digest('hex')}`, path: join(apiDir, CONTRACT_CACHE) };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const [apiDir, lockFile] = process.argv.slice(2);
  if (!apiDir) throw new Error('Usage: node spec-cache.mjs <api-dir> [lock-file]');
  const { key, path } = specCache(apiDir, JSON.parse(await readFile(lockFile ?? apiPaths(apiDir).lock, 'utf8')));
  console.log(`key=${key}\npath=${path}`);
}
