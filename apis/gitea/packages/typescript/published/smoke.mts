// Smoke test of the published package, run by the published packages workflow against the mock, never a live instance.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { GiteaClient } from 'gitea-rest';

const PACKAGE = 'gitea-rest';
const { SMOKE_BASE_URL: mock = '', SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

// The mock serves each path without `/api/v1`, which the client adds, so a fetch removes it on the way out.
const fetch: typeof globalThis.fetch = (input, init) => {
  const url = new URL(String(input));
  url.pathname = url.pathname.replace(/^\/api\/v1\//, '/');
  return globalThis.fetch(url, init);
};
const client = new GiteaClient({ baseUrl: mock, token: 'smoke-synthetic-access-token', fetch });
const version = await client.misc.getVersion();
console.log(`${PACKAGE} ${expected}: the mock reports version ${version.version}`);
