import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'mercury-banking';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const SECRETS = ['secret-token:your-token', 'secret-token:your-sandbox-token', 'your-webhook-secret'];
const ID = '00000000-0000-4000-8000-000000000000';

function respond(url: URL): Response {
  const json = (body: unknown, status = 200) =>
    new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
  const page = { nextPage: null };
  if (url.pathname === '/api/v1/accounts') return json({ accounts: [{ id: ID, name: 'Checking' }], page });
  if (url.pathname === '/api/v1/transactions') return json({ transactions: [{ id: ID, amount: -1 }], page });
  if (url.pathname === '/api/v1/recipients') return json({ recipients: [{ id: ID, name: 'Synthetic' }], page });
  if (url.pathname.endsWith('/transactions')) return json({ id: ID, status: 'pending' });
  return new Response('synthetic not found', { status: 404 });
}

/** A snippet's import becomes a lookup on the package. Snippets use no TypeScript-only syntax. */
const runnable = (snippet: string): string =>
  snippet.replace(/^import \{(.*)\} from 'mercury-banking';$/m, 'const {$1} = sdk;');

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
    assert.equal(fetch.mock.callCount() > 0, snippet.includes('new MercuryClient'));
    assert.notEqual(lines.length, 0);
    const output = JSON.stringify(lines);
    assert.deepEqual(
      SECRETS.filter((secret) => output.includes(secret)),
      [],
    );
  });
}
