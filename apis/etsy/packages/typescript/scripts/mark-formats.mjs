// Each build directory needs its own `type`, so Node reads dist/cjs as CommonJS inside this ESM package.
import { writeFile } from 'node:fs/promises';

for (const [format, type] of [
  ['esm', 'module'],
  ['cjs', 'commonjs'],
]) {
  await writeFile(new URL(`../dist/${format}/package.json`, import.meta.url), `${JSON.stringify({ type })}\n`);
}
