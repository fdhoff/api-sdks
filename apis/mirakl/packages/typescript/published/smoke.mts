// Smoke test of the published package, run by the published packages workflow against the mock, never a live instance.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { MiraklClient } from 'mirakl-seller';

const PACKAGE = 'mirakl-seller';
const { SMOKE_BASE_URL: mock = '', SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

const client = new MiraklClient({ baseUrl: mock, apiKey: 'smoke-synthetic-shop-key' });
const shop = await client.shop.get();
console.log(`${PACKAGE} ${expected}: read shop ${shop.shop_id}`);
