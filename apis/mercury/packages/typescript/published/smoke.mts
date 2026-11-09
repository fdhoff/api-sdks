// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { MercuryClient } from 'mercury-banking';

const PACKAGE = 'mercury-banking';
const { SMOKE_BASE_URL: mock = '', SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

const client = new MercuryClient({ token: 'secret-token:smoke-synthetic-token', hosts: { api: mock, vault: mock } });
const page = await client.accounts.list();
console.log(`${PACKAGE} ${expected}: listed ${page.accounts.length} accounts`);
