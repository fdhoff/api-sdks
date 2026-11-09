import assert from 'node:assert/strict';
import { generateKeyPairSync } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'ebay-sell';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const SECRETS = ['your-cert-id', 'your-user-token', 'your-refresh-token', 'synthetic-new'];
// The body of the key without its PEM lines, as Key Management returns it.
const PRIVATE_KEY = String(generateKeyPairSync('ed25519').privateKey.export({ type: 'pkcs8', format: 'pem' }))
  .trim()
  .split('\n')
  .slice(1, -1)
  .join('');

function respond(url: URL): Response {
  const json = (body: unknown, status = 200) =>
    new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
  switch (url.pathname) {
    case '/identity/v1/oauth2/token':
      return json({ access_token: 'v^1.1#synthetic-new-token', expires_in: 7200, token_type: 'Bearer' });
    case '/commerce/taxonomy/v1/get_default_category_tree_id':
      return json({ categoryTreeId: '0', categoryTreeVersion: '1' });
    case '/sell/fulfillment/v1/order':
      return json({ orders: [{ orderId: '01-00001-00001' }], total: 1 });
    case '/developer/key_management/v1/signing_key':
      return json({ signingKeyId: 'synthetic-key-id', privateKey: PRIVATE_KEY, jwe: 'synthetic.jwe' });
    case '/sell/finances/v1/seller_funds_summary':
      return json({ totalFunds: { currency: 'GBP', value: '1.00' } });
    default:
      return json({ errors: [{ errorId: 62004, message: 'Synthetic missing category tree' }] }, 404);
  }
}

/** A snippet's import becomes a lookup on the package. Snippets use no TypeScript-only syntax. */
const runnable = (snippet: string): string =>
  snippet.replace(/^import \{(.*)\} from 'ebay-sell';$/m, 'const {$1} = sdk;');

const text = await readFile(new URL('../README.md', import.meta.url), 'utf8');
const snippets = [...text.matchAll(/```ts\n(.*?)```/gs)].map((match) => match[1] as string);

test('the README has snippets', () => assert.ok(snippets.length >= 4));

for (const [index, snippet] of snippets.entries()) {
  test(`README snippet ${index} runs`, async (t) => {
    const fetch = t.mock.method(globalThis, 'fetch', async (input: string | URL | Request) =>
      respond(new URL(String(input))),
    );
    const lines: unknown[][] = [];
    const log = (...args: unknown[]) => void lines.push(args);
    await new AsyncFunction('sdk', 'console', runnable(snippet))(sdk, { log });
    assert.notEqual(fetch.mock.callCount(), 0);
    const output = JSON.stringify(lines);
    assert.deepEqual(
      SECRETS.filter((secret) => output.includes(secret)),
      [],
    );
  });
}
