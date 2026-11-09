import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { test } from 'node:test';
import * as sdk from 'mirakl-seller';

const AsyncFunction = (async () => {}).constructor as new (...args: string[]) => (...args: unknown[]) => Promise<void>;
const SECRETS = ['your-shop-api-key'];
const BASE = 'https://your-operator.mirakl.net';

function respond(url: URL): Response {
  const json = (body: unknown, status = 200) =>
    new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
  const shop = Number(url.searchParams.get('shop_id') ?? 2001);
  switch (url.pathname) {
    case '/api/account':
      return json({ shop_id: shop, shop_name: 'Synthetic shop' });
    case '/api/orders':
      return json({ orders: [{ order_id: 'order-1', order_state: 'SHIPPING' }], total_count: 1 });
    case '/api/offers/imports':
      return json({ import_id: 41 }, 201);
    case '/api/offers/imports/41':
      return json({ import_id: 41, status: 'COMPLETE', has_error_report: true });
    case '/api/offers/imports/41/error_report':
      return new Response('sku;error\n', { headers: { 'content-type': 'application/octet-stream' } });
    case '/api/offers/export/async':
      return json({ tracking_id: 'tracking-1' });
    case '/api/offers/export/async/status/tracking-1':
      return json({ status: 'COMPLETED', urls: [`${BASE}/exports/offers-1.json`] });
    case '/exports/offers-1.json':
      return new Response('[]', { headers: { 'content-type': 'application/json' } });
  }
  return new Response('synthetic not found', { status: 404 });
}

/** A snippet's import becomes a lookup on the package. Snippets use no TypeScript-only syntax. */
const runnable = (snippet: string): string =>
  snippet.replace(/^import \{(.*)\} from 'mirakl-seller';$/m, 'const {$1} = sdk;');

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
    assert.ok(fetch.mock.callCount() > 0);
    assert.ok(fetch.mock.calls.every(({ arguments: [input] }) => String(input).startsWith(`${BASE}/`)));
    assert.notEqual(lines.length, 0);
    const output = JSON.stringify(lines);
    assert.deepEqual(
      SECRETS.filter((secret) => output.includes(secret)),
      [],
    );
  });
}
