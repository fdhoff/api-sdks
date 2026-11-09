// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { EtsyClient } from 'etsy-seller';

const PACKAGE = 'etsy-seller';
const { SMOKE_BASE_URL: baseUrl, SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

const client = new EtsyClient({
  apiKey: 'smoke-synthetic-keystring',
  sharedSecret: 'smoke-synthetic-shared-secret',
  baseUrl,
});
const pong = await client.application.ping();
if (pong.application_id === undefined) throw new Error('The ping has no application_id');
console.log(`${PACKAGE} ${expected}: pinged application ${pong.application_id}`);
