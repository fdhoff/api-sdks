import { resolve } from 'node:path';

export function apiPaths(apiDir) {
  return {
    spec: resolve(apiDir, 'spec/upstream/openapi.yaml'),
    lock: resolve(apiDir, 'spec/upstream/lock.json'),
    overlay: resolve(apiDir, 'spec/overlay.yaml'),
    build: resolve(apiDir, 'build/openapi.yaml'),
  };
}

export function apiDirFromArgs(argv) {
  const apiDir = argv.slice(2).find((arg) => !arg.startsWith('--'));
  if (!apiDir) throw new Error('Usage: node <script> <api-dir> [--verify|--pin]');
  return apiDir;
}
