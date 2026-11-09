// Smoke test of the published package, run by the published packages workflow against the mock, never the live API.
// Installed from npm into a clean project, type-checked against the package's declarations, then run by Node.
import { readFile } from 'node:fs/promises';
import { EbayClient } from 'ebay-sell';

const PACKAGE = 'ebay-sell';
const { SMOKE_BASE_URL: mock = '', SMOKE_VERSION: expected } = process.env;
const manifest = JSON.parse(await readFile(new URL('../../package.json', import.meta.resolve(PACKAGE)), 'utf8')) as {
  version: string;
};
if (manifest.version !== expected) throw new Error(`${PACKAGE} reports version ${manifest.version}, not ${expected}`);

const client = new EbayClient({
  appToken: 'smoke-synthetic-app-token',
  hosts: { api: mock, apiz: mock, apim: mock },
  marketplaceId: 'EBAY_US',
});
const tree = await client.taxonomy.categoryTrees.getDefaultId({ marketplaceId: 'EBAY_US' });
if (tree?.categoryTreeId === undefined) throw new Error('The category tree has no categoryTreeId');
console.log(`${PACKAGE} ${expected}: got category tree ${tree.categoryTreeId}`);
