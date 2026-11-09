// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { BackMarketClient } from 'backmarket-seller';

const PACKAGE = 'backmarket-seller';
const { SMOKE_BASE_URL: baseUrl, SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

const client = new BackMarketClient({
  token: 'smoke-synthetic-token',
  userAgent: 'BM-Example-Smoke;smoke@example.com',
  locale: 'en-us',
  baseUrl,
});
const order = await client.orders.get(1);
if (order.order_id === undefined) throw new Error('The order has no order_id');
console.log(`${PACKAGE} ${expected}: got order ${order.order_id}`);
