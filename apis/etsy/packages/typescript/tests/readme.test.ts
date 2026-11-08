import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'etsy-seller';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const SECRETS = ['your-keystring', 'your-shared-secret', 'your-access-token', 'your-refresh-token', 'synthetic-new'];

function respond(url: URL): Response {
  const json = (body: unknown, status = 200) =>
    new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
  if (url.pathname === '/v3/public/oauth/token') {
    const tokens = { access_token: '12345678.synthetic-new-access', refresh_token: '12345678.synthetic-new-refresh' };
    return json({ ...tokens, expires_in: 3600, token_type: 'Bearer' });
  }
  if (url.pathname === '/v3/application/users/me') return json({ user_id: 12345678, shop_id: 1 });
  if (['/v3/application/listings/active', '/v3/application/shops/1/receipts'].includes(url.pathname)) {
    return json({ count: 1, results: [{ listing_id: 1, receipt_id: 1, title: 'Mug' }] });
  }
  return json({ error: 'Synthetic missing shop' }, 404);
}

/** A snippet's import becomes a lookup on the package. Snippets use no TypeScript-only syntax. */
const runnable = (snippet: string): string =>
  snippet.replace(/^import \{(.*)\} from 'etsy-seller';$/m, 'const {$1} = sdk;');

const text = await readFile(new URL('../README.md', import.meta.url), 'utf8');
const snippets = [...text.matchAll(/```ts\n(.*?)```/gs)].map((match) => match[1] as string);

test('the README has snippets', () => assert.ok(snippets.length >= 3));

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
