import { resolve } from 'node:path';

// `build` is the one document Prism serves and Spectral lints. For an API built from several contracts it
// merges them, and each contract is also built on its own under build/contracts/.
export function apiPaths(apiDir) {
  return {
    spec: resolve(apiDir, 'spec/upstream/openapi.yaml'),
    lock: resolve(apiDir, 'spec/upstream/lock.json'),
    overlay: resolve(apiDir, 'spec/overlay.yaml'),
    build: resolve(apiDir, 'build/openapi.yaml'),
  };
}

// Where an API with several contracts caches their upstream specs, relative to its directory.
export const CONTRACT_CACHE = 'spec/upstream/contracts';

export function contractPaths(apiDir, name) {
  return {
    spec: resolve(apiDir, CONTRACT_CACHE, `${name}.yaml`),
    overlay: resolve(apiDir, 'spec/overlay', `${name}.yaml`),
    build: resolve(apiDir, 'build/contracts', `${name}.yaml`),
  };
}

const CONTRACT_NAME = /^[a-z][a-z0-9_]*$/;

// A lock pins one spec at its top level, or several under `sources`, each with a `name`.
export function lockSources(lock) {
  if (!('sources' in lock)) return [{ ...lock, name: null }];
  if (!Array.isArray(lock.sources) || lock.sources.length === 0) throw new Error('lock.json `sources` must list at least one source');
  const seen = new Set();
  for (const { name } of lock.sources) {
    if (!CONTRACT_NAME.test(name ?? '')) throw new Error(`lock.json source name ${JSON.stringify(name)} must match ${CONTRACT_NAME}`);
    if (seen.has(name)) throw new Error(`lock.json names source ${name} twice`);
    seen.add(name);
  }
  return lock.sources;
}

// Where each source's spec is cached, its overlay read and its build written.
export function sourcePaths(apiDir, source) {
  return source.name === null ? apiPaths(apiDir) : contractPaths(apiDir, source.name);
}

export function apiDirFromArgs(argv) {
  const apiDir = argv.slice(2).find((arg) => !arg.startsWith('--'));
  if (!apiDir) throw new Error('Usage: node <script> <api-dir> [--verify|--pin]');
  return apiDir;
}
